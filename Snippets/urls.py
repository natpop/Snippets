from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', views.login_page, name="auth"),
    path('logout/', views.logout, name="logout"),
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippet/<int:id>', views.snippet_detail, name="snippet_detail"),
    path('delete/<int:id>', views.snippet_delete, name="snippet_delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
