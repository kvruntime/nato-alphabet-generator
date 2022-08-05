from pathlib import Path
from typing import Dict, List



def extract_nato_dico(filename: Path | str) -> Dict[str, str]:
    """ Extract the nato dico form file. """

    with open(filename, mode="r") as rfile:
        raw_content = rfile.readlines()

    content = raw_content[1:]
    nato_dico = {value.split(",")[0]: value.split(
        ",")[1].strip() for value in content}
    return nato_dico