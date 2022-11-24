from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from rest_framework.parsers import BaseParser
from .serializers import CompanySerializer


# Create your views here.
def index(request):
    return render(request, "company/index.html", {})


class PlainTextParser(BaseParser):
    media_type = "text/plain"

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


class CompanyView(APIView):
    parser_classes = [PlainTextParser]

    def post(self, request: Request, format=None) -> Response:

        minha_dict = request.data.decode("utf-8")

        lol = minha_dict.split("\n")

        for file in lol:
            info_dict = {
                "type": file[0:1],
                "date": file[1:9],
                "value": float(file[9:19]) / 100,
                "cpf": file[19:30],
                "credit_card": file[30:42],
                "hour": file[42:48],
                "owner_company": file[48:62],
                "name_company": file[62:80],
            }
            serializer = CompanySerializer(data=info_dict)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)
