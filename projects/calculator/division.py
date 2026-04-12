class Division:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def divide(self) -> int:
        if self.b == 0:
            return 0
        else:
            return self.a / self.b
