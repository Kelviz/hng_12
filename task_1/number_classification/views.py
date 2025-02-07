import math
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

class NumberClassificationView(View):
    def get(self, request):
        number = request.GET.get("number", None)

        # Validate input
        if not number or not number.isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        number = int(number)

        # Check properties
        is_prime = self.is_prime(number)
        is_perfect = self.is_perfect(number)
        is_armstrong = self.is_armstrong(number)
        is_even = self.is_even(number)
        digit_sum = sum(int(digit) for digit in str(number))
        parity = "even" if is_even else "odd"
        
        # Determine properties list
        properties = []
        if is_armstrong:
            properties.append("armstrong")
        properties.append(parity)

        # Fetch fun fact
        fun_fact = self.get_fun_fact(number)

        # Return response
        return JsonResponse({
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }, status=200)
     

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_armstrong(self, num):
                num_str = str(num)
                n = len(num_str)
                total = 0
                for digit in num_str:
                        total += int(digit) ** n
                return total == num


    def is_even(self, num):
        return num % 2 == 0


    def is_perfect(self, num):
        num_list = []
        for i in range(1, num):
                if num % i == 0:
                        num_list.append(i)
        return num == sum(num_list)


    def get_fun_fact(self, num):
        try:
            response = requests.get(f"http://numbersapi.com/{num}/math?json")
            if response.status_code == 200:
                return response.json().get("text", "No fact available")
        except requests.exceptions.RequestException:
            pass
        return "No fact available"

