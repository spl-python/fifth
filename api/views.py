from utils.response import APIResponse
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import ViewSet
from api.models import Student
from api.serializer import StudentModelSerializer

class StudentAPI(GenericAPIView,
                 ListModelMixin,
                 RetrieveModelMixin,
                 CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):

    queryset = Student.objects.all()

    serializer_class =  StudentModelSerializer

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        response = self.create(request,*args,**kwargs)
        return APIResponse(results=response.data)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request,*args,**kwargs)
        return APIResponse(results=response.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request,*args,**kwargs)
        return APIResponse(results=response.data)

class UserView(ViewSet):
    def change_count(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        if book_id:
            book_obj = Student.objects.filter(pk=book_id).first()
            data = StudentModelSerializer(book_obj).data

            return APIResponse({"message": "查询单个成功", "results": data})
        else:
            query_set = Student.objects.all()
            data = StudentModelSerializer(query_set, many=True).data
            return APIResponse({"message": "查询单个成功", "results": data})
    def user_login(self,request,*args,**kwargs):

        return APIResponse(results='成功')