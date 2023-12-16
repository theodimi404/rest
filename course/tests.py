from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from course.models import Course


class CourseViewsTest(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()
        self.random_id = 1234

    def test_course_list_and_create_view(self):
        # Test GET request to list all courses
        response = self.client.get(reverse('course-list-and-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST request to create a new course
        data = {'title': 'New Course', 'description': 'A new course description'}
        response = self.client.post(reverse('course-list-and-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test POST request to create a new course with a title that already exists
        data = {'title': 'New Course', 'description': 'A new course description'}
        response = self.client.post(reverse('course-list-and-create'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_course_operations_by_id_view(self):
        # Assuming there's a course in the database with id=1
        course = Course.objects.create(title='Test Course', description='A test course description')

        # Test GET request to retrieve a specific course by ID
        response = self.client.get(reverse('course-operations-by-id', args=[course.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test GET request to retrieve a specific course by ID that doesn't exist
        response = self.client.get(reverse('course-operations-by-id', args=[self.random_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Test PUT request to update a specific course by ID
        updated_data = {'title': 'Updated Course', 'description': 'An updated course description'}
        response = self.client.put(reverse('course-operations-by-id', args=[course.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test PUT request to update a specific course by ID that doesn't exist
        updated_data = {'title': 'Updated Course', 'description': 'An updated course description'}
        response = self.client.put(reverse('course-operations-by-id', args=[self.random_id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test DELETE request to delete a specific course by ID
        response = self.client.delete(reverse('course-operations-by-id', args=[course.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Test DELETE request to delete a specific course by ID that doesn't exist
        response = self.client.delete(reverse('course-operations-by-id', args=[self.random_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
