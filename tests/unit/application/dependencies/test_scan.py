import application.dependencies.scan as _scan


def test_scan_dependencies_returns_vulnerabilities():
    dependencies = [
        {"package": "Django", "version": "3.2.0"},
        {"package": "requests", "version": "2.25.0"},
    ]

    scanner = _scan.ScanDependencies()
    result = scanner(dependencies)

    assert isinstance(result, list)
    assert all("package" in v for v in result)
    assert all("version" in v for v in result)
    assert all("vulnerabilities" in v for v in result)

    django_vuls = next((v for v in result if v["package"] == "Django"), None)
    assert django_vuls is not None
    assert len(django_vuls["vulnerabilities"]) > 0
