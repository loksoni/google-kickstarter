T=int(input("Enter no. of test cases:"))
num=0
for i in range(0,T):
    F = int(input("Enter first number:"))
    L = int(input("Enter last number:"))
    num=F
    for j in range(F,L+1):
        if num>0 and type(num)==int and '9' not in str(num) and num%9!=0:
            print(num)

        num+=1