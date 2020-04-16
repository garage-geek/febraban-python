
def clean_data_return_only_number(data):
    return ''.join([n for n in str(data) if n.isdigit()])
