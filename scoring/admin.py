from django.contrib import admin
from .models import Amount, Age, Duration, Rate

# Register your models here.
admin.site.register(Amount)
admin.site.register(Age)
admin.site.register(Duration)
admin.site.register(Rate)