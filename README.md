# PeerGroup AI - Intelligent Collaborative Learning Teams

## Overview
**PeerGroup AI** is a Flask-based web application designed to automatically form effective peer learning groups. By analyzing student data—such as grades, learning styles, and interests—the system uses Unsupervised Machine Learning (K-Means Clustering) to create balanced or homogenous groups, enhancing collaboration and learning outcomes in classrooms.

![Upload Page](static/upload_page.png) *(Note: Placeholder for actual screenshot)*

## Key Features
- **Web Interface**: Modern, glassmorphism-inspired UI for easy interaction.
- **Dynamic Dataset Support**: Upload any CSV file containing student profiles.
- **Flexible Feature Selection**: Dynamically choose which columns to use as **Numerical** (e.g., Grades) or **Categorical** (e.g., Interests) features.
- **Automated Preprocessing**: seamless encoding of categorical data and scaling of numerical data.
- **Visualization**: Interactive PCA-reduced 2D plots to visualize the formed clusters.
- **Downloadable Results**: Export the group allocations as a CSV file.

## Tech Stack
- **Frontend**: HTML5, CSS3 (Custom Glassmorphism), Bootstrap 5, Jinja2.
- **Backend**: Python, Flask.
- **Machine Learning**: Scikit-learn (K-Means, PCA, StandardScaler, OneHotEncoder).
- **Data Processing**: Pandas, NumPy.
- **Visualization**: Matplotlib, Seaborn.

## Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/khushiyadav03/PeerGroup-AI.git
    cd PeerGroup-AI
    ```

2.  **Create a Virtual Environment** (Recommended)
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1.  **Start the Application**
    ```bash
    python app.py
    ```
2.  **Open in Browser**
    Navigate to `http://127.0.0.1:5000`.
3.  **Upload Data**
    - Upload your own CSV file or use the built-in "Generate Synthetic Data" feature.
4.  **Configure Clustering**
    - Select **Numerical Features** (e.g., Math_Grade, Science_Grade).
    - Select **Categorical Features** (e.g., Learning_Style, Interest).
    - Set the desired **Number of Groups**.
5.  **View & Download**
    - See the visual clusters and a preview of the groups.
    - Download the full result CSV.

## Project Structure
```
PeerGroup-AI/
├── app.py                # Main Flask Application
├── data/
│   └── data_generator.py # Synthetic data generation script
├── src/
│   ├── clustering.py     # K-Means logic
│   ├── preprocessing.py  # Data cleaning & encoding
│   └── visualization.py  # Plot generating logic
├── static/
│   ├── style.css         # Custom CSS
│   └── uploads/          # Temporary storage for uploaded/generated files
├── templates/
│   ├── base.html         # Base layout template
│   ├── index.html        # Landing & Upload page
│   ├── configure.html    # Feature selection page
│   └── results.html      # Results & Visualization page
└── requirements.txt      # Project dependencies
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.
