from django.test import TestCase
from .models import NewPolicy
# Create your tests here.

class NewPolicyTest(TestCase):
    def setUp(self):
        NewPolicy.objects.create(
                                 Title="Test Title",
                                 IssueBureau='MFA',
                                 Text='Test text',
                                )
    def test_New_Policy_Create(self):
        test_policy=NewPolicy.objects.get(Title='Test Title')
        self.assertEqual(test_policy.IssueBureau, 'MFA')
        self.assertEqual(test_policy.Text, 'Test text')
