vize = float(input(f" vize notunuzu girin : "))
final = float(input(f"final notunuzu girin : "))
ortalama = float((vize * 0.4) + (final * 0.6))
if ortalama <50 :
    print(" ortalamanız : " , ortalama , "notunuz FF")
elif (ortalama > 49) &   (ortalama < 60) :
    print("ortalamanız :" ,ortalama ,"notunuz DD")
elif (ortalama >59) & (ortalama < 70):
    print("ortalamanız : " ,ortalama , "notunuz CC")
elif (ortalama >69) & (ortalama <80) :
    print( "ortalamanız : " , ortalama ," notunuz BB")
else :
    print("ortalamanız :" ,  ortalama , " notunuz AA")