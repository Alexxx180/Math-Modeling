from menu.model.interface import RandomModelReverseMethod, RandomModelReverseMethodCMD
from common.flow.entry import AbstractRandomEntry, AbstractRandomEntryCMD

name: str = 'continuous'

def RandomModelEntry() -> None:
	AbstractRandomEntry(RandomModelReverseMethod, name)

def RandomModelEntryCMD() -> str:
	return AbstractRandomEntryCMD(RandomModelReverseMethodCMD, name)
