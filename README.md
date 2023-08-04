# Proyek Django

Proyek ini adalah proyek Django standar, yang memiliki struktur direktori sebagai berikut:

```bash
belajar/ # Direktori root proyek
├── manage.py # Script command-line untuk mengelola proyek
└── belajar/ # Direktori aplikasi utama
├── __init__.py # Mengindikasikan bahwa direktori ini adalah paket Python
├── settings.py # File konfigurasi proyek
├── urls.py # Definisi URL utama proyek
└── asgi.py or wsgi.py # Poin masuk untuk server web
```

## Direktori `belajar/` Tingkat Atas

Direktori `belajar/` tingkat atas adalah direktori root proyek Anda. Ini hanya direktori yang berisi proyek Django Anda.

## Direktori `belajar/` Tingkat Kedua

Direktori `belajar/` tingkat kedua adalah konfigurasi dasar proyek Anda (dalam `settings.py`), definisi URL utama (dalam `urls.py`), dan poin masuk untuk server web (dalam `asgi.py` atau `wsgi.py`).

## Membuat Aplikasi Baru

Untuk membuat aplikasi baru dalam proyek Django Anda, jalankan perintah berikut di direktori root proyek Anda:

```bash
python manage.py startapp nama_app
```

Perintah ini akan membuat direktori baru dengan nama `nama_app/` yang berisi file-file yang diperlukan oleh aplikasi Django Anda, seperti `models.py`, `views.py`, dan `urls.py`.

Setelah membuat aplikasi baru, tambahkan nama aplikasi ke daftar `INSTALLED_APPS` di file `settings.py` Anda pada direktori `belajar/` tingkat 2. Contohnya seperti berikut:

```python
INSTALLED_APPS = [
    # ...
    'nama_app',
    # ...
]
```

juga, tambahkan rute aplikasi ke file `urls.py` di direktori belajar/ tingkat kedua. Contohnya seperti berikut:

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path("nama_app/", include("nama_app.urls")),
    # ...
]
```

Ingatlah untuk mengganti `nama_app` dengan nama aplikasi Anda sendiri.

## contoh app yang kita punya ialah `myapp`

Aplikasi ini memiliki struktur file dan direktori sebagai berikut:

```bash
myapp/ # Direktori aplikasi myapp
├── __init__.py # File yang menjadikan direktori myapp/ sebagai package Python
├── admin.py # File untuk konfigurasi halaman admin Django
├── apps.py # File untuk konfigurasi aplikasi myapp
├── models.py # File untuk mendefinisikan model dalam aplikasi myapp
├── tests.py # File untuk penulisan test unit aplikasi myapp
├── urls.py # File untuk mendefinisikan URL aplikasi myapp
├── views.py # File untuk mendefinisikan views dalam aplikasi myapp
└── templates/ # Direktori untuk menyimpan file template HTML
├──── base.html
├──── home.html
└──── movielist.html
```

## File `admin.py`

File `admin.py` digunakan untuk mengkonfigurasi halaman admin Django. Di sini, model `MovieList` di-registrasi ke halaman admin dengan `admin.site.register(MovieList)`, sehingga data `MovieList` dapat ditambahkan, dilihat, diedit, dan dihapus melalui halaman admin.

## File `apps.py`

File `apps.py` berisi konfigurasi aplikasi `myapp`. Dalam class `MyappConfig`, variabel `name` di-set ke 'myapp' yang merupakan nama aplikasi.

## File `models.py`

File `models.py` digunakan untuk mendefinisikan model dalam aplikasi `myapp`. Di sini, terdapat dua class model yaitu `GenreChoices` dan `MovieList`. `GenreChoices` adalah sub-class dari `models.TextChoices` yang mendefinisikan pilihan genre film. `MovieList` adalah class yang mewakili list film, dengan atribut `title`, `genre`, dan `year`.

## File `tests.py`

File `tests.py` digunakan untuk menulis test unit untuk aplikasi `myapp`. Contoh sederhana untuk tes pada model `MovieList` adalah sebagai berikut:

```python
from django.test import TestCase
from .models import MovieList, GenreChoices

class MovieListTestCase(TestCase):
    def setUp(self):
        MovieList.objects.create(title="Test Movie", genre=GenreChoices.ACTION, year=2022)

    def test_movie_list_created(self):
        """MovieList objects are saved properly"""
        movie = MovieList.objects.get(title="Test Movie")
        self.assertEqual(movie.genre, GenreChoices.ACTION)
        self.assertEqual(movie.year, 2022)
```

## File `urls.py`

File `urls.py` mendefinisikan URL aplikasi `myapp`. Setiap path dihubungkan dengan view yang sesuai. Misalnya, path "" (root) dihubungkan dengan view `home`, dan path "movies/" dihubungkan dengan view `movielist`.

## File `views.py`

File `views.py` mendefinisikan views dalam aplikasi `myapp`. Ada dua fungsi view yaitu `home` dan `movielist`. Fungsi `home` merender template `home.html`, sedangkan fungsi `movielist` merender template `movielist.html` dengan context berisi semua objek `MovieList`.

## Direktori `templates/`

Direktori `templates/` digunakan untuk menyimpan file template HTML. Django akan otomatis mencari file HTML dalam direktori ini saat fungsi `render` dipanggil dalam views.
