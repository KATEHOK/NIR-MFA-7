from pydantic import BaseModel

class Message(BaseModel):
    user_id: int
    is_from_auth_server: bool
    theme: str
    token: str
    body: str