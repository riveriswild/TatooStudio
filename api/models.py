from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class Master(SingletonModel):
    """
    Tattoo artist's main page content
    """
    name = models.CharField(max_length=120, default="Nati")
    image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name='Фото мастера')
    description = models.TextField(blank=True, null=True, verbose_name="О себе для главной страницы")
    image_work = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Пример работы на главной")

    class Meta:
        verbose_name = "Страница мастера"
        verbose_name_plural = "Страница мастера"

    def __str__(self):
        return self.name


class Info(SingletonModel):
    """
    Artist's info
    """
    name = models.CharField(max_length=124, blank=False, null=False, default="Nati")
    info = models.TextField(verbose_name="Инфо для всплывающей плашки")
    telegram = models.CharField(max_length=124)
    vk = models.CharField(max_length=124)
    phone_number = models.CharField(max_length=14)
    price_info_prim = models.TextField(blank=True, null=True, verbose_name="Инфо о ценах слева")
    price_info_sec = models.TextField(blank=True, null=True, verbose_name="Инфо о ценах справа")

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    """
    Image for a gallery
    """
    name = models.CharField(max_length=124, blank=False, null=False, default="photo")
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    All works
    """

    NEW = 'new'
    OLD = 'old'
    SKETCH = 'sketch'

    IMAGE_CHOICES = [
        (NEW, 'new'),
        (OLD, 'old'),
        (SKETCH, 'sketch'),
    ]
    name = models.CharField(max_length=124, blank=False, null=False, default="photo")
    image = models.FileField(upload_to='images/', blank=True, null=True)
    image_status = models.CharField(choices=IMAGE_CHOICES, max_length=8, default=NEW, verbose_name='status')


    class Meta:
        verbose_name = "Пример работы"
        verbose_name_plural = "Примеры работ"

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Clients' reviews
    """
    client_image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Фото клиента")
    tattoo_image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Фото тату клиента")
    client_name = models.CharField(max_length=124, verbose_name='Имя клиента')
    client_review = models.TextField(blank=True, null=True, verbose_name="Текст отзыва")   # TODO CHANGE BLANKS AND NULLS

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.client_name


class Application(models.Model):
    """
    Application form for a tattoo
    """
    client_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Имя клиента")
    contacts = models.CharField(max_length=255, null=False, blank=False, verbose_name="Контакты")
    tattoo_description = models.TextField(null=True, blank=True, verbose_name="Описание тату")
    sketch = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Эскиз")  #TODO add datetime

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.client_name


class Price(models.Model):
    tattoo_image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Пример тату")
    price = models.CharField(max_length=255, null=False, blank=False, verbose_name="Цена")

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return self.price


class FAQ(models.Model):
    title = models.TextField(max_length=50, blank=True, null=True, verbose_name="Заголовок")
    text = models.TextField(blank=True, null=True, verbose_name="Текст")
    image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.title
