int = 1
float = 1.1
str = "Hello world"
list = ['a', '1']
tuple = ('b', '2')
dict = {'animal': 'cat', 'age': '2'}

list = [int, float, str, list, tuple, dict]
for a in list:
    print(f'{a} is {type(a)}')