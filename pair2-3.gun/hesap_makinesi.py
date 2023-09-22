while True:
    print("iki adet sayi giriniz: ")


    sayi1 = int(input(f"ilk sayi : " ))
    sayi2 = int(input(f"ikinci  sayi : "))
    deger = [ "+" , "-" , "*" , "/" , "%"]
    print("lütfen hangi işlemi yapmak istediginizi secin:  + , - , * , /  , %")
    a = input()
    if a == "q":
         
         break
    for i in range (4):
                    
                        if a == deger[0]:
                            def Toplama(sayi1,sayi2):
                                sonuc = (sayi1) + (sayi2)
                                return sonuc
                            
                
                        if a == deger[1]:
                            def Cıkartma(sayi1,sayi2):
                                sonuc = (sayi1) - (sayi2)
                                return sonuc
                    
                        if a == deger[2]:
                            def Carpma(sayi1,sayi2):
                                sonuc = (sayi1) * (sayi2)
                                return sonuc
                    
                            if a == deger[3]:
                                def Bolme(sayi1,sayi2):
                                    sonuc = (sayi1) / (sayi2)
                                    return sonuc
                    
                        if a == deger[4]:
                            def ModAlma(sayi1,sayi2):
                                sonuc = (sayi1) % (sayi2)
                                return sonuc
                
                
                #print("Hatalı bir istekte bulundunuz!")
                    
    if a == deger [0]:
        print(Toplama(sayi1,sayi2))     
    elif a == deger[1]:
        print(Cıkartma(sayi1,sayi2))
    elif a == deger[2]:
        print(Carpma(sayi1,sayi2))
    elif a == deger[3]:
        print(Bolme(sayi1,sayi2)) 
    elif a == deger[4]:
        print(ModAlma(sayi1,sayi2))
    else : 
         print("Hatalı islem  yaptınız")

