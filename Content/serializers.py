from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Content, Rate


class ContentSerializer(serializers.ModelSerializer):
    count_rate_users = serializers.ReadOnlyField()
    rate_avg = serializers.ReadOnlyField()

    class Meta:
        model = Content
        fields = (
            'title',
            'count_rate_users',
            'rate_avg'
        )


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'score',
            'content',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Rate.objects.all(),
                fields=('list', 'position')
            )
        ]

    def save(self, **kwargs):
        score = self.validated_data['score']
        user = self.context['request'].user
        content = self.validated_data['content']
