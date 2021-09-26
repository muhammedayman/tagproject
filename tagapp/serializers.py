
from tagapp.models import TagModel, TagUser
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields='__all__'
class TagUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagUser
        fields='__all__'

class TagUserCreateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    title = TagSerializer(many=False)
    class Meta:
        model = TagUser
        fields='__all__'

    def to_internal_value(self, data):
        data['auth_user'] = self.context['request'].user.id
        data = super(TagUserCreateSerializer, self).to_internal_value(data)
        return data

    def validate(self, attrs):
        user = self.context['request'].user
        attrs.update({'auth_user': user})
        attrs = super().validate(attrs)
        return attrs

class TagUserDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    title = TagSerializer(many=False)
    class Meta:
        model = TagUser
        fields='__all__'
    
    def to_representation(self, instance):
        data = super(serializers.ModelSerializer, self).to_representation(instance) 
        data['url'] = f'{self.context["request"].build_absolute_uri()}{instance.id}'
        return data        

class TagDetailSerializer(serializers.ModelSerializer):
    snippet = TagUserSerializer(source = 'taguser')
    class Meta:
        model = TagModel
        fields='__all__'