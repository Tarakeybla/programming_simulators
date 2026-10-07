class Solution:
    def countBits(self, n: int) -> list[int]:
        result: list = []
        count = 0
        for numb in range(n + 1):
            for num in self.convert_to_bin(num=numb):
                if int(num) == 1:
                    count += 1
            result.append(count)
            count = 0
        return result

    def convert_to_bin(self, num: int) -> str:
        bin_num = ''
        while num != 0:
            bin_num += f'{num % 2}'
            num = num // 2
        return bin_num
