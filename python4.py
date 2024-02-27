import random

kelimeler = ('ibrahim', 'ali', 'muhammed', 'salih', 'ahmet', 'yusuf')
secilen_kelime = random.choice(kelimeler)
gecerliHarfler = "abcçdefgğhıijklmnoöprsştuüvyz"
toplamHak = 5
yapilanTahmin = ""
while toplamHak > 0:
    gercekKelime = ""
    for harf in secilen_kelime:
        if harf in yapilanTahmin:
            gercekKelime += harf
        else:
            gercekKelime +="_ "
    
    if gercekKelime == secilen_kelime:
        print(gercekKelime)
        print("kazandın")
        break

    print([5 - toplamHak])
    print("kelimeyi tahmin edin", gercekKelime)
    print(f"kalan hakkınız: {toplamHak}")

    tahmin = input("harf tahmin et: ")

    if tahmin in gecerliHarfler:
        yapilanTahmin += tahmin
        if tahmin not in secilen_kelime:
            toplamHak -= 1
    else:
        print("Lütfen geçerli bir harf giriniz...")
 
else:
    print("Maalesef kaybettiniz. Doğru kelime:", secilen_kelime)