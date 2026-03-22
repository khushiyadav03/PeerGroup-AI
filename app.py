from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SECRET_KEY'] = 'dev_key'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Read CSV to get columns
        df = pd.read_csv(filepath)
        columns = df.columns.tolist()
        
        return render_template('configure.html', filename=filename, columns=columns)

@app.route('/use-synthetic')
def use_synthetic():
    from data.data_generator import generate_student_data
    df = generate_student_data(50)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'synthetic_students.csv')
    df.to_csv(filepath, index=False)
    
    columns = df.columns.tolist()
    return render_template('configure.html', filename='synthetic_students.csv', columns=columns)

@app.route('/cluster', methods=['POST'])
def cluster_data():
    filename = request.form.get('filename')
    num_features = request.form.getlist('numerical_features')
    cat_features = request.form.getlist('categorical_features')
    n_clusters = int(request.form.get('n_clusters', 5))
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)
    
    # Run Pipeline
    from src.preprocessing import preprocess_data
    from src.clustering import perform_kmeans
    from src.visualization import plot_clusters
    
    # Preprocess
    X, _ = preprocess_data(df, num_features, cat_features)
    
    # Cluster
    labels = perform_kmeans(X, n_clusters)
    df['Cluster_Label'] = labels
    
    # Save Result CSV
    output_filename = f"clustered_{filename}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    df.to_csv(output_path, index=False)
    
    # Visualize
    plot_filename = f"plot_{filename.split('.')[0]}.png"
    # Save generated plots alongside uploaded/generated CSVs so runtime-created files
    # stay in the same writable location across local and hosted environments.
    plot_output_path = os.path.join(app.config['UPLOAD_FOLDER'], plot_filename)
    plot_clusters(X, labels, save_path=plot_output_path)
    
    # Preview Data (First 10 rows)
    preview_cols = list(df.columns)
    preview_data = df.head(10).to_dict(orient='records')
    
    return render_template('results.html', 
                           n_clusters=n_clusters,
                           plot_image=plot_filename,
                           output_file=output_filename,
                           n_students=len(df),
                           preview_cols=preview_cols,
                           preview_data=preview_data)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    # Keep local development convenient while avoiding the unstable Windows reloader.
    debug_mode = os.environ.get('FLASK_DEBUG', '1') == '1'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, use_reloader=False, host='0.0.0.0', port=port)

