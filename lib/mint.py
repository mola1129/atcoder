MOD = 10 ** 9 + 7


class mint:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            mint(self.x + other.x) if isinstance(other, mint) else
            mint(self.x + other)
        )

    def __sub__(self, other):
        return (
            mint(self.x - other.x) if isinstance(other, mint) else
            mint(self.x - other)
        )

    def __mul__(self, other):
        return (
            mint(self.x * other.x) if isinstance(other, mint) else
            mint(self.x * other)
        )

    def __truediv__(self, other):
        return (
            mint(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            mint(pow(self.x, other.x, MOD)) if isinstance(other, mint) else
            mint(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            mint(other.x - self.x) if isinstance(other, mint) else
            mint(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            mint(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            mint(pow(other.x, self.x, MOD)) if isinstance(other, mint) else
            mint(pow(other, self.x, MOD))
        )
