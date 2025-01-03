from django.contrib import admin
from reviews.models import Review

# Register your models here.


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['created_at']


admin.site.register(Review, ReviewsAdmin)
