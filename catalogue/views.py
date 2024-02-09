from django.shortcuts import render
from . models import Catalogue, MasterCatalogue, Categories
from . serializers import CatalogueSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Categories
# Create your views here.


# to get catalogue of logged in user
class GetCatalogues(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_catalogues = Catalogue.objects.filter(seller=request.user)
        data = []

        for catalogue in all_catalogues:
            if catalogue.mapped_to_master:
                category = catalogue.category
                corresponding_master_catalogue = MasterCatalogue.objects.filter(category=category).first()

                if corresponding_master_catalogue:
                    # Use master catalogue images
                    catalogue.product_image_1 = corresponding_master_catalogue.product_image_1
                    catalogue.product_image_2 = corresponding_master_catalogue.product_image_2
                    catalogue.product_image_3 = corresponding_master_catalogue.product_image_3
                    catalogue.product_image_4 = corresponding_master_catalogue.product_image_4
                    catalogue.product_image_5 = corresponding_master_catalogue.product_image_5

            serializer = CatalogueSerializer(catalogue)
            data.append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)
    
class CreateCatalogue(APIView):
    
    def post(self, request): 
        try:
            # Extract image files from request.FILES
            image_files = [request.FILES.get(f'product_image_{i+1}') for i in range(5)]

            # Create a Categories instance or get an existing one
            category_instance, _ = Categories.objects.get_or_create(category=request.data.get('category'))

            # Create a Catalogue instance with image files
            catalogue_instance = Catalogue.objects.create(
                product_name=request.data.get('product_name'),
                mrp=request.data.get('mrp'),
                seller=request.user,
                selling_prize=request.data.get('selling_prize'),
                buying_prize=request.data.get('buying_prize'),
                hsn_code=request.data.get('hsn_code'),
                gst_percentage=request.data.get('gst_percentage'),
                unit=request.data.get('unit'),
                quantity=request.data.get('quantity'),
                standardized=request.data.get('standardized'),
                category=category_instance,
                mapped_to_master=request.data.get('mapped_to_master'),
                product_image_1=image_files[0],
                product_image_2=image_files[1],
                product_image_3=image_files[2],
                product_image_4=image_files[3],
                product_image_5=image_files[4],
            )

            return Response({'message': 'Catalogue Saved Successfully'}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
                
# to get all catalogues even without logging in    
class GetAllCatalogues(APIView):
    def get(self, request):
        all_catalogues = Catalogue.objects.all()
        data = []

        for catalogue in all_catalogues:
            if catalogue.mapped_to_master:
                category = catalogue.category
                corresponding_master_catalogue = MasterCatalogue.objects.filter(category=category).first()

                if corresponding_master_catalogue:
                    # Use master catalogue images
                    catalogue.product_image_1 = corresponding_master_catalogue.product_image_1
                    catalogue.product_image_2 = corresponding_master_catalogue.product_image_2
                    catalogue.product_image_3 = corresponding_master_catalogue.product_image_3
                    catalogue.product_image_4 = corresponding_master_catalogue.product_image_4
                    catalogue.product_image_5 = corresponding_master_catalogue.product_image_5

            serializer = CatalogueSerializer(catalogue)
            data.append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)
        
def get_all_categories(request):
    categories = Categories.objects.all().values_list('category', flat=True)
    return JsonResponse({'categories': list(categories)})


class GetCataloguesByCategory(APIView):
    
    def get(self, request, category):
        
        all_catalogues = Catalogue.objects.filter(category=category)
        data = []

        for catalogue in all_catalogues:
            if catalogue.mapped_to_master:
                category = catalogue.category
                corresponding_master_catalogue = MasterCatalogue.objects.filter(category=category).first()

                if corresponding_master_catalogue:
                    # Use master catalogue images
                    catalogue.product_image_1 = corresponding_master_catalogue.product_image_1
                    catalogue.product_image_2 = corresponding_master_catalogue.product_image_2
                    catalogue.product_image_3 = corresponding_master_catalogue.product_image_3
                    catalogue.product_image_4 = corresponding_master_catalogue.product_image_4
                    catalogue.product_image_5 = corresponding_master_catalogue.product_image_5

            serializer = CatalogueSerializer(catalogue)
            data.append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)
    
    
class GetAllCataloguesByCategory(APIView):
    
    def get(self, request):
        all_categories = Categories.objects.all()
        result_data = {}

        for category in all_categories:
            category_name = category.category
            catalogues = Catalogue.objects.filter(category=category)

            # If mapped to master, use master catalogue images
            for catalogue in catalogues:
                if catalogue.mapped_to_master:
                    corresponding_master_catalogue = MasterCatalogue.objects.filter(category=category).first()
                    if corresponding_master_catalogue:
                        # Update the catalogue images with master catalogue images
                        catalogue.product_image_1 = corresponding_master_catalogue.product_image_1
                        catalogue.product_image_2 = corresponding_master_catalogue.product_image_2
                        catalogue.product_image_3 = corresponding_master_catalogue.product_image_3
                        catalogue.product_image_4 = corresponding_master_catalogue.product_image_4
                        catalogue.product_image_5 = corresponding_master_catalogue.product_image_5

            # Serialize the catalogues for the current category
            catalogue_serializer = CatalogueSerializer(catalogues, many=True)
            result_data[category_name] = catalogue_serializer.data

        return Response(result_data, status=status.HTTP_200_OK)
    
    
    
def trial(request):
    return render(request, 'catalogue.html')