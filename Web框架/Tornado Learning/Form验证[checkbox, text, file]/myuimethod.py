def display_error_info(self, error_dict, key):
    if error_dict.get(key):
        return error_dict[key]
    else:
        return ''