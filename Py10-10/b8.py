a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Tam giac deu")
    elif a == b or b == c or a == c:
        print("Tam giac can")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giac vuong")
    else :
        print("Tam giac thuong")
else :
    print("Khong hop le")
