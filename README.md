Nama : Samuel Indriano
NPM : 2406400524
Kelas : B

## TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Urutan dari prioritas tertinggi hingga terendah:
    1. !important --> Prioritas tertinggi, akan selalu override semua selector lain.
    2. inline styles --> contoh: <h1 style="color: pink;"> --> weight=1000
    3. Id selectors --> contoh: #id --> weight=0100
    4. Class, attribute, pseudo class --> contoh: .class, [type=""], :hover --> weight=0010
    5. Element and pseudo element --> contoh: h1, ::before --> weight=0001
    6. Universal selector and :where() --> contoh: *, where() --> weight=0000

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
    Alasan responsive web design penting:
    1. Meningkatkan user experience
    Website yang responsive bisa melakukan adjusting untuk ukuran layar dari user, sehingga user dapat melakukan navigasi dan interaksi pada website dengan mudah.
    2. Kemudahan dalam maintenance
    Karena tidak perlu untuk mengembangkan versi web berbeda untuk setiap device user yang berbeda, sehingga maintenance akan lebih mudah dan cepat.
    3. Loading time yang cepat
    Website yang responsive sudah mengoptimisasi resource nya, seperti gambar, CSS, dll.

    Aplikasi yang sudah menerapkan responsive design: Tokopedia, karena sudah menerapkan hamburger sehingga dapat menyesuaikan tampilan untuk smartphone maupun desktop.

    Aplikasi yang belum menerapkan responsive design: Scele Jadul (2014), tidak ada penyesuaian tampilan di HP sehingga sama persis seperti di desktop, navigasi tetep memanjang, dan tidak ada hamburger.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    Margin: Ruang kosong di luar border
    Border: Sebuah garis batas yang mengelilingi padding dan konten
    Padding: Ruang kosong di sekitar konten 

    Implementasi ketiganya:
    div {
        width: 200px; 
        border: 10px solid green; 
        padding: 40px; 
        margin: 15px; 
    }

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    Flex box adalah sistem layout 1 dimensi yang berfungsi untuk mengatur dan mengalokasikan ruang antar item dalam suatu container. Sedangkan untuk grid layout adalah sistem 2 dimensi berbasis grid, yang berfungsi untuk memudahkan pembuatan halaman web tanpa harus menggunakan float atau positioning.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    - Checklist 1: Untuk implementasi fitur edit news, saya menambahkan fungsi edit_news di views, membuat file html bernama edit_news, melakukan routing url, dan melakukan sedikit modifikasi tombol di main.html. Proses yang mirip juga saya lakukan untuk implementasi fitur delete news.

    - Checklist 2: Saya menggunakan tailwind untuk CSS framework pada aplikasi yang saya buat. Saya menyambungkan django dan tailwind dengan menambahkan script cdn tailwind di bagian head base.html.

    - Checklist 3: Untuk halaman login, register, edit product, dan detail product, saya melakukan implementasi mirip dengan tutorial. Hanya saja, saya merubah palet warna nya yang tadinya gray dan green --> stone dan teal. Di detail product, saya juga mengganti warna badge category menjadi gradient, dan menambahkan harga product.

    - Checklist 4: Untuk dasar dari halaman daftar product, saya melakukan implementasi yang juga mirip dengan tutorial, tapi saya melakukan beberapa modifikasi. Saya melakukan modifikasi zoom in image ketika di hover, mengganti warna badge category menjadi gradient, menebalkan brand product dan menambahkan harganya, dan terakhir menebalkan border dan shadow dari card agar tidak terlalu menyatu dengan background halaman yang putih. Saya juga sudah menambahkan gambar apabila belum ada product yang tersimpan.

    - Checklist 5: Untuk menambahkan navigation bar, saya membuat file navbar.html dan mengisinya dengan kode yang diperlukan. Kemudian saya juga melakukan pentautan navbar tersebut ke main.html. Modifikasi yang saya lakukan di navbar adalah mengubah font logo "AdiduShop" dengan melakukan import google fonts API melalui base.html.
    
## TUGAS 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah suatu form yang dapat mengautentikasi atau memvalidasi status user yang sedang login. Kelebihannya adalah keamanan yang baik dan terintegrasi dengan authenticate() dan login(). Kekurangannya adalah harus melakukan banyak kustomisasi misalnya seperti pengaturan izin user untuk login, login dengan email/OTP, dan lainnya. 

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi tugasnya melakukan verifikasi terhadap user yang login, sedangkan otorisasi tugasnya memberikan izin aktivitas bagi user setelah melakukan autentikasi. Implementasi autentikasi pada Django misalnya dengan form/view tools seperti AuthenticationForm, LoginView, LogoutView, ataupun dengan middleware seperti AuthenticationMiddleware. Sedangkan untuk implementasi otorisasi pada Django misalnya dengan dekorator seperti @login_required, @permission_required, ataupun dengan API seperti user.has_perm('app_label.action_model').

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
- Session
Kelebihan:  - Data lebih aman, karena disimpan di server sehingga tidak bisa diubah-ubah.
            - Bisa menyimpan data dengan ukuran yang besar

Kekurangan: - Membutuhkan storage pada server untuk menyimpan data.
            - Kecepatan penyimpanan data tidak maksimal karena setiap request membutuhkan server processing.
            - Data hilang ketika session expired atau ketika server restart.

- Cookies
Kelebihan:  - Data disimpan di browser, sehingga tidak membutuhkan storage server tambahan.
            - Kecepatan penyimpanan data maksimal karena data disimpan pada browser pengguna.
            - Data tidak hilang meskipun browser sudah ditutup.

