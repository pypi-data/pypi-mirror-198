from jsonpickle import encode, decode
from appdirs import user_data_dir
from typing import Callable
from os.path import join
from time import time

from .chai_bots import ChaiBot

from .chai_tools import (
    list_dir,
    make_dir,
    remove_file,
)


class ChaiData(object):
    """
    This class handles chat data for a ChaiArchive and its ChaiChats.

    Attributes
    ----------
    get_time: Callable
        ChaiData uses this callback function to name its log files.
    data_dir: str
        The directory for loading and saving chat history.
    convos_dir: str
        Beneath data_dir, stores full JSON chat history and data files.
    scripts_dir: str
        Beneath data_dir, stores pretty human-readable transcripts of chats.
    logs_dir: str
        Beneath data_dir, stores event log files.
    verbosity: int, optional
        Level of verbosity at which to log events.

    Methods
    -------
    __init__()
        Sets up the user data directory.
    list_chats()
        Returns all files in the
    print_chat_history_oneline()
        Prints a numbered list of conversations in the archive.
    log()
        Event logger with a range of verbosities.
        Always log to file and sometimes log to console too.
    """

    LOG_LVL = 3  # 0 to 3, 0 is none, 3 is very detailed

    def __init__(self, get_time: Callable, bot: ChaiBot, data_dir: str = None, verbosity: int = 0):
        """
        Sets up the user data directory.

        Parameters
        ----------
        get_time: Callable
            ChaiData uses this callback function to name its log files.
        data_dir: str, optional
            The directory for loading and saving chat history (defaults to appdirs.user_data_dir).
        verbosity: int, optional
            Level of verbosity at which to log events.
        """

        self.get_time = get_time
        self.verbosity = verbosity
        self.bot = bot
        if data_dir is not None:
            self.data_dir = data_dir
        else:
            self.data_dir = user_data_dir(appname="ChaiGPT", appauthor="VulcanicAI")

        self.convos_dir = join(self.data_dir, "Chai Files")
        self.scripts_dir = join(self.data_dir, "Pretty Chats")
        self.logs_dir = join(self.data_dir, "Debug Logs")

        make_dir(self.data_dir)
        make_dir(self.convos_dir)
        make_dir(self.scripts_dir)
        make_dir(self.logs_dir)

    def list_chats(self, suffix=".json"):
        """
        Returns a list of all chats in the archive.

        Parameters
        ----------
        suffix: str
            The pattern to filter by when listing the files.

        Returns
        -------
        list
            A list of all the files in the Chai 
            Data directory, in chronological order 
            (because the filenames start with their touchstamps)
        """
        return sorted([log for log in list_dir(self.convos_dir) if suffix in log])

    def print_chat_history_oneline(self, begin=0, end=None):
        """
        Prints a numbered list of conversations in the archive.

        Parameters
        ----------
        begin: int
            How many recent chats to skip.
        end: int
            How far back to go.
        """

        logs = self.list_chats()

        self.log((self.convos_dir, logs))

        if end is None:
            end = len(logs)

        for n in range(end, begin, -1):
            with open(join(self.convos_dir, logs[len(logs) - n],)) as json_file:
                chat = decode(json_file.read())
                if len(chat.history) > 0:
                    print(
                        f"{n}: {chat.title}\n", sep="", end="",
                    )

    def archive_chat(self, chat):
        if len(chat.history) <= 0:
            return

        old_filename = chat.filename
        overwrite = False
        if old_filename is not None:
            with open(join(self.convos_dir, "chat_" + old_filename + ".json",)) as f:
                old_archive = decode(f.read())
                if old_archive.birthstamp == chat.birthstamp:
                    overwrite = True

        time_log = time()

        chat.timestamps += [time_log] * (len(chat.history) - len(chat.timestamps))
        chat.touchstamp = time_log
        self.write_files(chat)
        if overwrite:
            remove_file(join(self.convos_dir, "chat_" + old_filename + ".json",))
            remove_file(join(self.scripts_dir, "transcript_" + old_filename + ".txt",))

    def open_(self, filepath, open_type="r", encoding="utf-16"):
        try:
            return open(filepath, open_type, encoding=encoding)
        except BaseException:
            self.log(("Couldn't open file:", filepath))
            pass

    def write_files(self, chat):
        script = chat.format_transcript()
        if not chat.title:
            self.log("Auto-titling transcript")
            chat.title = self.bot.title_script(script)
            self.log(("Auto-titled:", chat.title))
        chat.make_filename()
        json_filename = "chat_" + chat.filename + ".json"
        json_filepath = join(self.convos_dir, json_filename)
        with open(json_filepath, "w",) as f:
            self.log(("Saving chat JSON file at", json_filepath))
            f.write(encode(chat, f, indent=4))
        txt_filename = "transcript_" + chat.filename + ".txt"
        txt_filepath = join(self.scripts_dir, txt_filename)
        with self.open_(txt_filepath, open_type="w") as f:
            self.log(("Saving transcript text file at", txt_filepath))
            try:
                f.writelines([script])
            except BaseException:
                with self.open_(txt_filepath, open_type="w", encoding="utf-32",) as f:
                    try:
                        f.writelines([script])
                    except BaseException:
                        self.log(
                            ("Failed to write script: \n", script,), sep="",
                        )
                        pass
                pass

    def log(self, s, end="\n", sep=" ", v=3):
        """
        Event logger with a range of verbosities.
        Always log to file and sometimes log to console too.

        Parameters
        ----------
        s: str
            The message to log.
        end: str, optional
            What to end the string with.
        sep: str, optional
            What to separate tokens in the tuple with, if applicable.
        v: int, optional
            The level of verbosity of this message.
        """

        if type(s) == tuple:
            s = "".join([str(f) + sep for f in s])
        elif type(s) != str:
            s = str(s)

        s += end

        log = "LOG: "[: -v - 2] + "log: "[-v - 2 :]
        log += s

        if v <= self.verbosity:
            print(log, end="")
        with open(
            join(self.logs_dir, "log_" + str(self.get_time()) + ".log",), "a",
        ) as f:
            f.write(s)
