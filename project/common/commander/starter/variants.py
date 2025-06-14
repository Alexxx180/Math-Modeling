from common.commander.starter.resources import resource_file, resource
from common.commander.resources import Resources

variant: int = 0

def variant_showcase() -> None:
	global variant
	print("Program No {0}, Variants check...\n".format(variant))

def set_variant(no: int) -> None:
	global variant
	variant = no

def get_variant(no: int, count: int, start: int = 0) -> int:
	return (no - start) % count

def _correct_variant(variants: dict, no: int) -> int:
	values: list = variants["Numbers"]
	count: int = len(values)
	return values[get_variant(no, count)]

def variant_look(variants: dict, path: str, count: int, start: int = 1) -> int:
	global variant
	no: int = get_variant(variant, count, start)
	return _correct_variant(variants, no) if variants[path] else no + start

def variant_print(variants: dict, path: str, count: int) -> int:
	no: int = variant_look(variants, path, count)
	print(Resources.Texts["Common"]["Variant"].format(path, count, no))
	return no

def check_variant(variants: dict, path: str, check) -> dict:
	file: dict = resource_file(path)
	count: int = len(file) - 1
	no: int = check(variants, path, count)
	return file[str(no)] # json supports only str

def main(behavior) -> None:
	manifest: dict = resource_file('manifest')
	variants: dict = resource_file(manifest["Variants"])
	check = lambda path: check_variant(variants, path, behavior)
	for name in ('Texts', 'Fields', 'Hints', 'Enabled', 'Formula', 'Defaults'):
		setattr(Resources, name, resource(manifest[name], check))
