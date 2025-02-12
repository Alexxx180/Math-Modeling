import matplotlib
from common.handlers.interaction import pause
from common.handlers.input.specific import setup_input
from common.commander.resources import Resources
from start import dropdown, setup_menu

variant: int

def variant_check(path: str, count: int):
	start: int = 1
	no: int = (variant - start) % count + start
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
	matplotlib.use('TkAgg')

	with open('variant.txt') as no:
		variant = int(no.readline())

	print("Program No {0}, Variants check...\n".format(variant))
	main()
	setup_input(Resources.at('resources/texts/queries.json'))
	setup_menu()
	pause()
	dropdown()
