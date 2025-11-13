class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbrajanje(self):
        print(self.a + self.b)

    def oduzimanje(self):
        print(self.a - self.b)

    def mnozenje(self):
        print(self.a * self.b)

    def dijeljenje(self):
        if(self.b == 0):
            print("Dijeljenje s 0 nije moguce")
        else:
            print(self.a / self.b)

    def potenciranje(self):
        print(self.a ** self.b)

    def korijenovanje(self):
        print(self.a ** (1/self.b))

k1 = Kalkulator(9 , 2)
k1.zbrajanje()
k1.oduzimanje()
k1.mnozenje()
k1.dijeljenje()
k1.potenciranje()
k1.korijenovanje()