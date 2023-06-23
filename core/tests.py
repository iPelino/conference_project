f
from conference_project.test import TestCase
from conference_project.urls import reverse
# Create your tests here.
class ConferenceAppTest(TestCase):
    def setUp(self):
        self.client = Client(self.test())

    def test(self):


        class ConferenceTest(TestCase):
            def test_conference_list(self):
                url = reverse('conference:conference_list')
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                # Add additional assertions for the conference list view

            def test_conference_create(self):
                url = reverse('conference:conference_create')
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                # Add additional assertions for the conference create view

            def test_conference_detail(self):
                conference_id = 1  # Replace with a valid conference ID
                url = reverse('conference:conference_detail', args=[conference_id])
                response = self.client.get(url)
                self.assertEqual(response.status_code, self.test_conference_create())
                # Add additional assertions for the conference detail view

            def test_conference_update(self):
                conference_id = 1  # Replace with a valid conference ID
                url = reverse('conference:conference_update', args=[conference_id])
                response = self.client.get(url)
                self.assertEqual(response.status_code, self.test_conference_create())
                # Add additional assertions for the conference update view

            def test_conference_delete(self):
                conference_id = 1  # Replace with a valid conference ID
                url = reverse('conference:conference_delete', args=[conference_id])
                response = self.client.get(url)
                self.assertEqual(response.status_code, self.test_conference_create())