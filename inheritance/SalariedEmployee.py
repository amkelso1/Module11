"""
Author: Alex Kelso
Date:10/4/2020
program: employee.py

purpose: constructor and method for employee info
"""
from datetime import date
from inheritance import Employee


class SalariedEmployee(Employee.Employee):

    #  Constructor
    def __init__(self, lname, fname, s_date, salary):
        super().__init__(lname, fname)
        self.start_date = s_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
            raise ValueError('Pay rate needs to be greater than current pay rate')
        self.salary = value

    def display(self):
        return Employee.Employee.display(self) + ', ' + str(self.start_date) + ', $' + str(self.salary) + '/yr'

