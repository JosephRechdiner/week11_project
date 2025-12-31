from typing import Optional
from pydantic import BaseModel, Field

class ContactCreate(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    phone_number: str = Field(max_length=20)

class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(max_length=50)
    last_name: Optional[str] = Field(max_length=50)
    phone_number: Optional[str] = Field(max_length=20)
