import base64
import json

def encrypt_payload(payload_dict):
    """
    Simulates encryption of a dictionary payload by encoding as JSON and base64.
    """
    json_str = json.dumps(payload_dict)
    return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

def decrypt_payload(encoded_str):
    """
    Decodes the base64 string back into a dictionary.
    """
    json_bytes = base64.b64decode(encoded_str.encode('utf-8'))
    return json.loads(json_bytes.decode('utf-8'))

