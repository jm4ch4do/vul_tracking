import typing as _t

import domain.project as _d_pro
import providers.repository.projects as _p_projects


class ToogleVulsInProjects:
    def __init__(self):
        self.repo = _p_projects.ProjectRepo()

    def __call__(self, project_ids: _t.Tuple[str]) -> None:
        self.repo.toggle_vulnerability(project_ids)
