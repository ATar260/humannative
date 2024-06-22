from flask import request
from flask_restful import Resource
from .models import ViolationReport
from .utils import authenticate, validate_report

class ReportViolation(Resource):
    def get(self):
        return {"message": "GET request received"}, 200
    @authenticate
    def post(self):
        data = request.json
        try:
            report = ViolationReport(**data)
            
            if not validate_report(report):
                return {"error": "Invalid report data"}, 400

            # Process the report (in a real scenario, this would involve database operations)
            # For now, we'll just return a success message
            return {"message": "Violation report submitted successfully"}, 201
        except TypeError as e:
            return {"error": str(e)}, 400

def add_resources(api):
    api.add_resource(ReportViolation, '/report')