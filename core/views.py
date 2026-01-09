from django.shortcuts import render

# Create your views here.
import hashlib


def crypto_example(request):
    hashed = None
    password = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password:
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return render(request, 'core/crypto_example.html', {
        'hashed': hashed,
        'password': password,
    })
