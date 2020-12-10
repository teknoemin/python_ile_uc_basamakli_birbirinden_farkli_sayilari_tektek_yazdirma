for alinan_deger in range(100, 1000):
    ilk_kontrol = int(alinan_deger / 100)
    ikinci_kontrol = int((alinan_deger % 100) / 10)
    ucuncu_kontrol = int(alinan_deger % 10)

    if ilk_kontrol != ikinci_kontrol and ilk_kontrol != ucuncu_kontrol and ikinci_kontrol != ucuncu_kontrol:
        print(ilk_kontrol, ikinci_kontrol, ucuncu_kontrol, sep='')