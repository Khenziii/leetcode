class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_string = str(x)

        if len(int_string) % 2 == 0:
            left_side = int_string[:int(len(int_string) / 2)]
            right_side = int_string[int(len(int_string) / 2):]

            right_side_reversed = right_side[::-1]

            if left_side == right_side_reversed:
                return True
        else:
            middle_char_index = int(len(int_string) / 2)
            middle_char = int_string[middle_char_index]

            left_side = int_string[:middle_char_index]
            right_side = int_string[middle_char_index+1:]
           
            if left_side == right_side:
                return True
            
        return False

