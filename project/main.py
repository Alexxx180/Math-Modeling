import sys
import os
from common.handlers.interaction import pause
from common.handlers.input.specific import setup_input
from common.commander.resources import Resources
from common.commander.starter.variants import set_variant
from common.commander.starter.api.api import api_cui, api_cmd

if __name__ == '__main__':
	count: int = len(sys.argv)
	path: str = os.path.dirname(os.path.realpath(__file__))
	Resources.set_initial_dir(path)

	if count == 3:
		set_variant(int(sys.argv[2]))
	else:
		set_variant(Resources.get_variant_number())

	if count > 1:
		print(api_cmd(sys.argv[1]))
	else:
		api_cui()
