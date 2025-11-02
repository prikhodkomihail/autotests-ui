from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator

class FileInput(BaseElement):
    def set_input_files(self, files: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(files)