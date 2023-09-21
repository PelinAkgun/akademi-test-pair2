ilk_sayi = 1
ikinci_sayi =  1
fib = [ 1 , 1]
next= 0
for i in range(2,21):
    next= ikinci_sayi + ilk_sayi
    ilk_sayi = ikinci_sayi
    ikinci_sayi = next
    fib.append(next)
print(fib)


    
