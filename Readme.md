# ❤️ Heart Attack Risk Prediction Using Retinal Eye Images

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-green?logo=opencv)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-blue)

### 🩺 AI-Powered Non-Invasive Heart Attack Risk Prediction Using Retinal Fundus Images

Predicting cardiovascular risk through retinal image analysis using **Fuzzy C-Means Clustering** and **Deep Learning (RNN)**.

</div>

---

# 📑 Table of Contents

- Project Overview
- Problem Statement
- Objectives
- Features
- System Architecture
- Workflow
- Technologies Used
- Dataset
- Project Structure
- Installation
- Usage
- Docker Deployment
- Results
- Screenshots
- Applications
- Future Scope
- Author
- License

---

# 📌 Project Overview

Cardiovascular diseases remain one of the leading causes of death worldwide. Early diagnosis significantly improves patient outcomes, but conventional diagnostic procedures are often expensive, invasive, and require specialized medical equipment.

This project presents an **Artificial Intelligence-based system** that predicts the risk of heart attack using **retinal fundus images**. Since retinal blood vessels reflect cardiovascular health, analyzing retinal images can provide valuable insights into a patient's heart condition without invasive procedures.

The system integrates **Image Processing**, **Machine Learning**, and **Deep Learning** techniques to automatically analyze retinal images and estimate heart attack risk.

---

# ❗ Problem Statement

Develop an intelligent healthcare system capable of predicting heart attack risk using retinal fundus images through advanced image processing and deep learning techniques, enabling early diagnosis with a non-invasive approach.

---

# 🎯 Objectives

- Develop an accurate AI-based heart attack prediction system.
- Analyze retinal blood vessel patterns.
- Improve early cardiovascular disease detection.
- Reduce dependency on invasive diagnostic procedures.
- Provide a user-friendly healthcare application.
- Assist doctors with intelligent decision support.

---

# ✨ Key Features

- 👁️ Retinal Image Analysis
- 🧠 Deep Learning Prediction using RNN
- 🎨 Fuzzy C-Means Image Clustering
- 📊 Risk Classification
- 📈 Feature Visualization
- 🔐 User Authentication
- 🌐 Web-based Interface
- ⚡ Fast Prediction
- 🏥 Healthcare Decision Support

---

# 🏗️ System Architecture

```text
                 ┌───────────────────────┐
                 │   Retinal Eye Image   │
                 └──────────┬────────────┘
                            │
                            ▼
               Image Preprocessing
                            │
                            ▼
             Fuzzy C-Means Clustering
                            │
                            ▼
              Feature Extraction Layer
                            │
                            ▼
              Recurrent Neural Network
                            │
                            ▼
             Heart Attack Risk Prediction
                            │
                            ▼
                 Result Visualization
```

---

# 🔄 Project Workflow

```text
Retinal Image
      │
      ▼
Image Upload
      │
      ▼
Image Preprocessing
      │
      ▼
Fuzzy C-Means Clustering
      │
      ▼
Feature Extraction
      │
      ▼
RNN Prediction Model
      │
      ▼
Heart Attack Risk Detection
      │
      ▼
Display Result
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning

- TensorFlow
- Keras
- Scikit-Learn
- Recurrent Neural Network (RNN)
- AdaBoost

## Image Processing

- OpenCV
- NumPy

## Data Analysis

- Pandas
- Matplotlib

## Web Development

- Flask
- HTML
- CSS
- JavaScript
- Bootstrap

## Database

- SQLite / MySQL

## Tools

- Git
- GitHub
- VS Code
- Jupyter Notebook

---

# 📂 Dataset

The project uses **Retinal Fundus Images** collected from publicly available retinal datasets and research resources.

### Dataset Contents

- Healthy Retina Images
- Diseased Retina Images
- Blood Vessel Structures
- Retinal Features

### Image Format

- JPG
- JPEG
- PNG

### Folder Structure

```
dataset/
│
├── Healthy/
├── Diseased/
├── Test/
└── Validation/
```

> **Note:** Ensure that all medical datasets are used only for research and educational purposes while maintaining patient privacy and ethical standards.

---

# 📁 Project Structure

```text
Heart-Attack-Risk-Prediction/
│
├── dataset/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── vendor/
│
├── templates/
│
├── app.py
├── label_image.py
├── image_fuzzy_clustering.py
├── requirements.txt
├── README.md
├── .gitignore
└── output_labels.txt
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Heart-Attack-Risk-Prediction.git
cd Heart-Attack-Risk-Prediction
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Verify Installation

