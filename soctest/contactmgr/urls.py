from django.conf.urls import url

from .views import FileUploadView, RetrieveDestroyContact


urlpatterns = [
    url(r'^upload$', FileUploadView.as_view(), name='upload'),
    url(r'(?P<pk>\d+)$',
        RetrieveDestroyContact.as_view(),
        name='retrieve-destroy-contact'),
]
