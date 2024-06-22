# Human Native AI - Violation Reporting Service

This service allows licensees to report data they expect is in violation of local laws or regulations.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: 
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the Service

Run the following command:

python run.py

python -m unittest discover tests


## API Usage

To report a violation, send a POST request to `/report` with the following JSON body:

```json
{
    "dataset_id": "example_dataset",
    "data_id": "example_data",
    "violation_type": "PII",
    "description": "Contains personal email address",
    "multimedia_type": "text",
    "content_identifier": "document1.txt"
}