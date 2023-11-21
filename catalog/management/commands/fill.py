from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_list = [
            {"title": "vegetables", "description": "plants",},
            {"title": "meat", "description": "animals",},
            {"title": "chocolate", "description": "sweet food",},
        ]

        category_to_create = []
        for item in category_list:
            category_to_create.append(Category(**item))

        Category.objects.bulk_create(category_to_create)


        product_list = [
            {"title": "cucumber", "category_id": 25, "price": "150"},
            {"title": "pork", "category_id": 26, "price": "200"},
            {"title": "Twix", "category_id": 27, "price": "60"},
        ]

        product_to_create = []
        for item in product_list:
            product_to_create.append(Product(**item))

        Product.objects.bulk_create(product_to_create)
