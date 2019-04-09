

sorular =['Türkiyede kaç yaşından itibaren ehliyet sahibi olabilirsiniz?',
           'Haftanın ilk günü nedir?',
           'Amerikada  denince akla gelen  en ünlü şehri nedir?',
           'Sultanahmet cami nerede bulunur?',
           'Bornova hangi  ilimizde bulunur?']
cevaplar =['A','B','C','D','A']
puan=0
CevapA =["18","salı","orlando","konya","izmir"]
CevapB =["17","pazartesi","miami","izmir","samsun"]
CevapC =["16","cuma","new york city","ankara","van"]
CevapD =["15","pazar","chicago","istanbul","rize"]
CevapE =["19","perşembe","san diego","bolu","antalya"]
for i in range(len(sorular)):
    print("Soru" + str(i+1) + ":" + sorular[i])
    print("A)"+CevapA[i])
    print("B)"+CevapB[i])
    print("C)"+CevapC[i])
    print("D)"+CevapD[i])
    print ("E)"+CevapE[i])
    cevap=input("Cevabınızı yazınız:")
    if cevaplar [i] == cevap.upper():
        puan += 1
print("Soruları cevapladınız.Aldığınız Puan: " + str(int((puan/len(sorular))*100)))