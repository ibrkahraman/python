x = float(input("Derece girin: "))
birim = str(input("fahrenheit ise F celcius ise C yazınız"))
if birim == "C":
    print((x-32)/1.8)
if birim == "F":
    print((x*1.8)+32)