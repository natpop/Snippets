from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logon/', views.login_page, name="logon"),
    path('logout/', views.logout, name="logout"),
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('my_snippets/list', views.my_snippets_page, name="my_snippets-list"),
    path('snippet/<int:id>', views.snippet_detail, name="snippet_detail"),
    path('delete/<int:id>', views.snippet_delete, name="snippet_delete"),
    path('edit/<int:id>', views.snippet_edit, name="snippet_edit"),
    path('register', views.create_user, name="create_user"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
