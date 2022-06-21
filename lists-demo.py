# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz. 

list1= ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2 - Liste kaç elemanlıdır.

print(len(list1))

# 3 - Listenin ilk ve son elemanı nedir?

print(list1[0])
print(list1[-1])

# 4 - "Mazda" değerini "Toyota" ile değiştirin.

"""list1[-1]= "Toyota" 
print (list1)"""# burda direkt değişkeni baştan tanımlayarak gittik. aşağıda ise .replace fonksiyonunu kullandık.

""" list2 = [item.replace('Mazda', 'Toyota') for item in list1]"""#burası anlaşılacak! 
"""print(list2)"""

# 5 - Mercedes listenin bir elemanı mıdır?

print("Mercedes" in list1)

"""print(list1.index("Mercedes"))""" # burda .index metodunu kullanarak index aratıyoruz. derste bakıcaz. derste in operatörü kullanıldı.


# 6- listenin -2 indexindeki değer nedir.

print(list1[-2])

# 7- Listenin ilk 3 elemanını alın.

print(list1[0:3])

# 8 - Listenin son ii elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.


list1[-2:-1] = ["Toyota","Renault"]
print(list1)

# 9 - listeye "audi" ve "nissan" ekle

print(list1 + ["audi","nissan" ])

# 10 listenin son iki elemanını silin

del list1[-1]
print(list1)

#11 listeyi tersten yadır.
 
print(list1[::-1])