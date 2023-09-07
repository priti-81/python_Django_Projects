from django.urls import path
from Homeonline import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('bloggrid/',views.bloggrid,name='blog'),
   path('buy/<int:id>',views.buy,name='buy'),
   path('sell_rent/',views.sell_rent, name='sell_rent'),
   path('update/',views.updatedata,name='updateprofile'),
   path('contact/',views.contact,name='contact'),
   path('signup/',views.signupview.as_view(),name='signup'),
   path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
   path('logout/',auth_views.LogoutView.as_view(next_page='index'),name='logout'),
   path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='password.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
   path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
   path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
   path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
   path('propertygrid',views.propertygrid,name='property')
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
