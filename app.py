from flask import Flask, render_template,request
from werkzeug.utils import secure_filename


# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

import requests
import os
from datetime import datetime

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "C:\\Users\\Vaibhav\\OneDrive\\Desktop\\WHOIS1"
app.secret_key = 'super-secret-key'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/domain', methods =['POST', 'GET'])
def whois():
    if request.method == 'POST':
        
        f = request.files['fname1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    
    f1 = open(f.filename)
    content = f1.read()
    l = content.split(" ")
    final = []
    for i in l:
        complete_api_link = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_ppZZaH1leBYYW3LC4U7eVUh8WLxYi&domainName="+i+"&outputFormat=JSON"
    
        api_link = requests.get(complete_api_link)
        api_data = api_link.json
        final.append(api_data)

    return render_template("next.html",len = len(final),l=l,final = final)
    

if __name__ == '__main__':

    app.run(debug=True)
