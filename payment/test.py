import unittest
import payment
from unittest.mock import patch, MagicMock
from flask import Flask

class TestPayment(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    @patch('payment.requests.get')
    def test_health(self, mock_get):
        mock_get.return_value.status_code = 200
        response = payment.health()
        self.assertEqual(response, 'OK')

    @patch('payment.requests.get')
    def test_pay(self, mock_get):
        with self.app.test_request_context('/?total=100&items=[{"sku": "SHIP"}]'):
            # Mocking the request.get call in the pay function
            mock_get.return_value.status_code = 200
            payment.request.get_json = MagicMock(return_value={'total': 100, 'items': [{'sku': 'SHIP'}]})
            response = payment.pay('id')
            self.assertEqual(response[1], 200)

    @patch('payment.requests.get')
    def test_pay_payment_error(self, mock_get):
        with self.app.test_request_context('/?total=100&items=[{"sku": "SHIP"}]'):
            # Mocking the request.get call in the pay function
            mock_get.return_value.status_code = 400
            payment.request.get_json = MagicMock(return_value={'total': 100, 'items': [{'sku': 'SHIP'}]})
            response = payment.pay('id')
            self.assertEqual(response[1], 400)

    @patch('payment.requests.get')
    def test_pay_invalid_cart(self, mock_get):
        with self.app.test_request_context('/?total=0&items=[{"sku": "SHIP"}]'):
            # Mocking the request.get call in the pay function
            mock_get.return_value.status_code = 200
            payment.request.get_json = MagicMock(return_value={'total': 0, 'items': [{'sku': 'SHIP'}]})
            response = payment.pay('id')
            self.assertEqual(response[1], 400)

if __name__ == '__main__':
    unittest.main()
