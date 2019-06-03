from rest_framework import serializers

from apps.risk import models


class RiskTypeSerializer(serializers.ModelSerializer):
    field_names_ = serializers.SerializerMethodField()

    class Meta:
        model = models.RiskType
        fields = '__all__'

    @staticmethod
    def get_field_names_(ob):
        names = ob.risk_fields.values_list('name', flat=True)
        return names[0] if len(names) else None


class RiskFieldSerializer(serializers.ModelSerializer):
    enum_choices = serializers.SerializerMethodField()

    class Meta:
        model = models.RiskField
        fields = '__all__'

    @staticmethod
    def get_enum_choices(ob):
        choices = ob.choices.values_list('name', flat=True)
        return choices[0] if len(choices) else None


class EnumChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnumChoice
        fields = '__all__'
