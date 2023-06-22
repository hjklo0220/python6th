from django.contrib import admin

from polls.models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1


class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']  # admin페이지에 순서 바꿔주는것
	fieldsets = [  # 구체적으로 커스텀하는것
		('Question Statement', {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date']})
	]

	inlines = [ChoiceInline]  # Question 테이블 추가할때 선택지도 등록할 수 있도록(위 ChoiceInline클래스)
	list_display = ('question_text', 'pub_date')  # 시간 정보도 표시
	list_filter = ["pub_date"]  # 시간정보에 대한 필터 추가
	search_fields = ['question_text']  # 검색창 생성


admin.site.register(Question, QuestionAdmin)  # 여기 클래스 추가해줘야함
admin.site.register(Choice)


