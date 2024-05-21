from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):

    def setUp(self):
        """ Creates about me content """
        self.about_content = About(
            title='About Me', content='This is about me.'
        )
        self.about_content.save()

    def test_render_about_page_with_collaboration_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"about", response.content)
        self.assertIsInstance(
            response.content['collaborate_form'], CollaborateForm
        )

    def test_successful_collaboration_request(self):
        post_data = {
            'name': 'John',
            'email': 'test@test.com',
            'message': 'This is a test collaboration request.'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )