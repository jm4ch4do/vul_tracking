import datetime as _dt

import pydantic as _p


class ProjectOutputDTO(_p.BaseModel):
    id: str
    name: str
    description: str
    created_at: _dt.date
    since_days: _dt.timedelta

    @_p.field_serializer("since_days", return_type=int)
    def serialize_since(self, td: _dt.timedelta, _info):
        return td.days
