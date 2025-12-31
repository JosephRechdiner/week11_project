from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints

class ContactCreate(BaseModel):
    first_name: Annotated[str, StringConstraints(max_length=50)]
    last_name: Annotated[str, StringConstraints(max_length=50)]
    phone_number: Annotated[str, StringConstraints(max_length=20)]

class ContactUpdate(BaseModel):
    first_name: Optional[Annotated[str, StringConstraints(max_length=50)]]
    last_name: Optional[Annotated[str, StringConstraints(max_length=50)]]
    phone_number: Optional[Annotated[str, StringConstraints(max_length=20)]]
