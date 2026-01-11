import requests

def download_files_from_repository(repository_url: str, output_dir: str) -> None:
    """
    Download files from a repository and save them in the specified output directory.

    Args:
        repository_url (str): The URL of the repository.
        output_dir (str): The directory where the files will be saved.

    Returns:
        None
    """
    response = requests.get(repository_url)
    if response.status_code == 200:
        content_type = response.headers.get("content-type")
        if content_type == "application/json":
            repository_contents = response.json()
            for file in repository_contents["tree"]:
                if file["type"] == "file":
                    file_url = file["download_url"]
                    file_name = file_url.split("/")[-1]
                    file_path = os.path.join(output_dir, file_name)
                    response = requests.get(file_url)
                    if response.status_code == 200:
                        with open(file_path, "wb") as file:
                            file.write(response.content)
                        print(f"Downloaded: {file_name}")
                    else:
                        print(f"Failed to download: {file_name}")
        else:
            print("Response content type is not JSON!!.")
    else:
        print(f"Failed to retrieve the repository. Status code: {response.status_code}")

# Usage example
repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"
output_dir = "./onnx"
download_files_from_repository(repository_url, output_dir)


# import requests

# # Define the repository URL
# repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"

# # Define the directory to save the ONNX files
# onnx_dir = "./onnx"

# # Send a GET request to the repository URL
# response = requests.get(repository_url)
# if response.status_code == 200:
#     # Check the response content type
#     content_type = response.headers.get("content-type")
#     if content_type == "application/json":
#         # Extract the repository contents
#         repository_contents = response.json()

#         # Iterate over the repository contents and download the files
#         for file in repository_contents["tree"]:
#             if file["type"] == "file":
#                 file_url = file["download_url"]
#                 file_name = file_url.split("/")[-1]
#                 file_path = os.path.join(onnx_dir, file_name)
#                 response = requests.get(file_url)
#                 if response.status_code == 200:
#                     with open(file_path, "wb") as file:
#                         file.write(response.content)
#                     print(f"Downloaded: {file_name}")
#                 else:
#                     print(f"Failed to download: {file_name}")
#     else:
#         print("Response is not in JSON format.")
# else:
#     print(f"Failed to retrieve the repository. Status code: {response.status_code}")


# import requests

# # Define the repository URL
# repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"

# # Define the directory to save the ONNX files
# onnx_dir = "./onnx"

# # Send a GET request to the repository URL
# response = requests.get(repository_url)
# if response.status_code == 200:
#     # response = response.json()
#     pass

# Check the response status code
# if response.status_code == 200:
#     # Check the response content type
#     content_type = response.headers.get("content-type")
#     if content_type == "application/json":
#         # Extract the repository contents
#         repository_contents = response.json()

#         # Iterate over the repository contents and download the files
#         for file in repository_contents["tree"]:
#             if file["type"] == "file":
#                 file_url = file["download_url"]
#                 file_name = file_url.split("/")[-1]
#                 file_path = f"{onnx_dir}/{file_name}"
#                 response = requests.get(file_url)
#                 if response.status_code == 200:
#                     with open(file_path, "wb") as f:
#                         f.write(response.content)
#                     print(f"File downloaded: {file_name}")
#                 else:
#                     print(f"Failed to download file: {file_name}")
#     else:
#         print("Response content type is not JSON.")
# else:
#     print(f"Failed to retrieve the repository. Status code: {response.status_code}")


# import requests

# # Define the repository URL
# repository_url = "https://huggingface.co/onnx-community/text_summarization-ONNX/tree/main/onnx"

# # Define the directory to save the ONNX files
# onnx_dir = "./onnx"

# # Send a GET request to the repository URL
# response = requests.get(repository_url)

# # Check the response status code
# if response.status_code == 200:
#     # Check the response content type
#     content_type = response.headers.get("content-type")
#     if content_type == "application/json":
#         # Extract the repository contents
#         repository_contents = response.json()

#         # Iterate over the repository contents and download the files
#         for file in repository_contents["tree"]:
#             if file["type"] == "file":
#                 file_url = file["download_url"]
#                 file_name = file_url.split("/")[-1]
#                 file_path = f"{onnx_dir}/{file_name}"
#                 response = requests.get(file_url)
#                 if response.status_code == 200:
#                     with open(file_path, "wb") as f:
#                         f.write(response.content)
#                     print(f"File downloaded: {file_name}")
#                 else:
#                     print(f"Failed to download file: {file_name}")
#     else:
#         print("Response content type is not JSON.")
# else:
#     print(f"Failed to retrieve the repository. Status code: {response.status_code}")