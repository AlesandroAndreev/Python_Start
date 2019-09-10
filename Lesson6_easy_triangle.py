class Triangle:

    def __init__(self,a,b,c):
        import math
        self.a=a
        self.b=b
        self.c=c
        self.AB = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.BC = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.AC = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)

    def h(self):
        import math
        return (abs((self.b[1]-self.c[1])*self.a[0] +(self.c[0]-self.b[0])*self.a[1] + (self.b[0]*self.c[1] - self.c[0]*self.b[1])))/self.BC

    def s(self):
        return(self.BC*self.h())/2

    def p(self):
        return self.AB + self.BC+ self.AC


t1=Triangle([1,2],[3,4],[4,2])

print(t1.s())
