import os
from uuid import uuid4
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from flask import Flask, request, render_template, current_app, jsonify
from werkzeug.utils import secure_filename
import label_image
import image_fuzzy_clustering as fem
from dotenv import load_dotenv


# ------------------- Load Environment Variables ---------------
load_dotenv()

# ------------------- Helper Functions -------------------
def load_image(image_path):
    """Call label_image.main() to process the image and return result"""
    text = label_image.main(image_path)
    return text

def prepare_image(image, target):
    """Preprocess image for Keras model"""
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image

def save_img(img, filename):
    """Save uploaded image to static/images"""
    picture_path = os.path.join(current_app.root_path, 'static/images', filename)
    with Image.open(img) as i:
        i.save(picture_path)
    return picture_path

# ------------------- Flask App -------------------
app = Flask(__name__)
model = None  # Load your model if needed

UPLOAD_FOLDER = os.path.join(app.root_path, 'static/img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.after_request
def add_header(response):
    """Prevent browser caching for fresh predictions"""
    response.headers['Cache-Control'] = 'no-store'
    return response

# ------------------- Routes -------------------
@app.route('/')
@app.route('/first')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/upload')
def upload():
    return render_template('index1.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        i = request.form.get('cluster')
        f = request.files['file']
        original_pic_path = save_img(f, f.filename)
        print(f"Starting clustering for {i} clusters on {original_pic_path}")
        clustering_results = fem.plot_cluster_img(original_pic_path, i)
        print(f"Clustering completed: {clustering_results}")
    return render_template('success.html', clustering_results=clustering_results)

@app.route('/index')
def index():
    return render_template('index.html')

# ------------------- Predict Route with Health Tips -------------------
@app.route('/predict', methods=['POST'])
def upload1():
    f = request.files.get('file')
    if not f:
        return "No file uploaded", 400

    filename = secure_filename(f.filename)
    unique_filename = str(uuid4()) + "_" + filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    f.save(file_path)

    try:
        # Get model prediction
        result = load_image(file_path).strip()

        # Map string labels to numeric keys
        label_mapping = {
            "high risk": "4",
            "low risk": "1",
            "midium risk": "2",
            "no risk": "0"
        }

        # Use result directly as key, or map if it's a string
        key = label_mapping.get(result, result)

        # Temporary fix: treat '1' as high risk
        # if key == '1':
        #     key = '4'

        d = {"1":" → Age = 30-35 , SBP = 140-160 mmHg, DBP = 80-90 mmHg, BMI = 27-29, HbA1c = 4-5.6, Risk of Heart Attack = Very Low Risk 20% ",
        '2':" → Age = 35-40 , SBP = 150-166 mmHg, DBP = 85-95 mmHg, BMI = 29-31, HbA1c = 7.5 -10.5 , Risk of Heart Attack = Mild Risk 40%",
        '3':" → Age = 35-40 , SBP = 120-136 mmHg, DBP = 75-55 mmHg, BMI = 18-25, HbA1c = 5.5 -6.5 , Risk of Heart Attack = No Risk You are Healthy",
        '4':" → Age = 45-60 , SBP = 160-176 mmHg, DBP = 95-100 mmHg, BMI = 30-35, HbA1c = 13.4 -14.9 , Risk of Heart Attack = High Chance of Heart Attack 60%",
        "0":" → Age = 20-25 , SBP = 111-126 mmHg, DBP = 80-85 mmHg, BMI = 18-25, HbA1c = 5.4 -7.0 , Risk of Heart Attack = No Risk You are Healthy",
        "5":" → invalid input " }

        result_text = result + d[key]

        # Add health tips and risk level based on risk
        if key == "0":
            health_tip = "Health Tip: Maintain your healthy lifestyle. Keep exercising and eat well!"
            risk_level = "no-risk"
        elif key == "2":
            health_tip = "Health Tip: Regular walking improves blood flow, reduces cholesterol, and supports heart function."
            risk_level = "mild"
        elif key == "4":
            health_tip = "Health Tip: Consult a cardiologist immediately and follow a strict health plan."
            risk_level = "high"
        else:
            health_tip = "Health Tip:Monitor your blood pressure regularly. Exercise and maintain a balanced diet."
            risk_level = "low"

    except Exception as e:
        result_text = f"Error processing image: {e}"
        health_tip = "Health Tip: Please try again or consult a professional."
        risk_level = "error"

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    print(f"Prediction Result: {result_text}")
    print(f"Health Tip: {health_tip}")
    print(f"Risk Level: {risk_level}")
    return jsonify({"result": result_text, "health_tip": health_tip, "risk_level": risk_level})

@app.route('/health-tips')
def health_tips():
    return render_template('health_tips.html')


# ------------------- Run App -------------------
if __name__ == '__main__':
    app.run(debug=True)








# import os
# from uuid import uuid4
# from PIL import Image
# import numpy as np
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.applications import imagenet_utils
# from flask import Flask, request, render_template, jsonify, current_app
# from werkzeug.utils import secure_filename
# import label_image
# import image_fuzzy_clustering as fem
# import openai
# from dotenv import load_dotenv

# # ------------------- Load Environment Variables -------------------
# load_dotenv() # loads variables from .env
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # ------------------- Helper Functions -------------------

# def load_image(image_path):
#     """Call label_image.main() to process the image and return result"""
#     text = label_image.main(image_path)
#     return text

# def prepare_image(image, target):
#     """Preprocess image for Keras model"""
#     if image.mode != "RGB":
#         image = image.convert("RGB")
#     image = image.resize(target)
#     image = img_to_array(image)
#     image = np.expand_dims(image, axis=0)
#     image = imagenet_utils.preprocess_input(image)
#     return image

# def save_img(img, filename):
#     """Save uploaded image to static/images"""
#     picture_path = os.path.join(current_app.root_path, 'static/images', filename)
#     with Image.open(img) as i:
#         i.save(picture_path)
#     return picture_path

# # ------------------- Flask App -------------------

# app = Flask(__name__)
# model = None # Load your model if needed

# UPLOAD_FOLDER = os.path.join(app.root_path, 'static/img')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.after_request
# def add_header(response):
#     """Prevent browser caching for fresh predictions"""
#     response.headers['Cache-Control'] = 'no-store'
#     return response

# # ------------------- Routes -------------------

# @app.route('/')
# @app.route('/first')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/chart')
# def chart():
#     return render_template('chart.html')

# @app.route('/upload')
# def upload():
#     return render_template('index1.html')

# @app.route('/success', methods=['POST'])
# def success():
#     if request.method == 'POST':
#         i = request.form.get('cluster')
#         f = request.files['file']
#         original_pic_path = save_img(f, f.filename)
#         fem.plot_cluster_img(original_pic_path, i)
#     return render_template('success.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def upload1():
#     f = request.files.get('file')
#     if not f:
#         return "No file uploaded", 400

#     filename = secure_filename(f.filename)
#     unique_filename = str(uuid4()) + "_" + filename
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
#     f.save(file_path)

#     try:
#         # Get model prediction
#         result = load_image(file_path).strip()

#         # Map string labels to numeric keys
#         label_mapping = {
#             "high risk": "3",
#             "low risk": "1",
#             "medium risk": "2",
#             "no risk": "0"
#         }

#         # Use result directly as key, or map if it's a string
#         key = label_mapping.get(result, result)

#        d = {"1":" → Age = 30-35 , SBP = 140-160 mmHg, DBP = 80-90 mmHg, BMI = 27-29, HbA1c = 4-5.6, Risk of Heart Attack = Very Low Risk 20% ",
# 	'2':" → Age = 35-40 , SBP = 150-166 mmHg, DBP = 85-95 mmHg, BMI = 29-31, HbA1c = 7.5 -10.5 , Risk of Heart Attack = Mild Risk 40%",
#         '3':" → Age = 35-40 , SBP = 120-136 mmHg, DBP = 75-55 mmHg, BMI = 18-25, HbA1c = 5.5 -6.5 , Risk of Heart Attack = No Risk You are Healthy",
#         '4':" → Age = 45-60 , SBP = 160-176 mmHg, DBP = 95-100 mmHg, BMI = 30-35, HbA1c = 13.4 -14.9 , Risk of Heart Attack = High Chance of Heart Attack 60%",
#         "0":" → Age = 20-25 , SBP = 111-126 mmHg, DBP = 80-85 mmHg, BMI = 18-25, HbA1c = 5.4 -7.0 , Risk of Heart Attack = No Risk You are Healthy",
#         "5":" → invalid input " }

#         result_text = result + d[key]

#         # Add health tips and risk level based on risk
#         if key == "0":
#             health_tip = "Health Tip: Maintain your healthy lifestyle. Keep exercising and eating well!"
#             risk_level = "no-risk"
#         elif key == "1":
#             health_tip = "Health Tip: Monitor your health indicators. Consider lifestyle adjustments."
#             risk_level = "low"
#         elif key == "2":
#             health_tip = "Health Tip: Monitor your blood pressure regularly. Exercise and maintain a balanced diet."
#             risk_level = "medium"
#         elif key == "3":
#             health_tip = "Health Tip: Consult a cardiologist immediately and follow a strict health plan."
#             risk_level = "high"
#         else:
#             health_tip = "Health Tip: Keep a healthy lifestyle and monitor regularly."
#             risk_level = "invalid"

#     except Exception as e:
#         result_text = f"Error processing image: {e}"
#         health_tip = "Health Tip: Please try again or consult a professional."
#         risk_level = "error"

#     finally:
#         if os.path.exists(file_path):
#             os.remove(file_path)

#     print(f"Prediction Result: {result_text}")
#     print(f"Health Tip: {health_tip}")
#     print(f"Risk Level: {risk_level}")
#     return jsonify({"result": result_text, "health_tip": health_tip, "risk_level": risk_level})

# # ------------------- Chatbot Routes -------------------

# @app.route('/chat')
# def chat():
#     return render_template('chat.html')

# @app.route('/chat_history')
# def chat_history():
#     # You can show a list of previous messages or just a placeholder page
#     return render_template('chat_history.html')

# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_message = request.form.get('message')
#     if not user_message:
#         return jsonify({"response": "Please type something!"})

#     try:
#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": user_message}],
#             max_tokens=150,
#             temperature=0.7
#         )
#         answer = completion.choices[0].message['content'].strip()
#     except Exception as e:
#         answer = "Sorry, I am having trouble responding. Please try again."

#     return jsonify({"response": answer})

# # ------------------- Run App -------------------

# if __name__ == '__main__':
#     app.run(debug=True)
