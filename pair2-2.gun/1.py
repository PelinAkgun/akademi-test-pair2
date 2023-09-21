print("iki adet sayi giriniz: ")


sayi1 = int(input(f"ilk sayi : " ))
sayi2 = int(input(f"ikinci  sayi : "))
deger = [ "+" , "-" , "*" , "/"]
print("lütfen hangi işlemi yapmak istediginizi secin:  + , - , * , / ")
a = input()
#print(a)
for i in range (3):
    if a == deger[0]:
        sonuc = (sayi1) + (sayi2)
       
    elif a == deger[1]:
        sonuc = (sayi1) - (sayi2)
    elif a == deger[2]:
        sonuc = (sayi1) * (sayi2)
    elif a == deger[3]:
        sonuc == (sayi1) / (sayi2)
    else : 
        print("Hatalı bir istekte bulundunuz!")
    
print(sonuc)

