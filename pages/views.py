from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import reverse, render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from cart.models import CompletedOrder


class HomePageView(TemplateView):
    template_name = "home.html"


class ContactPageView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("pages:contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for reaching out. We have received your message"
        )
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        message_instance = (
            'Contact form message: "Name:{name}", "Email:{email}", "Message:{message}"'
        )
        return super(ContactPageView, self).form_valid(form)


def profile_view(request):
    user = request.user
    users_plans = request.user.usersplans.plans.all()
    profile_name = user.username
    orders = CompletedOrder.objects.filter(order__user=user)
    context = {
        "orders": orders,
        "username": profile_name,
        "users_plans": users_plans,
        }
    return render(request, "user-profile.html", context)
