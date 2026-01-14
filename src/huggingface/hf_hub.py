from huggingface_hub import hf_hub_download

# huggingface_hub is designed to download a specific file from a repository

# Define the repository ID
repository_id = "onnx-community/text_summarization-ONNX"

# Define the filenames of the ONNX model and the tokenizer
# onnx_filename = "model.onnx"
tokenizer_filename = "tokenizer.json"

# Define the directories to save the ONNX model and the tokenizer
onnx_dir = "./onnx"
tokenizer_dir = "./tokenizer"

# Download the ONNX model
# hf_hub_download(
#     repo_id=repository_id,
#     # filename=onnx_filename,
#     local_dir=onnx_dir,
#     # recursive=True # to download entire folder if needed, but herte its says unexpected argument "recursive"!!
# )

# Download the tokenizer
hf_hub_download(
    repo_id=repository_id,
    filename=tokenizer_filename,
    local_dir=tokenizer_dir
)




# from huggingface_hub import hf_hub_download, HfFolder

# # Authenticate with your Hugging Face account
# HfFolder.save_token("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")

# # Download ONNX model
# hf_hub_download(
#     # repo_id="openai-chatgpt/gpt2-large",
#     # repo_id="openai-community/gpt2-medium",
#     repo_id="onnx-community/text_summarization-ONNX",
#     # repo_type="model",
#     filename="onnx/model.onnx",
#     local_dir="./onnx"
# )

# # Download tokenizer
# hf_hub_download(
#     # repo_id="openai-chatgpt/gpt2-large",
#     # repo_id="openai-community/gpt2-medium",
#     repo_id="onnx-community/text_summarization-ONNX",
#     # repo_type="tokenizer",
#     filename="tokenizer.json",
#     local_dir="./tokenizer"
# )

# from huggingface_hub import hf_hub_download

# # Download ONNX model
# hf_hub_download(
#     repo_id="openai-community/gpt2-medium",
#     filename="onnx/model.onnx",
#     local_dir="./onnx"
# )

# # Download tokenizer
# hf_hub_download(
#     repo_id="openai-community/gpt2-medium",
#     filename="tokenizer.json",
#     local_dir="./tokenizer"
# )   