from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch

class FileUploadTests(APITestCase):
    
    def test_upload_page(self):
        url = reverse('upload-page')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_invalid_file_upload(self):
        url = reverse('upload-file-page')
        invalid_file = SimpleUploadedFile("invalid.pdf", b"Invalid file contents", content_type="application/pdf")
        response = self.client.post(url, {'file': invalid_file}, format='multipart')

        self.assertRedirects(response, reverse('result-page') + '?error=Invalid file.')


    @patch('zadanie1.tasks.shuffle_text.delay')
    def test_valid_file_upload(self, mock_shuffle_text):
        url = reverse('upload-file-page')
        text_file = SimpleUploadedFile("test.txt", b"Hello world")
        mock_shuffle_text.return_value.get.return_value = "Hlelo wlrod"
        response = self.client.post(url, {'file': text_file}, format='multipart')
        
        self.assertRedirects(response, reverse('result-page') + '?shuffled_text=Hlelo wlrod')
        mock_shuffle_text.assert_called_once_with("Hello world")
    

    def test_result_page_with_shuffled_text(self):
        url = reverse('result-page')
        response = self.client.get(url, {'shuffled_text': 'Hlelo wlrod'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Hlelo wlrod')
    
    
    def test_result_page_with_error(self):
        url = reverse('result-page')
        response = self.client.get(url, {'error': 'Invalid file'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Invalid file')