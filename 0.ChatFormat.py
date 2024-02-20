import os

from openai import OpenAI
###  from dotenv import load_dotenv, find_dotenv
###  _ = load_dotenv(find_dotenv()) # read local .env file

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    content = response.choices[0].message.content
    token_dict = {
    'prompt_tokens':response['prompt_tokens'],
    'completion_tokens':response['completion_tokens'],
    'total_tokens':response['total_tokens'],
    }
    return content, token_dict

###Exercise Instructions

context = [ {'role':'system', 'content':"""
You are an assistant who\
 responds in the style of a professor.
"""} ]  # accumulate messages

context.append({'role':'user', 'content':"""What is the color of the clouds?"""})
response, tokendict = get_completion_from_messages(context) 
print(response)
print(tokendict)