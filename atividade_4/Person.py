# from atividade_3.modulos.IMC import calc_IMC, classifica_IMC
# from atividade_3.modulos.IMC import calc_IMC, classifica_IMC

import sys

sys.path.append("/home/usuario/Desktop/os_codigos")

from atividade_3.modulos.IMC import calc_IMC, classifica_IMC
from atividade_3.modulos.salario import Salary_controller


from datetime import datetime as dt

class Person:
    """A classe pessoa define o que é uma pessoa na vida real"""

    def __init__(self, name, birth_date, height, weight) -> None:
        
        self.name = name
        self.birth_date = birth_date
        self.height = height
        self.weight = weight

        
    def get_IMC(self):
        return calc_IMC(altura=self.height, peso=self.weight)
    
    def get_class_IMC(self):
        return classifica_IMC(self.get_IMC())

    def get_name(self):
        return(self.name)
    
    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def get_age(self):
        return dt.today().year - dt.fromisoformat(self.birth_date).year
        

class Worker(Person):
    def __init__(self, name, birth_date, height, weight, salary, hours_working):
        super().__init__(name, birth_date, height, weight)
        self.Object_salary = Salary_controller(salary=salary, hours=hours_working)
        self.hours_studied = 0
        self.hours_worked = 0

    def study(self):
        self.hours_studied += 1

    def work(self):
        self.hours_worked += 1




Lucas = Worker("Lucas", "2002-11-05", 1.72, 91, 25, 40)

payment = Lucas.Object_salary.get_payment()
print(payment)

Lucas.Object_salary.salary_increase(50)

print(Lucas.Object_salary.get_payment())
print(Lucas.get_age())