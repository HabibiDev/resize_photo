from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class S3FileStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = getattr(settings, 'AWS_MEDIA_BUCKET_NAME')
        super(S3FileStorage, self).__init__(*args, **kwargs)