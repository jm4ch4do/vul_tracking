import requests as _requests
from behave import given, then, when

BASE_URL = "http://127.0.0.1:8000/"


@given("I create a project through the API")
def step_impl(context):
    url = f"{BASE_URL}/projects"
    for row in context.table:
        payload = {
            "name": row["name"],
            "description": row["description"],
            "created_at": row["created_at"],
        }
        response = _requests.post(url, json=payload)
        assert response.status_code == 201
    context.response = response


@when("I make the following API call")
def step_impl(context):
    row = context.table[0]
    method = row["method"].upper()
    endpoint = row["endpoint"]
    url = f"{BASE_URL}{endpoint}"

    if method == "GET":
        response = _requests.get(url)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

    context.response = response


@then('response contains "{count:d}" records')
def step_impl(context, count):
    assert context.response.status_code == 200
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) == count, f"Expected {count} records, got {len(data)}"


@then('the response should contain the following "{entity}"')
def step_impl(context, entity):
    actual = context.response.json()
    expected = [dict(row.items()) for row in context.table]

    def match_records(actual_record, expected_record):
        return all(
            actual_record.get(k) == expected_record.get(k) for k in expected_record
        )

    for exp in expected:
        assert any(
            match_records(act, exp) for act in actual
        ), f"Missing {entity} record: {exp}"
