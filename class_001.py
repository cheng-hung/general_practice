# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class bank_account:
    
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('Balance is not enough.')
        elif amount < 0:
            raise ValueError('Withdraw amount must be positive.')
        self.balance -= amount

    
        

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print(f'{self.name}: {self.score}')
        


class Person:
    
    def __init__(self, name, job=None, pay=10):
        self.name = name
        self.job = job
        self.pay = pay
        
    def getLastName(cls):
        return cls.name.split(' ')[-1]  ## Use space to split first and last name
    
    def getRaise(self, percent):
        self.pay = int(self.pay*(1+percent))
        return self.pay
    
    
        
        
