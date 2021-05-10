import re

str_list = ["2a", "3", "hello", "2", "f4"]

def is_int(obj: str) -> bool:
    return (re.match(r"[0-9]+$", obj) is not None)

def sum_of_ints(items: list) -> int:
    return sum(int(item) for item in items if is_int(item))

def prod(l: list) -> int:
    res = 1
    for e in l:
        res *= e
    return res

def persistence(n: int) -> int:
    iterations = 0
    number = n
    while True:
        if number < 10:
            break
        iterations += 1
        digits = [int(d) for d in str(number)]
        number = prod(digits)
    return iterations
    

def sum_consecutives(items: list) -> list:
    res = []
    for index, item in enumerate(items):
        if index > 0 and items[index-1] == item:
            res[-1] += item
        else:
            res.append(item)

    return res

if __name__ == "__main__":
    #print(sum_of_ints(str_list))
    #print(persistence(524))
    print(sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]))