```bash
python --version
pip list
```

---

# ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🚀 How to Use

1. Launch the web application.
2. Login as an authorized user.
3. Upload a retinal fundus image.
4. Image preprocessing begins automatically.
5. Fuzzy C-Means clustering extracts retinal vessel features.
6. The trained RNN model predicts cardiovascular risk.
7. View prediction results and clustered retinal image.
8. Analyze patient risk level.

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t heart-attack-prediction .
```

## Run Docker Container

```bash
docker run -d -p 5000:5000 heart-attack-prediction
```

## Docker Compose

```bash
docker compose up --build
```

---

# 📊 Model Pipeline

```text
Input Retinal Image
          │
          ▼
Image Preprocessing
          │
          ▼
Noise Removal
          │
          ▼
Fuzzy C-Means Clustering
          │
          ▼
Feature Extraction
          │
          ▼
Deep Learning (RNN)
          │
          ▼
Heart Attack Prediction
          │
          ▼
Result Visualization
```

---

# 📈 Results

The developed model successfully predicts the risk of heart attack from retinal images by analyzing retinal blood vessel characteristics.

### Output Includes

- ✅ Clustered Retinal Image
- ✅ Predicted Risk Level
- ✅ Age Category
- ✅ Blood Pressure Information
- ✅ BMI Category
- ✅ Hemoglobin Range
- ✅ Graphical Visualization

---

# 📷 Screenshots

## 🏠 Home Page

<p align="center">
<img src="images/home.png" width="800">
</p>

---

## 🔐 Login Page

<p align="center">
<img src="images/login.png" width="800">
</p>

---

## 📤 Image Upload

<p align="center">
<img src="images/upload.png" width="800">
</p>

---

## 🎨 Fuzzy C-Means Clustering

<p align="center">
<img src="images/cluster.png" width="800">
</p>

---

## ❤️ Prediction Result

<p align="center">
<img src="images/result.png" width="800">
</p>

---

# 🌍 Applications

- 🏥 Early Heart Disease Screening
- ❤️ Cardiovascular Risk Assessment
- 👨‍⚕️ Clinical Decision Support
- 📱 Telemedicine
- 🌐 Remote Healthcare
- 🩺 Preventive Healthcare
- 👴 Elderly Patient Monitoring
- 📊 Population Health Analysis

---

# 🚀 Future Scope

- Improve prediction accuracy using advanced Deep Learning models.
- Integrate Vision Transformers (ViT).
- Deploy the system on cloud platforms.
- Develop Android and iOS mobile applications.
- Support real-time retinal image analysis.
- Integrate Electronic Health Records (EHR).
- Enable continuous AI model updates using Federated Learning.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is developed for **educational and research purposes**.

You are free to use, modify, and improve this project with proper attribution.

---

# 👩‍💻 Author

**Megha B Biradar**

🎓 Computer Science & Engineering

💻 Aspiring DevOps Engineer | Java Full Stack Developer | AI & ML Enthusiast

📧 Email: your-email@example.com

🔗 GitHub: https://github.com/Megha11092018

🔗 LinkedIn: https://www.linkedin.com/

---

# 🙏 Acknowledgements

Special thanks to:

- KLS Vishwanathrao Deshpande Institute of Technology
- Project Guide & Faculty Members
- Open Source Community
- TensorFlow
- OpenCV
- Flask
- Scikit-Learn
- GitHub

---

<div align="center">

## ⭐ If you found this project useful, please give it a Star ⭐

**Made with ❤️ by Megha B Biradar**

</div>
