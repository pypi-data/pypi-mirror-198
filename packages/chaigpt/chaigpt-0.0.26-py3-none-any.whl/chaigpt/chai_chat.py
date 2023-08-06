from time import time, localtime, strftime
from duckduckgo_search import ddg
from slugify import slugify
from typing import List
from subprocess import run
from sys import executable
from os.path import join

from .chai_tools import clamp, plural, contains_any, contains_all
from .chai_data import ChaiData

from .chai_bots import (
    ChaiBot,
    NUM_RESULTS,
    introduction_professor,
    introduction_python,
    introduction_search,
    reminder_professor,
    reminder_search,
)

from .chai_ai import _ChaiMessage, ChaiAI

TOOL_PROMPTS = [
    "search",
    "python",
]

CMDS_SEARCH = [
    "summarize_url",
    "search_web",
]

CMDS_PYTHON = [
    "python",
]

BOT_CMDS = CMDS_SEARCH + CMDS_PYTHON
MAX_COMMANDS = 5
LIMIT_ERR = "[ERROR: CONVERSATION LIMIT REACHED]"


class ChaiChat(object):
    """
    This class represents a single chat with Chai and the metadata thereof.

    Attributes
    ----------
    title: str
        A fitting title for the chat.
    chaidata: ChaiData
        The user data directory.
    filename: str
        The most recent filename used to save this chat.
    birthstamp: float
        The time when this chat was birthed.
    touchstamp: float
        The time when this chat was last changed.
    history: list
        A list of dictionaries representing chat messages.
    timestamps: list
        A list of floats representing chat timestamps.
    prompts: dict
        A structure that keeps track of what Chai has been injected with.

    Methods
    -------
    __init__()
        Initializes the chat.
    format_transcript()
        Returns a transcript of the chat in markdown format.
    erase_messages()
        Removes messages from the end of the chat history and updates the birthstamp
    """

    IS_HEADLESS = False
    REMINDER_TIMER = 5  # ChitChats before prompt injection reminders

    def __init__(
        self,
        chaidata: ChaiData,
        ai: ChaiAI,
        bot: ChaiBot,
        title: str = None,
        filename: str = None,
        birthstamp: float = time(),
        touchstamp: float = None,
        history: List[_ChaiMessage] = [],
        timestamps: List[float] = [],
        prompts: dict = {},
    ):
        """
        Initializes the chat.
        TODO: Load data from JSON

        Parameters
        ----------
        chaidata: ChaiData
            The user data directory.
        data: dict
            A dict loaded from a JSON file to load as a ChaiChat, or None
        """

        self.chaidata = chaidata
        self.log = self.chaidata.log
        self.ai = ai
        self.bot = bot

        self.title = title
        self.filename = filename
        self.birthstamp = birthstamp
        self.touchstamp = self.birthstamp if touchstamp is None else touchstamp
        self.history = history
        self.timestamps = timestamps
        self.prompts = prompts

        # self.cmd_funcs = [
        #     self.summarize_url,
        #     self.search_web,
        #     self.run_python,
        # ]
        # self.parse_funcs = [self.parse_python, self.parse_search]
        # self.log((self.cmd_funcs), v=3)
        # self.log((self.parse_funcs), v=3)

    def append_prompt_from_args(self, args):
        prompt = [_ChaiMessage(args.prompt)]

        if args.system is not None:
            prompt = [_ChaiMessage(args.system, "system")] + prompt

        if args.search:
            self.log("Injecting web search capabilities", v=0)
            if "search" not in self.prompts.keys():
                self.prompts["search"] = {
                    "search_reminder_timer": self.REMINDER_TIMER,
                }
            prompt = _ChaiMessage.format_injection(introduction_search) + prompt
        elif "search" in self.prompts.keys():
            self.prompts["search"]["search_reminder_timer"] -= 1
            if self.prompts["search"]["search_reminder_timer"] <= 1:
                self.log("Injecting web search reminder")
                self.prompts["search"]["search_reminder_timer"] = self.REMINDER_TIMER
                prompt = _ChaiMessage.format_injection(reminder_search) + prompt

        if args.python:
            self.log("Injecting Python capabilities", v=0)
            if "python" not in self.prompts.keys():
                self.prompts["python"] = {
                    "pipreqs": [],
                    "interpreter_hist": "",
                }
            prompt = _ChaiMessage.format_injection(introduction_python) + prompt

        if args.professor:
            self.log("Injecting Professor Chai", v=0)
            if "professor" not in self.prompts.keys():
                self.prompts["professor"] = {
                    "professor_reminder_timer": self.REMINDER_TIMER,
                }
            prompt = _ChaiMessage.format_injection(introduction_professor) + prompt
        elif "professor" in self.prompts.keys():
            self.prompts["professor"]["professor_reminder_timer"] -= 1
            if self.prompts["professor"]["professor_reminder_timer"] <= 1:
                self.log("Injecting Professor Chai reminder")
                self.prompts["professor"][
                    "professor_reminder_timer"
                ] = self.REMINDER_TIMER
                prompt = _ChaiMessage.format_injection(reminder_professor) + prompt

        self.append_prompt(prompt)

    def append_prompt(self, prompt: str or _ChaiMessage or List[_ChaiMessage]):
        if isinstance(prompt, str):
            prompt = _ChaiMessage(prompt)
        if isinstance(prompt, _ChaiMessage):
            prompt = [prompt]
        self.history += prompt
        self.chaidata.archive_chat(self)

    def generate_and_append_reply(self, do_parse_cmds=True):
        self.log(
            (
                "\n".join(
                    ["History:"] + [str(m) for m in self.history] + ["End of history."]
                )
            ),
            v=3
        )

        response = self.ai.generate_reply(self.history)

        self.history += [response]
        self.chaidata.archive_chat(self)

        if not contains_any(self.prompts.keys(), TOOL_PROMPTS):
            return  # No commands enabled

        if do_parse_cmds:
            self.parse_cmds()

    def chat(self, prompt):
        self.append_prompt(prompt)
        self.generate_and_append_reply()

    def make_filename(self):
        filename = slugify(self.title).replace("-", "_")
        self.filename = str(self.touchstamp) + "_" + filename

    def erase_messages(self, num_messages_to_erase):
        """
        Removes messages from the end of the chat and updates the birthstamp.
        
        Parameters
        ----------
        num_messages_to_erase: int
            How many messages to erase.
        """
        # Clamp the argument to valid values
        num_messages_to_erase = clamp(num_messages_to_erase, 0, len(self.timestamps))
        # Only trim if the argument is nonzero
        if num_messages_to_erase > 0:
            self.log(
                (
                    "Trimming last",
                    num_messages_to_erase,
                    plural("message", num_messages_to_erase),
                    "from chat",
                )
            )
            self.history = self.history[:-num_messages_to_erase]
            self.timestamps = self.timestamps[:-num_messages_to_erase]
            # Update birthstamp so original doesn't get deleted
            self.birthstamp = self.touchstamp

    def format_transcript(
        self, limit=None, truncation=None, linestart="",
    ):
        """
        Returns a transcript of the chat in markdown format.
        Each message is a blockquote with the date, time, and sender's 
        name in a level 5 header in the top of the blockquote.
        TODO: Format in markdown

        Parameters
        ----------
        limit: int
            The amount of messages to limit the transcription to.
        truncation: int
            The amount of characters to limit each message to.
        linestart: str
            What to start each message with.

        Returns
        -------
        str
            The entire chat history formatted in markdown.
        """

        script = ""
        archive_len = len(self.history)
        if limit is not None and limit < archive_len:
            script_len = limit
        else:
            script_len = archive_len
        for n in range(archive_len - script_len, archive_len):
            at = self.timestamps[n]
            ah = self.history[n]
            script += linestart + strftime("[%A, %m-%d-%Y, %H:%M:%S]", localtime(at))
            script += " [" + ah.role + "]: "
            s = ah.content.strip()
            script += (
                (s[:truncation] + "...") if truncation and len(s) > truncation else s
            ) + "\n"
        return script

    def parse_user_cmds(self):
        self.parse_cmds(reprompt=False)

    def parse_cmds(self, reprompt=True, cmd_chain=0):
        if len(self.history) < 1:
            self.log("No messages to parse for commands")
            return
        cmd, arg = self.parse_msg(self.history[-1].content)
        if cmd < 0:
            return

        cmd_chain += 1
        if cmd_chain > MAX_COMMANDS:
            print(
                f"""\
The maximum allowed number of bot commands in a row is {MAX_COMMANDS}, \
but Chai would like to keep going. To allow {MAX_COMMANDS} more \
bot {plural('command', MAX_COMMANDS)}, use the -b flag."""
            )
            return

        result = self.run_cmd(cmd, arg)
        if result[0].role == "quit":
            return

        self.append_prompt(result)
        if not reprompt:
            return

        self.log("Reprompting with command output")
        self.generate_and_append_reply(do_parse_cmds=False)
        self.log("Parsing message for commands")
        self.parse_cmds(reprompt=reprompt, cmd_chain=cmd_chain + 1)

    def parse_msg(self, text):
        # parse_results = [parse_func(text) for parse_func in self.parse_funcs]

        parse_result_python = self.parse_python(text)
        self.log(("parse_result_python: ", parse_result_python), sep="")

        parse_result_search = self.parse_search(text)
        self.log(("parse_result_search: ", parse_result_search), sep="")

        parse_results = [
            parse_result_python,
            parse_result_search,
        ]

        self.log(("parse_results: ", parse_results), sep="")

        for parse_result in parse_results:
            cmd, arg = parse_result
            if cmd >= 0:
                self.log(("Found", BOT_CMDS[cmd], "command"))
                return cmd, arg

        return -1, ""

    def parse_search(self, message):
        for line in message.split("\n"):
            for cmd in CMDS_SEARCH:
                if cmd + "(" in line.lower():
                    query = line[line.lower().index(cmd + "(") + len(cmd) + 1 :].strip()
                    if ")" in query:
                        query = query[: query.index(")")]
                    return (
                        self.cmd_id(cmd),
                        query,
                    )
        return -1, ""

    def parse_python(self, message):
        if not contains_all(message, ["python", "```"]):
            return -1, ""

        message = message.split("```")
        message = [message[n] for n in range(len(message)) if n % 2 != 0]
        message = "".join(message)
        message_trim = message.replace("python3", "", 1)
        if len(message_trim) == len(message):
            message_trim = message.replace("python", "", 1)

        return (
            self.cmd_id("python"),
            message_trim,
        )

    def cmd_id(self, cmd):
        if cmd not in BOT_CMDS:
            return

        return BOT_CMDS.index(cmd)

    def summarize_url(self, query):
        if "search" not in self.prompts:
            return [_ChaiMessage("", "quit")]

        url = query.split()[0]
        # The URL is the first token
        query = query[len(url) :].replace(",", "").strip().strip('"').strip("'")
        # The rest is a question to ask the summarization bot
        url = url.replace(",", "").strip().strip('"').strip("'")

        return [_ChaiMessage(self.bot.summarize_webpage(url, query), "system")]

    def search_web(self, query, num_results=NUM_RESULTS):
        if "search" not in self.prompts:
            return [_ChaiMessage("", "quit")]

        query = query.strip('"').strip("'")

        summary = f"""Search results for "{query}":\n\n"""
        for n, result in enumerate(ddg(query)[:num_results]):
            summary += f"""\
    Title: {result["title"]}\nURL: {result["href"]}\n{result["body"]}\n\n"""

        summary += """\
    Here are your search results. Use summarize_url to learn more"""

        if not self.IS_HEADLESS:
            print(summary)

        return [_ChaiMessage(summary, "system")]

    def run_python(self, script):
        if "python" not in self.prompts:
            return [_ChaiMessage("", "quit")]

        script = script.strip() + "\n"
        num_lines = script.count("\n")

        prev_script = self.prompts["python"]["interpreter_hist"]
        num_lines_prev = 0

        filename = "transcript_" + self.filename + "_pyscript_" + str(time()) + ".py"
        filepath = join(self.chaidata.scripts_dir, filename)

        with open(filepath, "w") as f:
            f.write(script)

        while True:
            user_input = input(
                f"""\
Chai wants to execute {num_lines} line\
{("s" if num_lines > 1 else "")} of \
{"new" if num_lines_prev > 0 else "python"} code. \
Will you allow Chai to execute this code?
([Y]es/[N]o/[P]rint the code/Open with e[X]plorer)\n: """
            ).lower()[:1]
            if user_input == "y":
                break
            if user_input == "p":
                print("\n" + script + "\n")
            if user_input == "x":
                # p = run(["open", filepath], check=True)
                p = run(["explorer.exe", filepath])
            if user_input == "n":
                return [_ChaiMessage("", "quit")]

        with open(filepath) as f:
            new_script = f.read()
            if new_script:
                script = new_script

        num_lines = script.count("\n")
        full_script = (
            prev_script
            + f"""\n# \
    {self.history[-1].role} added {num_lines} \
    line{("s" if num_lines > 1 else "")}: \n"""
            + script
        )

        self.prompts["python"]["interpreter_hist"] = full_script

        p = run([executable, filepath], capture_output=True, text=True)
        output = (p.stdout + p.stderr).replace(filename, "pyscript.py")

        if not self.IS_HEADLESS:
            print(output)
        return [_ChaiMessage(output, "system")]

    def run_cmd(self, cmd, arg):
        if cmd == 0:
            return self.summarize_url(arg)
        if cmd == 1:
            return self.search_web(arg)
        if cmd == 2:
            return self.run_python(arg)

        # self.log(("in run_cmd, self.cmd_funcs[cmd] is", self.cmd_funcs[cmd]), v=3)
        # return self.cmd_funcs[cmd](arg)
