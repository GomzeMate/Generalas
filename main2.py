import random

#0
print("véletlen dátum generálása: 2005-2010")

#1 a részek generálása
ev=random.randint(2005, 2010)
honap=random.randint(1, 12)
nap=random.randint(1, 28)
#dátum össze állítása
datum = f"{ev}.{honap:0>2d}.{nap:0>2d}"

#2-3
print(datum)