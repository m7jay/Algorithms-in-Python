
#different methods to generate fibonacci numbers
from typing import Dict, Generator

fib: Dict[int,int] = {0:0,1:1}

def GetFib (n:int)->int:
    """
    returns nth fibonacci number using recursion
    params:
    n       integer value representing the position in the Fibonacci sequence
    """
    if n not in fib:
        fib[n] = GetFib (n-1) + GetFib (n-2)
    return fib[n]

def fib5 (n:int)->int:
    """
    returns the nth fibonacci number using for loop with O(n) complexity
    params:
    n       integer value representing the position in the Fibonacci sequence
    """
    if n == 0: return 0;
    last = 0;
    next = 1;
    for _ in range(1,n):
        last, next = next, last+next
    return next

def fib6(n:int)->Generator[int,None,None]:
    """
    returns series of fibonacci numbers till n, using for loop with O(n) complexity
    params:
    n       integer value representing the position in the Fibonacci sequence
    """
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1

    for _ in range(1,n):
        last, next = next, last+next
        yield next


print(GetFib(50))
print(fib5(50))
for i in fib6(50):
    print(i)