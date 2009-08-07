from django.template import Context, loader
from lunch_django.lunch.models import Product, Transaction
from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required


def index(request):
  products = Product.objects.all().order_by('name')
  t = loader.get_template('products/index.html')
  c = Context({ 'products' : products })
  return HttpResponse(t.render(c))

@login_required
def order(request, product_id):
  products = Product.objects.filter(id=product_id)
  amount = int(request.POST['amount'])
  if len(products) != 1:
    # show error page
    return HttpResponse('Invalid product id')
  product = products[0]
  user = request.user.username
  transaction = Transaction(who=user, when=datetime.now(), amount=(product.price * amount), bywho=user, currentamount=product.price)
  transaction.save()
  return index(request)
