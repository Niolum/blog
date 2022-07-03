from ..models import Post, Category, Comment
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib import auth
from django.urls import reverse

# Create your tests here.
class UserTests(APITestCase):

    def setUp(self):
        new_user1_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }

        self.new_user1 = User.objects.create_user(
            username=new_user1_data["username"],
            first_name=new_user1_data["first_name"],
            last_name=new_user1_data["last_name"],
            email=new_user1_data["email"],
            password=new_user1_data["password"]
        )

    
    def test_login_and_logout(self):
        """
        тест на вход и выход пользователя
        """
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print("[!] Login failed!")
        user = auth.get_user(self.client)
        print("user: ", user)
        print(User.objects.all())

        self.client.logout()
        user = auth.get_user(self.client)
        print("user: ", user)


class BlogTests(APITestCase):

    def setUp(self):
        new_user1_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }


        self.new_user1 = User.objects.create_user(
            username=new_user1_data["username"],
            first_name=new_user1_data["first_name"],
            last_name=new_user1_data["last_name"],
            email=new_user1_data["email"],
            password=new_user1_data["password"]
        )


    def test_post_list(self):
        """
        тест на создание категории
        """
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print("[!] Login failed!")
        user = auth.get_user(self.client)
        print("user: ", user)
        print(User.objects.all())

        url1 = reverse('category-list')
        data1 = {'name': 'Game'}
        response1 = self.client.post(url1, data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        print(response1.data)

        """
        тест на создание поста
        """
        url2 = reverse('post-list')
        data2 = {'title': 'VideoGame',
            'text': 'text',
            'owner': 1,
            'categories': 1
        }
        response2 = self.client.post(url2, data2)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        print(response2.data)

        """
        тест на создание комментария к посту
        """
        url3 = reverse('comment-list')
        data3 = {'text': 'Message',
            'owner': 1,
            'post': 1
        }
        response3 = self.client.post(url3, data3)
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        print(response3.data)
