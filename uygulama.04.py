metin="Açık bilim,araştırma çıktılarına ve süreçlerine herkesin serbetçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:20])

liste=["Açık Bilim","Açık Erişim","Açık Lisans","Açık Eğitim","Açık Veri","Açık Kültür"]
for i in liste:
    print(i)

sozluk={"Elma":"Ağaçta yetişen bir tür meyve","Salatalık":"Fidan üzerinde büyüyen bir tür sebze"}
kullanıcı =input("Kelime yaz:...")
if kullanıcı == "Elma":
    print ("Ağaçta yetişen bir tür meyve")
elif kullanıcı == "Salatalık":
    print("Fidan üzerinde büyüyen bir tür sebze")
else:
        print("Sozlukte kelime yok")


