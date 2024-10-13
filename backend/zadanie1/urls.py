from django.urls import path

from .views import FileUploadView, upload_page, result_page


urlpatterns = [
    path('', upload_page, name='upload-page'),
    path('upload-file-page', FileUploadView.as_view(), name='upload-file-page'),
    path('result/', result_page, name='result-page')
]
