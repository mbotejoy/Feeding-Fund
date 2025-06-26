from django.contrib import admin
from django.urls import path, include            # include lets us plug in other url configs
from django.conf import settings                 # Import settings
from django.conf.urls.static import static       # Import static()

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the URLs from your core app
    path('', include('core.urls')),  # Now your core views are accessible via paths like /roles/, /users/, etc.
] 

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

