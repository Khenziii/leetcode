class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        reversed_x = x_str[::-1]

        if reversed_x[-1] == "-":
            reversed_x = f"-{reversed_x}"
            reversed_x = reversed_x[:-1]

        half_of_x_int = int(reversed_x) / 2
        if half_of_x_int * 2 < -(2 ** 31) or half_of_x_int * 2 > 2 ** 31 - 1:
            return 0
        
        return int(reversed_x)

