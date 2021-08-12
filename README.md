# Tournament-django-app
This is Football (soccer) tournament django template
Demo live [click](http://brsfc.herokuapp.com/home/).
## setup on Linux or in any windows (python installed directory or better to use pycharm/vscode project directory)

1. Clone This Project `git clone https://github.com/AhteshamSid/Tournament-django-app.git`
2. Go To Project Directory `cd Tournament-django-app`
3. Create a Virtual Environment `python -m venv venv`
4. Activate Virtual Environment `source venv/bin/activate`
5. Install Requirements Package `pip install -r requirements.txt`
6. Migrate Database `python manage.py migrate`
7. Create Super User `python manage.py createsuperuser`
8. Finally Run The Project `python manage.py runserver`
## Homepage ( without login)
<img src="home.gif" >

## Homepage ( with login)
<img src="home1.gif" >


## Email Verification
**apps/urls.py**

```python
urlpatterns = [
'''...........'''

    path('signup/', signup, name="signup"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
```




**apps/forms.py**

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):  
        class Meta:  
            model = User  
            fields = ('email', 'first_name', 'last_name', 'username')

```


**apps/views.py**

```python

from __future__ import unicode_literals

from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel = get_user_model()
from .forms import SignUpForm

def signup(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            print(current_site)
            mail_subject = 'Activate your account.'
            message = render_to_string('account-active.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            # print(message)
            recipient_list = [user.email, ]
            msg = EmailMessage(mail_subject, message, to=recipient_list)
            msg.send()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
```



**fixtureapp/settings.py**

```python

DEFAULT_FROM_EMAIL = 'workorbit@gmail.com'
DEFAULT_FROM_EMAIL = 'workorbit@gmail.com'
SERVER_EMAIL = 'workorbit@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'workorbit@gmail.com'
EMAIL_HOST_PASSWORD = 'P@ssw0rd5'
```

**templates/account-active.html**

```html
{% autoescape off %}
Hi {{ user.username }},
Please click on the link to confirm your registration,
http://{{ domain }}{% url 'activate' uidb64=uid token=token %}
If you think, it's not you, then just ignore this email.
{% endautoescape %}
```


**templates/signup.html**
form fillup
```html
<h2>Signup</h2>
        <form method="post">
          {% csrf_token %}
          <div class="form-group">
            <label for="first_name">First Name:</label>
            <input type="text" class="form-control" id="first_name" placeholder="Enter first name" name="first_name">
          </div>
          <div class="form-group">
            <label for="last_name">Last Name:</label>
            <input type="text" class="form-control" id="last_name" placeholder="Enter last name" name="last_name">
          </div>
          <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" class="form-control" id="username" placeholder="Enter username" name="username">
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
          </div>
          <div class="form-group">
            <label for="pwd1">Password:</label>
            <input type="password" class="form-control" id="pwd1" placeholder="Enter password" name="password1">
          </div>
          <div class="form-group">
            <label for="pwd2">Confirm Password:</label>
            <input type="password" class="form-control" id="pwd2" placeholder="Reenter password" name="password2">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>

```

