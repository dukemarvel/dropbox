from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Set up a route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
  # Get the file from the request
  file = request.files['file']

  # Save the file to the server
  file.save(os.path.join('/path/to/server/files', file.filename))

  # Return a success message
  return jsonify({'message': 'File uploaded successfully'})

# Set up a route to handle file downloads
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
  # Check if the file exists
  if not os.path.exists(os.path.join('/path/to/server/files', filename)):
    return jsonify({'message': 'File not found'}), 404

  # Read the file and send it back to the client
  with open(os.path.join('/path/to/server/files', filename), 'rb') as f:
    file_data = f.read()
  return file_data

# Run the app
if __name__ == '__main__':
  app.run()
