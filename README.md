Nama : Samuel Indriano
NPM : 2406400524
Kelas : B

Tautan PWS: https://samuel-indriano-adidushop.pbp.cs.ui.ac.id/

1. Checklist 1: Pertama bikin direktori baru bernama "adidu-pbp". Kemudian inisiasi repo baru dengan "git init". Selanjutnya saya buat repo baru "adidu-pbp" di GitHub. Lanjut saya menghubungkan repo lokal dengan repo yang di github dan melakukan clone repo github ke VS Code.

Lanjut bikin venv dan mengaktifkannya, kemudian menambahkan dan modifikasi syarat" yang diperlukan seperti pada "requirements.txt", ".env", ".env.prod", dan "settings.py", baru akhirnya bisa di migrate dan berhasil membuat proyek django.

Checklist 2: Pada terminal yang sudah teraktifkan venv, jalankan "python manage.py startapp main" untuk membuat aplikasi main.

Checklist 3: Saya add "main" dalam list bernama installed apps di settings.py dari direktori adidu_shop agar aplikasi "main" terdafatar di proyek.

Checklist 4: Selanjutnya saya membuat model dengan membuat class Product di models.py. Class tersebut berisi atribut seperti name, price, description, thumbnail, category yang merujuk pada list "CATEGORY_CHOICES" untuk pilihan produk, is_featured, brand, dan terakhir stock.

Checklist 5: Memodifikasi views.py dengan membuat function bernama "show_main" yang nantinya akan berisikan dictionary dengan key npm, nama, dan class. main.html juga tidak lupa di modif dengan template variables. Terakhir, kembali pada views.py yang di akhir akan return render untuk request http, dan menampilkan berkas html sesuai dengan data yang diteruskan dari dictionary.

Checklist 6: Pertama untuk konfigurasi routing pada URL aplikasi main, urls.py di direktori main dilakukan import path dan show_main. Kemudian buat list yang isinya berupa function path, untuk mendefinisikan pola URL.

Kedua untuk konfigurasi routing pada URL proyek, urls.py di direktori adidu_shop dilakukan import path dan include, kemudian ditambahkan juga list yang isinya berupa function path.

Checklist 7: Lakukan migration dulu dan commit semua perubahan. Baru di terminal ketik "git remote add pws https://pbp.cs.ui.ac.id/samuel.indriano/adidushop" dan kemudian "git push pws master". Terakhir tinggal buka "https://samuel-indriano-adidushop.pbp.cs.ui.ac.id/" dan selesai!


2. BAGAN

3. File yang berisi seluruh konfigurasi aplikasi kita. Mulai dari pengaturan keamanan app, pengaturan database, dan masih banyak lainnya.

4. 

5. 

6. Tidak ada