import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API kaha hai love_de")

client = Groq(api_key=my_api_key)

model = os.getenv("MODEL")
if not model:
    raise ValueError("Model to bata")

prompt1 = "Hi!"
prompt2 = "Write an essay on India under 100 words"
prompt3 = "Write a detailed essay on time travel theories in 1000 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {"role": "user", "content": prompt}
    messages = [message]

    response = client.chat.completions.create(
        model=model, messages=messages, max_tokens=100
    )
    # max_tokens sets the limit for the maximum number of tokens the model can generate in its response (in some models: it limits the input as well)

    usage = response.usage

    print(response.choices[0].message.content)

    print(
        f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens} || completions tokens: {usage.completion_tokens} || total tokens: {usage.total_tokens} || Finish reason: {response.choices[0].finish_reason}"
    )
    print("#########################################################")

"""
Finish Reason : stop -> The API returned a complete message 
Finish Reason : length -> The output was cut off because it reached the maximum token limit defined in the API call
"""
