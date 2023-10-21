import requests


def upload_file(file_to_send, host_ip):

    # Stores the binary data of the file opened and puts it in a
    # JSON or Dictionary with the name of 'files'
    files = {'file': open(file_to_send, 'rb')}

    # Send the file as part of a POST request to the receivers address
    response = requests.post(host_ip, files=files)

    # Check the response from the server
    if response.status_code == 200:
        return {"MSG": "File sent PASSED"}
    else:
        return {"MSG": "File sent FAILED"}
