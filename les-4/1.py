import sys

f_obj, name_v, rate_v, hours_v = sys.argv
print(f_obj)

def calculate(rate, hours):
    try:
        print(f' {name_v} заработал {int(rate) * int(hours) * 1.25}')
    except TypeError:
        print("Ошибка")
        exit()

calculate(rate_v, hours_v)