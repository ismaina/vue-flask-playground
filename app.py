import json
from flask import Flask, jsonify, render_template, request

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# definitions
SITE = {
        'logo': 'FLASK-VUE',
        'version': '0.0.1'
}

OWNER = {
        'name': 'Wilber Wanjira',
        'website': 'https://wilber.co.ke'
}

# pass data to the frontend
site_data = {
    'site': SITE,
    'owner': OWNER
}

# landing page
@app.route('/')
def welcome():
  return render_template('index.html', **site_data)


# health check
@app.route('/ping', methods=['GET'])
def health():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
