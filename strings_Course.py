from inspect import BoundArguments


website = "http://www.sadikturan.com"
course = "Phyton Kursu: Baştan sona phyton programlama rehberiniz (40 Saat)"
# 1- course karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))
# 2 - website içinden www karakerlerini alın
print(website [7:10])
# 3- website içinden "com" karakterini alın
print(website[-3:])
# 4- course içinden ilk 15 ve son 15 karakteri alın
print(course [:15]), print(course[-15:])
#5 course ifadesindeki karakterleri tersten yazdırın
print(course[::-1])

name, surname, age, job = "Bora" , "yılmaz", 30, "mühendis"
# yukarıdaki değişkenlerle "benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis" yazdırın
print('Benim adım {} {}. {} yaşındayım ve mesleğim {}.'.format(name,surname,age,job)) # parantezi en son kapat ki cereyan yapmasın :)
print(f'Benim adım {name} {surname}. {age} yaşındayım ve mesleğim {job}.')
# "hello world" kelimesindeki w harfini W ile değiştir.

word = "hello world"
print ((word[:6])+"W"+(word[-4:]))
print (word.replace("w","W"))

# abc ifadesini 5 kere yazdır
print("abc"*5)  