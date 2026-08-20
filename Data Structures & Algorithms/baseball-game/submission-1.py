class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for i in operations:

            if i.lstrip("-").isdigit():
                x.append(int(i))
            
            elif i == "D":
                value = x[-1] * 2
                x.append(value)
            
            elif i == "C":
                x.pop()
            
            else:
                value = x[-2] + x[-1]
                x.append(value)

        return sum(x)