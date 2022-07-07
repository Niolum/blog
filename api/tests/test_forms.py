from django.test import TestCase
from ..models import Category, Comment, Post
from django.urls import reverse


class AddPostFormTest(TestCase):
    fixtures = ['db.json']

    def test_create_post(self):
        post_count = Post.objects.count()
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_post'), 
                                    {'title': 'All Games',
                                    'text':'games games games games',
                                    'owner': 1,
                                    'categories': 'Gaming'})
        self.assertRedirects(resp, '/post/13/')                            
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Post.objects.count(), post_count+1)
        self.assertTrue(Post.objects.filter(title='All Games'))


class AddCategoryFormTest(TestCase):
    fixtures = ['db.json']

    def test_create_category(self):
        category_count = Category.objects.count()
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_category'), { 'name':'AllGames',})
        self.assertRedirects(resp, '/category/10/')
        self.assertEqual(Category.objects.count(), category_count+1)
        self.assertTrue(Category.objects.filter(name='AllGames'))


class CommentFormTest(TestCase):
    fixtures = ['db.json']

    def test_create_review(self):
        comment_count = Comment.objects.count()
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_comment', args=[1]), { 'text':'cool',})
        self.assertRedirects(resp, '/post/1/')
        self.assertEqual(Comment.objects.count(), comment_count+1)
        self.assertTrue(Comment.objects.filter(text='cool'))