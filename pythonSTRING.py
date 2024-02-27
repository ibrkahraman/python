print('ALi\'nin evi')

print("""Merhaba
Dünya

!!!""")

print("Merhaba\nDünya")

print("Merhaba\tDünya")

mesaj = "Merhaba"
mesaj2 = "Dünya"
print(mesaj + " " + mesaj2)

print(mesaj[1])
print(mesaj[-1])

print(mesaj[0:5])
print(mesaj[2:4])

print(mesaj[::2])
print(mesaj[::-1])

print(mesaj.upper())
print(mesaj.lower())
mesaj3 = "merhaba"
print(mesaj3.capitalize())

print(mesaj.startswith("me"))
print(mesaj.startswith("Me"))
print(mesaj.endswith("ba"))

print(len(mesaj))
print(len(mesaj + mesaj2))

print("Merhaba" * 10)

isim = "Ali"
yas = "20"
print("{}, {} yaşındadır")
print("{}, {} yaşındadır".format(isim,yas))
print(f"{isim} {yas} yaşındadır")