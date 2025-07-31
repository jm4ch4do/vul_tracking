import datetime as _dt
import typing as _t

import pydantic as _p


class ProjectCreateDTO(_p.BaseModel):
    name: str
    description: str
    created_at: _t.Optional[_dt.date] = _p.Field(default_factory=_dt.date.today)


class ProjectOutputDTO(_p.BaseModel):
    id: str
    name: str
    description: str
    created_at: _dt.date
    since_days: _dt.timedelta

    @_p.field_serializer("since_days", return_type=int)
    def serialize_since(self, td: _dt.timedelta, _info):
        return td.days
