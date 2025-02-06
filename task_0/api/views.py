from django.http import JsonResponse
from datetime import datetime, timezone
import pytz

def public_api(request):
    response_data = {
        "email": "mysviurch@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Kelviz/hng_12/tree/main/task_0"
    }
    return JsonResponse(response_data, status=200)
