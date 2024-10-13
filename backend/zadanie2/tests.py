from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

from .tasks import check_pesel_data


class PeselCheckTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('check-pesel')


    @patch('zadanie2.tasks.check_pesel_data')
    def test_valid_pesel(self, mock_check_pesel_data):
        valid_pesel = '00323106070'  # 2000-12-31, male

        response = self.client.post(self.url, {'pesel': valid_pesel}, format='json')
        print("Response data 1:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['birthdate'], '2000-12-31')
        self.assertEqual(response.data['sex'], 'Male')


    @patch('zadanie2.tasks.check_pesel_data')
    def test_invalid_pesel(self, mock_check_pesel_data):
        mock_check_pesel_data.return_value = None

        invalid_pesel = '123456789' # less than 11 digits

        response = self.client.post(self.url, {'pesel': invalid_pesel}, format='json')
        print("Response data 2:", response.data)    
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid PESEL number: not exact 11 digits')


    @patch('zadanie2.tasks.check_pesel_data')
    def test_invalid_characters_in_pesel(self, mock_check_pesel_data):
        invalid_pesel = '00210x12345'  # x inside pesel

        response = self.client.post(self.url, {'pesel': invalid_pesel}, format='json')
        print("Response data 3:", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid PESEL number: not a number')


    @patch('zadanie2.tasks.check_pesel_data')
    def test_invalid_pesel_control_digit(self, mock_check_pesel_data):
        invalid_pesel = '00323106071'  # Invalid control digit, should be 0
        response = self.client.post(self.url, {'pesel': invalid_pesel}, format='json')
        print("Response data 4:", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid PESEL: incorrect control digit')
