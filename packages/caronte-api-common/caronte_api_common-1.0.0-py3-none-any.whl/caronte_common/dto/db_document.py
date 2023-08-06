from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Literal, Optional, TypeVar

T = TypeVar("T")


@dataclass
class FieldConfig:  # pylint: disable=R0903
    field_name: str
    params: Dict[str, Any]
    config_type: Literal["create_index"]


@dataclass
class Document(Generic[T]):  # pylint: disable=R0903
    field_config: List[FieldConfig]
    config: Dict[str, Any]
    name: str
    instance: Optional[T] = None
