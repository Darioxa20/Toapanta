'''
print("Quiero hacer un modulo")

a=int(input("Indique el numero:"))

b=int(input("Indique el numero:"))

print(a+b)'''

'''
if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")'''
    
__counter=0

def sum1(list):
    global __counter
    __counter+=1
    sum=0
    for el in list:
        sum+=el
    return sum

def prod1(list):
    global __counter
    __counter+=1
    prod=1
    for el in list:
        prod*=el
    return prod

if __name__=="_main_":
    print("I prefer to be module, but I can do some tests for you")
    l=[i+1 for i in range(5)]
    print(sum1(l)==15)
    print(prod1(l)==120)