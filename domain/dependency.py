import typing as _t
import pydantic as _p


class Dependency(_p.BaseModel):
    id: _t.Optional[str] = None
    name: str
    version: str
