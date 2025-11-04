liste=["a", "b", "c", "d"]
liste2=["e", "f", "g"]


append()
Listenin sonuna eleman ekler.
örn: liste.append("i") 

insert()
Listeye indexe göre eleman ekler.
örn: liste.insert(2, "z")

extend()
Listenin sonuna farklı bir listeyi ekleyerek birleştirir.
örn: liste.extend(liste2)

remove()
Listeden eleman siler. Aynı elemandan birden fazla varsa yalnızca ilk sıradakini siler.
örn: liste.remove("c")

pop()
Listeden eleman siler ancak remove'den farklı olarak indexe göre siler ve sildiği elemanı çıktı olarak verir.
örn: liste.pop(5)

clear()
Tüm listeyi temizler ve boşaltır.
liste.clear()

sort()
Listeyi ilgili parametreye göre sıralar. Bir parametre girilmezse liste alfabetik/sayısal sıraya göre sıralanır.
örn: liste.sort()

reverse()
Listeyi tersine çevirir.
örn: liste.reverse()

count()
İstenen bir elemanın listede kaç defa geçtiğini verir.
örn: liste.count("a") (1 çıktısını verir)

index()
İstenen bir elemanın kaçıncı sırada olduğunu yani indexini verir.
örn: liste.index("a") (a)

len()
Listede kaç eleman olduğunu söyler.
örn: len(liste)

max()
Listedeki en büyük elemanı verir.
örn: max(liste) (Sayılardan oluşan listelerde kullanılır)

max()
Listedeki en büyük elemanı verir.
örn: max(liste) (Sayılardan oluşan listelerde kullanılır)

min()
Listedeki en küçük elemanı verir.
örn: min(liste) (Sayılardan oluşan listelerde kullanılır)


sum()
Listedenin elemanlarını toplar. Yalnızca sayısal listelerde kullanılır.
örn: liste.sum()

copy()
Listenin bir kopyasını oluşturur. Liste üzerinde bir değişiklik yapmak istediğimizde ancak listenin eski halinin de ayrıca kullanılmak istenmesi durumu gibi durumlarda tercih edilir.