class Subtraction:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def minus(self) -> int:
        if self.a > self.b:
            return self.a - self.b
        else:
            return self.b - self.a
