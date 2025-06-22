from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                    # لوحة التحكم
    path('', include('clients.urls')),                  # ✅ ربط الصفحة الرئيسية
    path('tasks/', include('tasks.urls')),              # روابط تطبيق المهام
    path('reports/', include('reports.urls')),          # روابط تطبيق التقارير
    path('clients/', include('clients.urls')),          # روابط تطبيق العملاء
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
