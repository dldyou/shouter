import os
from uuid import uuid4

def renameToKey(instance, filename):
    ext = filename.split('.')[-1]
    uuid = uuid4().hex

    filename = f'{uuid}.{ext}'
    
    return filename