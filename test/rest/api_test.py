import http.client
import os
import unittest
from urllib.request import urlopen, HTTPError


import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK
        )
        self.assertEqual(response.read().decode(), "4")
        
    def test_api_add_error(self):
        url = f"{BASE_URL}/calc/add/2/a"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)
        
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/10/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5")
    
    def test_api_substract_error(self):
        url = f"{BASE_URL}/calc/substract/10/a"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/4/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "12")
    
    def test_api_multiply_error(self):
        url = f"{BASE_URL}/calc/multiply/10/a"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5.0")
        
    def test_api_divide_error(self):
        url = f"{BASE_URL}/calc/divide/t/2"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4.0")

    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-16"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)
        
    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/e"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)
        
    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/t"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)