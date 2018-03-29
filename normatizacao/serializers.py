# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Normatizador
from rest_framework import serializers
from .classificacao import Classificacao

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class NormatizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Normatizador
        fields = ('__all__')

    def create(self, data):
        classificador = Classificacao.Analise()
        normatizado = Normatizador()
        normatizado.text = classificador.classificar(data['text'])
        return normatizado