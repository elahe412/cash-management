from rest_framework.test import APITestCase
from faker import Factory
import factory.fuzzy

faker = Factory.create()


class TestSetup(APITestCase):

    def setUp(self) -> None:
        self.email = faker.email()
        self.password = faker.password()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
