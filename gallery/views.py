from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PaintLastSerializer, PaintFilterSerializer
from .models import Paint


class PaintLastAPIView(APIView):
    serializer_class = PaintLastSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        cant = serializer.validated_data['cant']

        paints = Paint.objects.all().order_by('-date_created')[:cant]

        paint_object = []

        for i in paints:
            paint_object.append({
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'description': i.description,
                'autor': i.author,
                'img': i.img.url,
                'is_recommended': i.is_recommended,
                'size_paint': i.size_paint,
                'tecnical': i.tecnical
            })

        return Response({'data': paint_object}, status=status.HTTP_200_OK)


class PaintRecommendedAPIView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        paints_recommended = Paint.objects.filter(
            is_recommended=True).order_by('-date_created')

        paint_recommended_object = []

        for i in paints_recommended:
            paint_recommended_object.append({
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'description': i.description,
                'autor': i.author,
                'img': i.img.url,
                'is_recommended': i.is_recommended,
                'size_paint': i.size_paint,
                'tecnical': i.tecnical
            })

        return Response({'data': paint_recommended_object}, status=status.HTTP_200_OK)


class PaintFilterAPIView(APIView):
    serializer_class = PaintFilterSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        search = serializer.validated_data['search']
        filter = serializer.validated_data['filter']

        paints = []

        if filter.lower() == 'todo':
            paints = Paint.objects.filter(
                name__contains=search, author__icontains=search, price__contains=search, tecnical__contains=search)
        elif filter.lower() == 'artista':
            paints = Paint.objects.filter(author__icontains=search)
        elif filter.lower() == 'precio':
            paints = Paint.objects.filter(price__icontains=search)
        elif filter.lower() == 'estilo':
            paints = Paint.objects.filter(tecnical__icontains=search)

        paint_object = []

        for i in paints:
            paint_object.append({
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'description': i.description,
                'autor': i.author,
                'img': i.img.url,
                'is_recommended': i.is_recommended,
                'size_paint': i.size_paint,
                'tecnical': i.tecnical
            })

        return Response({'data': paint_object}, status=status.HTTP_200_OK)
