import pytest

from src.generate_data import PeopleAnalyticsDataGenerator


def test_active_employees_have_payroll_with_nullable_termination_dates():
    tables = PeopleAnalyticsDataGenerator(50, "2022-01-01", "2024-12-31").generate_all()
    active = tables["raw_employees"].query("is_active == True")
    assert not active.empty
    assert set(active.employee_id) <= set(tables["raw_payroll"].employee_id)


@pytest.mark.parametrize("count", [0, -1, True, 1.5])
def test_invalid_population(count):
    with pytest.raises(ValueError):
        PeopleAnalyticsDataGenerator(count)


def test_reversed_dates():
    with pytest.raises(ValueError):
        PeopleAnalyticsDataGenerator(50, "2024-01-01", "2022-01-01")
