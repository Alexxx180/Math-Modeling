from menu.table.interface import RandomTableReverseMethod, RandomTableReverseMethodCMD
from common.flow.entry import AbstractRandomEntry, AbstractRandomEntryCMD

name: str = 'table'

def RandomTableEntry() -> None:
	AbstractRandomEntry(RandomTableReverseMethod, name)

def RandomTableEntryCMD() -> str:
	return AbstractRandomEntryCMD(RandomTableReverseMethodCMD, name)
