class Solution(object):
    def formatted_correctly(self, number):
        if len(number) != 14:
            return False
        
        if number[0] != "(" or number[4] != ")" or number[5] != " " or number[9] != "-":
            return False

        for i in range(1, 4):
            if not number[i].isdigit():
                return False
        
        for i in range(6, 9):
            if not number[i].isdigit():
                return False
        
        return True
