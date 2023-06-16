from flask import Flask, render_template, request, send_file
import pandas as pd

# import a custom function under the utils folder
from utils.dataTools import rowToTable

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename.endswith('.xlsx'):
        data = pd.read_excel(file, header=None)
        
        # call the custom function
        result = rowToTable(data)

        # Save the result as a new Excel file
        result_file = 'result.xlsx'
        result.to_excel(result_file, index=True)
        return send_file(result_file, as_attachment=True)
    else:
        return "Invalid file format. Please upload an Excel file (.xlsx)."

if __name__ == '__main__':
    app.run(debug=True)
