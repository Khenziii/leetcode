class Solution:
    def __init__(self):
        self.romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        """converts roman numbers to int"""
        num_to_return = 0

        for index, char in enumerate(s):
            num_to_return += self.romans[char]

            # check if the previous character was smaller than the current one
            # if so, multiply it times 2 and substract it from the num_to_return
            # don't substract anything if we're at the first index
            if index == 0:
                continue

            if self.romans[s[index - 1]] < self.romans[char]:
                num_to_return -= self.romans[s[index - 1]] * 2

        return num_to_return
