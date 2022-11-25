from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from .serializers import CompanySerializer
from .parse import PlainTextParser
from .models import Company


# Create your views here.
def index(request):
    return render(request, "company/index.html", {})


class CompanyView(APIView):
    parser_classes = [PlainTextParser]

    def post(self, request: Request, format=None) -> Response:

        archive_txt = request.data.decode("utf-8")

        list_companys = archive_txt.split("\n")

        for file in list_companys:
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

    def get(self, request: Request) -> Response:
        company = Company.objects.all()

        serializer = CompanySerializer(company, many=True)

        return Response(serializer.data)
