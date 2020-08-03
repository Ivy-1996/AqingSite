from django.views.generic import TemplateView, DetailView, ListView
from . import models


# Create your views here.
class BaseView:

    @property
    def extra_context(self):
        company_info = models.CompanyInfo.objects.filter(display=True).first()
        banners = models.Banner.objects.filter(display=True)
        return {'company_info': company_info, 'banners': banners}


class IndexView(BaseView, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        news = models.News.objects.filter(display=True).order_by('-id')[0:2]
        cases = models.Cases.objects.filter(display=True).order_by('-id')[0:8]
        context['news'] = news
        context['cases'] = cases
        context['active'] = 'index'
        return context


class AboutView(BaseView, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['active'] = 'about'
        return context


class RecruitmentView(BaseView, ListView):
    template_name = 'zhaopin.html'
    model = models.Recruitment
    paginate_by = 8

    def get_queryset(self):
        return super(RecruitmentView, self).get_queryset().filter(display=True)


class RecruitmentDetailView(BaseView, DetailView):
    template_name = 'zhaopin_info.html'
    model = models.Recruitment


class NewsView(BaseView, ListView):
    template_name = 'news.html'
    model = models.News
    paginate_by = 8

    def get_queryset(self):
        type = self.request.GET.get('type', 0)
        return super(NewsView, self).get_queryset().filter(display=True, type=type)

    @property
    def extra_context(self):
        data = super().extra_context
        data['type'] = self.request.GET.get('type', '0')
        return data


class NewsDetailView(BaseView, DetailView):
    template_name = 'news_detail.html'
    model = models.News

    def get_queryset(self):
        return super(NewsDetailView, self).get_queryset().filter(display=True)


class CaseView(NewsView):
    template_name = 'case.html'
    model = models.Cases


class CaseDetailView(BaseView, DetailView):
    template_name = 'case_detail.html'
    model = models.Cases


class ContactView(BaseView, TemplateView):
    template_name = 'contact.html'


class TeamView(BaseView, ListView):
    template_name = 'team.html'
    model = models.Staff
    paginate_by = 8

    def get_queryset(self):
        return super().get_queryset().filter(display=True)
