from django.urls import path

from course.views import CourseListAndCreate, CourseOperationsById

urlpatterns = [
    path('', CourseListAndCreate.as_view(), name='course-list-and-create'),
    path('<int:course_id>', CourseOperationsById.as_view(), name='course-operations-by-id'),
]
