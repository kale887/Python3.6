#!/usr/bin/python
0
class Employee:
    """ Common base class for Employee"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.count

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


emp1 = Employee.displayCount()
