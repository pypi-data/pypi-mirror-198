"""Django urlpatterns declaration for blackdark_nautobot_secrets_providers plugin."""
from django.urls import path

from blackdark_nautobot_secrets_providers import views


app_name = "blackdark_nautobot_secrets_providers"

urlpatterns = [
    path("", views.SecretsProvidersHomeView.as_view(), name="home"),
]
