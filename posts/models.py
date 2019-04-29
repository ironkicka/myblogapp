from django.db import models


# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=100)
    published=models.DateTimeField()
    image=models.ImageField(upload_to='media/')
    body=models.TextField()

    #管理サイトで記事名表示する用　消してみたらわかる
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

