from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post


class PostsSerializer(serializers.HyperlinkedModelSerializer):

    headline = serializers.CharField(required=False)
    body_text = serializers.CharField(required=False)

    def validate_headline(self, headline):
        if len(headline) < 2:
            raise ValidationError('headline 2 karakterden kısa olamaz.')
        return headline

    def validate_body_text(self, body_text):
        if len(body_text) < 10:
            raise ValidationError('bodytext 10 karakterden kısa olamaz.')
        return body_text

    def save(self, **kwargs):
        validated_data = self.validated_data
        data = self.initial_data

        post = Post.objects.create(
            headline = validated_data.get("headline"),
            body_text = validated_data.get("body_text"),
            pub_date = data.get("pub_date"),
            author =data.get("author"),
        )

        post.save()
        return self

    class Meta:
        model = Post
        fields = ('headline','body_text','pub_date',"author_id",'id')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('headline','body_text','pub_date',"author_id",'id')

