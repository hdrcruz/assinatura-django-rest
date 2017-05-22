from django.conf.urls import url, include
from rest_framework import routers
from assinatura_rest.viewsets import AssinaturaViewSet, DocumentoViewSet

router = routers.DefaultRouter()
router.register('images', AssinaturaViewSet, 'images')
router.register('documentos', DocumentoViewSet, 'documentos')

urlpatterns = [
    url(r'^', include(router.urls)),
]
