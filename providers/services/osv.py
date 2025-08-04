import datetime as _dt
import typing as _t

import requests as _requests

import domain.dependency as _d_dep
import domain.vul as _d_vul


class OSVScanner:
    API_URL = "https://api.osv.dev/v1/querybatch"
    _cache: _t.Dict[str, _t.Tuple[_t.List[_d_vul.Vul], _dt.datetime]] = {}
    _TTL_SECONDS = 10

    def __call__(
        self, dependencies: _t.List[_d_dep.Dependency]
    ) -> _t.Dict[str, _t.List[_d_vul.Vul]]:
        """Queries osv API for vulnerabilities in the provided 'dependencies' list."""

        cached, to_query = self._get_cached_or_new_results(dependencies)

        if not to_query:
            return cached

        payload = {
            "queries": [
                {
                    "package": {"name": dep.name, "ecosystem": "PyPI"},
                    "version": dep.version,
                }
                for dep in to_query
            ]
        }

        response = _requests.post(self.API_URL, json=payload)
        if response.status_code != 200:
            raise Exception(f"OSV API failed: {response.status_code} {response.text}")

        raw_results = response.json().get("results", [])
        new_results = self._format_results(to_query, raw_results)

        self._update_cache(new_results)

        combined = {**cached, **new_results}
        return combined

    def _get_cached_or_new_results(
        self, dependencies: _t.List[_d_dep.Dependency]
    ) -> _t.Tuple[
        _t.Dict[str, _t.List[_d_vul.Vul]],
        _t.List[_d_dep.Dependency],
    ]:
        cached = {}
        to_query = []
        now = _dt.datetime.now(_dt.timezone.utc)

        for dep in dependencies:
            cache_entry = self._cache.get(dep.id)
            if cache_entry:
                vulns, cached_time = cache_entry
                elapsed = (now - cached_time).total_seconds()
                if elapsed <= self._TTL_SECONDS:
                    cached[dep.id] = vulns
                    continue  # cache valid
                else:
                    del self._cache[dep.id]  # expired, remove cache entry

            to_query.append(dep)

        return cached, to_query

    def _update_cache(self, new_results: _t.Dict[str, _t.List[_d_vul.Vul]]) -> None:
        now = _dt.datetime.now(_dt.timezone.utc)
        for dep_id, vulns in new_results.items():
            self._cache[dep_id] = (vulns, now)

    def _format_results(
        self,
        dependencies: _t.List[_d_dep.Dependency],
        raw_results: _t.List[_t.Dict[str, _t.Any]],
    ) -> _t.Dict[str, _t.List[_d_vul.Vul]]:

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

            results[dep.id] = formatted_vuls
        return results
