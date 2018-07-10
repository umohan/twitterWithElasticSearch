from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import API
# Create your views here.
class TwitterCount(APIView):
    def post(self, request, format=None):
        print request
        returnData = API.getNoOfData(self, request.data, format=None)
        if returnData == "Bad_Request":
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class addData(APIView):
    def post(self, request, format=None):
        print request
        returnData = API.addTweet(self, request.data, format=None)
        if returnData == "Bad_Request":
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class searchData(APIView):
    def post(self,request,format=None):
        print request
        returnData=API.searchText(self,request.data,format=None)
        if returnData == "Bad_Request":
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)
