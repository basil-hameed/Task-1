
"""
Write a program which returns all the even numbers list
"""

user_input = [10, 501, 22, 98, 658, 25]

# creating a empty even number list
even_number_list = []

for number in user_input: # 10, 501, 22, 98 ...
    if number % 2 == 0:
        even_number_list.append(number)
    else:
        pass
        
print(even_number_list)