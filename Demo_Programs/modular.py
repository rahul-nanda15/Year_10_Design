newlist = []
finallist = []
def get_factors(x):
   for i in range(1, i+1):
       if x % i == 0 and i != x:
           newlist.append(i)

def addlist():
    sumlist = sum(newlist)
    def perfectnum():
        for n in range(2,1000):
            if n == sumlist:
                finallist.append(n)
                print(finallist)

get_factors(x)
addlist()
perfectnum()
            
    
    


         


