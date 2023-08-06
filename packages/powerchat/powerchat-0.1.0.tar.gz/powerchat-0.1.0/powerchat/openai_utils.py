import os
import openai

MODEL = "gpt-3.5-turbo"


class OpenAIUtils:
    @staticmethod
    def send_to_openai_api(prompt):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        messages = [{"role": "assistant", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
        )

        reply = response["choices"][0]["message"]["content"]
        return reply
