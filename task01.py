import random

print("raqam topish oyini")
sirli_son = random.randint(1, 20)  

while True:
    taxminan = int(input(" 1 dan 20gacha son kiriting:" ))
    if taxminan < sirli_son:
         print("katta son!")
    elif taxminan > sirli_son:
         print("kichik son!")
    else:
         print("togri topdingiz!") 
         breakr