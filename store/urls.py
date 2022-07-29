from django.urls import include, path
from store import views
from  django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(),name='product-detail'),
    path('mobile/', views.mobile, name='mobile'),
    path('profile/', views.profile, name='profile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistraion"),
    path('accounts/login', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
