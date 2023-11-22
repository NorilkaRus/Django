import json
import os.path
from django.contrib.sites import management
from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR
from django.shortcuts import get_object_or_404

fixtures_path = os.path.join(BASE_DIR, 'data.json')

class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'category.json')
        path_1 = os.path.join(BASE_DIR, 'product.json')

        with open(path) as f:
            file_content = f.read()
            categories_info = json.loads(file_content)
            categories_for_create = []
            for info in categories_info:
                categories_for_create.append(
                    Category(**info["fields"])
                )
            Category.objects.all().delete()
            Category.objects.bulk_create(categories_for_create)

        with open(path_1) as f:
            file_content = f.read()
            products_info = json.loads(file_content)
            products_for_create = []
            for info in products_info:
                products_for_create.append(
                    Product(**info["fields"])
                )
            Product.objects.all().delete()
            Product.objects.bulk_create(products_for_create)
