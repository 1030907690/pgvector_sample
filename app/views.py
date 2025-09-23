from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Item
from app.serializers import ItemSerializer
from sentence_transformers import SentenceTransformer, util
from PIL import Image
from pgvector.django import L2Distance

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vector(request):
    model = SentenceTransformer('clip-ViT-B-32')
    # Encode an image:
    img_emb = model.encode(Image.open('C:/Users/Administrator/Pictures/sc.png'))
    print(len(img_emb.tolist()))
    print(img_emb.tolist())
    if request.method == 'GET':
        result = Item.objects.order_by(L2Distance('embedding', img_emb.tolist()))[:5]
        serializer = ItemSerializer(result, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        item = Item(embedding=img_emb.tolist())
        item.save()
        return Response({'message': f'Hello, world! {item.id}'})
    return Response({'message': 'Hello, world!'})

