from src.generate_data import PeopleAnalyticsDataGenerator


def run():
    tables = PeopleAnalyticsDataGenerator(200, "2019-01-01", "2024-12-31", 42).generate_all()
    employees = tables["raw_employees"]
    assert len(employees) == 200 and employees.employee_id.is_unique
    for name, table in tables.items():
        if "employee_id" in table and name != "raw_employees":
            assert set(table.employee_id.dropna()) <= set(employees.employee_id)
    return {
        "synthetic": True,
        "seed": 42,
        "employees": 200,
        "tables": {
            name: {"rows": len(table), "columns": list(table.columns)}
            for name, table in tables.items()
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), ensure_ascii=False, indent=2, allow_nan=False))
