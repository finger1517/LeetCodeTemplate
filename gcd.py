def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

   