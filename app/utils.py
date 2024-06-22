from functools import wraps
from flask import request
from .models import ViolationReport

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return {'error': 'Missing or invalid authentication token'}, 401
        # In a real scenario, you would validate the token here
        return func(*args, **kwargs)
    return wrapper

def validate_report(report: ViolationReport) -> bool:
    valid_multimedia_types = {'text', 'image', 'audio', 'video', 'animation'}
    return all([
        report.dataset_id,
        report.violation_type,
        report.description,
        report.multimedia_type in valid_multimedia_types,
        report.content_identifier
    ])