# import base64
# import requests
# from inference_sdk import InferenceHTTPClient

# class CustomInferenceHTTPClient(InferenceHTTPClient):
#     def __init__(self, api_url: str, api_key: str):
#         super().__init__(api_url=api_url, api_key=api_key)
    
#     def infer(self, file_path: str, model_id: str):
#         return super().infer(file_path, model_id)