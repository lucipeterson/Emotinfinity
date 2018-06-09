#lucis_emot_gen.py
import random

print("~~Emotinfinity~~")
print("Press Ctrl + C at any time to exit.")

p = input("Start? ")
x = random.choice
eyes = [":", "=", ";"]
nose = ["-", "^", "~"]
mouth = ["(", ")", "|", "[", "]", "{", "}"]

while p == "yes":
    print(x(eyes) + x(nose) + x(mouth)) 

while p == "Yes":
    print(x(eyes) + x(nose) + x(mouth))
