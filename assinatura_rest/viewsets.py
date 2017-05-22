from rest_framework import viewsets
from assinatura_rest.serializers import AssinaturaSerializer, DocumentoSerializer
from assinatura.models import Assinatura, Documento

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
