import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY environment variable first")

client = OpenAI(api_key=api_key)

prompt = input("Prompt: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
)

print(response.choices[0].message.content)