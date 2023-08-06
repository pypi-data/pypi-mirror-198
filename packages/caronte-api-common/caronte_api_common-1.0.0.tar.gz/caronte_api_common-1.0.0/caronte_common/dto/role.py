from typing import List, Optional

from pydantic import UUID4, BaseModel  # pylint: disable=E0611


class Role(BaseModel):  # pylint: disable=R0903
    name: str
    claims: List[UUID4]
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
