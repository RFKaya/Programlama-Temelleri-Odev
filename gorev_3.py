arabalar=["Bmw", "Mercedes", "Opel", "Totoya", "Renault", "Audi"]
print("Liste:", arabalar)
print("Eleman sayısı:", len(arabalar))
print("İlk eleman:", arabalar[0])
print("Son eleman:", arabalar[-1])

#listede mazda olmadığı için tam tersini yaptım hocam
arabalar[arabalar.index("Totoya")] = "Mazda"

print("Totoya değeri Mazda olarak değiştiridli:", arabalar)
print("Mercedes listenin elemanı mıdır:", "Mercedes" in arabalar)
print("Sondan ikinci değer:", arabalar[-2])
print("İlk 3 eleman:", arabalar[0], arabalar[1], arabalar[2])

#renault olduğu için yerine citroen ekledim
arabalar[-1] = "Citroen"
arabalar[-2] = "Toyota"
print("Listenin son 2 elemanı değişimi:", arabalar)

arabalar.append("Audi")
arabalar.append("nissan")
print("listenin sonuna audi ve nissan ekledim", arabalar)

arabalar.pop()
print("listenin son elemanı silindi:", arabalar)

arabalar.reverse()
print("liste ters çevirldi", arabalar)