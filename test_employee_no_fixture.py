# test_employee_no_fixture.py
from employee import Employee # type: ignore

def test_give_default_raise():
    emp = Employee("Ashley", "Ramos", 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    emp = Employee("Ashley", "Ramos", 50000)
    emp.give_raise(8000)
    assert emp.annual_salary == 58000



