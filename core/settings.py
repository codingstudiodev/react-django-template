"""Django settings for core project."""


import os
from datetime import timedelta
from decouple import config, Csv
from corsheaders.defaults import default_methods, default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING
SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_ALLOW_METHODS = default_methods

CORS_ALLOW_HEADERS = (
    *default_headers,
    "HTTP_AUTHORIZATION",
)

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS


# Application definition

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "server.apps.base",
    "server.apps.users",
]

THIRD_APPS = [
    "rest_framework",
    "drf_yasg",
    "corsheaders",
    "django_filters",
    "rest_framework_simplejwt",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_APPS


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # cors headers
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("PGDATABASE"),
        "USER": config("PGUSER"),
        "PASSWORD": config("PGPASSWORD"),
        "HOST": config("PGHOST"),
        "DATABASE_PORT": config("PGPORT"),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Rest framework config

REST_FRAMEWORK = {
    # Authentication
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    # Permissions
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # # Pagination
    # "DEFAULT_PAGINATION_CLASS": "server.apps.base.pagination.CustomPagination",
    # "PAGE_SIZE": 20,
    # Filter
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}


# Json web token config

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=6),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=12),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("Bearer"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
}


# Internationalization

LANGUAGE_CODE = "es-MX"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"


# Static files (CSS, JavaScript, Images)

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, "server/staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "./server/static"),
    # os.path.join(BASE_DIR, "dist"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "server/media")
MEDIA_URL = "/media/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Swagger config

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "HTTP_AUTHORIZATION",
            "in": "header",
        }
    },
    "DOC_EXPANSION": "None",
    "LOGIN_URL": "/v1/auth/login/",
    "LOGOUT_URL": "/admin/logout/",
    "PERSIST_AUTH": True,
}


# Jazzmin config

X_FRAME_OPTIONS = "SAMEORIGIN"

JAZZMIN_SETTINGS = {
    "site_title": "CS-Ventas Admin",
    "site_header": "CS-Ventas",
    "site_brand": "CS-Ventas",
    "site_logo": "img/cs_logo.png",
    "site_icon": "img/cs_icon.png",
    "welcome_sign": "Bienvenido a CS-Ventas",
    "copyright": "Coding Studios",
    "user_avatar": None,
    "navigation_expanded": True,
    # "hide_apps": ["auth"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "icons": {
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        "books.Author": "fas fa-user",
        "books.Book": "fas fa-book",
        "books.Genre": "fas fa-photo-video",
        "loans.BookLoan": "fas fa-book-open",
        "loans.Library": "fas fa-book-reader",
    },
    "related_modal_active": True,
}
