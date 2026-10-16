#xanh sm
km = int(input())
if km <=2:
    tien = 30500
elif km>2 and km <=12:
    tien = 30500 + (km-2)*15200
elif km>12 and km <=25:
    tien = 30500 + 10*15200 + (km-12)*14150
else :
    tien = 30500 + 10*15200 + 13*14150 + (km-25)*12200
print(f"Tien cuoc Xanh SM la {tien}")    
    
