# message = 'Hello There. My Name is Çağrı ŞİMŞEK'.split()
# print(message[0])

from pickle import TRUE


# mylist= [1,2,3]
# mylist = ["bir",2,True, 6.5]
# print(mylist)

userA = ["çağrı", 31] # burada iki indexli bir değişken tanımladık.
userB = ["haydar", 25] # burada da aynı işlemi yaptık

users1 = userA + userB #users1 değişkeninde iki değişkeni toplayıp bir değişken elde ettik
print(users1[0]) #burada 0. indexi aldığımızda 4 indexten ilkini bize veriyor.

users2 = [userA + userB] #köşeli parantez kullanarak 2'şer indexli değişkenleri kendi içinde listeledik. yani 0. index bize userA verisini 1. index de userB verisini veriyor.
print(users2[0][1]) # bunu yazdırdığımızda direkt olarak ilk değişkenin içindeki indexi yazdırabiliyoruz. keze [1][1] olsaydı 25 verisi karşımıza çıkacaktı.
