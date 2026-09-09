class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join([(bin(int(date)))[2:] for date in date.split('-')])