from django.contrib import messages
from django.shortcuts import reverse, render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from cart.models import Order


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactPageView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('pages:contact')
    
    def form_valid(self, form):
        messages.info(self.request, "Thanks for reaching out. We have received your message")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        message_instance = 'Contact form message: "Name:{name}", "Email:{email}", "Message:{message}"'      
        return super(ContactPageView, self).form_valid(form)


def profile_view(request):
    orders = Order.objects.filter(user=request.user, purchased=True)
    context = {
        'orders': orders
    }
    
    return render(request, "user_profile.html", context)