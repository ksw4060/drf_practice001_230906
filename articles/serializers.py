from rest_framework import serializers
from articles.models import Article, Comment



class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    # SerializerMethodField로 값을 가져오려면, models.py 에 있는 Article 모델에, 현존하는 field 로 해야한다.
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'user', 'uploaded_image', "likes"]
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

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    def get_article(self, obj):
        return obj.article.title
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_article(self, obj):
        return obj.article.title

    class Meta:
        model = Comment
        fields = ["id", "user", "article", "comment", "created_at",]
        extra_kwargs = {
                "comment": {
                    "error_messages": {
                        "blank": "댓글 내용을 입력해주세요",
                    }
                },
            }
