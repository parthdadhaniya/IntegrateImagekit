from . import imagekit
import base64


class ImagekitClient:
    def __init__(self, file):
        self.file = self.convert_to_binary(file)
        self.file_name = file.name

    def convert_to_binary(self, file):
        self.binary_file = base64.b64encode(file.read())
        return self.binary_file

    @property
    def upload_media(self):
        result = imagekit.upload_file(
            file=self.file,
            file_name=self.file_name,
        )
        return result.response_metadata.raw
