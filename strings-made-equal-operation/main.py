def swap_operation(string, index) -> str:
    first_char = string[index]
    second_char = string[index + 2]

    new_string = list(string)

    new_string[index] = second_char
    new_string[index + 2] = first_char

    return "".join(new_string)


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        for i in range(2):
            swapped_string = swap_operation(s1, i)
            if swapped_string == s2:
                return True

            if i >= 1:
                break

            swapped_string = swap_operation(swapped_string, i+1)

            if swapped_string == s2:
                return True

        return False
