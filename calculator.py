print(
"""-----------
HESAP MAKİNESİ
İşlemler:
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
-----------
""")

numFirst = float(input("Birinci sayı: "))
numSecond = float(input("İkinci sayı: "))
operation = input("Yapmak istediğiniz işlem: ")

if operation == "1":
    print(f"Toplama işleminin sonucu: {numFirst+numSecond}")
elif operation == "2":
    print(f"Çıkarma işleminin sonucu: {numFirst-numSecond}")
elif operation == "3":
    print(f"Çarpma işleminin sonucu: {numFirst*numSecond}")
elif operation == "4":
    print(f"Bölme işleminin sonucu: {numFirst/numSecond}")
else:
    print("Geçersiz işlem, tekrar deneyiniz.")
