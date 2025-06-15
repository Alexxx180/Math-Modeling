from common.commander.resources import Resources

def extract_resources(file: dict, feedback) -> dict:
	resources: dict = {}
	for key, value in file.items():
		resources[key] = feedback(value)
	return resources

def resource_file(file: str):
	return Resources.at(f'resources/{file}.json')

def resource(file, check):
	if isinstance(file, dict):
		return extract_resources(file, lambda file: resource(file, check))
	elif isinstance(file, list):
		return check(file[0])
	else:
		return resource_file(file)
