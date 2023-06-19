import pywhatkit as kt
from flask import Flask, request

# Constants
REQUEST_FILE_PART = "file"
ALLOWED_FILE_EXTENSIONS = { "jpg" }

def is_filename_allowed(filename):
    '''
    Determines if a file is allowed for ASCII conversion by checking its filename extension. 

    param filename: Name of the file to check.
    return: True if the file is allowed, False otherwise. If a null or empty filename is provided, False is returned. 
    '''

    if filename is None or filename == "":
        return False;

    filename_split = filename.rsplit(".", 1)
    return len(filename_split) == 2 and filename_split[1] in ALLOWED_FILE_EXTENSIONS

# Initialize the Flask server
ascii_server = Flask(__name__)

# Define the API /ascii/convert
@ascii_server.route('/ascii/convert', methods=['POST'])
def ascii_convert():
    '''
    Converts an image, provided as a file in the request, to its corresponding ASCII version. 

    return: A JSON object with a single key/value pair, where key is "ascii" and value is the converted ASCII string. 
    '''

    if REQUEST_FILE_PART not in request.files:
        return "Could not find file part in request", 400

    image_to_convert = request.files[REQUEST_FILE_PART]

    if image_to_convert is None or image_to_convert.filename == "":
        return "A file path must be included", 400
    if not is_filename_allowed(image_to_convert.filename):
        return f"File extension not allowed. Allowed file extensions: {ALLOWED_FILE_EXTENSIONS}", 400

    try:
        converted_image_string = kt.image_to_ascii_art(image_to_convert)
        return {'ascii': converted_image_string}
    except Exception as err:
        return f"Could not convert image to ASCII art. Error: {err}", 500

if __name__ == "__main__":
    ascii_server.run();
