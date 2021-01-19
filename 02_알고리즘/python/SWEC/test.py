m=[5,7,12,18] 
w=20
class solution(object):
    def __init__(self):
        self.max_weight = 0
        
    def weight(self, m, wt, w):
        self.max_weight = max(self.max_weight, wt)
        if len(m)==0:
            return
        for i in range(len(m)):
            if wt +m[i]<w:
                wt += m[i]
                self.weight(m[i:], wt, w)
                wt -= m[i]

sol = solution()
sol.weight(m,0,w)
print (sol.max_weight)