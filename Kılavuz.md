# LEXTR - Kurulum ve Çalıştırma Kılavuzu

Bu kılavuz, LEXTR projesini kurmak ve çalıştırmak için gereken tüm adımları açıklar. Lütfen sırasıyla takip edin.

---

## 📋 İçindekiler

1. [Ön Gereksinimler](#ön-gereksinimler)
2. [Google Gemini API Key Alma](#google-gemini-api-key-alma)
3. [Python Ortamının Kurulması](#python-ortamının-kurulması)
4. [Projenin Çalıştırılması](#projenin-çalıştırılması)
5. [Sorun Çözme](#sorun-çözme)

---

## 🔧 Ön Gereksinimler

Başlamadan önce bilgisayarınızda aşağıdakilerin yüklü olduğundan emin olun:

- **Python 3.10 veya üzeri**: [python.org](https://www.python.org/downloads/) adresinden indirin
- **Git** (opsiyonel): [git-scm.com](https://git-scm.com/download/win) adresinden indirin
- **Metin Editörü veya IDE**: VS Code, PyCharm, vb.
- **İnternet Bağlantısı**: API erişimi için gereklidir

Python yüklü mü kontrol etmek için PowerShell açın ve şunu yazın:

```powershell
python --version
```

---

## 🔑 Google Gemini API Key Alma

LEXTR projesi Google'ın Gemini modelini kullanır. API key almak için bu adımları takip edin:

### Adım 1: Google Cloud Console'a Erişim

1. Tarayıcınızda [Google AI Studio](https://aistudio.google.com/apikey) sayfasına gidin
2. Google hesabınızla giriş yapın (eğer girişli değilseniz)

### Adım 2: API Key Oluşturma

1. **"Get API Key"** (API Key Al) düğmesine tıklayın
2. **"Create API key in new project"** (Yeni projede API key oluştur) seçeneğini tıklayın
3. Sistem otomatik olarak bir API key oluşturacak
4. **Açılır penceredeki key'i kopyalayın** (Copy icon)

### Adım 3: API Key'i Bilgisayarınıza Kaydetme

Oluşturduğunuz API key'i environment variable olarak kaydetmek için:

**Windows (PowerShell) kullanıyorsanız:**

1. PowerShell'i **Yönetici olarak açın**
2. Aşağıdaki komutu çalıştırın (YOUR_API_KEY yerine kopyaladığınız key'i yapıştırın):

```powershell
[Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", "YOUR_API_KEY", "User")
```

**Örnek:**
```powershell
[Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", "AIzaSyD...", "User")
```

3. Değişikliği uygulamak için PowerShell'i **kapatıp yeniden açın**

4. Doğru kaydedildiğini kontrol edin:

```powershell
$env:GOOGLE_API_KEY
```

Eğer API key'iniz ekrana yazdıysa başarılı demektir.

### ⚠️ Güvenlik Uyarısı

- **API Key'inizi kimseyle paylaşmayın**
- **GitHub'a commit etmeyin**
- **Genel projelerinizde gözükmesine dikkat edin**

---

## 🐍 Python Ortamının Kurulması

### Adım 1: Proje Klasörünü Açın

LEXTR projesinin bulunduğu klasöre gidin. PowerShell'de:

```powershell
cd "Konum\Lextr"
```

(Yolunuza göre ayarlayın)

### Adım 2: Virtual Environment Oluşturma

Proje klasörü içinde PowerShell açın ve çalıştırın:

```powershell
python -m venv env
```

Bu komut `env` isminde bir sanal ortam klasörü oluşturacak.

### Adım 3: Virtual Environment'ı Etkinleştirme

Virtual environment'ı etkinleştirmek için:

```powershell
.\env\Scripts\Activate.ps1
```

Başarılı olduğunu anlamak için PowerShell komut satırının başında `(env)` yazan bir prefix göreceksiniz:

```
(env) PS C:\Users\Konum\...>
```

**Eğer hata alırsanız** (execution policy hatası):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Sonra tekrar `.\env\Scripts\Activate.ps1` çalıştırın.

### Adım 4: Gerekli Paketleri Kurma

Virtual environment aktif iken, tüm gerekli paketleri kurun:

```powershell
pip install -r requirements.txt
```

Bu işlem birkaç dakika sürebilir. Paketler indirilen sırada ekranı izleyin.

**İndirme tamamlandıktan sonra kontrol edin:**

```powershell
pip list
```

`google-genai`, `langchain`, `pydantic` gibi paketleri görebilmelisiniz.

---

## ▶️ Projenin Çalıştırılması

Tüm kurulum tamamlandıktan sonra projeyi çalıştırın:

### Adım 1: Virtual Environment Aktif Olduğundan Emin Olun

PowerShell'de komut satırının başında `(env)` prefix'i görmelisiniz. Görmüyorsanız:

```powershell
.\env\Scripts\Activate.ps1
```

### Adım 2: Programı Çalıştırın

```powershell
python main.py
```

Başarılı olduğunda ekranda LEXTR'nin çıktısını göreceksiniz.

### Adım 3: Programı Durdurmak

Program çalışırken `Ctrl+C` tuşlarına basarak durdurun.

---

## 🐛 Sorun Çözme

### Problem 1: "python command not found" hatası

**Çözüm:** Python yüklü değil veya PATH'e eklenmemiş.
- Python'u [python.org](https://www.python.org/downloads/) adresinden indirin
- Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretleyin
- Bilgisayarı yeniden başlatın

### Problem 2: Virtual environment oluştulamıyor

**Çözüm:** Klasörün yazma izni olmayabilir
```powershell
# Klasör izinlerini kontrol edin veya başka bir konuma taşıyın
python -m venv C:\temp\lextr_env
```

### Problem 3: "pip install" hata veriyor

**Çözüm:** pip'i güncelleyin
```powershell
python -m pip install --upgrade pip
```

Sonra tekrar:
```powershell
pip install -r requirements.txt
```

### Problem 4: API Key hatası: "Could not find credentials"

**Kontrol listesi:**
1. Google Gemini API key'i almış mısınız?
2. Environment variable doğru ayarlanmış mı? (Kontrol: `$env:GOOGLE_API_KEY`)
3. PowerShell'i yönetici olarak açıp environment variable ayarladınız mı?
4. Environment variable ayarladıktan sonra PowerShell'i kapatıp yeniden açtınız mı?

**Çözüm:** Tüm adımları tekrar sırasıyla yapın.

### Problem 5: ModuleNotFoundError hatası

**Örnek:** `ModuleNotFoundError: No module named 'langchain'`

**Çözüm:**
1. Virtual environment aktif mü? (Komut satırında `(env)` görebiliyor musunuz?)
2. Aktif değilse:
```powershell
.\env\Scripts\Activate.ps1
```
3. Paketleri tekrar kurun:
```powershell
pip install -r requirements.txt
```

### Problem 6: Gemini API limit hatası

Eğer "quota exceeded" veya benzer bir hata alırsanız:
- API çok hızlı sorgulanıyor olabilir
- main.py dosyasındaki `TIMEOUT` değerini artırın
- Birkaç dakika bekleyip tekrar deneyin

---

## ✅ Kontrol Listesi

Projeyi başlatmadan önce tüm adımları tamamladığınızdan emin olun:

- [ ] Python 3.10+ yüklü
- [ ] Google Gemini API key alınmış
- [ ] API key environment variable'a kaydedilmiş
- [ ] Proje klasörüne gidilmiş
- [ ] Virtual environment oluşturulmuş
- [ ] Virtual environment etkinleştirilmiş (komut satırında `(env)` görüyorum)
- [ ] Paketler kurulmuş (`pip install -r requirements.txt`)
- [ ] `python main.py` ile program başarılı çalışıyor

Tüm kontrol noktaları tamamlandıysa LEXTR'yi kullanmaya hazırsınız! 🎉

---

## 📞 Ek Yardım

Herhangi bir sorun yaşarsanız:

1. **Hata mesajınızı dikkatlice okuyun** - Genellikle sorunun ne olduğunu söyler
2. **Google'da hata mesajını arayın** - Birçok sorun internette çözümü vardır
3. **Proje ekibine başvurun** - Ekip üyeleri: Furkan Yallıç, Remzi Özmen, Said Berk, Tunahan Yılmaz

---

## 📚 Faydalı Linkler

- [Python Resmi Sitesi](https://www.python.org/)
- [Google Gemini API](https://aistudio.google.com/apikey)
- [LangChain Dokümantasyonu](https://python.langchain.com/)
- [Pydantic Dokümantasyonu](https://docs.pydantic.dev/)

---

**Son Güncelleme:** Aralık 2025  
**Sürüm:** 1.0
