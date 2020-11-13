"""
Author: Alex kelso
date: 11/12/2020
program: overide_methods.py
purpose:__
"""
from datetime import date
from inheritance import HourlyEmployee
from inheritance import SalariedEmployee


h_employee = SalariedEmployee.SalariedEmployee('Kelso', 'Alex', date.today(), 40000)
print(h_employee.display())
h_employee.give_raise(45000)
print(h_employee.display())
del h_employee

print('\n')

h_employee = HourlyEmployee.HourlyEmployee('Kelso', 'Alex', date.today(), 10.00)
print(h_employee.display())
h_employee.give_raise(12.00)
print(h_employee.display())
del h_employee
