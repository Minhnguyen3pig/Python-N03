a = float(input())
b = float(input())
if a == 0:
    if b == 0:
        print("VSN")
    else:
        print("VN")
else :
    x = -b/a
    x1 = round(x,2)
    print(f"x = {x1}")
