from common.commander.starter.resources import resource_file, resource
from common.commander.resources import Resources

variant: int = 1

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

def _determine_variant(variants: dict, path: str, count: int, start: int = 1) -> int:
	global variant
	no: int = get_variant(variant, count, start)
	return _correct_variant(variants, no) if variants[path] else no + start

def variant_cmd(variants: dict, path: str, count: int) -> dict:
	no: int = _determine_variant(variants, path, count)
	return resource_file(f'{path}/{no}')

def variant_cui(variants: dict, path: str, count: int) -> dict:
	no: int = _determine_variant(variants, path, count)
	print(Resources.Texts["Common"]["Variant"].format(path, count, no))
	return resource_file(f'{path}/{no}')

def main(variant_check) -> None:
	manifest: dict = resource_file('manifest')
	variants: dict = resource_file(manifest["Variants"])
	check = lambda path, count: variant_check(variants, path, count)
	for name in ('Texts', 'Fields', 'Hints', 'Enabled', 'Formula', 'Defaults'):
		setattr(Resources, name, resource(manifest[name], check))
