# HNG12 Task 0 - Public API

This is a simple public API developed for **HNG12 Task 0**. It provides basic information such as the registered email address, the current UTC datetime in ISO 8601 format, and the GitHub repository URL of this project.

## Features

- Returns a JSON response containing:
  - Registered email address
  - Current datetime in ISO 8601 format
  - GitHub repository URL
- Uses Django framework
- Supports CORS for cross-origin requests

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Kelviz/hng_12.git
cd task_0
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

---

## API Documentation

### Endpoint:

```http
GET /
```

### Response Format:

```json
{
  "email": "mysviurch@gmail.com",
  "current_datetime": "2025-02-06T17:02:10Z",
  "github_url": "https://github.com/Kelviz/hng_12/tree/main/task_0"
}
```

### Example Usage:

#### cURL

```bash
curl -X GET http://127.0.0.1:8000/
```

#### Python (requests library)

```python
import requests
response = requests.get("http://127.0.0.1:8000/")
print(response.json())
```

---

## Deployment

The API is deployed and accessible at:

```http
https://urchdev-task-0.vercel.app/
```

---

## Resources

For more information about Python developers:
🔗 [Hire Python Developers](https://hng.tech/hire/python-developers)

---

## Author

**Kelviz**

🔗 GitHub: [kelviz](https://github.com/kelviz)
