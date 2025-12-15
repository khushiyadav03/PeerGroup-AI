import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'test'

# Mock Data
mock_filename = "test.csv"
mock_columns = ["Math", "Science", "Style"]
mock_clusters = 5
mock_students = 50
mock_preview = [{"Math": 90, "Science": 80, "Style": "Visual"}]

def verify_templates():
    print("Verifying templates...", flush=True)
    with app.test_request_context():
        try:
            print("Checking index.html...", end=" ")
            render_template('index.html')
            print("OK", flush=True)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

        try:
            print("Checking configure.html...", end=" ")
            render_template('configure.html', filename=mock_filename, columns=mock_columns)
            print("OK", flush=True)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

        try:
            print("Checking results.html...", end=" ")
            render_template('results.html', 
                          n_clusters=mock_clusters, 
                          plot_image="mock.png", 
                          output_file="mock.csv", 
                          n_students=mock_students, 
                          preview_cols=mock_columns, 
                          preview_data=mock_preview)
            print("OK", flush=True)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

if __name__ == "__main__":
    verify_templates()
