# Chest X-Ray Görüntülerinin CNN ile İkili Sınıflandırılması (NORMAL vs PNEUMONIA)

**Öğrenci:** MAHMOUD KARZOUN  
**No:** 251238003  
**Bölüm:** Bilgisayar Programcılığı  
**Üniversite:** KTO Karatay Üniversitesi  
**Ders:** Yapay Zekâ’ya Giriş  

📌 **Veri Kümesi (Kaggle):** https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

---

## TR — Proje Özeti
Bu projede göğüs röntgeni (Chest X-Ray) görüntüleri kullanılarak bir **CNN (Convolutional Neural Network)** modeli geliştirilmiştir.  
Model, görüntüleri **NORMAL** ve **PNEUMONIA** olmak üzere iki sınıfa ayırmayı hedefler.

- Eğitim (train): **5216**
- Doğrulama (val): **16**
- Test (test): **624**
- Görüntü boyutu: **224×224**
- Optimizasyon: **Adam (varsayılan learning rate = 0.001)**
- Kayıp fonksiyonu: **Binary Crossentropy**
- Test doğruluğu: **~0.8365**

---

## EN — Project Summary
In this project, a **Convolutional Neural Network (CNN)** was built to classify **Chest X-Ray** images into two classes: **NORMAL** and **PNEUMONIA**.

- Train: **5216**
- Validation: **16**
- Test: **624**
- Input size: **224×224**
- Optimizer: **Adam (default learning rate = 0.001)**
- Loss: **Binary Crossentropy**
- Test accuracy: **~0.8365**

---

## Kullanılan Teknolojiler / Tech Stack
- Python
- Google Colab (GPU)
- TensorFlow / Keras
- NumPy, Matplotlib
- scikit-learn (Confusion Matrix)

---

## Dosya Yapısı / Repository Structure
Chest_XRay_CNN_Projem/
├─ report.pdf
├─ notebook/
│ └─ Chest_XRay_CNN_Projem.ipynb
├─ docs/
│ └─ index.html
│ └─images
│ ├─ normal.png
│ ├─ pneumonia.png
│ ├─ accuracy.png
│ ├─ loss.png
│ └─ confusion_matrix.png
└─ README.md


---

## Nasıl Çalıştırılır? (Colab) / How to Run (Colab)

1) Colab defterini aç:  
https://colab.research.google.com/drive/1QvDpyKWrpE22qfl4iTTptSRBUgG38PCZ

2) Veri setini indir (kagglehub ile):  
Defter içindeki ilgili hücreyi çalıştır (dataset otomatik iner).

3) Eğitimi başlat:  
Model tanımı + `fit()` hücrelerini çalıştır.

4) Sonuçlar:  
Accuracy/Loss grafikleri + Confusion Matrix görüntülenir.

---

## Sonuçlar / Results
- Eğitim doğruluğu artarken loss azalmıştır.
- Test setinde yaklaşık **%83.65** doğruluk alınmıştır.
- Confusion Matrix, PNEUMONIA sınıfının genelde iyi yakalandığını göstermektedir.

---

## Bağlantılar / Links
- 📒 Colab Notebook: https://colab.research.google.com/drive/1QvDpyKWrpE22qfl4iTTptSRBUgG38PCZ
- 📦 Drive (Tüm proje dosyaları): https://drive.google.com/drive/folders/1vNgznY5VEGaM7bJkusPOXPHcRzHzcEag
- 🧾 GitHub Repo: https://github.com/mkarson1997/Chest_XRay_CNN_Projem
- 🌐 GitHub Pages: https://mkarson1997.github.io/Chest_XRay_CNN_Projem/

---

## Notlar
- Doğrulama seti (val) çok küçük olduğu için val_accuracy dalgalanması normaldir.
- Daha güçlü sonuçlar için Transfer Learning (MobileNetV2, DenseNet, ResNet) denenebilir.


Bu proje üniversite dersi kapsamında akademik amaçlı hazırlanmıştır.
