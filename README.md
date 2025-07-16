# OpenAI API Chat Uygulaması
Bu proje, OpenAI'nin GPT modellerini kullanarak basit bir soru-cevap sistemi oluşturur.

## Kod Açıklaması

### Kullanılan Kütüphaneler
```python
from openai import OpenAI  # OpenAI API'sini kullanmak için
import os                  # Sistem ve çevre değişkenleri için
from dotenv import load_dotenv  # .env dosyasından güvenli veri okumak için
```

## Temel Yapılandırma
.env dosyasından API anahtarı güvenli bir şekilde yüklenir

OpenAI istemcisi oluşturulur

## API İsteği

Model: gpt-4o-mini

Temperature: 0 (tutarlı yanıtlar için)

Max Tokens: 256 (yanıt uzunluğu sınırı)

## Örnek Kullanım

Kod, mevsimler hakkında basit bir soru sorar ve AI'dan yanıt alır.


## Kurulum

Gerekli kütüphaneleri yükleyin:

```pip install openai python-dotenv```

.env dosyası oluşturun:

```openai_apikey=your_api_key_here```

Kodu çalıştırın:

```python your_file_name.py```

## Özelleştirme

* temperature değerini değiştirerek (0-1 arası) yanıtların yaratıcılık seviyesini ayarlayabilirsiniz

* max_tokens değerini değiştirerek yanıt uzunluğunu ayarlayabilirsiniz

* messages listesine yeni mesajlar ekleyerek farklı sorular sorabilirsiniz


