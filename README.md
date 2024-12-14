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

#### 8. Loading file statis images

        new file:   static/images/homepage.png
        modified:   templates/main/index.html

#### 9. Menggunakan include

        modified:   README.md
        modified:   static/css/testing.css
        new file:   templates/inc/footer.html
        new file:   templates/inc/navbar.html
        modified:   templates/main/base_main.html

#### 10. Membuat path untuk apps pada settings.py

        modified:   README.md
        renamed:    app/main/__init__.py -> apps/main/__init__.py
        renamed:    app/main/admin.py -> apps/main/admin.py
        renamed:    app/main/apps.py -> apps/main/apps.py
        renamed:    app/main/migrations/__init__.py -> apps/main/migrations/__init__.py
        renamed:    app/main/models.py -> apps/main/models.py
        renamed:    app/main/tests.py -> apps/main/tests.py
        renamed:    app/main/urls.py -> apps/main/urls.py
        renamed:    app/main/views.py -> apps/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py

        Note:

        1. I created this in settings.py
        2. And modified the related files.

        # ING: Defining path for apps
        import os, sys 
        APPS_DIR = str(os.path.join(BASE_DIR, 'apps'))
        sys.path.insert(0, APPS_DIR)


## 8. USER MANAGEMENT

#### 1. Membuat user app

        modified:   README.md
        new file:   apps/user/__init__.py
        new file:   apps/user/admin.py
        new file:   apps/user/apps.py
        new file:   apps/user/migrations/__init__.py
        new file:   apps/user/models.py
        new file:   apps/user/tests.py
        new file:   apps/user/views.py

#### 2. Register user app pada proyek

        modified:   README.md
        modified:   config/settings.py

#### 3. House keeping: menambahkan url path untuk static file

        modified:   README.md
        modified:   config/urls.py

#### 4. Custom User model part 1 - Membuat UserManager

        modified:   README.md
        modified:   apps/user/models.py
        modified:   config/settings.py

#### 5. Custom User model part 2 - Membuat custom user

        # 1. Create migration file
        (venv312511) λ python manage.py makemigrations
        Migrations for 'user':
          apps\user\migrations\0001_initial.py
            + Create model User

        # 2. Create tables
        (venv312511) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions, user
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0001_initial... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying user.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying sessions.0001_initial... OK

        # 3. Create superuser
        (venv312511) λ python manage.py createsuperuser
        Email Address: admin@mail.com
        First Name: super
        Last Name: user
        Password:
        Password (again):
        Kata sandi terlalu mirip dengan Email Address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        # 4. Results
        # 4.1 Use db ind_80_dj5_jadual_vaksin
        (venv312511) λ python manage.py dbshell
        psql (16.2)
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        ind_80_dj5_jadual_vaksin=#

        # 4.2 Show tables
        ind_80_dj5_jadual_vaksin=# \t
        Tuples only is on.
        ind_80_dj5_jadual_vaksin=# \d
         public | auth_group                        | table    | postgres
         public | auth_group_id_seq                 | sequence | postgres
         public | auth_group_permissions            | table    | postgres
         public | auth_group_permissions_id_seq     | sequence | postgres
         public | auth_permission                   | table    | postgres
         public | auth_permission_id_seq            | sequence | postgres
         public | django_admin_log                  | table    | postgres
         public | django_admin_log_id_seq           | sequence | postgres
         public | django_content_type               | table    | postgres
         public | django_content_type_id_seq        | sequence | postgres
         public | django_migrations                 | table    | postgres
         public | django_migrations_id_seq          | sequence | postgres
         public | django_session                    | table    | postgres
         public | user_user                         | table    | postgres
         public | user_user_groups                  | table    | postgres
         public | user_user_groups_id_seq           | sequence | postgres
         public | user_user_id_seq                  | sequence | postgres
         public | user_user_user_permissions        | table    | postgres
         public | user_user_user_permissions_id_seq | sequence | postgres


        # 4.3 Describe table: user_user
        ind_80_dj5_jadual_vaksin=# \d user_user;
         id                       | bigint                   |           | not null | generated by default as identity
         password                 | character varying(128)   |           | not null |
         last_login               | timestamp with time zone |           |          |
         email                    | character varying(254)   |           | not null |
         first_name               | character varying(30)    |           | not null |
         middle_name              | character varying(30)    |           |          |
         last_name                | character varying(30)    |           | not null |
         date_of_birth            | date                     |           |          |
         gender                   | character varying(1)     |           |          |
         blood_group              | character varying(3)     |           |          |
         identity_document_type   | character varying(32)    |           |          |
         identity_document_number | character varying(32)    |           | not null |
         photo                    | character varying(100)   |           |          |
         date_joined              | timestamp with time zone |           | not null |
         created                  | timestamp with time zone |           | not null |
         last_updated             | timestamp with time zone |           | not null |
         is_email_verified        | boolean                  |           | not null |
         is_active                | boolean                  |           | not null |
         is_staff                 | boolean                  |           | not null |
         is_superuser             | boolean                  |           | not null |

        # 4.4 Select data from user_user table
        ind_80_dj5_jadual_vaksin=# SELECT first_name, last_name, email FROM user_user;
         super      | user      | admin@mail.com <-----------------

        modified:   README.md
        modified:   apps/user/admin.py
        new file:   apps/user/migrations/0001_initial.py
        modified:   apps/user/models.py

