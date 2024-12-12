from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import SignUpForm
from django.contrib import messages
from gestorProductos.models import Producto

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field in form:
            for error in field.errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

@login_required
def usuariosIndex(request):
    if request.user.is_superuser:
        productos_count = Producto.objects.count()
        return render(request, 'gestorUser/dashboard_admin.html', {
            'productos_count': productos_count
        })
    elif request.user.is_staff:
        return render(request, 'gestorUser/dashboard_staff.html')
    else:
        return render(request, 'gestorUser/dashboard_user.html')
