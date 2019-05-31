from rest_framework import serializers

from apps.risk import models


class RiskTypeSerializer(serializers.ModelSerializer):
    field_names = serializers.SerializerMethodField()

    class Meta:
        model = models.RiskType
        fields = '__all__'

    @staticmethod
    def get_field_names_(ob):
        has_fields = True
        try:
            ob.risk_fields
        except models.RiskField.DoesNotExist:
            has_fields = False
        return ob.risk_fields.values_list('name') if has_fields else None


class RiskFieldSerializer(serializers.ModelSerializer):
    enum_choices = serializers.SerializerMethodField()

    class Meta:
        model = models.RiskField
        fields = '__all__'

    @staticmethod
    def get_enum_choices(ob):
        has_choices = True
        try:
            ob.choices
        except models.EnumChoice.DoesNotExist:
            has_choices = False
        return ob.choices.values_list('name') if has_choices else None
