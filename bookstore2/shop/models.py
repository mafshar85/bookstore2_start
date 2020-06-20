from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
       abstract  = True


class Category(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()


class BOOK(BaseModel):
    COVER_HARD = 'hard'
    COVER_SOFT = 'soft'
    COVER_CHOICE = ((COVER_HARD, 'Hard Cover'),
                    (COVER_SOFT, 'Soft Cover' ))
    name = models.CharField(max_length=255)
    publish_year = models.IntegerField(null=True, blank=True)
    cover_type = models.CharField(null=True, blank=True,
                                  choices=COVER_CHOICE,
                                  max_length=5)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag)
    price = models.IntegerField()
    cover = models.ImageField(upload_to='shop/File/book-covers/', null=True, blank=True)
    pdf = models.FileField(upload_to='shop/File/pdf/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}-({self.author})"


class Author(BaseModel):
    name = models.CharField(max_length=255)
    birth = models.IntegerField(null=True)
    death = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}-({self.birth})"

