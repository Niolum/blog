from django.test import TestCase
from django.urls import reverse


class PostListViewTest(TestCase):
    fixtures = ['db.json']

    def test_post_list_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
    
    def test_post_list_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_post_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp, 'api/post_list.html')


class PostDetailViewTest(TestCase):
    fixtures = ['db.json']

    def test_post_deatil_view_url_exists_at_desired_location(self):
        resp = self.client.get('/post/1/')
        self.assertEqual(resp.status_code, 200)
    
    def test_post_detail_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('post', args=['1']))
        self.assertEqual(resp.status_code, 200)

    def test_post_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('post', args=['1']))
        self.assertTemplateUsed(resp, 'api/post_detail.html')


class CategoryListViewTest(TestCase):
    fixtures = ['db.json']

    def test_category_list_view_url_exists_at_desired_location(self):
        resp = self.client.get('/category/')
        self.assertEqual(resp.status_code, 200)
    
    def test_category_list_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('categories'))
        self.assertEqual(resp.status_code, 200)

    def test_category_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('categories'))
        self.assertTemplateUsed(resp, 'api/category_list.html')


class CategoryDetailViewTest(TestCase):
    fixtures = ['db.json']

    def test_category_deatil_view_url_exists_at_desired_location(self):
        resp = self.client.get('/category/1/')
        self.assertEqual(resp.status_code, 200)
    
    def test_category_detail_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('category', args=['1']))
        self.assertEqual(resp.status_code, 200)

    def test_category_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('category', args=['1']))
        self.assertTemplateUsed(resp, 'api/category_detail.html')


class AddCommentViewTest(TestCase):
    fixtures = ['db.json']

    def test_view_addreview(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_comment', args=['1']), { 'text':'cool',})
        self.assertRedirects(resp, '/post/1/')


class AddCategoryViewTest(TestCase):
    fixtures = ['db.json']

    def test_view_category(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_category'), { 'name':'AllGames',})
        self.assertRedirects(resp, '/category/10/')


class AddPostViewTest(TestCase):
    fixtures = ['db.json']

    def test_view_post(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_post'), 
                                    {'title': 'All Games',
                                    'text':'games games games games',
                                    'owner': 1,
                                    'categories': 'Gaming'})
        self.assertRedirects(resp, '/post/13/')


class SigninTest(TestCase):
    fixtures = ['db.json']

    def test_login_returns_200(self):
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')

    def test_login_invalid_form(self):
        resp = self.client.post('/accounts/login/', {
            "username": "niolum",
            "password": "170498"
        })
        form = resp.context.get('form')
        self.assertFalse(form.is_valid())


class LogoutTest(TestCase):
    fixtures = ['db.json']

    def test_logout_view(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get('/accounts/logout/')
        self.assertEqual(resp.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get('/accounts/logout/')
        self.assertTemplateUsed(resp, 'registration/logged_out.html')


class EditProfileTest(TestCase):
    fixtures = ['db.json']

    def test_login_and_open_editprofile(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('edit_profile', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('edit_profile', args=[1]))
        self.assertRedirects(resp, '/accounts/login/?next=/edit-profile/1/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('edit_profile', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/user_form.html')


class UserProfileTest(TestCase):
    fixtures = ['db.json']

    def test_view_userprofile(self):
        resp = self.client.get(reverse('user', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_userprofile_uses_correct_template(self):
        resp = self.client.get(reverse('user', args=[1]))
        self.assertTemplateUsed(resp, 'registration/user_detail.html')


class SignupTest(TestCase):

    def test_registration_view(self):
        resp = self.client.post(reverse('signup'), 
                                    {'username':'foo', 
                                    'password':'bar', 
                                    'password2':'bar' })
        self.assertEqual(resp.status_code, 200)

    def test_registration_uses_correct_template(self):
        resp = self.client.get(reverse('signup'))
        self.assertTemplateUsed(resp, 'registration/signup.html')