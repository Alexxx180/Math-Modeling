from json import load
import codecs

class Resources:
    @staticmethod
    def at(path: str) -> dict:
        with codecs.open(path, 'r', 'utf_8_sig') as data:
            result = load(data)
        return result

    # Tables / Plots switch
    Enabled: dict = {}
    Hints: dict = {}

    # Table fields / text labels
    Fields: dict = {}
    Texts: dict = {}

    # User input / defaults
    Formula: dict = {}
    Defaults: dict = {}
    Input: dict = {}
    Queries: dict = {}

    # Menu choices
    Main: dict = {}
    Methods: dict = {}
    Options: dict = {}
