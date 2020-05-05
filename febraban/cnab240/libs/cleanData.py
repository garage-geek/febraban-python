
def clean_data_return_only_number(data):
    return ''.join([n for n in str(data) if n.isdigit()])


def clean_data_return_only_alphanumeric(data):
    return ''.join(filter(str.isalnum, data))
