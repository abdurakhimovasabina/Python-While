while True:
    a = float(input("1 - sonni kiriting: "))
    b = float(input("2 - sonni kiriting: "))
    amal = input("hisoblash amalini tanlang:")
    
    if amal == "+":
        print(f"yigindi: {a + b}")

    elif amal == "--":
        print(f"Ayirma: {a - b}")
        
    elif amal == "*":
        print(f"Ko`paytma: {a * b}")
        
    elif amal == "/":
        if b != 0:
            print(f"Bo`linma: {a / b}")
    else:
        print("0 ga bo`lib bo`lmaydi! ")
        
else:
    print("Notug`ri amal tanlandi yoki sonlar kirtilmadi! ")
        
    print("Hisoblashni davom etamizmi? \n1. Ha \n2. Yo`q")
            
    while True:
        
                answer = int(input("Javobingiz: "))
                if answer == 1:
                    break
        
                elif answer == 2:
                    print("Dastur tugadi! ")
                    break
        
                else:
                    print("Javobda faqat 1 yoki 2 tanlanishi kerak!")
                    break