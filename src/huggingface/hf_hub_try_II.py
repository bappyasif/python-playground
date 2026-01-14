from huggingface_hub import snapshot_download

# from src.huggingface.hf_hub import hf_hub_download

# hf_hub_download(
#     repo_id="onnx-community/text_summarization-ONNX",
#     # repo_type="tokenizer",
#     filename="tokenizer.json",
#     local_dir="./tokenizer"
# )

def download_files_from_repository(repository_url: str, output_dir: str) -> None:
    repo_id = "onnx-community/text_summarization-ONNX"
    snapshot_download(
        repo_id=repo_id,
        repo_type="model",
        local_dir=output_dir,
        local_dir_use_symlinks=False,
        allow_patterns="onnx/**"
    )
    print(f"Downloaded files to {output_dir}")

# Usage
repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"
output_dir = "./onnx"
download_files_from_repository(repository_url, output_dir)


# from huggingface_hub import snapshot_download
# import os

# def download_files_from_repository(repository_url: str, output_dir: str) -> None:
#     # Extract repo_id from URL
#     repo_id = "/".join(repository_url.strip("/").split("/")[-2:])
    
#     # Use allow_patterns to filter files in the 'onnx' subfolder
#     snapshot_download(
#         repo_id=repo_id,
#         repo_type="model",
#         local_dir=output_dir,
#         local_dir_use_symlinks=False,
#         allow_patterns="onnx/**"  # Downloads all files under the 'onnx/' directory
#     )
#     print(f"Downloaded files to {output_dir}")

# # Usage
# repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"
# output_dir = "./onnx"
# download_files_from_repository(repository_url, output_dir)   