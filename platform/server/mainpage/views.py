import os, subprocess, sys, threading
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, FileResponse
from .models import UploadedFile

ALLOWED_FILE_PROP = ['mp4']

# Script handler
def taskHandler(key):
    print('start task')
    process_path = default_storage.path('main.py')
    subprocess.run(args=[sys.executable, process_path, key])

# Create your views here.
def main(req):
    return render(req, 'index.html', status=200)

def recvFile(req):
    # Receive file
    if req.method == 'POST' and req.FILES.get('file'):
        file = req.FILES.get('file')
        file_prop = file.name.split('.')[-1].lower()
        if file_prop not in ALLOWED_FILE_PROP:
            return HttpResponse(status=415, reason='Unsupported Media type')

    # Save file        
        fileupload = UploadedFile(
            title='sample.mp4',
            file=file
        )
        fileupload.save()
        filekey = fileupload.key()
        print(filekey)

    # Run Script 
        taskHandler(filekey)
        output_path = os.path.join(settings.BASE_DIR, f'{filekey}.srt')
        if os.path.exists(output_path):
            res = FileResponse(open(output_path, 'rb'))
            res['Content-Disposition'] = f'attachment; filename="{filekey}.srt"'
            res['Content-Length'] = os.path.getsize(output_path)
            return res

        return HttpResponse(status=500)
    else:
        return HttpResponse("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|", status=418)