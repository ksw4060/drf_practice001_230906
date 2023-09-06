from rest_framework import serializers
from articles.models import Article



class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title', 'content']
        # blank = True 인 경우, serializer 에서 빈 값들에 대한 에러 메시지를 지정해줄 수 있음.
        extra_kwargs = {
                "title": {
                    "error_messages": {
                        "blank": "제목을 입력해주세요",
                    }
                },
                "content": {
                    "error_messages": {
                        "blank": "게시글 내용을 입력해주세요",
                    },
                },
            }
