def compute_gcd(a,b):
    while b!=0:
        a,b = b, a%b

    return a

print(compute_gcd(48,60))


def fact(n):
    if n<0:
        print('not a valid number')
    else:
        f = 1
        for i in range(1,n+1):
            f = i*f
    return f

print(fact(5))


def fizzbuzz():
    for i in range(1, 101):
        if i%3 == 0 and  i%5 ==0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else:
            print(i)
    
#fizzbuzz()
        
def countvowel(sent):
    c = 0
    for i in sent:
        if i in 'aeiouAEIOU':
            c = c+1
    return c
print(countvowel('hello what are you doing'))


def is_prime(n):
    if n>0:
        t =   int(n**0.5)
        for i in range(2, t+1):
            if n%i == 0:
                return 'not a prime number'
            
        return 'its a prime number'

print(is_prime(9)) 


def fibo(n):
    if n == 0:
        return []
    if n ==1:
        return [0]
    if n == 2:
        return [0,1]
    fs = [0,1]
    for i in range(2,n):
        new_n = fs[-1]+fs[-2]
        fs.append(new_n)

    return fs
print(fibo(5))
        

        