from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = self.get_object()  
            emps = Employee.objects.filter(company=company)

            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})

            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':"company might not exists. Error!",
                'error':str(e)
            }, status = 404)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
