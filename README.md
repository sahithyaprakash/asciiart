# ASCIIArt
A service that converts 2D image files into its corresponding ASCII version (also known as "ASCII Art"). 

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


# Running the Service
These instructions assume python (and pip) are already installed and added to the system's PATH environment variable. You can download the latest version of python [here](https://www.python.org/downloads/).

1. Clone the project.
2. Navigate to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt```.
3. Run ```py -m venv env``` to create a virtual environment env.
4. Run ```env\Scripts\activate``` (for Windows). You should now see (env) prepended to the shell prompt. 
5. Navigate two directies up to ```location/of/cloned/repo/asciiart``` and run ```pip install -r requirements.txt```. 
7. Navigate back to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt``` and run ```py ASCIIArt.py```. The server should now be running on ```http://localhost:5000```. 

# Generating a Sample ASCII Conversion
1. Once the service is running (using the steps above), either cURL or Postman can be used to call the server to convert an image file into ASCII art.

## cURL
1. Download cURL [here](https://everything.curl.dev/get).
2. In a separate command prompt, navigate to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt``` and run ```curl -F file=@Images/mona_lisa.jpg http://localhost:5000/ascii/convert```. This example is using the sample image file ```mona_lisa.jpg``; ```george_washington_large.jpg``` is another sample image file included that can also be used.
3. The JSON response of the cURL request should contain the ACII string version of the image file requested. 

## Postman
1. Download Postman [here](https://www.postman.com/downloads/). 
2. Create a new request window. Select POST and enter ```http://localhost:5000/ascii/convert``` at the top text bar.
3. In the Body tab, select form-data. Click on the dropdown arrow on the right-hand side of the Key column and select "File". Enter "file" in the Key column and select a sample image from the repo's Images directory in the Value column.
4. Hit Send. The response body should be a JSON object containing the ASCII string version of the image file requested. 

# Testing the Service
1. Navigate to ```location/of/cloned/repo/asciiart/ASCIIArt/ASCIIArt``` and run ```python -m pytest```

# Service Assumptions and Limitations
## Assumptions
1. The service's main functionality is to convert images it receives into ASCII art, so storing information in a database isn't necessary. Based on this assumption, a non-full stack web service framework like Django wasn't chosen. NOTE: We may want to increase performance in the future by adding caching or to expand functionality so that a user can retrieve all images they've requested. These additions will require a database layer.
2. Since we want to resize images to improve performance, a third party library should be picked appropriately.
3. There is not much business logic in the app to create unit tests for (except for the is_filename_allowed helper method), so I focused on integration testing and coupled the is_filanem_allowed logic in those tests.

## Limitations
1. **Pywhatkit is deprecated and another library should be used.**
2. Pywhatkit creates an extra text file upon output, which is unncessary for the service to run.
3. The service right now only accepts .jpg file extensions, but that can easily be changed.
4. The API path does not follow standard API convention (e.g. ideally we would want some sort of resource hirearchy)
5. Additonal work is required to run the service on production WSGI servers (better authentication, security)
6. Flask cannot handle multiple requests at a time by defualt. Migration/re-work to a new framework may be needed to handle increased load and scale without compromising developer maintenance time. 

# Libraries
## Flask
1. **Why was it chosen?** Flask was chosen due to its simplicity in spinning up a service. I assumed the service wouldn't need to store any information/a database layer, hence I chose a non-full-stack web service framework (I didn't want to pick a framework that was "overkill"). The service seemed to resemble a highly-specialized microservice, which Flask is well suited for (and I wanted to go the route of microservices architecture vs. a monolithic approach). Flask offers flexibility, e.g. if future functionality and design are still unknown, Flask makes it easy to add supplemental technologies/frameworks in the future.
2. **Limitations** Flask is not as stable and secure as other out-of-the-box full-stack frameworks like Django. It is also not as well-equipped to handle increased load and scale as other, more mature frameworks. A lot of fundamental things don't come for free in Flask, like security in production, and require developer work to add and maintain. All of these reasons add to the high maintenance cost of Flask, especially when the service has to grow. Also, Flask can only handle one request at a time by default; the service can be horizontally scaled, but it's not a scalable solution. Implementation in Flask may require migration/re-work in the future to account for increased scale. Finally, frameworks like Django have larger community support, increasing the likelihood of better documentation, faster bug fixes, and more features. 
3. **Maturity Level** Mature. Widely supported and popular, but not as much community support as frameworks like Django. 
4. **Testing** Works with the pytest framework. Also has its own Flask-Testing library. 
5. **Performance Considerations** Compared to bigger frameworks like Django, Flask is faster due to fewer abstraction layers. Since the service is highly specialized, running in Flask can help speed up performance. A dedicated WSGI server like Gunicorn is needed to host the service in production. 

## Pywhatkit
1. **Why was it chosen?** Of the libraries available, pywhatkit has the higher number of contributors and usage. It has over 30 contributors and has been used by over 3000 users. The library was also chosen due to its simplicity in integration and use. Also, pywahtkit automatically resizes large images, satisfying one of the service's requirement out-of-the-box and speeding up performance for large images. 
2. **Limitations** I recently discovered that this library is **deprecated** and should not be integrated with any further. With more development time, I would prioritize switching over to a different library that is being actively maintained. 
3. **Maturity Level** Production/Stable development status. 
