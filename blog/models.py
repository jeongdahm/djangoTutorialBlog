from django.db import models #다른 파일에 있는 것을 추가하라
from django.utils import timezone

'''
주석 여러줄
'''
class Post(models.Model):#모델을 정의하는 코드  models.Model: Post가 장고 모델임을 의미
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #models.ForeignKey - 다른 모델에 대한 링크를 의미합니다
    title = models.CharField(max_length=200) # models.CharField - 글자 수가 제한된 텍스트를 정의
    text = models.TextField() #models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField( #날짜 시간 
        default=timezone.now
    )
    published_date = models.DateTimeField(  #날짜 시간 
        blank=True, null=True
    )

    def publish(self): #def: 함수/ 메서드    -----  publish라는 메서드(method) 
        self.published_date = timezone.now()
        self.save()         

    def __str__(self):
        return self.title ## 리턴 있음