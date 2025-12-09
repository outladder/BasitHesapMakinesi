#!/usr/bin/env python2

print("=== Basit Hesap Makinesi ===")
print("İşlemler: +  -  *  /")

while True:
    try:
        s1 = float(input("Birinci sayı: "))
        islem = input("İşlem (+ - * /): ")
        s2 = float(input("İkinci sayı: "))
    except ValueError:
        print("Hatalı giriş!")
        continue

    if islem == "+":
        print("Sonuç:", s1 + s2)
    elif islem == "-":
        print("Sonuç:", s1 - s2)
    elif islem == "*":
        print("Sonuç:", s1 * s2)
    elif islem == "/":
        if s2 == 0:
            print("0'a bölünmez.")
        else:
            print("Sonuç:", s1 / s2)
    else:
        print("Geçersiz işlem!")

    devam = input("Devam? (e/h): ")
    if devam.lower() != "e":
        break
