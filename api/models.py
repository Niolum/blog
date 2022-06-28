from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('Название', max_length=100, blank=True, default='')
    text = models.TextField('Текст', blank=True, default='')
    created = models.DateTimeField('Дата', auto_now_add=True)
    owner = models.ForeignKey('auth.User', verbose_name='Имя', related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', verbose_name='Пост', related_name='posts')

    def __str__(self):
        return f"{self.id} | {self.title} | {self.owner}"

    class Meta:
        ordering = ['created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk":self.pk})

class Category(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={"pk":self.pk})


class Comment(models.Model):
    text = models.TextField('Текст комментария', blank=False)
    owner = models.ForeignKey('auth.User', verbose_name='Имя', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Пост', related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return f"{self.owner} | {self.post}"

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'