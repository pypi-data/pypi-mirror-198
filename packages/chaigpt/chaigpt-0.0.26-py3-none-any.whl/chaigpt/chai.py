from sys import argv

from .chai_archive import ChaiArchive

NOTES = f"""\
This command-line toolset implements the \
OpenAI API into several tools and bots.

For an up-to-date-list, run "ch -h". This \
header documents system conventions and to-dos.

TODO: Better titling
TODO: Assistant pip access
TODO: Automated tests
TODO: Search bot
TODO: FracTLDR botswarm (Recursive summarization botswarm)
    Is text too big?
    If yes,
        ask split bot to split text into conceptually distinct partitions.
        If split bot says no,
            Ask the summarization bot to summarize it!
            Then return the summary
        Otherwise,
            for each partition,
                Ask FracTLDR to summarize it!
                Then just return them concatenated together so they each have their own paragraph
    If it's not too much text,
        Just summarize it!
        Then return the summary
TODO: FracTLDR Variants
    Different text requires different prompts for best summarization.
    You wouldn't want the same bot summarizing assembly code as rap lyrics
    Ideally all variants take as input their niche text, and output similarly styled english prose
TODO: GenTLDR botswarm (Generalizable summarization botswarm)
    Ask classification bot which type of text this is
    # Current POR: hardcoded classes
    # Future POR: AI-generated prompt modifications to the FracTLDR botswarm enabling dynamic class creation at runtime
    Depending on which class the text is,
        Ask the variant of FracTLDR which is specialized in this class to summarize it!
TODO: Auto-git botswarm
    Commit decider, commit titler, FracTLDR_Code
TODO: transcriptbrief title search and timestamp search integration
TODO: AI-powered manual for this CLI
TODO: Ensure entire dependency tree is MIT license
TODO: Refactor history to inherit from OpenAI objects
TODO: Break out args handler
TODO: Break out command parser
TODO: Diagram for comparison to other assistants
TODO: generate_and_append_reply do_parse_cmds parameter seems hacky
TODO: Stacktrace summarizer
TODO: Automatic forgetting
TODO: Key input
TODO: ChatCompletion timeout watchdog
\
"""


def _chai():
    """
    This is the main entry point to the program from the 
    command-line. It uses sys.argv to create an instance of 
    ChaiArchive in accordance with the user's command-line arguments.
    """
    # Initialize a new ChatArchive with command-line arguments
    archive = ChaiArchive(argv=argv, verbosity=1)

    chat = archive.get_selected_chat()
    if chat is None:
        return

    archive.log("Starting chat")
    chat.generate_and_append_reply()
