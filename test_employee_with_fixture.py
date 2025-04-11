# test_employee_with_fixture.py
import pytest # type: ignore
from employee import Employee # type: ignore

@pytest.fixture
def employee():
    return Employee("Ashley", "Ramos", 50000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(7000)
    assert employee.annual_salary == 57000
