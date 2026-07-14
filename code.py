class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        value = num**(1/2)
        print(int(value))
        if value == int(value):
            
            return True
        return False
            
        
