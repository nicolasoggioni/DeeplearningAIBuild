import os
import openai
from openai import OpenAI
openai.api_key  = os.environ['OPENAI_API_KEY']

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'))

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content


input="""
Here's the plan.  We get the warhead, 
and we hold the world ransom...
...FOR ONE MILLION DOLLARS!
"""
response = client.moderations
moderation_output = response["results"][0]
print(moderation_output)