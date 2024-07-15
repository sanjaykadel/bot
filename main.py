import json
from selenium import webdriver
from fillform import fill_form  
from data import typeconversion 
from flask import Flask, jsonify , request

app = Flask(__name__)

url = "https://smartkyc.sourcecode.com.np/DPForm?type=3in1&appId=bibaabo&appSecret=1ede10a7-5244-4f9e-8e48-ac17dc6cc4b5"

gecko_driver_path = "geckodriver.exe"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)

@app.route('/api', methods=['POST'])
def post_example():
    try:
        data = request.json
        data = typeconversion(data)
        processed_data = fill_form(driver, url, data)
        print("Processed data:", processed_data)  
        
        if 'submissionNo' not in processed_data or not processed_data['submissionNo'] or not processed_data.get('submissionNo'):
          processed_data.pop('submissionNo', None) 
          response = {'status': 'Fail', 'data': processed_data}

        else:
            processed_data.pop('invalid', None)
            response = {'status': 'success', 'data': processed_data}



    except Exception as e:
        print("Error:", e)  
        response = {'status': 'error', 'message': str(e)}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)


