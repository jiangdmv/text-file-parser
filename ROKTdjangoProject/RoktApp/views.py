from django.shortcuts import render
from rest_framework import viewsets
from .models import FileModel
from .serializers import FileSerializer
from django.views import View
from django.http import JsonResponse, HttpResponse
import json
from dateutil import parser


# Upload file API
class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


# POST API, time interval, GET API
class TimeEventView(View):

    def post(self, request):

        datastring = request.body.decode()  # '{}' string format
        data = json.loads(datastring)  # {}  dict format
        filename = data.get('filename')
        timefrom = data.get('from')
        timeto = data.get('to')

        if filename is None or timefrom is None or timeto is None:
            return JsonResponse({'error': 'This information is needed.'}, status=400)

        try:
            parser.parse(timefrom)
        except:
            return JsonResponse({'error': 'This input information should be iso8601 UTC timestamps.'}, status=400)

        try:
            parser.parse(timeto)
        except:
            return JsonResponse({'error': 'This input information should be iso8601 UTC timestamps.'}, status=400)

        try:
            file1 = open('./upload/{}'.format(filename), 'r')
        except (OSError, IOError) as e:
            return JsonResponse({'error': str(e)}, status=404)

        lines = file1.readlines()
        starttime = parser.parse(timefrom)
        endtime = parser.parse(timeto)

        dict = {}
        res = []
        for line in lines:
            linedata = line.split()
            yourtime = parser.parse(linedata[0])

            if starttime <= yourtime <= endtime:
                dict['eventTime'] = linedata[0]
                dict['email'] = linedata[1]
                dict['sessionId'] = linedata[2]

                res.append(dict)
                dict = {}

        if not res:
            return JsonResponse({'error': 'Cannot find the from/to date in the file.'}, status=400)

        res.sort(key=lambda d: d.get('eventTime'))

        jsonfile = json.dumps(res)

        return JsonResponse(jsonfile, safe=False)

    def get(self, request):

        return HttpResponse('Welcome to this site.', content_type='text/plain')
