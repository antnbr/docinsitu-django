from django.contrib import admin
from .models import Article
from .models import Subject
from .models import Snap

admin.site.register(Article)
admin.site.register(Subject)
admin.site.register(Snap)
