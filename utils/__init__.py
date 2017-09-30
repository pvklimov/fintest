"""General utilities"""

API_KEYS_DIR = ''
API_KEYS_FILE = 'api_keys.rtf'


def get_api_key(directory=API_KEYS_DIR,
                filename=API_KEYS_FILE,
                source='QUANDL'):
    """Get API key for pulling data.
    
    It is assumed that API keys are stored in directory/filename: 
    
    Assumed file format:

    ***** TEXT START *****
    <source> <API key>
    <source 2> <API key>
    ...
    <source N> <API key>
    <new_line>
    ***** TEXT END *****
    
    Args: 
        directory (str): directory containing api key.
        filename (str): filename containing api key. 
        source (str): api source, e.g. QUANDL. 
    """
    text = open(directory+filename, 'r').read()
    return text.split(source + ' ')[1].split('\\\n')[0]