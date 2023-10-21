from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the directory where received files will be saved.
RECEIVER_DIR = 'received_files'


# Create directory for relaying files if it does not exist.
if not os.path.exists(RECEIVER_DIR):
    os.makedirs(RECEIVER_DIR)


# Handles incoming POST requests made to /receive
@app.route('/receive', methods=['POST'])
def receive():
    # File comes from the requests file attribute.
    file = request.files.get('file')

    # If there is no file in the request's file attribute
    # return JSON response error.
    if not file:
        return jsonify({'error': 'No file part in the request'})

    # Creates the file name for the file and saves it to the
    # received directory.
    filename = os.path.join(RECEIVER_DIR, file.filename)
    file.save(filename)

    return jsonify({"MSG": "FILE SAVED IN RECEIVER DIR"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
