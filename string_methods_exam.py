website = "http://www.sadikturan.com"
course = "Phyton Kursu: Baştan Sona Phyton Programlama Rehberiniz (40 Saat)"

# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

a = " Hello World "
print(a.strip()) #Başındaki ve sonundaki boşlukları silmek için lstrip ya da rstrip kullanılır. 


# 2- "www.sadikturan.com" içerisindeki sadikturan bilgisi haricindeki her karakteri silin.

print(website[11:21])

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.

print(course.lower())

# 4- "website" içinde kaç tane a karakteri vardır? .count("a")

print(website.count("a"))

# 5- "website" www ile başlayıp com ile bitiyor mu?

print(website.endswith(".com"))
print(website.startswith("wwww"))

# 6- website içinde ".com" ifadesi var mı?

print(website.find(".com"))

# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (.isalpha, isdigit)

print(course.isalpha())
print(course.isdigit())

# 8- "Contents" ifadesini 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz. 
# ljust veya rjust kullanarak da sağına soluna boşluk veya belirtilen karakteri ekleyebiliriz.

print('Content'.center(50,"*"))

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.

print(course.replace(" ","-"))

# 10- "hello world" karakter dizisinin "world" ifadesini "there" olarak değiştirin.

print("Hello World".replace("World","There"))

# 11 - "course" karakter dizisini boşluk karakterlerinden ayırın.

print(course.split("a"))