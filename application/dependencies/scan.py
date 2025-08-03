import typing as _t
from typing import Any, Dict, List

import application.dependencies as _a_dep
import application.projects as _a_pro
import domain.dependency as _d_dep
import domain.vul as _d_vul
import providers.services.osv as _s_osv


class UpdateVuls():

    def __call__(
        self, dependencies: List[Dict[str, str]] = None
    ) -> List[Dict[str, Any]]:
        deps = _a_dep.GetDependencies()()
        scanned_deps = ScanDependencies()(deps)
        project_ids, dep_ids = self._find_entities_with_vuls(deps, scanned_deps)
        _a_pro.ToogleVulsInProjects()(project_ids)
        _a_dep.ToogleVulsInDependencies()(dep_ids)

    @staticmethod
    def _find_entities_with_vuls(
        deps: _t.List[_d_dep.Dependency],
        scanned_deps: _t.List[_t.Dict[_d_dep.Dependency, _t.List[_d_vul.Vul]]],
    ) -> _t.Tuple[_t.Set[str], _t.Set[str]]:
        """Finds ids for entities that need a change in the is_vul flag"""

        deps_to_toggle = set()
        projects_to_toggle = set()
        for dep in deps:
            vuls = scanned_deps.get(dep.id)
            new_value = False if len(vuls) == 0 else True
            old_value = dep.is_vul
            if new_value == old_value:
                continue
            deps_to_toggle.add(dep.id)
            projects_to_toggle.add(dep.project_id)

        return projects_to_toggle, deps_to_toggle


class ScanDependencies:
    def __init__(self, osv_scanner: _s_osv.OSVScanner = _s_osv.OSVScanner()):
        self._osv_scanner = osv_scanner

    def __call__(
        self, dependencies: List[Dict[str, str]] = None
    ) -> _t.List[_t.Dict[_d_dep.Dependency, _t.List[_d_vul.Vul]]]:
        return self._osv_scanner(dependencies)
