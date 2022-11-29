from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from .serializers import CompanySerializer
from .parse import PlainTextParser
from .models import Company
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "company/index.html", {})


class CompanyView(APIView):
    parser_classes = [PlainTextParser]

    def post(self, request: Request, format=None) -> Response:

        archive_txt = request.data.decode("utf-8")

        list_companys = archive_txt.split("\n")

        for file in list_companys:
            date = datetime(
                int(file[1:5]),
                int(file[5:7]),
                int(file[7:9]),
                int(file[42:44]),
                int(file[44:46]),
                int(file[46:48]),
            )

            info_dict = {
                "type": file[0:1],
                "date_and_hour": date,
                "value": float(file[9:19]) / 100,
                "cpf": file[19:30],
                "credit_card": file[30:42],
                "owner_company": file[48:62],
                "name_company": file[62:80],
            }

            serializer = CompanySerializer(data=info_dict)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            print(serializer)
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        company = Company.objects.all()

        serializer = CompanySerializer(company, many=True)

        return Response(serializer.data)
