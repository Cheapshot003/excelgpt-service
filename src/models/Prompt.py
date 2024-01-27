from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str
    temp: float | None = None
    data: str | None = None