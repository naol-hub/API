from rest_framework import serializers
from api_basic.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','email' ,'auther']
   