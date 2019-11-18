from flask import request

def Fibonacci(n):
    a = 0
    b = 1
    global eredmeny
    if n < 0:
        return "Incorrect input\n"
    elif n == 0:
        return str(a)
    elif n == 1:
        return str(b)
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        eredmeny = b
        return str(eredmeny)

def main():
    n = int(request.args.get('num'))
    ered = Fibonacci(n)
    return ered
