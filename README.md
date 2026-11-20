# Student Placement Predictor

**Algorithm:** Logistic Regression | **Language:** Python | **Interface:** Streamlit

## Run
1. Extract this ZIP and open the folder in VS Code.
2. Open Terminal → New Terminal (PowerShell).
3. If required, install dependencies: `python -m pip install -r requirements.txt`
4. The trained model is already included. Start the app: `python -m streamlit run app.py`
5. A browser opens. Enter student details and click Predict Placement.

To retrain the model: `python train_model.py`

## Files
- `app.py`: interactive web app
- `dataset.csv`: sample dataset
- `placement_model.pkl`: pre-trained model
- `train_model.py`: training and evaluation
- `requirements.txt`: dependencies
- `VIVA_NOTES.md`: quick viva preparation

## Academic note
The included dataset is synthetic demonstration data, not real placement records. Test accuracy (84.29%) is measured only on a held-out split of this synthetic dataset and is not validated real-world placement performance.
