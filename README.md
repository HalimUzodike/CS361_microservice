# Pounds to Kilograms Converter Service

## Overview
This Python Flask microservice provides an API endpoint for converting weights from pounds to kilograms. It's a simple and lightweight service designed for ease of use and integration into larger systems or for educational purposes.

## Features
- **Conversion Endpoint**: A POST endpoint accepting weight in pounds and returning the equivalent weight in kilograms.
- **CORS Enabled**: Cross-Origin Resource Sharing (CORS) is enabled, allowing the service to be accessed from different domains.

## Requirements
- Python 3.x
- Flask
- Flask-CORS

## Installation
First, clone the repository or download the source code. Then, install the required dependencies:

```bash
pip install Flask flask-cors
``` 
## Running the Service
To run the service, execute the following command:

```bash
python app.py
```

The service will start on `localhost` at port `5000`.

## Usage
Send a POST request to the `/convert` endpoint with a JSON payload containing the weight in pounds. For example:

```bash
curl -X POST -H "Content-Type: application/json"
-d '{"pounds": 150}'
http://localhost:5000/convert
```

The service will return a JSON response containing the weight in kilograms:

```json
{
  "kilograms": 68.0388555
}
```

![uml_361_microservice](https://github.com/HalimUzodike/CS361_microservice/assets/98881780/da5c4397-392f-462c-ba81-71ebff18c87f)