from django.conf.urls import include, url
from django.contrib import admin
import blog.views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    # url(r'',blog.views.post_list),
]
