from random import choice

while True:
    print("Hoşgeldiniz..." + " Adam Asmaca Oyununa..."+"Kelimeler Meyve isimlerinden oluşuyor")
    print("Hazırsanız Başlayalım...")

    kelime = choice(["armut", "elma", "çilek"])

    kelime = kelime.upper()
    harfsayisi = len(kelime)

    print("Kelimemiz {} harflidir.".format(harfsayisi))

    tahminler = []
    hata = []

    deneme = 3

    while deneme > 0:

        bosluk = ""

        for harf in kelime:
            if harf in tahminler:
                bosluk = bosluk + harf

            else:
                bosluk = bosluk + " _ "

        if bosluk == kelime:
            print(" DOGRU BILDINIZ.")
            break

        print("Kelimeyi Tahmin Ediniz", bosluk)

        print(deneme, "CANIN KALDI")

        Tahminet= input("Bir Harf Soyleyin...")
        Tahminet= Tahminet.upper()

        if Tahminet == kelime:
            print("DOGRU BILDINIZ")
            break

        if Tahminet in hata:
            print("{} bunu girdin.Baska Bir Harf gir ".format(Tahminet))

        elif Tahminet in kelime:
            rpt = kelime.count(Tahminet)
            print("Dogru.{0} harfi kelimemiz icerisinde {1} kere geciyor".format(Tahminet, rpt))
            tahminler.append(Tahminet)

        else:
            print("Yanlis.Kelimede bu harf yok")
            hata.append(Tahminet)
            deneme = deneme - 1

    if deneme == 0:
        print("Hakkın Bitti... ")
        print("Kelimemiz {} ".format(kelime))

    print("Oyun Sona Eriyor...")

