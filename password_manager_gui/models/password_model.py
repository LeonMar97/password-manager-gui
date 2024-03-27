from pydantic import BaseModel


class Password(BaseModel):
    website_user_name: str
    website_password: str
    website_url: str
