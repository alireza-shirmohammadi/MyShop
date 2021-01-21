from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
    #    return reverse('product_list_by_category', args=[self.slug])
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Subcat(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_subcat', args=[self.category.slug, self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat = models.ForeignKey(Subcat, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', blank=True)
    color=models.CharField(max_length=100,blank=True)
    size=models.TextField(blank=True)
    brand=models.CharField(max_length=100,blank=True)
    material=models.TextField(default='')
    tags=models.TextField(blank=True)
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        """
        Return self.photo.url if self.photo is not None,
        'url' exist and has a value, else, return None.
        """
        if self.image:
            return getattr(self.image, 'url', None)
        return None


    def get_absolute_url(self):
       return reverse('product_detail', args=[self.category.slug, self.subcat.slug, self.slug])
