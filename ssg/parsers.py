from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extensions(self, extension):
        return extension in self.extensions