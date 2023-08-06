from typing import List, Optional

from pydantic import UUID4, BaseModel  # pylint: disable=E0611

from caronte_common.dto.claim import Claim
from caronte_common.dto.config import Config
from caronte_common.dto.role import Role
from caronte_common.dto.user import User


class Project(BaseModel):  # pylint: disable=R0903
    name: str
    description: str
    config: Optional[Config] = None
    claims: Optional[List[Claim]] = None
    roles: Optional[List[Role]] = None
    users: Optional[List[User]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    external_id: Optional[UUID4] = None
