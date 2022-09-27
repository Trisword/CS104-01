temp = input("What is the temperature today? ")

int(temp)

temp = int(temp)
if temp >= 90:
    print("Wear shorts.")
elif 90 > temp and temp >= 72:
    print("Short sleeves are fine.")
elif 72 > temp and temp >= 50:
    print("Wear a coat.")
elif 50 > temp and temp >= 32:
     print("Wear a heavy jacket.")
else:
     print("Stay inside")
