Rice Yield Prediction



This is my machine learning project. It predicts how many rice packets we can get from a given land size (in acres).



WHY I MADE THIS PROJECT



I wanted to build a complete machine learning project from start to end. I picked a simple problem: if a farmer knows the land size, can we guess the rice production? This helped me understand the full flow: data cleaning, training, saving the model, prediction and a web app.



ALGORITHM USED



I used Simple Linear Regression.



\- Simple means there is only one input column (land size).

\- Linear Regression means the model draws the best straight line through the data.

\- Using this line, it predicts the output (rice packets) for a new land size.

\- If the land size is bigger, the predicted rice packets will also be bigger.



WHAT I DID, STEP BY STEP



1\. Load the raw data. I read the dataset from the data folder using Pandas.

2\. Fill missing values. Some rows had no land size. I filled them so the model does not fail on empty values.

3\. Save the cleaned data. I saved the cleaned dataset in a new file, so the raw data stays safe.

4\. Train the model. I gave the land size (input) and rice packets (output) to Linear Regression, so it can learn the pattern.

5\. Save the model. I saved the trained model with Joblib. Now I do not need to train it again every time.

6\. Predict. I load the saved model and give a new land size. It returns the predicted rice packets.



PROJECT FOLDERS



\- src : main code for training and prediction

\- data : raw data and cleaned data

\- models : the saved model file

\- config : config files

\- app\_streamlit.py : web app made with Streamlit

\- app\_gradio.py : web app made with Gradio

\- requirements.txt : list of libraries to install



HOW TO RUN



Run all commands from the main project folder.



1\. Install the libraries



pip install -r requirements.txt



2\. Train the model and predict in the terminal



python -m src.main



3\. Run the Streamlit app



streamlit run app\_streamlit.py



4\. Run the Gradio app



python app\_gradio.py



HOW THE APPS WORK



You type a land size (for example 3.5 acres) and click Predict. The app loads the saved model and shows the predicted rice packets.



TOOLS USED



\- Python

\- Pandas : to read and clean the data

\- Scikit-learn : for Linear Regression

\- Joblib : to save and load the model

\- Streamlit and Gradio : to make the web apps



WHAT I LEARNED



\- How to handle missing values

\- How Simple Linear Regression works

\- How to save and load a trained model

\- How to arrange a project in folders

\- How to make a small web app for a model



LIMITATIONS



\- The model uses only land size. In real life, rice yield also depends on rain, soil, seeds and more.

\- The dataset is small, so the prediction is only a rough estimate.



FUTURE IMPROVEMENTS



\- Add more input columns like rainfall and soil type

\- Try other models and compare the results

\- Put the app online

