from django.contrib import admin
from django.urls import path, include  # include lets us plug in other url configs

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the URLs from your core app
    path('', include('core.urls')),  # Now your core views are accessible via paths like /roles/, /users/, etc.
]
