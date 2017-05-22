from rest_framework import serializers
from assinatura.models import Assinatura, Documento
from drf_extra_fields.fields import Base64ImageField

class AssinaturaSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Assinatura
        fields = ('pk','image',)

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documento
        fields = ('pk','numero','data','entregue','recibo',)
