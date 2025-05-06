import requests
from django.shortcuts import render

def exchange_policy(request):
    try:
        # Fetch content from Flask API
        response = requests.get('http://127.0.0.1:5000/api/exchange-policy')
        if response.status_code == 200:
            data = response.json()
            return render(request, 'user_app/exchange_policy.html', {
                'content': data['content']
            })
        else:
            return render(request, 'user_app/exchange_policy.html', {
                'error': 'Failed to load exchange policy content'
            })
    except requests.RequestException as e:
        return render(request, 'user_app/exchange_policy.html', {
            'error': 'Failed to connect to the service'
        })