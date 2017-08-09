a = float(input("Please enter the monthly payment: "))
n = float(input("Please enter the current principal: "))
o = float(input("Please enter the interest rate, in decimal form: "))
p = 365.25
q = 30
c = 1

def main(a,n,o,p,q,c):
    b = 1
    for i in range(b):
        k = n*o
        k = k/p
        k = k*q
        k = k+n
        k = k-a
        if k <= 0:
            print(c)
            return c
        else:
            print(k)
            c = c+1
            n = k
            main(a,n,o,p,q,c)

main(a,n,o,p,q,c)
