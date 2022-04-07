from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Название для URL-адреса')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """ Создание класса продука """

    category = models.ForeignKey(Category, related_name='products', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Название для URL-адреса')
    image_full = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Полное изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    avaible = models.BooleanField(default=True, verbose_name='Есть ли в наличии')
    energy_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Энерг.ценность')
    squirrels = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Белки')
    fats = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Жиры')
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Углеводы')
    weight_small = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес маленькой пиццы')
    weight_big = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес большой пиццы')
    diameter_small = models.IntegerField(verbose_name='Диаметр маленькой пиццы')
    diameter_big = models.IntegerField(verbose_name='Диаметр большой пиццы')
    div = models.CharField(max_length=100, verbose_name='ID для div-a')


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])









