from abc import ABC, abstractmethod
from files.base_file import BaseFile


class TextFile(BaseFile):
    def extract_data(self):
        return ''