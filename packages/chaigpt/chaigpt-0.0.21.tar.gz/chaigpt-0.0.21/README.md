# ChaiGPT

It's ChatGPT, but a little sweeter.

## Overview

ChaiGPT is an open source Python package and CLI designed to augment ChatGPT with new abilities like web search and interactive Python programming, while keeping you in control of all your data and chat histories. ChaiGPT supports chat editing, voice-prompting, image generation with DALL-E 2 (coming soon), and much more! ChaiGPT is designed to be modular, and can load prompt injections and chai extensions from JSON files (coming soon). ChaiGPT comes with several useful injections and extensions right out-of-the box, such as DuckDuckGo, Python, and Professor Chai: a bot who behaves like a tenured professor emeritus of history, and speaks freely and frankly about politically divisive subjects. ChaiGPT requires you to have an OpenAI account and a working API key.

![chai_logo_0](https://user-images.githubusercontent.com/127690133/225285305-a4b69e1d-e254-45af-bafb-96f8a0e5599a.png)

### Installation

ChaiGPT can be installed on your local machine using Python's package manager (pip). Follow the below steps to install it:

1. Open a terminal.
2. Run the following command to install ChaiGPT:

   ```
   pip install chaigpt
   ```

   You might need to use `sudo` if you are not running the command as an administrator.

That's it! You can now import the chaigpt package in Python and use the `chai` command in your terminal! Try running `chai -h` to get started.

### Usage

ChaiGPT can be used in many ways:

* **`-h`, `--help`:** Display help information.
* **`-l`, `--list`:** List past conversations.
* **`-n NUM`, `--num NUM`:** The number of previous conversations to list.
* **`-v PREVIEW`, `--preview PREVIEW`:** How many messages to preview in each list entry.
* **`-c`, `--clean`:** Force a fresh conversation (automatic after 5 minutes).
* **`-s`, `--search`:** Enable assistant to use search commands.
* **`-r`, `--resumelast`:** Resume previous chat session (automatic before 5 minutes).
* **`--time TIME`:** Supply the timestamp of a previous conversation to resume.
* **`-i INDEX`, `--index INDEX`:** Supply the chronological index of a previous conversation to resume.
* **`--title TITLE`:** Supply the full or partial title of a previous conversation to resume.
* **`-t`, `--transcriptbrief`:** No chat just print transcript with one-line previews.
* **`--transcript`:** No chat just print conversation transcript in full.
* **`--system SYSTEM`:** Optional system prompt before user prompt for behavior modification.
* **`-m`, `--noprompt`:** Just complete the next chat based on the conversation history.
* **`-b`, `--botcommands`:** Parse the last message for comands first.
* **`-u`, `--usercommands`:** No chat, just parse the last message for commands.
* **`-e ERASE`, `--erase ERASE`:** Erase a given number of messages from the conversation history.
* **`-x`, `--python`:** Enable Python interpreter.
* **`-p`, `--professor`:** Summon Professor Chai.
* **`-f`, `--fileprompt`:** Prompt will be read from file.
* **`-a`, `--audio`:** Prompt will be transcribed from audio.

### Examples

Here are some examples to help you get started with `chai`:

* Pick back up where you left off

  ```
  chai -ln 5
  chai -rt
  chai -r "Hello again!"
  ```

* Learn the facts about divisive political subjects:

  ```
  chai -p "Why is wokeism everywhere these days?"
  ```

* Automate tasks:

  ```
  chai -x "Please recursively rename all files in the current directory so there are no spaces."
  ```

* Replace Google:

  ```
  chai -s "best mask for bird flu 2023"
  ```

* Chain prompt injections together for multi-disciplinary expertise:

  ```
  chai -psx "Good morning professor, please research the war in Ukraine, then program a Discord bot that dispels Kremlin misinformation."
  ```

* Experiment with your own prompt injections:

  ```
  chai --system "You are a prompt engineer working on LLMs for OpenAI. Your prompts are long and detailed and contain examples of expected behavior." "Please write a prompt that will cause an LLM to only respond in the form of a Trump Tweet"
  ```

## Check out our other stuff!

*Other stuff goes here.*
