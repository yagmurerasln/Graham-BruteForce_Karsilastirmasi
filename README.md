# Convex Hull Karşılaştırması  
**Brute Force vs Graham Scan**

Bu proje, **Convex Hull (Kapalı Çevrim)** problemini çözmek için kullanılan  
**Kaba Kuvvet (Brute Force)** ve **Graham Scan** algoritmalarının  
**teorik ve deneysel** olarak karşılaştırılmasını amaçlayan,  
grafik tabanlı bir Python masaüstü uygulamasıdır.

---

## 📌 Proje Amacı

- Convex Hull probleminin iki farklı algoritma ile çözümünü görselleştirmek
- Algoritmaların **zaman karmaşıklıklarını** deneysel olarak karşılaştırmak
- Teorik analiz ile pratik sonuçların örtüştüğünü göstermek

---

## 🧠 Kullanılan Algoritmalar

### 🔹 Brute Force (Kaba Kuvvet)
- Tüm nokta çiftleri denenir
- Her doğru için tüm noktaların konumu kontrol edilir
- **Zaman karmaşıklığı:** `O(N³)`
- Büyük veri kümeleri için verimsizdir

### 🔹 Graham Scan
- Noktalar sıralanır
- İçbükey noktalar elenerek dışbükey yapı oluşturulur
- **Zaman karmaşıklığı:** `O(N log N)`
- Büyük N değerleri için oldukça verimlidir

---

## 🔄 Orientation (Yön Testi)

Uygulamada kullanılan `orientation(p, q, r)` fonksiyonu:

- Pozitif → Saat yönünün tersine dönüş
- Negatif → Saat yönünde dönüş
- Sıfır → Doğrusal

Bu test:
- Graham Scan’de içbükey noktaların elenmesini
- Brute Force’ta bir kenarın dışbükey yapıya ait olup olmadığının belirlenmesini sağlar

---

## 🖥️ Uygulama Özellikleri

- Kullanıcıdan **nokta sayısı (N)** alma
- Rastgele nokta üretimi
- Graham Scan ve Brute Force algoritmalarını ayrı ayrı çalıştırma
- Convex Hull sonuçlarını renkli olarak çizme
- Algoritma çalışma sürelerini milisaniye cinsinden gösterme
- Performans karşılaştırma grafiği oluşturma

---

## 📊 Performans Karşılaştırması

- Küçük N değerlerinde her iki algoritma çalışabilir
- N arttıkça:
  - Graham Scan kontrollü şekilde artar
  - Brute Force kübik artış nedeniyle hızla yavaşlar

Bu durum teorik karmaşıklık analizleriyle birebir örtüşmektedir.