a = float(input())
b = float(input())
c = float(input())
if a+b>c and a+c>b and b+c>a:
    print("Duoc")
else :
    print("Khong")
    if a + b <c:
        print(f"Vi {a} + {b} <{c}")
    elif a + c <b:
        print(f"Vi {a} + {c} <{b}")
    else :
        print(f"Vi {b} + {c} <{a}")
