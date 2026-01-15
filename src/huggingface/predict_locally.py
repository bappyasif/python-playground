import onnxruntime as ort
from tokenizers import Tokenizer
# from src.huggingface.onnx_runtime import load_session, tokenize_input
import numpy as np

def load_session():
    session = ort.InferenceSession("./onnx/model.onnx")
    return session

def tokenize_input(tokenizer, text):
    encoded = tokenizer.encode(text)
    input_ids = np.array([encoded.ids], dtype=np.int64)
    return input_ids

def predict_locally(text):
    # Load the ONNX session
    session = load_session()

    # Load the tokenizer
    tokenizer = Tokenizer.from_file("./tokenizer/tokenizer.json")

    # Tokenize the input
    input_ids = tokenize_input(tokenizer, text)

    # Run inference
    inputs = {session.get_inputs()[0].name: input_ids}
    outputs = session.run(None, inputs)

    # Return the prediction
    return outputs[0].tolist()


"""
    import onnxruntime as ort
    from tokenizers import Tokenizer

    # Load the ONNX model
    session = ort.InferenceSession("path/to/model.onnx")

    # Load the tokenizer
    tokenizer = Tokenizer.from_file("path/to/tokenizer.json")

    # Prepare the prompts and user inputs
    prompts = ["This is a prompt for text generation.", "Another prompt for text generation."]
    user_inputs = ["User input 1", "User input 2"]

    # Tokenize the inputs
    input_ids = []
    for prompt in prompts:
        input_ids.append(tokenizer.encode(prompt).ids)
    for user_input in user_inputs:
        input_ids.append(tokenizer.encode(user_input).ids)

    # Reshape the inputs
    input_shape = session.get_inputs()[0].shape
    input_ids = np.array(input_ids, dtype=np.int64).reshape((-1,) + input_shape[1:])

    # Run inference
    session.run(None, {"input": input_ids})

    # Get the output
    output = session.get_outputs()[0].data

    # Post-process the output
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(output_text)
"""


# # lets write a script that uses a pretrained model from Hugging Face to make predictions locally
# import onnxruntime as ort
# from tokenizers import Tokenizer
# import numpy as np

# # 1. Load the Tokenizer (fast, no torch)
# # tokenizer = Tokenizer.from_file("onnx_model/tokenizer.json")
# tokenizer = Tokenizer.from_file("src/huggingface/onnx_model/tokenizer.json")

# # 2. Load the ONNX Session (fast, no torch) 
# # session = ort.InferenceSession("onnx_model/model.onnx")
# session = ort.InferenceSession("src/huggingface/onnx_model/model.onnx")

# def predict_locally():
#     # 3. Make Predictions (fast, no torch)
#     input_ids = tokenizer.encode("Text to summarize").ids
#     input_ids = np.array([input_ids], dtype=np.int64)

#     inputs = {session.get_inputs()[0].name: input_ids}
#     outputs = session.run(None, inputs)

#     print(outputs)