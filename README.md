# ASCIIArt
An application that converts 2D image files into its corresponding ASCII version (also known as "ASCII Art"). 

# API Documentation
**URL**: POST /ascii/convert  
  
**Description**: Accepts a 2D image file and returns a JSON object with the string representing the corresponding ASCII version. Only .jpg files are supported.
  
**Parameters**: None  
  
**Body**:
| Type | Key | Value |
| --- | --- | --- |
| `form-data` | `file` | The image file |

**Returns**:
| Status Code | Description | Response Data |
| --- | --- | --- |
| `200` | Success | A JSON object with one key, "ascii", whose value is the string representing the ASCII version of the given image file. |
| `400` | Bad Request | Error message is returned if file body is not included, file in body is null or empty, or file type isn't supported. |
| `405` | Method Not Allowed | N/A |
| `500` | Internal Server Error | Error message is returned if the server is unable to process or complete the request. |


# Running the Application
These instructions assume python (and pip) are already installed and added to the system's PATH environment variable. You can download the latest version of python [here](https://www.python.org/downloads/).

1. Clone the project.
2. Navigate to ```location/of/cloned/repo/asciiart``` and run ```pip install -r requirements.txt```
3. From the current location, navigate to ```.../ASCIIArt/ASCIIArt``` and run ```py ASCIIArt.py```. The server should now be running on ```http://localhost:5000```.

# Generating a Sample ASCII Conversion
1. Once the application is running (using the steps above), either cURL or Postman can be used to call the server to convert an image file into ASCII art.

## cURL
1. Download cURL [here](https://everything.curl.dev/get).
2. In a separate command prompt, navigate to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt``` and run ```curl -F file=@Images/mona_lisa.jpg http://localhost:5000/ascii/convert```. This example is using the sample image file ```mona_lisa.jpg``; ```george_washington_large.jpg``` is another sample image file included that can also be used.
3. The JSON response of the cURL request should contain the ACII string version of the image file requested. 

## Postman
1. Download Postman [here](https://www.postman.com/downloads/). 
2. Create a new request window. Select POST and enter ```http://localhost:5000/ascii/convert``` at the top text bar.
3. In the Body tab, select form-data. Click on the dropdown arrow on the right-hand side of the Key column and select "File". Enter "file" in the Key column and select a sample image from the repo's Images directory in the Value column.
4. Hit Send. The response body should be a JSON object containing the ASCII string version of the image file requested. 

# Testing the Application
1. Navigate to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt``` and run ```python -m pytest```
