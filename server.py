import http.server
import socketserver
import joblib
import numpy as np
from PIL import Image
import io
import json

PORT = 8000
MODEL_PATH = "brain_tumor_rf_model.pkl"
IMG_SIZE = 100

# Load model
try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)
    exit(1)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/predict":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            try:
                start = body.find(b'\r\n\r\n') + 4
                end = body.rfind(b'\r\n------')
                file_bytes = body[start:end]
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error reading file: {e}".encode())
                return

            try:
                img = Image.open(io.BytesIO(file_bytes)).convert('L')
                img = img.resize((IMG_SIZE, IMG_SIZE))
                X = np.array(img).flatten().reshape(1, -1)
                pred = model.predict(X)[0]
                proba = model.predict_proba(X)[0][1]
                label = 'Tumor' if pred == 1 else 'No Tumor'
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error processing image: {e}".encode())
                return

            # Respond with JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {'prediction': label, 'probability': round(proba, 4)}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}/www/index.html")
    httpd.serve_forever()
