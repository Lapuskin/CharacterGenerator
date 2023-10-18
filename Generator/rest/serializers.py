from rest_framework import serializers

from rest import models
from rest.models import Race, Class, FirstName, LastName, Personality, Weakness, Ideal, Background, Peculiarities, \
    Attachment, Worldview


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('name', 'description', 'link', 'speed')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = ('id','number')

class FirstNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstName
        exclude = ('id','number')


class LastNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastName
        exclude = ('id','number')

class IdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideal
        exclude = ('id','number')

class WeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weakness
        exclude = ('id','number')

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        exclude = ('id','number')

class PeculiaritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peculiarities
        exclude = ('id','number')

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        exclude = ('id','number')

class WorldviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldview
        exclude = ('id','number')
class PersonalitySerializer(serializers.ModelSerializer):
    first_letter = serializers.SlugRelatedField(slug_field='meaning', read_only=True)
    second_letter = serializers.SlugRelatedField(slug_field='meaning', read_only=True)
    third_letter = serializers.SlugRelatedField(slug_field='meaning', read_only=True)
    fourth_letter = serializers.SlugRelatedField(slug_field='meaning', read_only=True)
    class Meta:
        model = Personality
        exclude = ('id', 'number')

