from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseStatus

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024
        
        def validate_uploaded_file(self, file:  UploadFile):
      
            # Implement your validation logic here
            if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
                return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value 

            if file.size > self.app_settings.MAX_FILE_SIZE * size_scale:
                return False, ResponseStatus.FILE_SIZE_EXCEEDED.value
            
            return True, ResponseStatus.FILE_VALIDATED_SUCCESS.value