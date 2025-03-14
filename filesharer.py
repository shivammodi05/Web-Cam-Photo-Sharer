from filestack import Client

class FileSharer:

    def __init__(self, filePath, api_key="Ab96owt4FS5yAFooS5lRCz"):
        self.filePath = filePath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file = client.upload(filepath=self.filePath)
        return new_file.url
