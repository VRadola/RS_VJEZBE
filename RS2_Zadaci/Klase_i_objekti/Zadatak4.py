import math

class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        opseg_kruga = (2 * self.r) * math.pi
        print(round(opseg_kruga, 2))
    
    def povrsina(self):
        povrsina_kruga = (self.r ** 2) * math.pi
        print(round(povrsina_kruga, 2))
    
krug = Krug(4)
krug.opseg()
krug.povrsina()