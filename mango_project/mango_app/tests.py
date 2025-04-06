from django.test import TestCase, Client
from django.urls import reverse
from .data import mango_items, get_item_by_id

class MangoAppViewTests(TestCase):

    def setUp(self):
        """Set up the test client."""
        self.client = Client()
        self.valid_item_id = 1  # Assuming item with ID 1 exists from data.py
        self.invalid_item_id = 999 # Assuming item with ID 999 does not exist

    def test_home_view(self):
        """Test the home view returns 200 and uses the correct template."""
        response = self.client.get(reverse('mango_app:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mango_app/home.html')

    def test_projects_list_view(self):
        """Test the projects list view returns 200, uses correct template, and has context."""
        response = self.client.get(reverse('mango_app:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mango_app/projects.html')
        self.assertTrue('mango_items' in response.context)
        self.assertEqual(len(response.context['mango_items']), len(mango_items))

    def test_project_detail_view_valid_id(self):
        """Test the project detail view with a valid ID returns 200 and correct context."""
        url = reverse('mango_app:project_detail', args=[self.valid_item_id])
        response = self.client.get(url)
        expected_item = get_item_by_id(self.valid_item_id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mango_app/detail.html')
        self.assertTrue('item' in response.context)
        self.assertEqual(response.context['item'], expected_item)

    def test_project_detail_view_invalid_id(self):
        """Test the project detail view with an invalid ID returns 404."""
        url = reverse('mango_app:project_detail', args=[self.invalid_item_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_project_detail_view_non_numeric_id(self):
        """Test the project detail view with a non-numeric ID returns 404."""
        # Need to construct the URL manually as reverse expects numeric args here
        response = self.client.get(f'/projects/abc/') # Using the pattern from urls.py
        # Note: Django's URL routing might catch this before the view, but testing is good.
        # Depending on server config, this might also be a 404 from the URL resolver.
        self.assertEqual(response.status_code, 404)

    def test_surveillance_view(self):
        """Test the surveillance view returns 200 and uses the correct template."""
        response = self.client.get(reverse('mango_app:surveillance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mango_app/surveillance.html')

    def test_about_view(self):
        """Test the about view returns 200, uses correct template, and has context."""
        response = self.client.get(reverse('mango_app:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mango_app/about.html')
        self.assertTrue('team_members' in response.context)
        self.assertIsInstance(response.context['team_members'], list)

class MangoAppContextProcessorTests(TestCase):

    def test_active_menu_context_processor(self):
        """Test the active_menu context processor adds correct flags."""
        # Test home URL
        response = self.client.get(reverse('mango_app:home'))
        self.assertTrue('active_section' in response.context)
        self.assertTrue(response.context['active_section']['is_home'])
        self.assertFalse(response.context['active_section']['is_projects'])
        
        # Test projects URL
        response = self.client.get(reverse('mango_app:projects'))
        self.assertTrue('active_section' in response.context)
        self.assertFalse(response.context['active_section']['is_home'])
        self.assertTrue(response.context['active_section']['is_projects'])
        
        # Test detail URL (should also flag projects as active)
        response = self.client.get(reverse('mango_app:project_detail', args=[1]))
        self.assertTrue('active_section' in response.context)
        self.assertFalse(response.context['active_section']['is_home'])
        self.assertTrue(response.context['active_section']['is_projects'])

        # Test surveillance URL
        response = self.client.get(reverse('mango_app:surveillance'))
        self.assertTrue('active_section' in response.context)
        self.assertTrue(response.context['active_section']['is_surveillance'])

        # Test about URL
        response = self.client.get(reverse('mango_app:about'))
        self.assertTrue('active_section' in response.context)
        self.assertTrue(response.context['active_section']['is_about'])

# Add more tests here if needed, e.g., for data functions if they were more complex
