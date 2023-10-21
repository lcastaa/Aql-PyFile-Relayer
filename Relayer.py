from flask import Flask, request, jsonify
import Sender
import os


app = Flask(__name__)

# Define the directory where received files will be saved.
RELAY_DIR = 'relayed_files'

# Created a global variable for the destination IP.
destination_ip = ""

# Create directory for relaying files if it does not exist.
if not os.path.exists(RELAY_DIR):
    os.makedirs(RELAY_DIR)


# Handles incoming POST requests made to /relay
@app.route('/relay', methods=['POST'])
def relay():
    # File comes from the requests file attribute.
    file = request.files.get('file')

    # If there is no file in the request's file attribute
    # return JSON response error.
    if not file:
        return jsonify({'error': 'No file part in the request'})

    # Creates the file name for the file and saves it to the
    # received directory.
    filename = os.path.join(RELAY_DIR, file.filename)
    file.save(filename)

    # Pass it to the sender method to complete the relay
    return Sender.upload_file(filename, destination_ip)


if __name__ == '__main__':
    app.run()
