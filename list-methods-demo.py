from re import A


names = ['Ali', 'Yağmur', 'Hakan' , 'Deniz']
years = [1998, 2000, 1998, 1987]
'''
1- 'Cenk' ismini listenin sonuna ekleyin.
2- "Sena" değerini listenin başına ekleyin.
3- "Deniz" ismini listeden silin. 
4- "Deniz" isminin indexi nedir?
5- "Ali" listenin bir elemanı mıdır?
6- Liste elemanlarını ters çevirin.
7- Liste elemanlarını alfabetik olarak sıralayın.
8- years listesini rakamsal büyüklüğe göre sıralayın.
9- str = "Chevrolet, Dacia" karakter dizisini listeye çevirin.
10- years dizisinin en büyük ve en küçük elemanı nedir. 
11- years dizisinde kaç tane 1998 değeri vardır. 
12- years dizisinin tüm elemanlarını silin. 
13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.  
'''
names.append("Cenk") #1
print(names)

names.insert(0,"Sena") #2
print(names)

names.remove("Deniz") #3
print(names)

print(names.index("Yağmur")) #4

print(names.count("Ali")) #5 eğer içinde 1 tane bile varsa bize verecektir. 
print("Ali" in names) # bu da içinde var mı diye sormak için kullanılıyor. asıl cevap bu

print(names[::-1]) #6
names.reverse()
print(names)

names.sort() # 7 - .short methodunu doğrudan print şeklinde çalıştıramadım. ama değişkeni öncesinde sıralayıp yazdırdığımda sıralı verdi. 
print(names)  

years.sort() #8
print(years)

#9 
str="Chevrolet, Dacia"
print(list(str))
str1 = "Chevrolet" , "Dacia"
print(str.split(","))
str2 = "Chevrolet" , "Dacia"
print(list(str2))

#10 
print(min(years),max(years))

#11
print(years.count(1998))

#12
years.clear()
print(years)

#13 
markalar = []  # bunu yaparken bir tane boş liste tanımladık. değişkenleri input opsiyonuyla içeri soktuk ve .append ile sona ekledik. şimdi deneme amacıyla bunları sort da
#edip mevcut listeyi yazdırıcaz.

listA = input("1 tane marka giriniz: ")
markalar.append(listA)
listB = input("1 tane daha marka giriniz: ")
markalar.append(listB)
listC = input("Son olarak 1 marka daha giriniz: ")
markalar.append(listC)

markalar.sort()
print(markalar)
