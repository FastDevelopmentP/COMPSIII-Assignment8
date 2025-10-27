# in http_requests.py
import requests

# JSONPlaceholder API interaction class
class JSONPlaceholder:
    # Initialize with base URL
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com/posts"):
        self.base_url = base_url
    
    # GET request method
    def get_request(self):
        response = requests.get(self.base_url)
        
        # Check for successful response
        if response.status_code == 200:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None

    # POST request method   
    def post_request(self, data):
        response = requests.post(self.base_url, data=data)
        
        # Check for successful creation
        if response.status_code == 201:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None
    # PUT request method
    def update_user(self, userId, title, body,):
        # Create payload for update
        payload = {
            "title": title,
            "body": body,
        }   
        
        # Send PUT request
        response = requests.put(f"{self.base_url}/{userId}", payload)
        
        # Check for successful update
        if response.status_code == 200:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None

    # DELETE request method
    def delete_user(self, userId):
        response = requests.delete(f"{self.base_url}/{userId}")

        if response.status_code == 200:
            return{
                "status_code": response.status_code,
            }