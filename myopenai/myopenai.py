"""
File: openai.py
Description: A simple wrapper for handling a variety of OpenAI API calls
"""

import base64
import openai
import dotenv
import os


class MyOpenAI:

    def __init__(self):
        dotenv.load_dotenv()
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    @staticmethod
    def read_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def ask(self, model="chatgpt-4o-latest", prompt=None, image=None):
        """ Ask ChatGPT a question
        model: The model to be used
        prompt: The input prompt
        image: An optional image to be read and interpreted"""

        if prompt is not None:
            if image is None:
                completion = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
            else:  # Image is specified

                completion = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": prompt,
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/png;base64,{MyOpenAI.read_image(image)}"},
                                },
                            ]
                        }])

            return completion.choices[0].message.content
        else:
            return None


