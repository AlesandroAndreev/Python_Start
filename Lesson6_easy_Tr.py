class Tr:

    def __init__(self,a,b,c,d):
        import math
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.AB = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.BC = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.CD = math.sqrt((d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2)
        self.AD = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)



    def s(self):
        import math
        return ((self.BC + self.AD)/2) + math.sqrt((self.AB**2) - ((self.BC - self.AD)**2)/4)

    def p(self):
        return self.AB + self.BC+ self.CD + self.AD

    def view(self):
        if self.AB == self.CD and self.BC < self.AD:
            print ('AB = {0}, BC = {1}, CD = {2}, AD = {3}, S = {4}, p = {5}'.format(self.AB,self.BC,self.CD,self.AD,self.s(),self.p()))
        else:
            print('Not Tr')


t1=Tr([0,1],[1,2],[2,2],[3,1])

t1.view()
