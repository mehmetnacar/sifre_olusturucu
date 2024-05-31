karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random
import time
sifre = ""
sayi = int(input("Kaç karakterli bir şifre istersin?\n"))
time.sleep(2)
for i in range(sayi):
    sifre += random.choice(karakterler)
print(sifre)