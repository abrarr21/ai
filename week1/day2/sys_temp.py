import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai love_de")

client = Groq(api_key=my_api_key)

model = os.getenv("MODEL")
if not model:
    raise ValueError("Model to de")

# System Role - case 1
# message_system = {
#     "role": "system",
#     "content": "You are my strict office collegue who happens to be the manaager also",
# }
#
# message = {"role": "user", "content": "I Love You baby"}

# System Role - case 2
message_system = {
    "role": "system",
    "content": "you are media company that specialises in story telling",
}

message = {
    "role": "user",
    "content": "Write a dystopian story about overuse of AI and AI consciousness",
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, temperature=1)

print(response.choices[0].message.content)
