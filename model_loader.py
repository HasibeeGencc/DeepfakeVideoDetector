import tensorflow as tf

def load_trained_model():
    try:
        model = tf.keras.models.load_model("saved_model")
        print("Model successfully loaded from saved_model")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
