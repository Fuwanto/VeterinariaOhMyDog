from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        return name
