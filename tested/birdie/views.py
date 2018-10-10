from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'biridie/home.html'


class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kargs):
        # import ipdb; ipdb.set_trace()  # BREAKPOINT
        return super(AdminView, self).dispatch(request, *args, **kargs)
