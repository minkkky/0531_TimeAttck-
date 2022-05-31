from django.db import models # django에서 제공하는 models를 사용

class Article(models.Model):
    class Meta: # 모델의 정보
        db_table = "article" # db 테이블명 설정

    title = models.CharField(max_length=50, default='')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    content = models.TextField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    class Meta: # 모델의 정보
        db_table = "category" # db 테이블명 설정

    name = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)