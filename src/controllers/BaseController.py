from helpers.config import get_settings, Settings
import os

class BaseController:
    
    def __init__(self):
        """
        Initialize the BaseController class.
        """
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_dir = os.path.join(
            self.base_dir, "assests/files"
        )
