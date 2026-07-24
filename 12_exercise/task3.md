
# Task 3: Build an AWS AI Services API Layer with FastAPI

## Objective

Design and implement a REST API using **FastAPI** that acts as a unified abstraction layer over multiple AWS AI services. The goal is to expose simple, consistent endpoints that internally communicate with AWS services such as Amazon Comprehend, Amazon Textract, and other native AWS AI services.

The implementation should demonstrate good API design, clean architecture, error handling and maintainability.

---

# Functional Requirements

Implement REST APIs for the following AWS services.

## 1. Amazon Comprehend

Create endpoints for:

* Detect Sentiment
* Detect Dominant Language
* Detect Entities
* Detect Key Phrases
* Detect PII Entities

Example:

```
POST /comprehends/{sentiment}
```

Request

```json
{
    "text": "I absolutely loved the customer service."
}
```

Response

```json
{
    "sentiment": "POSITIVE",
    "score": {
        "positive": 0.99,
        "negative": 0.0,
        "neutral": 0.01
    }
}
```

---

## 2. Amazon Textract

Support:

* Analyze uploaded document
* Extract text from PDF
* Extract text from image
* Support both synchronous and asynchronous processing (bonus)

Example:

```
POST /textracts/{fileupload}
POST /textracts/{extract}
```

Input:

* PDF
* PNG
* JPEG

Return extracted text in JSON format.

---

## 3. Amazon Rekognition

Implement APIs for:

* Detect Labels
* Detect Faces
* Moderate Content

Example

```
POST /rekognitions/{labels}
```

---

## 4. Amazon Translate

Create an endpoint to translate text.

```
POST /translate
```

Request

```json
{
    "text": "Hello",
    "target_language": "fr"
}
```

---

## 5. Amazon Polly

Generate speech from text.

```
POST /speechservices/{polly}
```

Return

* MP3 stream
* Download URL
* Base64 (candidate's choice)

---

## 6. Bedrock (Optional Bonus)

If Bedrock access is available, expose an endpoint that accepts a prompt and returns the generated response.

Example

```
POST /chatservices/{bedrock}
```

---

# Technical Requirements

The project should be implemented using:

* Python 3.11+
* FastAPI
* boto3
* Pydantic
* Uvicorn

---

# Project Structure

A clean architecture is expected.

Example

```
app/
│
├── routes/
│   └── dependencies.py
│
├── services/
│   ├── comprehend.py
│   ├── textract.py
│   ├── rekognition.py
│   ├── translate.py
│   └── polly.py
│
├── schemas/
│
├── core/
│   ├── config.py
│   ├── logging.py
│   └── aws.py
│
├── utils/
│
├── middlewares/
│
├── main.py
│
└── requirements.txt
```

---

# Non-Functional Requirements

The implementation should include:

* Input validation
* Proper HTTP status codes
* Centralized exception handling
* Logging
* Type hints
* Configuration via environment variables
* Clean separation of concerns
* Reusable service layer

---

# Error Handling

Handle common AWS errors gracefully, including:

* Invalid credentials
* Unsupported file formats
* AWS throttling
* Invalid request payloads
* Service unavailability
* Missing required parameters

Return meaningful error messages.

---

# API Documentation

The API should expose Swagger documentation automatically via FastAPI.

Example:

```
/docs
```

and

```
/redoc
```

---

# Bonus Features

Candidates are encouraged to implement one or more of the following:

* Request/response middleware
* Correlation IDs
* Structured logging
* S3 integration for document uploads

---
# Deliverables

The submission should include:

1. Source code
2. README with setup instructions
3. API documentation
4. Example requests
---
