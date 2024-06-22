import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import unittest
import requests

# Assuming your app is running on localhost:5000
BASE_URL = "http://localhost:5000"

class TestReportViolation(unittest.TestCase):
    def test_report_violation_success(self):
        headers = {'Authorization': 'Bearer test_token', 'Content-Type': 'application/json'}
        data = {
            'dataset_id': 'test_dataset',
            'data_id': 'test_data',
            'violation_type': 'PII',
            'description': 'Contains personal email address',
            'multimedia_type': 'text',
            'content_identifier': 'document1.txt'
        }
        response = requests.post(f"{BASE_URL}/report", headers=headers, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Violation report submitted successfully', response.json()['message'])

    def test_report_violation_missing_auth(self):
        data = {
            'dataset_id': 'test_dataset',
            'data_id': 'test_data',
            'violation_type': 'PII',
            'description': 'Contains personal email address',
            'multimedia_type': 'text',
            'content_identifier': 'document1.txt'
        }
        response = requests.post(f"{BASE_URL}/report", json=data)
        self.assertEqual(response.status_code, 401)

    def test_report_violation_invalid_data(self):
        headers = {'Authorization': 'Bearer test_token', 'Content-Type': 'application/json'}
        data = {
            'dataset_id': 'test_dataset',
            'violation_type': 'PII',
            'description': 'Contains personal email address',
            'multimedia_type': 'invalid_type',
            'content_identifier': 'document1.txt'
        }
        response = requests.post(f"{BASE_URL}/report", headers=headers, json=data)
        self.assertEqual(response.status_code, 400)

    def test_report_violation_different_multimedia_types(self):
        headers = {'Authorization': 'Bearer test_token', 'Content-Type': 'application/json'}
        multimedia_types = ['text', 'image', 'audio', 'video', 'animation']
        for mtype in multimedia_types:
            data = {
                'dataset_id': 'test_dataset',
                'violation_type': 'PII',
                'description': f'Contains personal information in {mtype}',
                'multimedia_type': mtype,
                'content_identifier': f'content1.{mtype}'
            }
            response = requests.post(f"{BASE_URL}/report", headers=headers, json=data)
            self.assertEqual(response.status_code, 201, f"Failed for multimedia type: {mtype}")

if __name__ == '__main__':
    unittest.main()