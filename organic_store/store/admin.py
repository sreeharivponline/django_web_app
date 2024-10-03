from django.contrib import admin
from .models import Product  # Import the Product model

class ProductAdmin(admin.ModelAdmin):
    # List of fields to display in the admin panel for each product
    list_display = ('name', 'price', 'description')
    
    # Fields to make searchable in the admin interface
    search_fields = ('name', 'description')
    
    # Add filter options in the admin list view
    list_filter = ('price',)

    # Customize how the fields are displayed in the form
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'description')
        }),
        ('Media', {
            'fields': ('image',)  # You can include an image or other media fields here if applicable
        }),
    )

# Register the Product model with the ProductAdmin configuration
admin.site.register(Product, ProductAdmin)
