from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Query, Header, Security
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader
from pydantic import BaseModel
import openai_srv
import auth
from models.Prompt import Prompt
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

auth.create_db()

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key_header: str = Security(api_key_header)):
    print(api_key_header)
    if auth.is_in_db(api_key_header): return api_key_header
    raise HTTPException(status_code=403, detail="API Key not valid")

def verify_admin_key(api_key_header: str = Security(api_key_header)):
    if auth.is_admin_key(api_key_header): return api_key_header
    raise HTTPException(status_code=403, detail="Wrong admin key")

@app.get("/")
def get_root():
    raise HTTPException(status_code=404)

@app.post("/v1/gpt-prompt")
def gpt_prompt(prompt: Prompt, api_key: str = Security(verify_api_key)) -> str:
    print(prompt.prompt)
    print(prompt.data)
    return openai_srv.send_prompt(prompt)

@app.get("/v1/admin/create_apikey")
def new_key(admin_key: str = Security(verify_admin_key)) -> str:
    return (auth.import_apikey())
