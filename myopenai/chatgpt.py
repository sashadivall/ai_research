"""
Author      : John Rachlin
File        : chatgpt.py
Description : A simple call to chatgpt-4


"""

import myopenai
import dotenv
import os

dotenv.load_dotenv()
client = myopenai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about Artificial Intelligence."
        }
    ]
)

print(completion.choices[0].message.content)

