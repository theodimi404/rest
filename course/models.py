from django.db import models


class CourseManager(models.Manager):
    def get_all_courses(self):
        return self.all()

    def get_course_by_id(self, course_id):
        try:
            return self.get(pk=course_id)
        except self.model.DoesNotExist:
            return None


class Course(models.Model):
    PUBLISHED = 'Published'
    PENDING = 'Pending'
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (PENDING, 'Pending')
    )

    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(default=PENDING, choices=STATUS_CHOICES, max_length=120)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CourseManager()

    def __str__(self):
        return self.title
