from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from course.services import CourseService
from course.serializers import CourseSerializer


class CourseListAndCreate(APIView):
    @staticmethod
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "List of all available courses.",
        },
        operation_description="Retrieve a list of all available courses.",
    )
    def get(request):
        all_courses = CourseService.get_all_courses()
        return Response(all_courses, status=status.HTTP_200_OK)

    @staticmethod
    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={
            status.HTTP_201_CREATED: "Course created successfully. Returns the created course details.",
            status.HTTP_400_BAD_REQUEST: "Invalid input. Returns details about the error.",
        },
        operation_description="Create a new course."
    )
    def post(request):
        course_object = request.data
        created_course = CourseService.create_new_course(course_object)

        if created_course['success']:
            return Response(created_course['response'], status=status.HTTP_201_CREATED)
        else:
            return Response(created_course['response'], status=status.HTTP_400_BAD_REQUEST)


class CourseOperationsById(APIView):
    @staticmethod
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Returns the details of the requested course.",
            status.HTTP_404_NOT_FOUND: "If the requested course does not exist. Body contains an error message.",
        },
        operation_description="Retrieve details of a specific course by its ID."
    )
    def get(request, course_id):
        course = CourseService.get_course_by_id(course_id)

        if course is not None:
            return Response(course, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": f"The requested course with id {course_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

    @staticmethod
    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={
            status.HTTP_200_OK: "Course updated successfully. Returns the updated course details.",
            status.HTTP_400_BAD_REQUEST: "Invalid input. Returns details about the error."
        },
        operation_description="Update details of a specific course by its ID."
    )
    def put(request, course_id):
        course_object = request.data
        created_course = CourseService.update_course_by_id(course_id, course_object)

        if created_course['success']:
            return Response(created_course['response'], status=status.HTTP_200_OK)
        else:
            return Response(created_course['response'], status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "Course deleted successfully.",
            status.HTTP_404_NOT_FOUND: "Course not found. Returns an error message.",
        },
        operation_description="Delete a specific course by its ID."
    )
    def delete(request, course_id):
        deleted_course = CourseService.delete_course_by_id(course_id)

        if deleted_course:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"message": f"The requested course with id {course_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
