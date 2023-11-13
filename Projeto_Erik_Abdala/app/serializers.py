from rest_framework import serializers
from . models import Questao

class QuestaoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Questao
        fields = ("id", "titulo", "enunciado", "alternativa_a", "alternativa_b",
                  "alternativa_c", "alternativa_d", "alternativa_e", "alternativa_correta")