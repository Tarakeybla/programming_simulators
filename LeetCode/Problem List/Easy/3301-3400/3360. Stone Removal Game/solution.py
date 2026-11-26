class Solution:
    def canAliceWin(self, n: int) -> bool:
        move_number = 0
        for stone_for_player in range(10, 0, -1):
            move_number += 1
            if n - stone_for_player >= 0:
                n -= stone_for_player
            else:
                if move_number % 2 == 0:
                    return True
                else:
                    return False