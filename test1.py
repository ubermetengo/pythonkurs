'''
Darie alanı :πr²
Daire Çevresi: 2πr

'''
from typing import Type


r=input("Yarıçapı giriniz:  ")
r=int(r)
π=3.14
alan=float(π*(r**2))
cevre=float(2*π*r)
print("Alan: " +str(alan))
print("Çevre: " +str(cevre))