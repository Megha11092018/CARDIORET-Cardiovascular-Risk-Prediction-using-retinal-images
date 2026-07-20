"""
Project Explanation: Heart Attack Risk Prediction Using Retinal Eye Images

This file provides a detailed explanation of each file in the project, including frameworks, models, and their purposes.

Project Overview:
This is a machine learning project that predicts heart attack risk based on retinal eye images. It uses a Flask web application for user interaction, TensorFlow for image classification, and fuzzy clustering for image preprocessing.

Frameworks and Technologies Used:
- Flask: Web framework for the application backend.
- TensorFlow: Machine learning framework for image classification model.
- OpenCV: Computer vision library for image processing.
- NumPy: Numerical computing library.
- SciPy: Scientific computing library.
- Scikit-learn: Machine learning library.
- Matplotlib: Plotting library for visualizations.
- Pillow (PIL): Image processing library.
- Werkzeug: WSGI utility library for Flask.
- Gunicorn: WSGI HTTP Server for deployment.
- Python-dotenv: Environment variable management.

Models:
- Retrained Inception V3 or MobileNet model: Used for classifying retinal images into risk categories (0-4).
- Fuzzy C-Means Clustering: Used for image segmentation and feature extraction.

File Explanations:
"""

# Root Directory Files
files_explanation = {
    ".gitattributes": "Git configuration file for handling line endings and file attributes in the repository.",
    ".gitignore": "Git configuration file specifying files and directories to ignore in version control.",
    "app1.py": """
Main Flask application file. Handles web routes, image uploads, model predictions, and user interactions.
Key components:
- Flask app setup with routes for home, login, upload, predict, etc.
- Image processing using PIL and TensorFlow preprocessing.
- Integration with label_image.py for model inference.
- Fuzzy clustering via image_fuzzy_clustering.py for image preprocessing.
- Health tips and risk level mapping based on prediction results.
- AJAX endpoints for prediction with JSON responses.
- File upload handling with secure filename generation.
- Caching prevention for fresh predictions.
""",
    "demo_retinal.jpg": "Sample retinal image used for demonstration and testing the model.",
    "image_fuzzy_clustering.py": """
Script for performing Fuzzy C-Means (FCM) clustering on retinal images.
Key functions:
- read_img(): Loads and preprocesses images (downsampling, blurring).
- flatten_img(): Converts 3D image to 2D array for clustering.
- recover_img(): Converts clustered 2D array back to 3D image.
- initialization(): Initializes cluster centers and memberships using k-means++.
- update_responsibility(): E-step of EM algorithm for FCM.
- update_means(), update_covariance(), update_labels(): M-step updates.
- EM_cluster(): Main EM algorithm for FCM clustering.
- plot_cluster_img(): Applies clustering and saves original/clustered images.
Uses Expectation-Maximization algorithm with fuzzy memberships for image segmentation.
""",
    "label_image.py": """
TensorFlow script for image classification using a retrained model.
Key functions:
- load_graph(): Loads the frozen TensorFlow graph from file.
- read_tensor_from_image_file(): Preprocesses image for model input.
- load_labels(): Loads class labels from text file.
- main(): Runs inference on an image and returns the top prediction.
Uses TensorFlow 1.x compatibility mode for model loading and inference.
Processes images through the retrained Inception V3 model to classify risk levels.
""",
    "output_labels.txt": "Output file containing class labels after retraining (similar to retrained_labels.txt).",
    "Readme.md": """
Markdown file with comprehensive project documentation.
Includes:
- Project overview and objectives.
- Problem statement and key features.
- System architecture description.
- Technologies used (Python, TensorFlow, Flask, etc.).
- Setup and installation instructions.
- Usage guide and testing information.
- Results, applications, limitations, and future scope.
- Author and license information.
""",
    "requirements.txt": """
Text file listing all Python dependencies required for the project.
Includes:
- numpy: Numerical computing
- tensorflow: Machine learning framework
- flask: Web framework
- Werkzeug: WSGI utilities
- gunicorn: WSGI server
- python-dateutil: Date/time utilities
- scipy: Scientific computing
- opencv-python: Computer vision
- imageio: Image I/O
- scikit-learn: Machine learning algorithms
- matplotlib: Plotting
- python-dotenv: Environment variables
- Pillow: Image processing
""",
    "retrain.py": """
TensorFlow script for retraining a pre-trained model on custom dataset.
Key features:
- Downloads and extracts pre-trained Inception V3 or MobileNet models.
- Creates image lists from directory structure.
- Caches bottleneck features for efficient retraining.
- Adds final training layers for classification.
- Supports data augmentation (flipping, cropping, scaling, brightness).
- Evaluates model accuracy on validation and test sets.
- Saves retrained graph and labels.
Uses transfer learning to adapt pre-trained models for retinal image classification.
""",
    "retrained_labels.txt": """
Text file containing the class labels for the retrained model.
Labels correspond to risk levels:
0: No risk
1: Low risk
2: Medium risk
3: High risk
4: Very high risk
""",
    "TODO.md": """
Markdown file tracking project tasks and progress.
Includes:
- Completed tasks (renaming folders, retraining model, testing).
- Pending improvements (augment dataset, tune hyperparameters, extensive testing).
- Notes on model performance and accuracy metrics.
"""
}

