import datetime as _dt
import typing as _t

import requests as _requests

import domain.dependency as _d_dep
import domain.vul as _d_vul


class OSVScanner:
    API_URL = "https://api.osv.dev/v1/querybatch"

    def __call__(
        self, dependencies: _t.List[_d_dep.Dependency]
    ) -> _t.List[_t.Dict[_d_dep.Dependency, _t.List[_d_vul.Vul]]]:
        """Queries osv API for vulnerabilities in the provided 'dependencies' list."""

        payload = {
            "queries": [
                {
                    "package": {"name": dep.name, "ecosystem": "PyPI"},
                    "version": dep.version,
                }
                for dep in dependencies
            ]
        }

        response = _requests.post(self.API_URL, json=payload)
        if response.status_code != 200:
            raise Exception(f"OSV API failed: {response.status_code} {response.text}")

        raw_results = response.json().get("results", [])
        return self._format_results(dependencies, raw_results)

    def _format_results(
        self,
        dependencies: _t.List[_d_dep.Dependency],
        raw_results: _t.List[_t.Dict[str, _t.Any]],
    ) -> _t.List[_t.Dict[_d_dep.Dependency, _t.List[_d_vul.Vul]]]:

        results = {}
        now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()

        for dep, res in zip(dependencies, raw_results):
            vuls = res.get("vulns", [])
            formatted_vuls = []
            for vul in vuls:
                vulnerability = _d_vul.Vul(
                    osv_id=vul.get("id"),
                    modified=vul.get("modified"),
                    dependency_id=dep.id,
                    updated=now_iso,
                )
                formatted_vuls.append(vulnerability)

            results[dep.id] = vuls
        return results
