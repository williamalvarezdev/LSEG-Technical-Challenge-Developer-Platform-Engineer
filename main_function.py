def main_fun(nested_dict, key_path):
    keys = key_path.split('/')
    current = nested_dict
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None 
    
    return current