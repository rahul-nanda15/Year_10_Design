def sumFactors(n):
    sum = 1
    for i in range(2,n//2+1):
        if n % i == 0:
            sum = sum + i
    return(sum)


for i in range(2,1000):
    if sumFactors(i) == i:
         print(i)
         print("finished")
   
         

      
