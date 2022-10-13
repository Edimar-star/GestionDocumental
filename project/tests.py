from django.test import TestCase, Client
from django.urls import reverse

STATUS_CODE_AUTH = 200
STATUS_CODE = 302

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login(self):
        resp = self.client.get('/accounts/login/')
        self.assertEquals(resp.status_code, STATUS_CODE_AUTH)
        self.assertTemplateUsed('signIn.html')

    def test_register(self):
        resp = self.client.get('/register/')
        self.assertEquals(resp.status_code, STATUS_CODE_AUTH)
        self.assertTemplateUsed('signUp.html')

    def test_home(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, STATUS_CODE)
        self.assertTemplateUsed('products.html')

    def test_history(self):
        resp = self.client.get('/history/')
        self.assertEquals(resp.status_code, STATUS_CODE)
        self.assertTemplateUsed('history.html')

    def test_admins(self):
        resp = self.client.get('/admins/')
        self.assertEquals(resp.status_code, STATUS_CODE)
        self.assertTemplateUsed('admin.html')

    def test_myDocuments(self):
        resp = self.client.get('/myDocuments/')
        self.assertEquals(resp.status_code, STATUS_CODE)
        self.assertTemplateUsed('myDocuments.html')

if __name__ == '__main__':
    main()