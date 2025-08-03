import application.dependencies as _a_dep
import domain.dependency as _d_dep


def test_scan_dependencies_returns_vulnerabilities():

    dependencies = [
        _d_dep.Dependency(
            id="d1",
            project_id="p1",
            name="django",
            version="2.2.10",
        ),
        _d_dep.Dependency(
            id="d2",
            project_id="p2",
            name="requests",
            version="2.18.4",
        ),
    ]

    scanner = _a_dep.ScanDependencies()
    result = scanner(dependencies)

    assert len(result) == 2
    assert "d1" in result
    assert "d2" in result

    assert any(len(v) > 1 for v in result.values())
