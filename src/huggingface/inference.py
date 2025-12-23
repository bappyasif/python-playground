import requests

from fastapi.routing import APIRouter, HTTPException

from dotenv import load_dotenv
import os

import logging

from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv("HF_TOKEN_PYTHON_PLAYGROUND")

# print(api_key)
logging.basicConfig(level=logging.INFO)

hfi_router = APIRouter()

# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# HEADERS = {"Authorization": f"Bearer {api_key}"}

client = InferenceClient(
    # model="facebook/bart-large-cnn",
    # model="philschmid/bart-msrd-compressor",    
    model="human-centered-summarization/financial-summarization-pegasus",
    token=api_key
)

@hfi_router.post("/summarize")
async def summarize_text(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text parameter cannot be empty")

    try:
        # Use regular requests - this is fine in FastAPI!
        # response = requests.post(API_URL, json={"inputs": text}, headers=HEADERS)

        response = client.summarization(text)
        response.raise_for_status()
        
        if response.status_code == 200:
            result = response.json()
            return {"summary": result[0]["summary_text"]}
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to summarize text")
            
    except requests.exceptions.RequestException as e:
        logging.error(f"Error making API request: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to make API request: {str(e)}")



# older version now deporicated!!
# import requests

# from fastapi.routing import APIRouter, HTTPException

# from dotenv import load_dotenv
# import os

# import logging

# load_dotenv()

# api_key = os.getenv("HF_TOKEN_PYTHON_PLAYGROUND")

# # print(api_key)
# logging.basicConfig(level=logging.INFO)

# hfi_router = APIRouter()

# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# HEADERS = {"Authorization": f"Bearer {api_key}"}

# @hfi_router.post("/summarize")
# async def summarize_text(text: str):
#     if not text:
#         raise HTTPException(status_code=400, detail="Text parameter cannot be empty")

#     try:
#         # Use regular requests - this is fine in FastAPI!
#         response = requests.post(API_URL, json={"inputs": text}, headers=HEADERS)
#         response.raise_for_status()
        
#         if response.status_code == 200:
#             result = response.json()
#             return {"summary": result[0]["summary_text"]}
#         else:
#             raise HTTPException(status_code=response.status_code, detail="Failed to summarize text")
            
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error making API request: {e}")
#         raise HTTPException(status_code=500, detail=f"Failed to make API request: {str(e)}")




# API_URL = "api-inference.huggingface.co"
# API_URL = "router.huggingface.co"
# HEADERS = {"Authorization": f"Bearer {api_key}"}

# @hfi_router.post("/summarize")
# async def summarize_text(text: str):
#     if not text:
#         raise HTTPException(status_code=400, detail="Text parameter cannot be empty")

#     try:
#         # response = requests.post(url=f"https://{API_URL}/models/facebook/bart-large-cnn", json={"text": text}, headers=HEADERS)
#         response = requests.post(url=f"https://{API_URL}/models/facebook/bart-large-cnn", json={"inputs": text}, headers=HEADERS)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error making API request: {e}")
#         raise HTTPException(status_code=500, detail="Failed to make API request")
#     except requests.HTTPError as e:
#         logging.error(f"API request failed with status code {e.response.status_code}: {e.response.text}")
#         raise HTTPException(status_code=e.response.status_code, detail="API request failed")

#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise HTTPException(status_code=response.status_code, detail="Failed to summarize text")
    
# async def summarize_text(text: str):
#     try:
#         response = requests.post(url=f"https://{API_URL}/models/facebook/bart-large-cnn", json={"text": text}, headers=HEADERS)
#     except requests.exceptions.RequestException as e:
#         return {"error": str(e)}
    
#     print(response)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "Failed to summarize text", api_key: api_key}