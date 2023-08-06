from jsonpickle import decode
from os.path import join
from math import floor
from time import time

from .chai_chat import ChaiChat
from .chai_data import ChaiData
from .chai_ai import ChaiAI
from .chai_bots import ChaiBot
from .chai_argparser import fetch_args
from .chai_tools import clamp

"""
This module handles the creation and maintainence of a chat archive object.
"""


class ChaiArchive(object):
    """
    A class representing the entire chat history of a user.

    Attributes
    ----------
    _timestamp: float
        The timestamp when this program started.
    _selected_chat: ChaiChat
        The currently selected ChaiChat instance, or None.
    chaidata: ChaiData
        The user data directory.
        
    Methods
    -------
    __init__()
        Initializes the archive.
    get_selected_chat()
        Getter function for private _selected_chat attribute.
    _get_timestamp()
        Private getter function for private _timestamp attributes.
    _load_chat()
        Searches the archive for a valid chat 
        to load based on the arguments provided
    handle_args()
        Parses argv and modifies the state of this instance accordingly.
    """

    def __init__(self, argv=None, data_dir=None, verbosity=0):
        """
        Initialize a new archive with a user data directory.

        Parameters
        ----------
        argv: list, optional
            If this parameter is not None, then this ChaiArchive 
            is assumed to be being created from the command 
            line, and will behave differently.
        data_dir: str, optional
            The directory for loading and saving chat 
            history (defaults to appdirs.user_data_dir).
        verbosity: int, optional
            Level of verbosity at which to log events.
        """

        self._timestamp = time()
        self._selected_chat = None
        self.ai = ChaiAI()
        self.bot = ChaiBot(self.ai)
        self.chaidata = ChaiData(
            self._get_timestamp, self.bot, data_dir=data_dir, verbosity=verbosity
        )
        self.log = self.chaidata.log

        if argv is not None:
            self._selected_chat = self.handle_args(argv)
        else:
            self._selected_chat = ChaiChat(self.chaidata, self.ai, self.bot)

    def get_selected_chat(self):
        return self._selected_chat

    def _get_timestamp(self):
        return self._timestamp

    def _load_chat(self, args):
        """
        Searches the archive for a valid chat 
        to load based on the arguments provided

        Parameters
        ----------
        args: argparse.Namespace
            The args that were parsed

        Returns
        -------
        dict
            The dict object that was loaded, or None
        """
        logs = self.chaidata.list_chats()

        if len(logs) == 0:
            return

        if args.resumelast:
            # Load the previous conversation
            with open(join(self.chaidata.convos_dir, logs[len(logs) - 1],)) as f:
                return decode(f.read())

        if args.index is not None:
            # Load a previous conversation by reverse chronological index
            args.index = clamp(args.index, 1, len(logs))
            with open(
                join(self.chaidata.convos_dir, logs[len(logs) - args.index],)
            ) as f:
                return decode(f.read())

        if args.time is not None:
            # Load a previous conversation by timestamp
            files = [log for log in logs if args.time in log]
            if len(files) > 0:
                with open(join(self.chaidata.convos_dir, files[len(files) - 1],)) as f:
                    return decode(f.read())

        if args.title is not None:
            # Load a previous conversation by title
            files = [
                log
                for log in logs
                if args.title.replace(" ", "").lower() in log.replace("_", "").lower()
            ]
            if len(files) > 0:
                with open(join(self.chaidata.convos_dir, files[len(files) - 1],)) as f:
                    return decode(f.read())

        # Check for chat in the last 5 minutes
        max_timestamp = floor(float(logs[0].split("_")[1]))
        max_index = 0
        for i in range(1, len(logs)):
            timestamp = floor(float(logs[i].split("_")[1]))
            if timestamp > max_timestamp:
                max_timestamp = timestamp
                max_index = i

        if self._timestamp - max_timestamp < 300:
            # Time since chat is fewer than 5 minutes
            with open(join(self.chaidata.convos_dir, logs[max_index])) as f:
                return decode(f.read())

    def handle_args(self, argv):
        """
        Parses argv and modifies the state of this instance accordingly.

        Parameters
        ----------
        argv: list
            The list of arguments to parse.
        """
        args = fetch_args(argv)

        self.chaidata.verbosity = args.verbosity

        # List previous chats
        if args.list:  # or args.transcriptbrief:
            self.log("Printing history then exiting")
            self.chaidata.print_chat_history_oneline()
            return

        # Load previous chat
        loaded_chat = None
        selected_chat = None
        if not args.clean:
            loaded_chat = self._load_chat(args)
            if isinstance(loaded_chat, ChaiChat):
                self.log(
                    ('Loaded previous chat: "', loaded_chat.title, '"',), sep="",
                )
                selected_chat = loaded_chat
                selected_chat.chaidata = self.chaidata
                selected_chat.log = self.chaidata.log
                selected_chat.ai = self.ai
                # Trim the script
                if args.erase is not None:
                    selected_chat.erase_messages(args.erase)

        if loaded_chat is None:
            self.log("No previous chat to load, starting a new one")
            selected_chat = ChaiChat(self.chaidata, self.ai, self.bot)

        # Now everything is initialized

        # No chat, just print transcripts
        if args.transcript_full:
            self.log("Printing transcript then exiting")
            if selected_chat is not None:
                print(selected_chat.format_transcript())
            else:
                print("No chat for which to print transcript")
            return

        # Parse the last message for commands and prompt
        if args.botcommands:
            self.log("Parsing last message for commands, then reprompting with output")
            selected_chat.parse_cmds()
            return

        # # if args.audio:
        # #     if args.fileprompt:
        # #         print("Loading audio prompt from file")
        # #     else:
        # #         args.prompt = record_prompt()
        # #     prompt = ""
        # #     with open(args.prompt, "rb") as f:
        # #         prompt = Audio.transcribe("whisper-1", f).text
        # #     args.prompt = prompt
        # #     if args.prompt != "":
        # #         print(f"Heard:\n{args.prompt}")
        # # elif args.fileprompt:  # Load prompt from file

        if args.fileprompt:  # Load prompt from file
            filepath = args.prompt
            args.prompt = ""
            with open(filepath) as f:
                self.log(("Reading text prompt from file:", filepath))
                args.prompt = f.read()

        # Treat the prompt as code, invoke the headless doctest bot, don't prompt
        if args.doctest_function:
            self.log(
                "Invoking the headless DocTest bot on the following code:\n\n{args.prompt[0].content}"
            )
            selected_chat.bot.doctest_function(args.prompt)
            return

        selected_chat.append_prompt_from_args(args)

        # Parse the last message for commands and don't prompt
        if args.usercommands:
            self.log("Parsing last message for commands, then exiting")
            selected_chat.parse_user_cmds()
            return

        return selected_chat
