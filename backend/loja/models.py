from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'

class Products(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.deletion.DO_NOTHING,
        related_name='products'
    )

    def __str__(self):
        return self.name