Kekurangan: - Keamanan tidak maksimal karena data bisa diakses client di web.
            - Data yang bisa disimpan hanya bisa 4KB per cookie.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookies aman dalam pengembangan web jika diimplementasi secara benar, namun tetap ada risiko potensial. Misalnya main-in-the-middle (MitM), XSS, hingga CSRF. Django bisa menangani hal tersebut dengan:
- SESSION_COOKIE_HTTPONLY --> agar cookie tidak bisa diakses JS, mencegah XSS
- SESSION_COOKIE_SECURE --> agar cookie hanya dikirim jika HTTPS, mencegah MitM dan CSRF.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Checklist 1: Pertama, saya buat form registrasi dengan melakukan import UserCreationForm dan messages, kemudian membuat suatu fungsi di views yang berfungsi untuk menghasilkan form registrasi secara otomatis dan membuat akun pengguna ketika data di submit dari form. Kemudian membuat halaman untuk register tersebut dengan register.html dan tidak lupa untuk menambahkan path url nya.

Kemudian, saya lanjut membuat untuk login dan logout dengan melakukan beberapa import yang dibutuhkan. Saya membuat fungsi login di views yang berfungsi untuk mengautentikasi pengguna yang sedang login, dan juga fungsi logout agar pengguna bisa logout. Kemudian membuat halaman login dengan login.html yang dan juga tidak lupa untuk menambahkan path url-nya.

- Checklist 2: Saya menjalankan servernya di local dan kemudian melakukan register untuk 2 akun, yang kemudian saya juga tes untuk melakukan login pada ke 2 akun tersebut. Kemudian saya menambahkan 3 produk sepatu pada setiap akun tersebut.

- Checklist 3: Di models, saya melakukan import User dan menambahkan atribut baru bernama user. Kemudian melakukan modifikasi fungsi views yaitu show_main dan create_product.

- Checklist 4: Saya melakukan beberapa import dan kemudian menambahkan beberapa modifikasi pada fungsi login_user, show_main, dan logout_user untuk mengatur akses data pada cookie dan juga menghapus cookie.

## TUGAS 3
1. Data delivery penting karena kita bisa mengakses data secara langsung, menjamin akurasi data, mendeteksi adanya error, hingga validasi data.

2. JSON lebih baik daripada XML karena JSON lebih mudah di parse dibanding XML dengan JavaScript object. JSON juga lebih populer karena lebih simpel untuk ditulis dan dibaca, lebih ringkas, dan bisa make array.

3. is_valid() pada form Django berawal dari form yang menjalankan proses validasi, seperti validasi input user, validasi model, cleaning data, dan beberapa proses lainnya. Jika proses validasi nya berhasil dilewati, maka is_valid() akan return True, jika gagal maka akan return False dan error akan dikirim pada form.errors. is_valid() dibutuhkan untuk melakukan banyak proses validasi, cleaning data, memberi feedback error, dan membuat validasi yang reusable tanpa harus implementasi manual di view.

4. Kita membutuhkan csrf_token untuk menjamin request datang dari user asli yang sedang login dan bukan dari request berbahaya yang dikirim penyerang. csrf_token bekerja dengan menambahkan token unik yang terdiri banyak karakter random, sehingga sulit untuk ditebak penyerang. Jika tidak ada token, penyerang dapat dengan mudah mengirim request palsu yang tidak kita ingingkan. Pengiriman request biasanya dilakukan penyerang melalui website berbahaya, dimana penyerang bisa menyisipkan request pada browser pengguna. Request juga akan dikirim bersama cookie dari browser pengguna ke server tujuan, sehingga terlihat seperti pengguna asli yang melakukannya.

5. Checklist 1: Pertama, saya mengimport yang dibutuhkan, yaitu HttpResponse dan serializers. Kemudian saya membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id.

Checklist 2: Kemudian mengedit urls.py, yaitu dengan menambahkan import dari keempat fungsi tersebut dan juga menambahkan path url agar keempat fungsi yang sudah di import bisa diakses.

Checklist 3: Pertama, tambahkan dulu function create_product dan show_product di views.py. Tidak lupa juga untuk menambahkan path url di urls.py dari kedua fungsi tersebut. Kemudian baru memodifikasi main.html dengan menambahkan button dan juga loop agar bisa menampilkan semua produk yang sudah ditambahkan. Lanjut membuat create_product.html untuk menampilkan halaman input product.

Checklist 4: Saya membuat forms.py dan mengisinya dengan kode yang diperlukan, yang nantinya akan digunakan untuk menerima input data product dari pengguna. Kemudian saya mengimport ProductForm di views.py dan memodifikasi dictionary pada function show_main agar bisa menampilkan data product secara otomatis.

Checklist 5: Terakhir, saya membuat product_detail.html yang akan menampilkan halaman berisi detail dari setiap product. Kemudian menambahkan url project pada CSRF_TRUSTED_ORIGINS di settings.py.

6. Tidak ada

7. Screenshots:
![show XML](image.png)
![show JSON](image-1.png)
![show XML by ID](image-2.png)
![show JSON by ID](image-3.png)


## TUGAS 2
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


2. ![Bagan Alur App Django](bagan-django.jpg)

3. File yang berisi seluruh konfigurasi aplikasi kita. Mulai dari pengaturan keamanan app, pengaturan database, dan masih banyak lainnya.

4. "makemigrations" akan membuat migrasi baru dari semua perubahan pada model, kemudian dilanjut "migrate" untuk menambahkan migrasi tersebut ke dalam database.

5. Django menggunakan arsitektur MVT, sehingga kode lebih mudah untuk diorganisir dan dijaga. Kemudian django juga memiliki object-relational mapping (ORM) sehingga bisa langsung connect ke database hanya dengan kode Python. Django juga menggunakan Django Template Language yang bisa mengirim data dari backend ke html dengan syntax sederhana.

6. Tidak ada