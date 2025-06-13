from json import load
import codecs

class Resources:
	@staticmethod
	def at(path: str) -> dict:
		path = Resources.InitialDir + path
		with codecs.open(path, 'r', 'utf_8_sig') as data:
			result = load(data)
		return result

	@staticmethod
	def set_initial(path: str) -> None:
		Resources.InitialDir = path

	InitialDir: str = ""
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
