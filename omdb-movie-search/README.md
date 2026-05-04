# OMDB Movie Search

Merhaba Ben Mert Eşsiz. Yazılım Mühendisliği 4. sınıf öğrencisiyim 
ve bu proje i2i Systems staj başvurusu kapsamında geliştirdiğim 
ilk tam stack web uygulamalarımdan biri.

## Proje Hakkında

OMDB API'sini kullanarak film, dizi ve bölüm arayabileceğiniz 
bir web uygulaması. Kullanıcı arama yapıyor, sonuçlar kart 
şeklinde listeleniyor, üzerine tıklayınca detaylı bilgi açılıyor.

Backend'i Python Flask ile, arayüzü sade HTML/CSS/JS ile yazdım.
Dışarıdan herhangi bir frontend framework kullanmadım — her şeyin
nasıl çalıştığını anlamak istediğim için vanilla JS tercih ettim.

## Öğrendiklerim

Flask ile daha önce küçük şeyler yapmıştım ama bu projede
REST API entegrasyonu, JSON parse etme ve dinamik DOM 
manipülasyonunu bir arada kullanmak oldukça öğreticiydi.
Özellikle hata yönetimi (geçersiz arama, API limiti vb.) 
konusunda dikkatli olmayı öğrendim.

## Özellikler

-  Film, dizi ve bölüm arama
-  Türe göre filtreleme (Movie / Series / Episode)
-  Detaylı film bilgisi: oyuncular, yönetmen, IMDb puanı, özet
-  Sayfalama (Load More)
-  karanlık arayüz

## Kurulum

```bash
pip install -r requirements.txt
python app.py
```

Tarayıcıda `http://127.0.0.1:5000` adresini açıyoruz.

## Kullanılan Teknolojiler

- Python 3 / Flask
- OMDB API
- HTML, CSS, JavaScript (Vanilla)

## İletişim

mail: mertessiz11@gmail.com

 Her türlü geri bildirime açığım. Teşekkürler.