#### 6. Signup part 1 - Create SignupForm

        new file:   apps/user/forms.py

#### 7. Signup part 2 - Create urls, view dan template

        modified:   README.md
        new file:   apps/user/urls.py
        modified:   apps/user/views.py
        modified:   config/urls.py
        new file:   templates/user/signup.html

#### 8. Signup part 3 - Mengisi html template untuk laman sign up

        modified:   README.md
        modified:   apps/main/urls.py
        modified:   apps/main/views.py
        ...
        modified:   templates/main/index.html
        modified:   templates/user/signup.html

        Note:

        1. Add template for signup page.
        2. Removed about page and its related files.

#### 8. Signup part 4 - Menambahkan logika pada signup view

        modified:   README.md
        modified:   apps/user/views.py
        new file:   media/profileImage/color-30.PNG
        ...
        new file:   media/profileImage/logo-6.PNG
        modified:   templates/base.html
        new file:   templates/inc/messages.html
        modified:   templates/user/signup.html
        new file:   templates/user/signup_ori.html

        Note:

        1. Sukses signup a new user tanpa verifikasi email.

        :)

        # Hasil
        ind_80_dj5_jadual_vaksin=# SELECT id, email, first_name, middle_name, last_name FROM user_user WHERE id=11;
         id |         email         | first_name | middle_name | last_name
        ----+-----------------------+------------+-------------+-----------
         11 | testnewuser7@mail.com | test       | new         | user7
        (1 row)

#### 9. Login part 1 - Membuat LoginForm

        modified:   README.md
        modified:   apps/user/forms.py
        new file:   templates/user/login.html

#### 10. Login part 2 - Membuat urls, views, dan template

        modified:   README.md
        modified:   apps/user/urls.py
        modified:   apps/user/views.py
        modified:   templates/inc/header.html

#### 11. Login part 3 - Menggunakan LoginForm pada login view

        modified:   README.md
        modified:   apps/user/views.py
        modified:   templates/user/login.html

#### 12. Login part 4 - Menambahkan html template pada laman login

        modified:   README.md
        modified:   templates/user/login.html

#### 13. Login part 5 - Menggunakan template tags pada laman login untuk login

        modified:   README.md
        modified:   templates/user/login.html

        Note:

        1. Login sukses.

        :)

#### 14. Logout

        modified:   README.md
        modified:   apps/user/urls.py
        modified:   apps/user/views.py
        modified:   templates/inc/header.html

        :)

#### 15. Change password part 1 - Membuat ChangePasswordForm

        modified:   README.md
        modified:   apps/user/forms.py

#### 16. Change password part 2 - Membuat urls, views, templates

        modified:   README.md
        modified:   apps/user/urls.py
        modified:   apps/user/views.py
        new file:   templates/user/change-password.html

#### 17. Change password part 3 - Add html tamplatge pada laman change-password

        modified:   README.md
        modified:   templates/user/change-password.html

#### 18. Change password part 4 - Add logika pada view change_password

        modified:   README.md
        modified:   apps/user/views.py

#### 19. Change password part 5 - Mendefinisikan tamplate tags pada laman change-password untuk change-password

        modified:   apps/user/views.py
        modified:   templates/user/change-password.html

        Note:

        1. Sukses change-password.

        :)

#### 20. Profile part 1 - urls, views, templates

        modified:   README.md
        modified:   apps/user/urls.py
        modified:   apps/user/views.py
        new file:   templates/user/profile.html