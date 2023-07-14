from django.urls import path
from goals import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("main_goal_input/", views.main_goal_input, name="main_goal_input"),
    path("sub_goal_input/<int:plan_id>/", views.sub_goal_input, name="sub_goal_input"),
    path("goal_edit/<int:plan_id>/", views.goal_edit, name="goal_edit"),
    path("3x3_table/<int:plan_id>/", views.three_by_three_table, name="3x3_table"),
    path(
        "way_goal_input/<int:plan_id>/<int:sub_goal_id>/",
        views.way_goal_input,
        name="way_goal_input",
    ),
    path("3x3_table/<int:plan_id>/comment/", views.comment, name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
