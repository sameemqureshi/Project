from django.shortcuts import render
from django.http import HttpResponse,request,Http404,JsonResponse
from air.models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



def company_detail(request, company_id):
    company = Company.objects.filter(company_id=company_id).first()
    company_data = {
        'company_id': company.company_id,
        'name': company.name,
        'address': company.address,
        'domain': company.Domain,
        'is_active': company.is_active,
    }
    return JsonResponse(company_data)

   

def entity_detail(request, entity_id):
    entity = Company.objects.filter(entity_id=entity_id).first()
    entity_data = {
        'entity_id': entity.entity_id,
        'entity_name': entity.entity_name,
        'is_active': entity.is_active,
        'company':entity.company
    }
    
    return JsonResponse(entity_data)

def all_companies(request):
    companies = Company.objects.all()
    company_list = []
    for company in companies:
        company_data = {
            'company_id': company.company_id,
            'name': company.name,
            'address': company.address,
            'domain': company.Domain,
            'is_active': company.is_active,
        }
        company_list.append(company_data)
    return JsonResponse(company_list, safe=False)

def all_entities(request):
    entities = Entity.objects.all()
    entity_list = []
    for entity in entities:
        entity_data = {
            'entity_id': entity.entity_id,
            'entity_name': entity.entity_name,
            'is_active': entity.is_active,
            'company': {
                'company_id': entity.company.company_id,
                'name': entity.company.name,
                'address': entity.company.address,
                'domain': entity.company.Domain,
                'is_active': entity.company.is_active,
            }
        }
        entity_list.append(entity_data)
    return JsonResponse(entity_list, safe=False)





from rest_framework.views import APIView
from .serializers import *



class EntityApiView(APIView):
    def get(self,request):
        entities=Entity.objects.all().values()
        entitydata=EntityData.objects.all().values()
        
        return Response({"message":"List of Entities","Entities are":entities,"Entity Data is":entitydata})
    def post(self, request):
        try:
            print("Request Data:", request.data)  # Print request data
            entity_id = request.data.get("entity_id")
            if entity_id is None:
                return Response({"error": "entity_id is required"}, status=status.HTTP_400_BAD_REQUEST)
            EntityData.objects.create(
                entity_id=request.data.get("entity_id"),
                physical_quantity=request.data.get("physical_quantity"),
                metric=request.data.get("metric"),
                value=request.data.get("value"),
                ts=request.data.get("ts")
            )
            return Response({"message": "Entity data created successfully"}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({"error": f"Missing required field: {e}"}, status=status.HTTP_400_BAD_REQUEST)

    
    

# @api_view(['POST'])
# def push_entity_data(request):
#     serializer = EntityDataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

