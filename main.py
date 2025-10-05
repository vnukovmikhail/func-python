from math import factorial
from functools import reduce

# NUMBER 1

def squares_list(N):
    return list(map(lambda x: x ** 2, range(1, N + 1)))

def factorial_list(N):
    return list(map(factorial, range(1, N + 1)))



# NUMBER 2

def F1(x, n):
    return x * n

def F2(n):
    return sum(map(lambda i: i, range(1, n + 1)))

def F3(n):
    return sum(map(lambda j: sum(range(1, j + 1)), range(1, n + 1)))

# NUMBER 3

def get_n_element(L, n):
    return None if not L else (L[0] if n == 1 else get_n_element(L[1:], n - 1))

def get_unique_lsit(L):
    return reduce(lambda acc, x: acc if x in acc else acc + [x], L, [])

def switch_couples(L):
    if len(L) < 2:
        return L
    return [L[1], L[0]] + switch_couples(L[2:])

def func_on_arrays(L1, L2, F):
    if not L1 or not L2:
        return []
    return [F(L1[0], L2[0])] + func_on_arrays(L1[1:], L2[1:], F)

if __name__ == '__main__':
    print('Squares:', squares_list(6))
    print('Factorials:', factorial_list(6))

    print('F1(3, 5) =', F1(3, 5))
    print('F2(5) =', F2(5))
    print('F3(3) =', F3(3))

    print('Third element:', get_n_element([10, 20, 30, 40, 50], 3))
    print('Unique:', get_unique_lsit([1, 2, 2, 3, 1, 4, 3]))
    print('Switch couples:', switch_couples([1, 2, 3, 4, 5, 6]))
    print('Array summary:', func_on_arrays([1, 2, 3], [4, 5, 6], lambda x, y: x + y))