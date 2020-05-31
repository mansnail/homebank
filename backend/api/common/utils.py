import uuid
from os.path import splitext


def file_upload_path(prefix, filename):
    __, ext = splitext(filename)
    return '{}/{}'.format(prefix, "{}{}".format(uuid.uuid4(), ext))
