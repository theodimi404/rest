from course.models import Course
from course.serializers import CourseSerializer


class CourseService:
    @staticmethod
    def get_all_courses():
        all_courses = Course.objects.get_all_courses()
        serializer = CourseSerializer(all_courses, many=True)

        return serializer.data

    @staticmethod
    def create_new_course(course_object):
        result = {
            'success': False,
            'response': None
        }
        serializer = CourseSerializer(data=course_object)

        if serializer.is_valid():
            serializer.save()

            result['success'] = True
            result['response'] = serializer.data
            return result
        else:
            result['response'] = serializer.errors
            return result

    @staticmethod
    def get_course_by_id(course_id):
        course = Course.objects.get_course_by_id(course_id)

        if course is not None:
            serializer = CourseSerializer(course)
            return serializer.data
        else:
            return None

    @staticmethod
    def update_course_by_id(course_id, course_object):
        result = {
            'success': False,
            'response': None
        }
        course = Course.objects.get_course_by_id(course_id)

        if course is not None:
            serializer = CourseSerializer(instance=course, data=course_object, partial=True)
            if serializer.is_valid():
                serializer.save()

                result['success'] = True
                result['response'] = serializer.data
                return result
            else:
                result['response'] = serializer.errors
                return result
        else:
            return result

    @staticmethod
    def delete_course_by_id(course_id):
        course = Course.objects.get_course_by_id(course_id)

        if course is not None:
            course.delete()
            return True
        else:
            return False
