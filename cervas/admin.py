from django.contrib import admin

# Register your models here.
from .models import Markets
from .models import Brands
from .models import Beers
from .models import Basket

admin.site.register(Markets)
admin.site.register(Brands)
admin.site.register(Beers)
admin.site.register(Basket)
