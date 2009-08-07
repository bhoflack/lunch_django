from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=70)
  price = models.DecimalField(max_digits=7, decimal_places=2)

  def __unicode__(self):
    return self.name

class Transaction(models.Model):
  products = models.ManyToManyField('Product')
  who = models.CharField(max_length=3)
  when = models.DateTimeField()
  amount = models.DecimalField(max_digits=7, decimal_places=2)
  comments = models.TextField()
  bywho = models.CharField(max_length=3)
  currentamount = models.DecimalField(max_digits=7, decimal_places=2)

  def __unicode__(self):
    return "%s %d" % (self.who, self.amount)
  
