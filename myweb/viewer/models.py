from django.db.models import *

class Category(Model):
    name = CharField(max_length=50)
    image = ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name


class Property(Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=CASCADE)
    image = ImageField(upload_to='uploads/')
    order = IntegerField()
    title = CharField(max_length=500)
    price = IntegerField(default=150)


class Order(Model):
    name_surname = CharField(max_length=200)
    email = EmailField()
    phone = CharField(max_length=20)
    date_from = DateField()
    date_to = DateField()
    address = CharField(max_length=100)
    city = CharField(max_length=100)
    postal = BigIntegerField()
    price = IntegerField(null=True, blank=True)
    paid = BooleanField(default=False)


