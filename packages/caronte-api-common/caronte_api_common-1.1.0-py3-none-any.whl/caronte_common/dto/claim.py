from typing import Optional, Union
from pydantic import UUID4, BaseModel  # pylint: disable=E0611


class Claim(BaseModel):  # pylint: disable=R0903
    name: str
    value: Union[str, int, float]
    external_id: Optional[UUID4] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
