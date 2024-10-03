# BoxMOT: Nesne Tespiti ve Takibi İçin Gelişmiş Bir Kütüphane

## Genel Bakış
Nesne tespiti ve takibi üzerine çalışmalarınızı geliştirmek için [BoxMOT](https://github.com/mikel-brostrom/boxmot.git) kütüphanesini öneriyorum. Bu Python kütüphanesi, nesne tespiti, sınıflandırma ve poz tahmini modelleriyle entegre olarak çoklu nesne takip yöntemleri sunar. Hem güçlü GPU donanımlarına sahip sistemlerde hem de sınırlı donanım kaynaklarına sahip ortamlarda çalışabilen çeşitli takip algoritmaları ve ReID (Re-Identification) modellerini destekler.

### BoxMOT’nin Kullanım Alanları
BoxMOT, özellikle otonom sistemler ve askeri uygulamalar için kritik öneme sahiptir. Örneğin, savaşan İHA'lar (İnsansız Hava Araçları) gerçek zamanlı nesne tespiti ve takibi ile hedef analizi yaparak görevlerini daha etkili bir şekilde yerine getirebilirler. BoxMOT, bu tür uygulamalar için esnek, hızlı ve verimli çoklu nesne takip modülleri sağlar.

## Nesne Tespiti ve Takibi
BoxMOT, **YOLOv8, YOLOv9 ve YOLOv10** gibi popüler nesne tespiti algoritmalarıyla kolayca entegre edilebilir. Bu modeller, görüntülerdeki nesneleri (araçlar, insanlar, dronlar vb.) hızlı ve doğru bir şekilde tespit eder. BoxMOT içindeki takip modülleri sayesinde, tespit edilen nesneler videolarda veya gerçek zamanlı akışlarda takip edilebilir.

**Örnek Uygulamalar:**
- İHA'lar, tespit ettiği bir hedefi sürekli olarak izleyerek hedefin hareketlerini ve konumunu belirleyebilir.
- Hedef kaybolduğunda veya örtüldüğünde, BoxMOT’nin takip algoritmaları sayesinde hedefin olası hareketleri tahmin edilerek takip sürdürülebilir.

## Desteklenen Takip Algoritmaları
BoxMOT, birçok state-of-the-art (SOTA) takip algoritmasını içerir. Bunlardan bazıları:
- **BoTSORT**
- **StrongSORT**
- **ByteTrack**
- **OCSORT**
- **DeepOCSORT**

Bu algoritmalar, performans ve hız açısından farklı donanım gereksinimlerine uygun şekilde tasarlanmıştır. Savaşan İHA'ların donanım kısıtlamalarına göre en uygun takip yöntemini seçmek mümkündür.

## ReID (Re-Identification) Kullanımı
**ReID (Re-Identification)**, bir nesneyi veya kişiyi farklı kamera açılarında veya farklı zamanlarda tekrar tanımlayabilme yeteneğidir. BoxMOT, hem ağır (CLIPReID) hem de hafif (LightMBN, OSNet gibi) ReID modellerini içerir. Bu modeller, nesnelerin görünümünü analiz ederek aynı nesnenin farklı zamanlarda veya açılardan tanımlanmasını sağlar.

### Savaşan İHA'lar İçin ReID'nin Önemi
- **Hedefin Takibi:** İHA belirli bir hedefi takip ediyorsa ve hedef bir süre için gizlenirse, ReID modelleri sayesinde aynı hedef yeniden ortaya çıktığında tanımlanabilir.
- **Farklı Perspektiflerde Tanımlama:** İHA, hedefin farklı perspektiflerini yakalayabilir ve ReID modelleri sayesinde hedefi farklı açılardan tanıyabilir.

BoxMOT, bu ReID modellerini nesne takibiyle entegre ederek, hedeflerin tespit edilmesini ve yeniden tanımlanmasını kolaylaştırır. Birden fazla İHA’nın aynı bölgede uçtuğu durumlarda, tespit edilen hedeflerin karışmasını önlemek ve doğru takibi sağlamak için ReID kullanılabilir.

## BoxMOT’nin Avantajları
- **Esneklik:** BoxMOT, çeşitli nesne tespit ve takip yöntemlerini destekler, bu da farklı görevler ve donanım gereksinimlerine kolayca uyum sağlar.
- **Yüksek Performans:** YOLO modelleri ile entegre çalışarak yüksek hızlı nesne tespiti ve takibi sunar. Bu, özellikle gerçek zamanlı operasyonlar için optimize edilmiştir.
- **Hızlı Deneyler:** Tespitleri ve gömmeleri saklayarak herhangi bir takip algoritmasıyla tekrar kullanılmasını sağlar, bu da deney sürecini hızlandırır.

## Örnek Uygulama
[BoxMOT](https://github.com/mikel-brostrom/boxmot.git) reposunu ziyaret ederek gerekli kurulumları yapabilir ve bu kütüphane ile kendi çalışmalarınızı test edebilirsiniz.

### Kodu Çalıştırma
Aşağıda, BoxMOT ile nesne takibi için örnek bir uygulama kodu ve komut satırı ile çalıştırma adımları verilmiştir:
### Manuel içinde çalıştırma 
Kodu manuel olarak çalıştırmak için [deneme.py].(Örnek_uygulama/deneme.py) dosyasına girip çalıştırabilirsiniz .

### Komut Satırından Çalıştırma
Kodu komut satırından çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```bash
python deneme.py --yolo-model yolov8_sabitkanat.pt --conf 0.5 --reid-model osnet_x1_0_msmt17.pt --video-source ucus6_1.mp4 --tracker botsort
```

Bu sayede, istediğiniz parametrelerle takip işlemini terminalden başlatabilir ve kendi uygulamanızı test edebilirsiniz.

## Sonuç
BoxMOT, savaşan İHA'lar ve benzeri gerçek zamanlı nesne tespiti ve takibi gereken uygulamalar için güçlü, esnek ve yüksek performanslı bir çerçeve sunar. Kendi veri setlerinizi kullanarak yeni modelleri test etmek ve performansınızı artırmak için bu kütüphaneyi mutlaka incelemenizi öneririm.

