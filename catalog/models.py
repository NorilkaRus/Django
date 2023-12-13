from django.db import models

NULLABLE = {'blank':  True, 'null': True}

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'наименование')
    description = models.TextField(verbose_name= 'описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name= 'изображение', **NULLABLE)
    category = models.ForeignKey(
        'catalog.Category',
        on_delete=models.CASCADE,
        verbose_name= 'категория',
    )
    price = models.PositiveIntegerField(verbose_name= 'цена за покупку')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='дата последнего изменения'
    )

    def __str__(self):
        return f'{self.title} ({self.description}): {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    version_number = models.IntegerField(default=1, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Название версии')
    is_current = models.BooleanField(choices=VERSION_CHOICES, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)  # сортировка по номеру версии
