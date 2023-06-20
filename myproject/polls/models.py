from django.db import models


# Create your models here.
class Question(models.Model):
	questioin_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('data published')

	def __str__(self):
		return self.questioin_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField  # 문항을 선택한 사용자 수 입력받을 변수

	def __str__(self):
		return self.choice_text
