
def isPrime(n):
    
  m=int(2)
  valor=True;
  while((valor) and (m<n)):

      if((n%m)==0):
          valor=False;
      else:
          m=m+1;
  return valor
   
for i in range(1,20):
    if isPrime(i+1):
        print(i+1,end="  ")
print()
