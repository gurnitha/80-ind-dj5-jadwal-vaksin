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


## 4. DATABASE

#### 1. Membuat mysql database

        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 35
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> CREATE DATABASE ind_80_dj5_jadual_vaksin;
        Query OK, 1 row affected (0.42 sec)

#### 2. Menseting path untuk menghubungan proyek ke database

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ind_80_dj5_jadual_vaksin',
            'USER': 'root',
            'PASSWORD': '',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        (venv312511) λ python manage.py check
        ...
        raise ImproperlyConfigured(
        django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
        Did you install mysqlclient?

#### 3. Menginstal mysqlclient

        (venv312511) λ pip install mysqlclient
        Collecting mysqlclient
          Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl.metadata (4.6 kB)

        Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl (203 kB)
        Installing collected packages: mysqlclient
        Successfully installed mysqlclient-2.2.4

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 4. Melindungi file penting

        modified:   README.md
        modified:   config/settings.py

#### 5. Mengganti database: dari mysql ke postgresql

        # 1. Login ke postgres server
        λ psql -U postgres
        psql (16.2)
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        postgres=#

        # 2. Membuat database
        postgres=# CREATE DATABASE ind_80_dj5_jadual_vaksin;
        CREATE DATABASE

        # 3. Menginstal driver
        (venv312511) λ python -m pip install psycopg2-binary
        Collecting psycopg2-binary
          Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
        Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)
        Installing collected packages: psycopg2-binary
        Successfully installed psycopg2-binary-2.9.9

        # 4. Mendifinisikan environ variabel pada file .env
        SECRET_KEY='django-insecure-@0l9(24a_h='-2-+&6n3dgs%*&)nk05(327n9&009gy$0m4un35'
        DB_NAME='ind_80_dj5_jadual_vaksin'
        DB_USER='posgres'
        DB_PASSWORD='posgres'
        DB_HOST='localhost'
        DB_PORT='5432'

        # 5. Mengganti DB ENGINE dari mysql ke postgresql_psycopg2
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': env('DB_NAME'),
                'USER': env('DB_USER'),
                'PASSWORD': env('DB_PASSWORD'),
                'PASSWORD': env('DB_HOST'),
                'PASSWORD': env('DB_PORT'),
            }
        }

        # 5. Testing
        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).


## 5. PROYEK DJANGO VS APLIKASI DJANGO


## 6. APLIKASI DJANGO

#### 1. Membuat aplikasi main

        modified:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

#### 2. Mengintegrasikan aplikasi main dengan proyek

        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 3. Halo Dunia! Waktu Jakarta sekarang

        modified:   README.md
        modified:   app/main/views.py
        modified:   config/urls.py


## 7. URLs, VIEWS, TEMPLATES

#### 1. Membuat laman home

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/urls.py
        new file:   templates/main/index.html

#### 2. Membuat laman about

        modified:   README.md
        modified:   app/main/urls.py
        modified:   app/main/views.py
        new file:   templates/main/about.html

#### 3. Mentautkan laman home dan laman about

        modified:   README.md
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 4. Menggunakan tempate tags Django untuk mentautkan laman situs web

        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 5. Template inheritance

        modified:   README.md
        modified:   templates/main/about.html
        new file:   templates/main/base_main.html
        modified:   templates/main/index.html

#### 6. Block Super untuk page title

        modified:   app/main/views.py
        modified:   templates/main/about.html
        modified:   templates/main/base_main.html
        modified:   templates/main/index.html

#### 7. Loading file statis css

        modified:   README.md
        new file:   static/css/testing.css
        modified:   templates/main/base_main.html