# Data Directory
data_files = {
    "data/input_images/": "Directory containing training images organized by risk level folders.",
    "data/input_images/0/": "Images labeled as 'No risk' for training.",
    "data/input_images/1/": "Images labeled as 'Low risk' for training.",
    "data/input_images/2/": "Images labeled as 'Medium risk' for training.",
    "data/input_images/3/": "Images labeled as 'High risk' for training.",
    "data/input_images/4/": "Images labeled as 'Very high risk' for training.",
    "data/input_images/High_Risk/": "Alternative folder for high-risk images.",
    "data/input_images/Low_Risk/": "Alternative folder for low-risk images.",
    "data/input_images/Midium_Risk/": "Alternative folder for medium-risk images (note: typo in 'Midium').",
    "data/input_images/NO_risk/": "Alternative folder for no-risk images.",
    "data/live_uploads/": "Directory for storing images uploaded through the web interface.",
    "data/live_uploads/1343_left.jpeg": "Example uploaded retinal image."
}

# Dataset Directory
dataset_files = {
    "dataset/": "Main dataset directory containing retinal images.",
    "dataset/10_right.jpeg": "Sample retinal image from the dataset.",
    "dataset/1178_right.jpeg": "Sample retinal image from the dataset.",
    "dataset/1343_left.jpeg": "Sample retinal image from the dataset.",
    "dataset/10244_left.jpeg": "Sample retinal image from the dataset.",
    "dataset/10321_left.jpeg": "Sample retinal image from the dataset.",
    "dataset/10758_right.jpeg": "Sample retinal image from the dataset.",
    "dataset/11035_right.jpeg": "Sample retinal image from the dataset.",
    "dataset/0/": "Subdirectory containing images labeled as risk level 0.",
    "dataset/1/": "Subdirectory containing images labeled as risk level 1.",
    "dataset/2/": "Subdirectory containing images labeled as risk level 2.",
    "dataset/3/": "Subdirectory containing images labeled as risk level 3.",
    "dataset/4/": "Subdirectory containing images labeled as risk level 4.",
    # Note: Individual image files in dataset/0/ are numerous and follow naming patterns
}

# Hospital Images Directory
hospital_images = {
    "hospital images/": "Directory containing additional retinal images, possibly from hospital sources.",
    "hospital images/15_right.jpeg": "Sample hospital retinal image.",
    "hospital images/1277_left.jpeg": "Sample hospital retinal image.",
    "hospital images/2426_right.jpg": "Sample hospital retinal image.",
    "hospital images/test image 4.jpeg": "Test image from hospital collection.",
    "hospital images/test image 6.jpeg": "Test image from hospital collection.",
    "hospital images/test image 7.jpeg": "Test image from hospital collection.",
    "hospital images/test image 8.jpeg": "Test image from hospital collection.",
    "hospital images/test image.png": "Test image in PNG format.",
    "hospital images/test image2.png": "Test image in PNG format.",
    "hospital images/test image3.png": "Test image in PNG format.",
    "hospital images/test image5.jpeg": "Test image from hospital collection.",
    "hospital images/test image9.jpeg": "Test image from hospital collection.",
    "hospital images/High_Risk/": "Hospital images categorized as high risk.",
    "hospital images/Low_Risk/": "Hospital images categorized as low risk.",
    "hospital images/Midium_Risk/": "Hospital images categorized as medium risk.",
    "hospital images/NO_risk/": "Hospital images categorized as no risk."
}

