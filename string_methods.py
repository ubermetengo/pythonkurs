message = 'Hello there. My name is Çağrı ŞİMŞEK.'

print(message)

print(message.upper()) #tüm harfleri büyük yapar .upper()

print(message.lower()) #tüm hargleri küçük yapar .lower()

print(message.title()) #her bir kelimenin ilk harfini büyük yapar .title

print(message.capitalize()) #tümce düzeni, ilk harfi büyük yapar .capitalize

print(message.strip()) #.strip baştaki ve sondaki karakterleri siler.

print(message.split()) #.split her bir string diziyi boşluklarından ayırarak böler, bi nevi bölme (indexlere ayırma.)

print(message.split()[1]) #köşeli parantezdeki sayı her bir kelimeden(indexlerden) seçilenleri alır. 

print(message.split()[1:3])#bu örnekte 1. indexten 3. indexe kadar olan kelimeleri aldı.

print(message.split("e")) #splitteki parantez içerisinde belirtilen (boşsa boşluk üzerinden ya da örnekteki gibi karakter üzerinden) bölerek aktarır. 
# örnekte her e harfinden sonra cümleyi indexlere ayırıyor. 

print(message.split("e")[1:4]) # burda da hem e harfinden indexlendi hem hem de ilk e harfinden sonraki 1(inddexler 0'dan başlıyor) ve 4. index arasını yazdırdık. 

message1 = message.split() #ilgili bölüm zaten splitlere ayırma şeklinde belirlenen bir obje,

message2=' *_* '.join(message1) # .join komutu öncesine " " içerisinde bir karakter dizisi vererek söz konusu karakterlerle split edilen indexleri birleştirir. 

print(message2)

index = message.find("Çağrı") #.find komutuyla string değeri içinde aranan kelimeyi bulur ve index numarasını verir. (BÜYÜK küçük HARF DUYARLILIĞI VARDIR.)

print(index)

isFound = message.startswith("Ç") #.startwith adı üstünde anlaşılacağı üzere belirtilen ifadenin o harfle başlayıp başlamadığını gösterir. 
#bunu print edersek bool bi ifadedir, true veya false olarak gelecektir. 

print(isFound)

isFound = message.startswith("H")

print (int(isFound)) #ilgili bölümde de başına int ekleyerek integer veriye çevirdik. 

isFound = message.endswith("k") #.endwith adı üstünde anlaşılacağı üzere stringin belirtilen ifadeyle bitip bitmediğini gösterir.
#bunu print edersek bool bi ifadedir,
#true veya false olarak gelecektir. 

print (float(isFound)) #sadece float şekline çevirdik bool'u float kesirli ifadeydi noktayla ayrılıyordu. 

print(message.replace("e","E")) # burda da görüldüğü üzere verilen string ifadedeki e harflerini büyüğüyle değiştirdik. 

print(message.replace("Çağrı","Şimşek"))
print(message.center(50,"X")) ##.center methodunu kullanınca ilgili string ifadeyi 50 karakterli bir alanın ortasına yerleştirir "," den sonraki bölümde ise o veriler
#boşlukları neyle doldurabileceğini anlatır. 

"""daha fazlası için https://www.w3schools.com/python/"""
