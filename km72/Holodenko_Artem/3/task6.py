import time
a=int(input("Число учнів у першому класі: "))
b=int(input("Число учнів у другому класі: "))
c=int(input("Число учнів у третьому класі: "))
print("Число парт у першому класі: ",(a//2)+(a%2))
print("Число парт у другому класі: ",(b//2)+(b%2))
print("Число парт у третьому класі: ",(c//2)+(c%2))
time.sleep(3)