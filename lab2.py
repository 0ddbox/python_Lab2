## 2.1
import math
## 1
name = 'Liam McSeveney'
age = 24
height = 6
favorite_color = 'pink'
## 1.2.1
print(name)
print(age)
print(height)
print(favorite_color)
## 1.2.2
print(name, age, height, favorite_color)
## 1.2.3
print(f"my name is {name} I am {age} years old I am {height} feet tall and my favorite color is {favorite_color}")
## 1.2.4
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")
## 1.3
radius = 5
area = math.pi * radius ** 2
area_rounded = round(area,1)

print(area_rounded)
## 2.2
age_squared = math.sqrt(age)

print(age_squared)
## 2.3
height_cos = math.cos(height)
height_sin = math.sin(height)

print('sine: ' + str(height_cos))
print('cosine: ' + str(height_sin))

## 3.1
sum_age = age + 5
print(sum_age)

diff_height = height - 4
print(f'''{diff_height} feet
''')

prod_age_height = age * height
print(prod_age_height)

quo_height = height / 2
print(quo_height)

age_divided = age % 3
print(age_divided)

age_exponent = age ** 2
print(age_exponent)

## 4
fahrenheit = input('enter temperature in fahrenheit: ')
celsius = (int(fahrenheit) - 32) * 5/9
cel_rounded = round(celsius, 1)

print(cel_rounded,"°")
