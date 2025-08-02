import datetime as _dt
import typing as _t

import requests as _requests

import domain.vulnerability as _d_vul


class OSVScanner:
    API_URL = "https://api.osv.dev/v1/querybatch"

    def __call__(
        self, dependencies: _t.List[_t.Dict[str, str]]
    ) -> _t.List[_t.Dict[str, _t.Any]]:
        """Queries osv API for vulnerabilities in the provided 'dependencies' list."""
        payload = {
            "queries": [
                {
                    "package": {"name": dep["package"], "ecosystem": "PyPI"},
                    "version": dep["version"],
                }
                for dep in dependencies
                if dep.get("version")
            ]
        }

        response = _requests.post(self.API_URL, json=payload)
        if response.status_code != 200:
            raise Exception(f"OSV API failed: {response.status_code} {response.text}")

        raw_results = response.json().get("results", [])
        return self._format_results(dependencies, raw_results)

    def _format_results(
        self,
        dependencies: _t.List[_t.Dict[str, str]],
        raw_results: _t.List[_t.Dict[str, _t.Any]],
    ) -> _t.List[_t.Dict[str, _t.Any]]:

        enriched_results = []
        now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()

        for dep, res in zip(dependencies, raw_results):
            vulns = res.get("vulns", [])
            formatted_vulns = []
            for vuln in vulns:
                vulnerability = _d_vul.Vulnerability(
                    vuln_id=vuln.get("id"),
                    modified=vuln.get("modified"),
                    updated=now_iso,
                )
                formatted_vulns.append(vulnerability)

            enriched_result = {
                "package": dep["package"],
                "version": dep["version"],
                "vulnerabilities": formatted_vulns,
            }
            enriched_results.append(enriched_result)

        return enriched_results
