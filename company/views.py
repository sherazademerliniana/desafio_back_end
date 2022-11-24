import csv
from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from rest_framework.parsers import BaseParser


# Create your views here.
class PlainTextParser(BaseParser):
    media_type = "text/plain"
    
    def parse(self, stream, media_type=None , parser_context=None):
        return stream.read()


class CompanyView(APIView):
    parser_classes=[PlainTextParser]

    def post(self, request: Request, format=None) -> Response:
        
        
        minha_dict = request.data.decode("utf-8")
        
        lol = minha_dict.split("\n")
        
        for file in lol:
            print(file)
        return Response()
       