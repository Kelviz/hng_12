# Number Classification API

## Overview

The **Number Classification API** takes an integer as input and returns interesting mathematical properties about it, along with a fun fact retrieved from the Numbers API.

## Features

- Checks if a number is **prime**.
- Checks if a number is **perfect**.
- Checks if a number is an **Armstrong number**.
- Determines if a number is **even or odd**.
- Returns the **sum of the digits**.
- Fetches a **fun fact** from the Numbers API.

## Technologies Used

- **Python** (Django)
- **Django REST Framework**
- **Numbers API** for fun facts
- **GitHub** for version control

## API Endpoint

### **GET /api/classify-number?number=371**

### **Request Parameters**

| Parameter | Type | Required | Description             |
| --------- | ---- | -------- | ----------------------- |
| number    | int  | Yes      | The integer to classify |

### **Response Format (200 OK)**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Response Format (400 Bad Request)**

```json
{
  "number": "invalid_input",
  "error": true
}
```

## Installation and Setup

### **1. Clone the repository**

```sh
git clone https://github.com/Kelviz/hng_12.git
cd task_1
```

### **2. Create a virtual environment and activate it**

```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Install dependencies**

```sh
pip install -r requirements.txt
```

### **4. Run Django server**

```sh
python manage.py runserver
```

### **5. Test API locally**

Use a browser or tools like **Postman** or **cURL**:

```sh
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

## Deployment

1. Deploy to **Heroku**, **Render**, or **Vercel**.
2. Set up a production-ready **Django server**.
3. Ensure the API is **publicly accessible**.

## CORS Handling

To enable Cross-Origin Resource Sharing (CORS), install Django CORS headers:

```sh
pip install django-cors-headers
```

Add it to `INSTALLED_APPS` and middleware in `settings.py`.

## Error Handling

- Invalid inputs (non-integer or missing `number`) return a **400 Bad Request**.
- Server errors return a **500 Internal Server Error**.

## Contribution

Feel free to fork the repository and submit a **pull request**.

## License

This project is licensed under the **MIT License**.

---
