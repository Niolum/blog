from django.test import TestCase
from ..models import Category, Post, Comment 
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name='Games',
        )

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/category/1/')


class PostModelTest(TestCase):

    fixtures = ['category.json', 'post.json', 'user.json']

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_text_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст')

    def test_created_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'Дата')

    def test_owner_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_categories_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('categories').verbose_name
        self.assertEquals(field_label, 'Категории')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/post/1/')


class CommentModelTest(TestCase):

    fixtures = ['category.json', 'post.json', 'user.json', 'comment.json']

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст комментария')

    def test_created_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'Дата')

    def test_owner_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEquals(field_label, 'Пост')