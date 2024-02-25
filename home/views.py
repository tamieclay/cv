from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.shortcuts import render, redirect
from .models import CV,CustomUser
from django.contrib import messages  # Import messages framework
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import CV
from django.views.generic import ListView
from .forms import CVCreationForm
from .models import CV
from django.views import View
from django.contrib.auth import logout
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.contrib import messages
from .forms import CVCreationForm
from .models import CV
from .forms import LoginForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser
from django.http import HttpResponse


from .models import CV  # Make sure to import the CV model at the top of your file

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, CustomUserForm
from django.views.generic import DetailView
from .models import CV, PageView
from ip2geotools.databases.noncommercial import DbIpCity

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserForm
from .models import CustomUser

class CustomUserView(View):
    def get(self, request):
        form = CustomUserForm()
        cvs = CV.objects.all()  # fetch all CVs from the database
        return render(request, 'dashboard/dashboard_home.html', {'form': form, 'cvs': cvs})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                phone_number=form.cleaned_data.get('phone_number'),
                address=form.cleaned_data.get('address'),
            )
            return redirect('signup')
        else:
            print(form.errors)  # print form errors
            return render(request, 'dashboard/dashboard_home.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('signup')
                else:
                    return redirect('cv_create')
            else:
                form.add_error(None, 'Invalid credentials')
        return render(request, 'auth/login.html', {'form': form})



class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

    def get(self, request):
        return self.post(request)





class CVCreateView(CreateView):
    model = CV
    form_class = CVCreationForm
    template_name = 'dashboard/dashboard_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cvs'] = CV.objects.filter(user=self.request.user)  # Only get CVs of the current user
        context['num_cvs'] = CV.objects.count()  # Get the total number of CVs
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user  # Set the user of the CV
            try:
                return super().form_valid(form)
            except Exception as e:
                # Handle unexpected errors
                print(f"Error creating CV: {e}")
                messages.error(self.request, 'An error occurred while creating the CV.')
                return self.form_invalid(form)
        else:
            # Forms are not always valid even if data is saved to the database
            # Handle form errors and display them to the user
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.pk})




class CVDetailView(DetailView):
    model = CV
    template_name = 'dashboard/cv_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cv'] = self.object
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        ip = request.META.get('REMOTE_ADDR')
        location = DbIpCity.get(ip, api_key='free')

        PageView.objects.create(
            page=request.path,
            user=request.user if request.user.is_authenticated else None,
            ip_address=ip,
            location=f'{location.city}, {location.region}, {location.country}'
        )

        return response


