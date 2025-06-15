from menu.table.entry import RandomTableEntryCMD
from menu.model.entry import RandomModelEntryCMD
from menu.evenly.entry import RandomEvenlyEntryCMD
from common.handlers.input.specific import setup_input
from common.handlers.interaction import pause
from common.commander.starter.api.cui import setup_menu, dropdown
from common.commander.starter.variants import main, variant_look, variant_print, variant_showcase

def api_cmd(kind: str) -> str:
	main(variant_look)
	match kind:
		case "model":
			return RandomModelEntryCMD()
		case "evenly":
			return RandomEvenlyEntryCMD()
		case _:
			return RandomTableEntryCMD()

def api_cui() -> None:
	variant_showcase()

	main(variant_print)
	setup_input()
	setup_menu()
	pause()

	dropdown()
