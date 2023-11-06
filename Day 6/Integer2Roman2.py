class Solution:
    def romanToInt(self, s: str) -> int:
        decimal = 0
        prev_value = 0
        dict1 ={"I": 1,"V":5,"X":10,"L":50,"C":100, "D":500, "M" :1000}
        lenght= len(s)
        for x in reversed(s) :
            value = dict1.get(x, 0)

            if value < prev_value:
                
                decimal -= value
            else:
                decimal += value

            prev_value = value
        return decimal