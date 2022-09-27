from typing import List, Optional
from intialize import NATO_FILES
from typing import Dict
from pathlib import Path

class NatoGenerator:

    def __init__(self):
        self.nato_phonetic = NatoGenerator.extract_nato_dico(NATO_FILES.as_posix())
        pass

    @staticmethod
    def extract_nato_dico(filename: str) -> Dict[str, str]:
        """ Extract the nato dico form file. """
        file = Path(filename).resolve()
        
        raw_content = file.open(mode="r").readlines()
        content = raw_content[1:]

        nato_dico = {
            value.split(",")[0]: value.split(",")[1].strip()
            for value in content}
        return nato_dico

    def convertion(self, word: str) -> List[Optional[str], ]:
        """ Conversion of letter. """
        output = [self.nato_phonetic.get(letter.upper())
                  for letter in list(word)]
        return output
