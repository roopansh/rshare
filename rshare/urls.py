from django.conf.urls import url, include#, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='share/',permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^share/', include('share.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
# urlpatterns += patterns(
	# '', url(r'^captcha/', include('captcha.urls')),
# )
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)