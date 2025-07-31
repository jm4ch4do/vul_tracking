import typing as _t

import domain.project as _d_pro
import providers.repository.projects as _p_projects


class AddProject:
    def __init__(self, repo: _p_projects.ProjectRepo = _p_projects.ProjectRepo()):
        self.repo = repo

    def __call__(self, project: _d_pro.Project) -> None:
        self.repo.add_project(project)
