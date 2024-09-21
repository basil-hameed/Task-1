
"""
Write a program with classes and methods for calculating the circumference,
take Pi value as private variable
"""

class CircumferenceCalculator:
    def __init__(self, my_list):
        self.my_list = my_list
        self._pi = 3.141
        
    def calculate_circumference(self):
        circumference = 2 * self._pi * 12
        return circumference

user_list = [25, 68, 56]
my_circumference_object = CircumferenceCalculator(user_list)
print(my_circumference_object.calculate_circumference())
