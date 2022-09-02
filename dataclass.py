from dataclasses import dataclass


class A:
    def __init__(self, a: int, b: str, c: tuple):
        self.a = a
        self.b = b
        self.c = c

# init -->
@dataclass
class B:
    a: int
    b: str
    c: tuple


A(1,'2',(3,4,5))

B(1,'2',(3,4,5))