import os

from openai import OpenAI
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content

###Exercise Instructions

