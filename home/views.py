from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'admin_bootstrap', 'url': 'http://pypi.python.org/pypi/admin_bootstrap/0.7.0'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-75',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
