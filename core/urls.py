from ninja import NinjaAPI
from django.urls import path
from django.contrib import admin
from users.api import router as auth_router
from common.api import router as common_router
from ninja_jwt.authentication import JWTAuth


# --- API SETUP ---
api = NinjaAPI(
    title="Ninja API",
    version="1.0.0",
    description="API built with Django Ninja.",
    urls_namespace="api",
    auth=JWTAuth(),
    docs_url="/",
)

# --- API ROUTES ---
api.add_router("/auth/", auth_router)
api.add_router("/common/", common_router)

# --- URLS ---
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
