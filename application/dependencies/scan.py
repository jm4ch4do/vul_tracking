import typing as _t
from typing import Any, Dict, List

import providers.services.osv as _s_osv


class ScanDependencies:
    def __init__(self, osv_scanner: _s_osv.OSVScanner = _s_osv.OSVScanner()):
        self._osv_scanner = osv_scanner

    def __call__(
        self, dependencies: List[Dict[str, str]] = None
    ) -> List[Dict[str, Any]]:
        return self._osv_scanner(dependencies)