# Static Directory
static_files = {
    "static/": "Directory for static web assets (CSS, JS, images).",
    "static/main1.js": """
JavaScript file for client-side functionality.
Key features:
- Image upload preview using FileReader API.
- AJAX request to /predict endpoint for model inference.
- Dynamic display of prediction results and health tips.
- Loading animation during prediction.
- Error handling for failed requests.
Uses jQuery for DOM manipulation and AJAX calls.
""",
    "static/style.css": "CSS file for styling the web interface.",
    "static/css/": "Subdirectory for additional CSS files.",
    "static/images/": "Directory for storing processed images (original and clustered).",
    "static/img/": "Alternative directory for images.",
    "static/js/": "Directory for additional JavaScript files."
}

# Templates Directory
template_files = {
    "templates/": "Directory containing Jinja2 HTML templates for Flask.",
    "templates/base.html": "Base template with common HTML structure, navigation, and footer.",
    "templates/chart.html": "Template for displaying charts or visualizations.",
    "templates/first.html": "Alternative home page template.",
    "templates/home.html": "Home page template with project introduction.",
    "templates/index.html": """
Main prediction interface template.
Features:
- File upload form for retinal images.
- Bootstrap tabs displaying information about risk factors (Age, BP, BMI, etc.).
- Image preview functionality.
- Prediction result display area.
- Health tips based on risk level.
Extends base.html and includes main1.js for interactivity.
""",
    "templates/index1.html": "Alternative upload page template.",
    "templates/layout.html": "Layout template for consistent page structure.",
    "templates/login.html": "Login page template for user authentication.",
    "templates/success.html": "Success page template for displaying clustering results."
}

# Test Images Directory
test_images = {
    "Test Images/": "Directory containing test images for model validation.",
    "Test Images/10_right.jpeg": "Test retinal image.",
    "Test Images/129_left.jpeg": "Test retinal image.",
    "Test Images/1178_right.jpeg": "Test retinal image.",
    "Test Images/1343_left.jpeg": "Test retinal image.",
    "Test Images/10321_left.jpeg": "Test retinal image.",
    "Test Images/11035_right.jpeg": "Test retinal image.",
    "Test Images/23692_left.jpeg": "Test retinal image.",
    "Test Images/chandu_retinal.jpg": "Named test retinal image.",
    "Test Images/testing.jpg": "General test image."
}

# Model Files (not directly visible but referenced)
model_files = {
    "retrained_graph.pb": """
Frozen TensorFlow graph file containing the retrained model.
- Created by retrain.py script.
- Contains the neural network architecture and trained weights.
- Used by label_image.py for inference.
- Based on Inception V3 or MobileNet architecture fine-tuned for retinal image classification.
""",
    "bottleneck/": "Directory for caching bottleneck features during retraining (created by retrain.py).",
    "summaries/": "Directory for TensorBoard summaries during training."
}

def print_explanation():
    """Print detailed explanations of all project files."""
    print("=== HEART ATTACK RISK PREDICTION PROJECT FILE EXPLANATIONS ===\n")

    print("FRAMEWORKS AND TECHNOLOGIES:")
    print("- Flask: Lightweight WSGI web application framework for Python.")
    print("- TensorFlow: Open-source machine learning framework for building and training models.")
    print("- OpenCV: Computer vision library for image processing.")
    print("- NumPy: Fundamental package for scientific computing with Python.")
    print("- SciPy: Library for mathematics, science, and engineering.")
    print("- Scikit-learn: Machine learning library for Python.")
    print("- Matplotlib: Comprehensive library for creating static, animated, and interactive visualizations.")
    print("- Pillow: Python Imaging Library for image processing.")
    print("- Fuzzy C-Means: Soft clustering algorithm for image segmentation.\n")

    print("MODELS:")
    print("- Retrained CNN Model: Transfer learning model based on Inception V3 or MobileNet.")
    print("- Fuzzy C-Means Clustering: Unsupervised clustering for retinal vessel segmentation.\n")

    sections = [
        ("ROOT DIRECTORY FILES", files_explanation),
        ("DATA DIRECTORY", data_files),
        ("DATASET DIRECTORY", dataset_files),
        ("HOSPITAL IMAGES", hospital_images),
        ("STATIC ASSETS", static_files),
        ("HTML TEMPLATES", template_files),
        ("TEST IMAGES", test_images),
        ("MODEL FILES", model_files)
    ]

    for section_name, section_dict in sections:
        print(f"=== {section_name} ===")
        for file_path, explanation in section_dict.items():
            print(f"{file_path}:")
            print(explanation.strip())
            print()

if __name__ == "__main__":
    print_explanation()
