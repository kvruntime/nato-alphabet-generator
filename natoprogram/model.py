
from typing import List, Optional
from natoprogram import NATO_RESSOURCE
from natoprogram.helper import extract_nato_dico


NATO_DICT = extract_nato_dico(NATO_RESSOURCE)

class ModelNato:
    
    def __init__(self):
        pass
    
    def convertion(self, word:str) -> List[str,]:
        """ Conversion of letter. """
        output = [NATO_DICT.get(letter.upper()) for letter in list(word)]
        return output #type:ignore