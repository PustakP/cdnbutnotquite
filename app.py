from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/BrandingBold.woff')
def serve_font():
    return send_from_directory('./', 'BrandingBold.woff')


@app.route('/BrandingBold.woff2')
def serve_font():
    return send_from_directory('./', 'BrandingBold.woff2')

if __name__ == '__main__':
    app.run(debug=True)
