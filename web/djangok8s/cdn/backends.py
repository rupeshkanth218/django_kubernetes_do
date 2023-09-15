from storages.backends.s3boto3 import S3Boto3Storage

class StaticRootS3BotoStorage(S3Boto3Storage):
    location = "static"
    default_acl = 'public-read'

class MediaRootS3BotoStorage(S3Boto3Storage):
    location = "media"
    default_acl = 'public-read'
    file_overwrite = False

class CustomS3Boto3Storage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_acl = "private"  # Set the default ACL to 'private'
        self.querystring_auth = True

    def _save(self, name, content):
        if name.startswith("static/ckeditor/"):
            # Make ckeditor/ folder inside static/ public
            self.default_acl = "public-read"
            self.querystring_auth = False
        else:
            self.default_acl = "private"  # Set all other files/folders to private
            self.querystring_auth = True

        return super()._save(name, content)
