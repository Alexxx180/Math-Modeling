import sys
from common.handlers.interaction import pause
from common.handlers.input.specific import setup_input
from common.commander.resources import Resources
from start import dropdown, setup_menu
from menu.table.entry import RandomTableEntryCMD
from menu.model.entry import RandomModelEntryCMD

variant: int
cmd: bool = len(sys.argv) > 1

def variant_check(path: str, count: int):
	start: int = 1
	no: int = (variant - start) % count + start
	if not cmd:
		print(Resources.Texts["Common"]["Variant"].format(path, count, no))
	return Resources.at(f'resources/{path}/{no}.json')

def extract_resources(file, feedback) -> dict:
	resources: dict = {}
	for key, value in file.items():
		resources[key] = feedback(value)
	return resources

def resource(file):
	if isinstance(file, dict):
		return extract_resources(file, resource)
	elif isinstance(file, list):
		return variant_check(file[0], file[1])
	else:
		return Resources.at(f'resources/{file}.json')


def main() -> None:
	manifest: dict = Resources.at('resources/manifest.json')

	for name in ('Texts', 'Fields', 'Hints', 'Enabled', 'Formula', 'Defaults'):
		setattr(Resources, name, resource(manifest[name]))

if __name__ == '__main__':
	p: str = sys.argv[0]
	if ':' in p:
		separator: str = '\\'
		Resources.set_initial(p[:p.rfind(separator)] + separator)

	if len(sys.argv) == 3:
		variant = int(sys.argv[2])
	else:
		p = Resources.InitialDir + 'variant.txt'
		with open(p) as no:
			variant = int(no.readline())

	main()
	if len(sys.argv) > 1:
		if sys.argv[1] == "model":
			print(RandomModelEntryCMD())
		else:
			print(RandomTableEntryCMD())
	else:
		print("Program No {0}, Variants check...\n".format(variant))
		setup_input(Resources.at('resources/texts/queries.json'))
		setup_menu()
		pause()
		dropdown()
