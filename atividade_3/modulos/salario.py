import time
from .calculadora import Calculadora

class Salary_controller():

    def __init__(self, salary, hours):

        self.Calc = Calculadora()
        self.salary = salary
        self.hours = hours
    
    def salary_increase(self, porcent):
        porcent_increase = self.salary/100 * porcent
        self.salary += porcent_increase

    def salary_desconted(self, porcent):
        porcent_decrease = self.salary/100 * porcent
        return self.get_payment() - porcent_decrease

    def get_payment_dollar(self):
        DOLLAR = 4.81
        return self.get_payment() / DOLLAR
    
    def get_payment_euro(self):
        EURO = 5,39 
        return self.get_payment() / EURO


    def get_payment(self):
       return self.salary*self.hours
    