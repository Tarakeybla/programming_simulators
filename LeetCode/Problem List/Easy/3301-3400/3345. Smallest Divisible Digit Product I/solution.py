class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if (str(n))[-1] == '0':
                return n
        for _ in range(100):
            if len(str(n)) == 1 and n % t != 0:
                n += 1
            elif len(str(n)) != 1 and int((str(n))[0]) * int((str(n))[1]) % t != 0:
                n += 1
        return n

