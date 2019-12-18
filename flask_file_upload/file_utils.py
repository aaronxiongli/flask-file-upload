"""
    Helper class
"""
import os

from ._config import Config


class FileUtils:

    table_name: str

    model = None

    config: Config

    id: int

    def __init__(self, model, config: Config, **kwargs):
        self.config = config
        self.model = model
        self.id = kwargs.get("id") or "id"
        self.table_name = kwargs.get("table_name")

    def allowed_file(self, filename):
        return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in self.config.allowed_extensions

    def get_file_root_path(self):
        return os.path.join(self.config.upload_folder)

    def postfix_file_path(self, id: int, filename: str):
        return f"/{self.table_name}/{id}/{filename}"

    def get_file_path(self, id: int, filename: str, file_type: str):
        return os.path.join(f"{self.config.upload_folder}{self.postfix_file_path(id, filename)}.{file_type}")

    def save_file(self, file, id: int, file_type: str):
        file.save(self.get_file_path(id, file.filename, file_type))
