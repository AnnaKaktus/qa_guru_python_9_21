import os
from dotenv import load_dotenv
import pydantic


class Creds(pydantic.BaseModel):
    load_dotenv()
    user_name: str = os.getenv("USER_NAME")
    access_key: str = os.getenv("ACCESS_KEY")
    remote_url: str = os.getenv("REMOTE_URL")


creds = Creds()
