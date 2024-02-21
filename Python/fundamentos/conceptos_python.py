
num1 = 42 # Se define una variable num1 con el valor 42
num2 = 2.3 # Se define una variable num2 con el valor 2.3
boolean = True # Se define una variable boolean con el valor True
string = 'Hello World' # Se define una variable string con el valor 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Se define una lista pizza_toppings con los valores 'Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Se define un diccionario person con los valores 'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False
fruit = ('blueberry', 'strawberry', 'banana') # Se define una tupla fruit con los valores 'blueberry', 'strawberry', 'banana'
print(type(fruit)) # Se imprime el tipo de dato de la variable fruit
print(pizza_toppings[1]) # Se imprime el valor en la posición 1 de la lista pizza_toppings
pizza_toppings.append('Mushrooms') # Se agrega el valor 'Mushrooms' a la lista pizza_toppings
print(person['name']) # Se imprime el valor de la llave 'name' en el diccionario person
person['name'] = 'George' # Se cambia el valor de la llave 'name' en el diccionario person por 'George'
person['eye_color'] = 'blue' # Se agrega la llave 'eye_color' con el valor 'blue' al diccionario person
print(fruit[2]) # Se imprime el valor en la posición 2 de la tupla fruit

if num1 > 45: # Si num1 es mayor a 45
    print("It's greater")   # Se imprime "It's greater"
else: # Si no
    print("It's lower") # Si no, se imprime "It's lower"

if len(string) < 5: # Si la longitud de la variable string es menor a 5
    print("It's a short word!")     # Se imprime "It's a short word!"
elif len(string) > 15: # Si no, si la longitud de la variable string es mayor a 15
    print("It's a long word!") # Se imprime "It's a long word!"
else: # Si no
    print("Just right!") # Se imprime "Just right"

for x in range(5): # Se recorre un rango de 0 a 5
    print(x) # Se imprime el valor de x
for x in range(2,5): # Se recorre un rango de 2 a 5
    print(x) # Se imprime el valor de x
for x in range(2,10,3): # Se recorre un rango de 2 a 10 con saltos de 3
    print(x) # Se imprime el valor de x
x = 0 # Se inicializa la variable x en 0
while(x < 5): # Mientras x sea menor a 5
    print(x)  # Se imprime el valor de x
    x += 1 # Se incrementa en 1 el valor de x

pizza_toppings.pop() # Se elimina el último valor de la lista pizza_toppings
pizza_toppings.pop(1) # Se elimina el valor en la posición 1 de la lista pizza_toppings

print(person) # Se imprime el diccionario person
person.pop('eye_color') # Se elimina la llave 'eye_color' del diccionario person
print(person) # Se imprime el diccionario person

for topping in pizza_toppings: # Se recorre la lista pizza_toppings
    if topping == 'Pepperoni': # Si el valor es 'Pepperoni'
        continue # Se continua con la siguiente iteración
    print('After 1st if statement') # Se imprime 'After 1st if statement'
    if topping == 'Olives': # Si el valor es 'Olives'
        break   # Se rompe el ciclo

def print_hello_ten_times(): # Se define una función print_hello_ten_times
    for num in range(10): # Se recorre un rango de 0 a 10
        print('Hello')    # Se imprime 'Hello'

print_hello_ten_times() # Se llama a la función print_hello_ten_times

def print_hello_x_times(x): # Se define una función print_hello_x_times con un parámetro x
    for num in range(x):    # Se recorre un rango de 0 a x
        print('Hello')      # Se imprime 'Hello'

print_hello_x_times(4) # Se llama a la función print_hello_x_times con el parámetro 4

def print_hello_x_or_ten_times(x = 10):  # Se define una función print_hello_x_or_ten_times con un parámetro x con valor por defecto 10
    for num in range(x): # Se recorre un rango de 0 a x
        print('Hello')   # Se imprime 'Hello'

print_hello_x_or_ten_times()  # Se llama a la función print_hello_x_or_ten_times
print_hello_x_or_ten_times(4)  # Se llama a la función print_hello_x_or_ten_times con el parámetro 4


"""
Bonus section
"""

# print(num3) # Se imprime el valor de la variable num3
# num3 = 72 # Se define una variable num3 con el valor 72
# fruit[0] = 'cranberry' # Se cambia el valor en la posición 0 de la tupla fruit por 'cranberry'
# print(person['favorite_team']) # Se imprime el valor de la llave 'favorite_team' en el diccionario person
# print(pizza_toppings[7]) # Se imprime el valor en la posición 7 de la lista pizza_toppings
#   print(boolean) # Se imprime el valor de la variable boolean
# fruit.append('raspberry') # Se agrega el valor 'raspberry' a la tupla fruit
# fruit.pop(1) # Se elimina el valor en la posición 1 de la tupla fruit