from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import openai_srv
from models.Prompt import Prompt



app = FastAPI()

@app.get("/")
def get_root():
    return ("TEST")

@app.post("/v1/gpt-prompt")
async def gpt_prompt(prompt: Prompt) -> str:
    print(prompt.prompt)
    print(prompt.data)
    return openai_srv.send_prompt(prompt)

