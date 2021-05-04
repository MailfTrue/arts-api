from django.db import models


class ArtWorkType(models.TextChoices):
    BAS_RELIEF = 'bas-relief'
    SCULPTURE = 'sculpture'
    PICTURE = 'picture'


class ArtWork(models.Model):
    """
    Art work types:
        Bas-relief: 'bas-relief'
        Sculpture: 'sculpture'
        Picture: 'picture'
    """
    image = models.ImageField()
    title = models.CharField(max_length=32)
    description = models.TextField()
    type = models.CharField(max_length=16, choices=ArtWorkType.choices)
    show = models.BooleanField(verbose_name="Отображать на сайте", default=True)

    class Meta:
        verbose_name = "Произведение искусства"
        verbose_name_plural = "Произведения искусства"
