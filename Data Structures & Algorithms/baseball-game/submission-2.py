class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for i in operations:

            if i.lstrip("-").isdigit():
                x.append(int(i))
            
            elif i == "D":
                x.append(x[-1] * 2)
            
            elif i == "C":
                x.pop()
            
            else:
                x.append(x[-2] + x[-1])

        return sum(x)