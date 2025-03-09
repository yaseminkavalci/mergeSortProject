def merge_sort(dizi):
    if len(dizi) <= 1:
        return dizi

    # Diziyi ortadan ikiye böl
    orta = len(dizi) // 2
    sol = merge_sort(dizi[:orta])
    sag = merge_sort(dizi[orta:])

    # Birleştir ve sırala
    return birlestir(sol, sag)

def birlestir(sol, sag):
    sonuc = []
    i = j = 0

    # İki parçayı karşılaştırarak sırala
    while i < len(sol) and j < len(sag):
        if sol[i] < sag[j]:
            sonuc.append(sol[i])
            i += 1
        else:
            sonuc.append(sag[j])
            j += 1

    # Kalan elemanları ekle
    sonuc.extend(sol[i:])
    sonuc.extend(sag[j:])
    return sonuc

dizi = [16, 21, 11, 8, 12, 22]
sirali_dizi = merge_sort(dizi)
print("Sıralı Dizi:", sirali_dizi)