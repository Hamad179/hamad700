from pathlib import Path
import os

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري للمشروع (غير آمن للنشر)
SECRET_KEY = 'django-insecure-xxx'

# وضع التطوير (اجعله False في حالة الإنتاج)
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الخاصة بالمشروع
    'tasks',
    'reports',
    'clients',
]

# الوسطاء (Middlewares)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# روابط المشروع
ROOT_URLCONF = 'config.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعداد ملف WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = []

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة (مثل CSS و JS)
STATIC_URL = 'static/'

# المفتاح الأساسي الافتراضي للجداول
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
