import typing as _t

import pydantic as _p


class Dependency(_p.BaseModel):
    id: _t.Optional[str] = None
    project_id: str
    name: str
    version: str
    is_vul: bool = False
