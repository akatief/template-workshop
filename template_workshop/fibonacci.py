class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        ##### YOUR CODE HERE #####
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 0:
            raise ValueError("n must be a positive integer")

        if n in self.mem:
            return self.mem[n]
        if n <= 1:
            return n
        self.mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.mem[n]
        ##########################