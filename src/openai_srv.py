from openai import OpenAI
from dotenv import load_dotenv
import os
from models.Prompt import Prompt
load_dotenv()

apikey = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=apikey)


def send_prompt(prompt: Prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are my assistant at my work at KPMG. Act accordingly. If you get a question or assignment, just do it and return the raw answer without any sentences before it or something. I want to integrate you into excel, so return the data in a format that would fit into an excel cell. Thanks!"},
            {"role": "user", "content": str(prompt.prompt)},
            {"role": "user", "content": str(prompt.data)}
    ]
)
    return(str(completion.choices[0].message.content))

