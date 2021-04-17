import sys
import os
from pathlib import Path

from django.conf import settings
from dotenv import load_dotenv


# Declare base directory
BASE_DIR = Path(__file__).resolve().parent

# Load dotenv file
dotenv_file = BASE_DIR / '.env'
if dotenv_file.exists():
    load_dotenv(dotenv_file)


# Declare settings
settings.configure(
    DEBUG=True,
    SECRET_KEY=os.environ['SECRET_KEY'],
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.urls import path
from django.http import HttpResponse


# Views
def index(_):
    return HttpResponse('This is a lightweight Django application')


# Routes
urlpatterns = [
    path('', index, name='index'),
]


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
