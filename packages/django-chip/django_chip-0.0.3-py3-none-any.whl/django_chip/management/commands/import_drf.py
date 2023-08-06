import os
import sys
import shutil
from django.conf import settings

from django.core.management.base import BaseCommand

from django_chip.management.utils import _make_writeable


class Command(BaseCommand):
    help = "Add drf configuration."

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        import django_chip
        
        base_dir = settings.BASE_DIR
        secret_key = settings.SECRET_KEY
        main_app_name = settings.ROOT_URLCONF.split('.')[0]
        project_name = os.path.split(base_dir)[-1]
        template_dir = os.path.join(django_chip.__path__[0], 'tmpl', 'drf_template')
        
        requirement_path = os.path.join(base_dir, 'requirements.txt')
        requirement_tmpl = os.path.join(template_dir, 'requirements.txt.tmpl')
        with open(requirement_tmpl, 'r') as fp_orig:
            data = fp_orig.read()
            
            with open(requirement_path, 'a+') as fp:
                fp.write(data)
        
        settings_path = os.path.join(base_dir, main_app_name, 'settings.py')
        settings_tmpl = os.path.join(template_dir, 'settings.py.tmpl')
        with open(settings_tmpl, 'r') as fp_orig:
            data = fp_orig.read()
            data = data.replace('{{ project_name }}', project_name)
            data = data.replace('{{ secret_key }}', secret_key)
            
            with open(settings_path, 'w') as fp:
                fp.write(data)
        
        urls_path = os.path.join(base_dir, main_app_name, 'urls.py')
        urls_tmpl = os.path.join(template_dir, 'urls.py.tmpl')
        with open(urls_tmpl, 'r') as fp_orig:
            data = fp_orig.read()
            
            with open(urls_path, 'w') as fp:
                fp.write(data)
        