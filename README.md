# 80-ind-dj5-jadual-vaksin
Membuat Aplikasi JADUAL VAKSIN Menggunakan Django Versi 5
Github:https://github.com/gurnitha/80-ind-dj5-jadual-vaksin
Proyek:C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin


## 1. SETUP

#### 1. Github: membuat repositori

#### 2. Github: mengklon repositori

#### 3. Membuat lingkungan virtual

#### 4. Menginstal Django

#### 5. Meng-upgrade pip

#### 6. Memverifikasi hasil instalasi Django


## 2. PROYEK DJANGO

#### 1. Menginisiasi proyek Django

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py

#### 2. Memodifikasi struktur proyek

        modified:   README.md
        renamed:    config/config/__init__.py -> config/__init__.py
        renamed:    config/config/asgi.py -> config/asgi.py
        renamed:    config/config/settings.py -> config/settings.py
        renamed:    config/config/urls.py -> config/urls.py
        renamed:    config/config/wsgi.py -> config/wsgi.py
        renamed:    config/manage.py -> manage.py


## 3. SETTINGS

#### 1. Menseting bahasa dan waktu

        modified:   README.md
        modified:   config/settings.py

#### 2. Menseting absolute path untuk templates

        modified:   README.md
        modified:   config/settings.py

        # testing
        (venv312511) λ python manage.py check

        # results
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src\config\settings.py
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src\config
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src

        System check identified no issues (0 silenced).

#### 3. Menseting absolute path untuk file statis

        modified:   README.md
        modified:   config/settings.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 4. Menseting absolute path untuk file media

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).