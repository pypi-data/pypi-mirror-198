import openai

from tiktoken import get_encoding, encoding_for_model
from typing import List
from dotenv import load_dotenv
from jsonpickle import decode
from time import sleep
from os import getenv

MAX_TOKENS = 2 ** 12


class _ChaiMessage(object):
    # TODO: Timestamps in _ChaiMessage
    def __init__(self, content="", role="user", message=None):
        if message is not None:
            self.role = message.role
            self.content = message.content
        else:
            self.role = role
            self.content = content

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"

    def items(self):
        return [("role", self.role), ("content", self.content)]

    def format_injection(injection: dict = {}):
        result = []

        for message in injection:
            if "content" in message.keys() and "role" in message.keys():
                result += [_ChaiMessage(message["content"], message["role"])]

        return result


class _ChaiResponse(object):
    def __init__(self, response: object = None):
        if response is not None:
            self.message = _ChaiMessage(message=response.message)
            self.finish_reason = response.finish_reason
            self.index = response.index
        else:
            self.message = _ChaiMessage(role="assistant")
            self.finish_reason = "stop"
            self.index = 0


"""
This module handles the OpenAI API
"""


class ChaiAI(object):
    """
    This class represents the AI component of Chai 
    and handles its dependences and administration

    Attributes
    ----------

    Methods
    -------
    """

    DEFAULT_TEMPERATURE = 1
    LIMIT_MSG = "[ERROR: CONVERSATION LIMIT REACHED]"
    EMPTY_MSG = "[ERROR: NO PROMPT]"

    def __init__(self):
        load_dotenv()
        openai.api_key = getenv("OPENAI_API_KEY")

    def generate_reply(
        self, history, stream=True, model="gpt-3.5-turbo",
    ):
        def dummy_message():
            dummy_message = _ChaiMessage("Let me think about that...", "assistant")
            sleep(1)
            if stream:
                print(dummy_message.content)
            return dummy_message

        # return dummy_message() # Debug option for no API calls

        # Check if history exists
        if len(history) <= 0:
            if stream:
                print(self.EMPTY_MSG, flush=True)
            return _ChaiMessage(self.EMPTY_MSG, "assistant")

        # Check if history will fit in model
        tokens = self.count_tokens(history)
        if tokens > MAX_TOKENS:
            if stream:
                print(self.LIMIT_MSG, flush=True)
            return _ChaiMessage(self.LIMIT_MSG, "assistant")

        response = self.chat_completion(model=model, messages=history, stream=stream)

        if response.finish_reason == "length":
            if stream:
                print(self.LIMIT_MSG, flush=True)
            response.message.content += self.LIMIT_MSG
            return response.message

        if stream:
            print("")

        return response.message

    def chat_completion(
        self,
        model: str,
        messages: List[_ChaiMessage],
        temperature: float = DEFAULT_TEMPERATURE,
        # n: int = 1,
        stream: bool = False,
        # stop: str or list = None,
        # max_tokens: int = None,
        # presence_penalty: float = 0,
        # frequence_penalty: float = 0,
    ):  # , logit_bias=None, user: str = None):

        dict_messages = [{key: val for key, val in m.items()} for m in messages]

        completion = openai.ChatCompletion.create(
            model=model,
            messages=dict_messages,
            temperature=temperature,
            # n=n,
            stream=stream,
            # stop=stop,
            # max_tokens=max_tokens,
            # presence_penalty=presence_penalty,
            # frequence_penalty=frequence_penalty,
            # logit_bias=logit_bias,
            # user=user,
        )

        if not stream:
            response = _ChaiResponse(completion.choices[0])
        else:
            response = _ChaiResponse()

            for event in completion:
                choice = event.choices[0]
                if "content" in choice.delta.keys():
                    response.message.content += choice.delta.content
                    print(choice.delta.content, end="", flush=True)
                response.finish_reason = choice.finish_reason
                response.index = choice.index

        return response

    def count_tokens(self, messages, model="gpt-3.5-turbo-0301"):
        if type(messages) == str:
            messages = [{"role": "user", "content": messages,}]
        try:
            encoding = encoding_for_model(model)
        except KeyError:
            encoding = get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo-0301":
            num_tokens = 0
            for message in messages:
                num_tokens += 4  # Every message follows {role/name}{content}
                for (key, value,) in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # If there's a name, the role is omitted
                        num_tokens += -1  # Role is always required and always 1 token
            num_tokens += 2  # Every reply is primed with assistant
            return num_tokens
        else:
            raise NotImplementedError(
                f"""\
num_tokens_from_messages() is not presently implemented for model {model}. \
See https://github.com/openai/openai-python/blob/main/chatml.md \
for information on how messages are converted to tokens."""
            )
