from django.views.generic import TemplateView

from django.apps import apps


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# context['app_list'] = ['polls', 'books']
		dictVerbose = {}  # 딕셔너리 변수 하나 생성
		for app in apps.get_app_configs():
			if 'site-packages' not in app.path:
				dictVerbose[app.label] = app.verbose_name
		context['verbose_dict'] = dictVerbose
		return context

