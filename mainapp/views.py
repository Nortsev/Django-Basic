from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')

def test_context(request):
    context = {
        'title': "wellcom home",
        "h1": "hello my friend",
        'user_name': "Timati",
        "product": [
            {'name': "Iphone 7", 'price': '7000'},
            {'name': "Iphone 8", 'price': '9000'},
        ],

        'promo_product': [
            #{'name': "Iphone 7", 'price': '6000'},
        ]



    }
    return render(request, 'mainapp/context.html', context)

