import functions

vize  = int(input("Vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

if vize and final in range(0, 101):
    
    vize = functions.vize_puani(vize)
    final = functions.final_puani(final)
    
    print(f"Vize puanın:  {vize} ")
    print(f"Final puanın: {final}")
    
    ders_notu = functions.ders_notu(vize, final)
    print(f"Ders notunuz: {ders_notu}")
    
else:
    print("Lütfen geçerli bir not giriniz!")
    