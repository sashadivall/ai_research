"""
File: openai.py
Description: A simple wrapper for handling a variety of OpenAI API calls
"""

import base64
import openai
import dotenv
import os
import json


class MyOpenAI:

    def __init__(self, instructions):
        dotenv.load_dotenv()
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_message = {
            "role": "system",
            "content": instructions
            }
        

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
                        self.system_message,
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

    def score_multiple_courses(self, course_descriptions: list, model="chatgpt-4o-latest"):
        """Scores multiple course descriptions and returns a list of floating-point scores."""

        descriptions_text = "\n\n".join(
            [f"Course {i+1}: {desc}" for i, desc in enumerate(course_descriptions)]
        )

        messages = [
            self.system_message,
            {
                "role": "user",
                "content": descriptions_text
            }
        ]

        completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )

        # Extract response and parse JSON safely
        response_text = completion.choices[0].message.content
        try:
            scores = json.loads(response_text)  # Convert response to Python list
            if isinstance(scores, dict):
                print(scores)
                return scores["values"], scores["justification"]
            else:
                raise ValueError("Unexpected response format")
        except json.JSONDecodeError:
            raise ValueError("Failed to parse LLM response as JSON")


    def generate_keyphrases(self, course_descriptions: list, model="chatgpt-4o-latest"):
        """Generates key words and phrases for each course description"""
        descriptions_text = "\n\n".join(
            [f"Course {i+1}: {desc}" for i, desc in enumerate(course_descriptions)]
        )

        messages = [
            self.system_message,
            {
                "role": "user",
                "content": descriptions_text
            }
        ]

        completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )

        # Extract response and parse JSON safely
        response_text = completion.choices[0].message.content
        try:
            scores = json.loads(response_text)  # Convert response to Python list
            if isinstance(scores, dict):
                print(scores)
                return scores["values"]
            else:
                raise ValueError("Unexpected response format")
        except json.JSONDecodeError:
            raise ValueError("Failed to parse LLM response as JSON")


