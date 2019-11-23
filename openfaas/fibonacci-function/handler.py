def handle(req):
    a = 0
    b = 1
    num = int(req)
    global eredmeny
    if num < 0:
        print("Incorrect input\n")
    elif num == 0:
        print(str(a))
    elif num == 1:
        print(str(b))
    else:
        for i in range(1,num):
            c = a + b
            a = b
            b = c
        eredmeny = b
        print(str(eredmeny))

