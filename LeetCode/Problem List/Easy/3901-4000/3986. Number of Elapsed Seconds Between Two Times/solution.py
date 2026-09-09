from datetime import datetime

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        return (
            datetime.strptime(endTime, "%H:%M:%S") - 
            datetime.strptime(startTime, "%H:%M:%S")
        ).seconds

startTime = "01:00:00"
endTime = "02:00:25"

test = Solution()
print(test.secondsBetweenTimes(startTime=startTime, endTime=endTime))