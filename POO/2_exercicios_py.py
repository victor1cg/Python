''' # PROBLEM FROM HACKER RANK
GIVE THE INPUT 


import operator
import pandas as pd



def person_lister(f):                                           #Obrigatorio definir o decorator antes
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))    
    return inner

@person_lister                                                  #esse é o decorator
def name_format(person):
    a = ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
    return a

if __name__ == '__main__':                                      #função disponivel somente quando rodo essa função
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

## -- 2
# All outputs must be +91 xxxxx xxxxx



def wrapper(f):
    def fun(l):
        # complete the function
        decorated_l = ['+91 {} {}'.format(n[-10:-5],n[-5]) for n in l]
        return f(decorated_l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input().split() for _ in range(int(input()))]
    sort_phone(l) '''

a_string = "This is a global variable"

def foo():
    a_string = "test_Local" # 1
    print(a_string)

print(a_string)
