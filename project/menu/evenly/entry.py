from menu.evenly.interface import RandomEvenlyMethod, RandomEvenlyMethodCMD
from common.flow.entry import AbstractRandomEntry, AbstractRandomEntryCMD

name: str = 'evenly'

def RandomEvenlyEntry() -> None:
	AbstractRandomEntry(RandomEvenlyMethod, name)

def RandomEvenlyEntryCMD() -> str:
	return AbstractRandomEntryCMD(RandomEvenlyMethodCMD, name)
