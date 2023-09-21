def Mukemmel() :

    sayi = int(input(f" 0'dan büyük bir sayi giriniz: ") )
    n = sayi
    toplam = 0
    for i in range (1,n-1):
        if (sayi % i ) == 0:
              toplam = toplam + i
        else :
             continue
    if sayi == toplam :
         print("mükemmel sayidir !" , toplam)
    else :
         print("mukemmel sayi degildir")
             
Mukemmel()