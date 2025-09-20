print("""***************************
Oluşturulan bir parolanın “güçlü” kabul edilebilmesi için aşağıdaki özellikleri göstermelidir.
En az 8 karakterden oluşur.
Harflerin yanı sıra, rakam ve “?, @, !, #, %, +, -, *, %” gibi özel karakterler içerir.
Büyük ve küçük harfler bir arada kullanılır.
Bu kurallara uygun parola oluştururken genelde yapılan hatalardan dolayı saldırganların ilk olarak denedikleri parolalar vardır. Bu nedenle parola oluştururken aşağıdaki önerileri de dikkate almak gerekir.

Kişisel bilgiler gibi kolay tahmin edilebilecek bilgiler parola olarak kullanılmamalıdır. (Örneğin doğum tarihiniz, çocuğunuzun adı, soyadınız, …. gibi)
Sözlükte bulunabilen kelimeler parola olarak kullanılmamalıdır.
Çoğu kişinin kullanabildiği aynı veya çok benzer yöntem ile geliştirilmiş parolalar kullanılmamalıdır.



***************************
""")
password=input("Password:")
point=0
has_letter = False
has_digit = False
has_symbol = False
if len(password)>7:
    point+=1
for i in password:
    if i.isalpha():
        has_letter = True
    elif  i.isdigit():
        has_digit = True
    else :
        has_symbol = True
if has_letter == True:
    point+=1
if has_digit == True:
    point+=1
if has_symbol == True:
    point+=1
if point ==4:
    print("Çok güçlü şifre")
if point == 3:
    print("Güçlü şifre")
if point == 2:
    print("Zayıf şifre")
if point ==1 or point==0:
    print("Çok zayıf şifre")
