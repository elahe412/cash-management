from django.urls import reverse

from common.base.base_test import TestSetup


class TestViews(TestSetup):

    def test_user_can_register(self):
        register_url = reverse('apps.user:create-user')
        user_data = {'email': self.email, 'password': self.password}
        res = self.client.post(path=register_url, data=user_data)
        self.assertEqual(res.status_code, 201)
