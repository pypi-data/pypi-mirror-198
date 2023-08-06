import openai
import os
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.getenv("OPENAI_KEY")


class Regext:
    def __init__(self, model: str = "gpt-3.5-turbo", enable_test=True):
        self.model = model
        self.response = None
        self.answer = None
        self.enable_test = enable_test

    def __call__(self, text: str):
        if self.response is not None:
            self.response = None

        self.response, self.answer = self._chat(text)

        if self.enable_test:
            if "[EXAM]" not in text and "[WANT]" not in text:
                raise ValueError(
                    "You need to provide at least one [EXAM] and [WANT] to test your regex.")

            self.text = text
            t, f = 0, 99
            iteration = 1
            while t < f:
                print(f"Iteration: {iteration}")
                t, f = self._test()
                print(f"Total: {t + f}, True: {t}, False: {f}")
                self.response, self.answer = self._chat(text)

                iteration += 1

            return self.answer
        return self.answer

    def _chat(self, text: str):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": self._prompt(text)
                }
            ],
            temperature=0.1,
            max_tokens=200,
            top_p=0.7,
        )

        answer = response["choices"][0]["message"]["content"]

        return response, answer

    def _test(self):
        import re
        examples, wants = self._parser(self.text)
        t, f = 0, 0

        for example, want in zip(examples, wants):
            if not isinstance(want, list):
                want = [want]
            if re.findall(self.answer, example)[0] is None:
                f += 1
            elif re.findall(self.answer, example) != want:
                f += 1
            else:
                t += 1

        return t, f

    def _parser(self, text: str):
        lines = text.splitlines()
        exam = []
        want = []

        for line in lines:
            if line.startswith("[EXAM]"):
                exam.append(line[6:].strip())
            elif line.startswith("[WANT]"):
                if ";;" in line:
                    want.append(line[6:].strip().split(";; "))
                else:
                    want.append(line[6:].strip())

        return exam, want

    def _prompt(self, text: str):
        return f"""\
You are assistant that really good at regex. Your task is to write a regex that \
corresponds to the following description. You can use any regex syntax you want as long as it is \
valid and works as expected. You only need to write the regex pattern. Answer correctly!

The user will use a code [DESC] to input a description in natural language. \
Your task is to write a regex that matches the description. \

The user will also use a code [EXAM] to input a string example and [WANT] to input the wanted \
output. Your task is to write a regex that matches the example and outputs the wanted output. \

User can user all of the code [DESC], [EXAM] and [WANT] at the same time, also can to only \
use [DESC] only, or use [EXAM] and [WANT] only.

DO NOT OUTPUT ANY OTHER STRING OTHER THAN THE REGEX PATTERN.

---

Example 1:
[DESC] A string that only contains the word "hello"
[EXAM] hello world
[WANT] hello

output: hello

---

Example 2:
[EXAM] My number is 123456789
[WANT] 123456789

output: \d+

---

Below is the actual input from the user:
{text}

output: 
"""
