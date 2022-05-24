from rest_framework import serializers
from .models import *

class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    base = BookJournalBaseSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    base = BookJournalBaseSerializer(many=True)

    class Meta:
        model = Journal
        fields = '__all__'