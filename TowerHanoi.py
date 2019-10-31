#step1: move top n-1 discs from tower-A to tower-B, using a temp tower-C
#step2: move single lowest disc from tower-A to tower-C
#step3: move the remaining n-1 discs from tower-B to tower-C, using tower-A as temp

from typing import TypeVar, Generic, List
T = TypeVar ('T')

class Stack (Generic[T]):
    """
    Generic Stack implementation using a list.
    Supports following operations:
        1. Push
        2. Pop
    """
    def __init__ (self) -> None:
        self._container: List[T] = []
    def push (self, item: T) -> None:
        self._container.append (item)
    def pop (self) -> T:
        return self._container.pop ()
    def __repr__ (self) -> str:
        return repr (self._container)

def tower_hanoi(start:Stack[int], end:Stack[int], temp:Stack[int], n:int ) -> None:
    """
    function to solve Tower of Hanoi using recursion.
    params:
        start    source tower from which the discs should be transfered.
        end      destination tower to which discs should be transfered.
        temp     temporary tower used to transfer.
        n        number of discs in the source tower.
    """
    print_towers(start, temp, end)
    if n == 1:
        end.push(start.pop())
    else:
        tower_hanoi(start, temp, end, n-1) #step1
        tower_hanoi(start, end, temp, 1)   #step2
        tower_hanoi(temp, end, start, n-1) #step3

def print_towers(A:Stack[int], B:Stack[int], C:Stack[int]):
    """
    function to print the towers.
    params:
        A   tower-1.
        B   tower-2.
        C   tower-3.
    """
    print("tower-A: {}".format(tower_A))
    print("tower-B: {}".format(tower_B))
    print("tower-C: {}".format(tower_C))
    print("---------------------------------------------")

if __name__ == "__main__":
    num_discs = int(input("Enter the number of discs to start:"))
    tower_A : Stack[int] = Stack()
    tower_B : Stack[int] = Stack()
    tower_C : Stack[int] = Stack()
    for i in range(num_discs, 0, -1):
        tower_A.push(i)
    tower_hanoi(tower_A, tower_C, tower_B, num_discs)
    print("Result:\n")
    print_towers(tower_A, tower_B, tower_C)