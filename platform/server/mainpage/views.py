import os, subprocess, sys
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import UploadedFile

ALLOWED_FILE_PROP = ['mp4', 'm4a']

# Create your views here.
def main(req):
    return render(req, 'index.html', status=200)

def recvFile(req):
    # Receive file
    if req.method == 'POST' and req.FILES['file']:
        file = req.FILES['file']
        file_prop = file.name.split('.')[-1].lower()
        if file_prop not in ALLOWED_FILE_PROP:
            return HttpResponse(status=415, reason='Unsupported Media type')
        # uploaded_file = UploadedFile.objects.create(file=file)

    # Save file        
        file_path = os.path.join(settings.BASE_DIR, '../../test/sample.mp4')
        with open(file.path, 'wb') as dest:
            for chunk in file.chunk():
                dest.wriet(chunk)

    # Run Script
        process_path = os.path.join(settings.BASE_DIR, '../../test/main.py')
        subprocess.run(args=[sys.executable, process_path])

        return HttpResponse("", status=200)
    else:
        return HttpResponse(status=415, reason='Unsupported Media type')