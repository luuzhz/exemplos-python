horas = float(input("Horas de estudo por dia: "))

if horas < 2:
    print("Pouco estudo")
elif horas <= 4:
    print("Estudo médio")
else:
    print("Muito estudo")