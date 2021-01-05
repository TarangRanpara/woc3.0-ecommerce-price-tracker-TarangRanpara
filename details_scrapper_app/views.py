from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Record


def main_page_view(request, *args, **kwargs):
    if request.method == "POST":
        content = request.POST
        link = content.get('link')
        site = content.get('site')
        price = content.get('price')
        email = content.get('email')

        print('link:', link)
        print('site:', site)
        print('price:', price)
        print('email:', email)

        Record.objects.create(
            link=link,
            site=site,
            price=price,
            email=email
        )

        #data scrapping will be performed here.

        context = {
            'link': link,
            'site': site,
            'price': price,
            'email': email
        }

        return render(request, "homepage.html", {'context': context})

    return render(request, 'homepage.html')
