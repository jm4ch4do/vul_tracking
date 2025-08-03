import datetime as _dt
import typing as _t

import pydantic as _p


class Project(_p.BaseModel):
    id: _t.Optional[str] = None
    name: str
    description: str
    created_at: _dt.date
    is_vul: bool = False

    @property
    def elapsed_time(self) -> _dt.timedelta:
        """Returns the time elapsed since the project was created."""
        return _dt.date.today() - self.created_at
