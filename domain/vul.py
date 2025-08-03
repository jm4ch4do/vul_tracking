import typing as _t

import pydantic as _p


class Vul(_p.BaseModel):
    id: _t.Optional[str] = None
    dependency_id: str
    osv_id: str
    modified: str
    updated: str
