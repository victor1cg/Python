from sqlmodel import Field, SQLModel
from typing import Optional             #SQLModel e FastAPI são baseado em tipagem


class User(SQLModel, table = True):
        """Represents the User Model"""

        id:Optional[int] = Field(default=None, primary_key=True)
        email:str = Field(unique=True, nullable=False)
        username:str = Field(unique=True, nullable=False)
        avatar:Optional[str] = None
        bio:Optional[str] = None
        password:str = Field(nullable=False)