print("ball toplash oyini")
ball = 0

while True:
    amal = input("ball qoshish uchun '+'yozing toxtatish uchun 'stop':")
    if amal == "+":
        ball += 10
    elif amal == "stop":
        print(f"oyin tugadi. umumiy ball:{ball}")
        break
    else:
        print("faqat '+' yoki 'stop'yozing!")