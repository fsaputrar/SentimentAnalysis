READ ME
Analisis Sentimen Opini Film Menggunakan Metode Naïve Bayes dengan Ensemble Feature dan Seleksi Fitur Pearson Correlation Coefficient

REMINDER!!!
Sebelum menjalankan program pastikan file path sesuai dengan tempat Anda menyimpan dataset atau file lainnya !!
ex:
Penulis menyimpan code penulis pada "C:\Users\ACER\PycharmProjects\ProgramSkripsi"

Kateglo.py 
- digunakan untuk mendapatkan pos tag dari API Kateglo http://kateglo.com/api.php?format=json&phrase=wah
- dan disimpan pada .csv
Steps:
Inputan:
1. berupa file dataset teks .csv
2. Ubah source code nama file pada code:
   with open("C:\Users\ACER\PycharmProjects\ProgramSkripsi\data\....csv",
          "rb") as data:
Output:
1. berupa file .csv
2. output akan tersimpan pada setiap postag
   ex: 
   untuk mendapatkan postag Noun maka hanya menjalankan method def Noun (self) dan otomatis tersimpan pada ...\Postag\Noun10.csv

REMINDER!!! jalankan permethod agar tidak terjadi ConnectionAborted dan pastikan untuk time.sleep(1) agar tidak dikenal sebagai bot


Ensemble Features 
- Proses digunakan untuk mengambil nilai fitur berdasarkan fitur description F1 - F37
Steps:
1. berupa file dataset teks .csv
2. Ubah source code nama file pada code sesuai dengan nama dataset Anda
   ex:
   Dataset penulis terletak pada folder data dengan nama datasetbaku
   with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\datasetbaku.csv","rb") as data:

Output:
1. Fitur F1-F37 akan terekstraksi pada file .csv
   fitur akan tersimpan pada folder output dan akan disimpan pada folder sfiturrdb dengan naman ekstrakbaku.csv 
   sesuaikan dengan nama folder pengguna 
   with open('C:\Users\ACER\PycharmProjects\Skripsimaster\output\sfiturrdb\ekstrakfiturbaku.csv', 'wb')


Preprocessing.py
digunakan untuk menambahkan fitur pada file fitur ensemble, Pastikan nama file (wb) pada ensemble sama dengan pada Preprocessing.py
semisal pada ensemble nama file yang dibuat adalah:
with open('C:\Users\ACER\PycharmProjects\Skripsimaster\output\sfiturrdb\ekstrakfiturbaku.csv', 'wb')

PASTIKAN pada Preprocessing.py
with open("C:\Users\ACER\PycharmProjects\Skripsimaster\output\sfiturrdb\ekstrakfiturbaku.csv", "ab")

DAN PASTIKAN dataset inputan sama dengan pada EnsembleFeatures.py
with open("C:\Users\ACER\PycharmProjects\Skripsimaster\data\datasetbaku.csv","rb") as data:


Catatan:
PROSES RUNNING FILE DILAKUKAN SETIAP FILE CODING DAN SEMUA OUTPUT AKAN DISIMPAN PADA FILE.CSV dan pada masing - masing Folder


   

