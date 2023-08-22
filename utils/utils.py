
import re


def get_id_from_email (email):

    pattern = r'\d+'  # Matches one or more digits

    matches = re.findall(pattern, email)
    if matches:
        extracted_number = matches[0]
        return str(extracted_number)
    else:
        return None
    
