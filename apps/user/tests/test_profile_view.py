from django.urls import reverse

from common.base.base_test import TestSetup


class TestViews(TestSetup):

    def test_unauthorized_user_profile(self):
        register_url = reverse('apps.user:user-profile')
        res = self.client.get(path=register_url)
        self.assertEqual(res.status_code, 401)
