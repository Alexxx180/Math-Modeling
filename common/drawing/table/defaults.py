from prettytable import PrettyTable

def TableDefaults(title: str, align: dict) -> PrettyTable:
    table = PrettyTable()
    table.align = align['Right']
    table.title = title
    table.float_format = '.8'
    return table
