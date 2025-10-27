import requests

class JSONPlaceholder:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com/posts"):
        self.base_url = base_url
    
    def get_request(self):
        response = requests.get(self.base_url)
        
        if response.status_code == 200:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None
        
    def post_request(self, data):
        response = requests.post(self.base_url, data=data)
        
        if response.status_code == 201:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None
    
    def update_user(self, userId, title, body,):
        payload = {
            "title": title,
            "body": body,
        }   
        
        response = requests.put(f"{self.base_url}/{userId}", payload)

        if response.status_code == 200:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None


    def delete_user(self, userId, title, body,):
        payload = {
            "title": title,
            "body": body,
        }   
        
        response = requests.delete(f"{self.base_url}/{userId}", payload)

        if response.status_code == 200:
            return{
                "status_code": response.status_code,
                "headers": response.headers,
                "content": response.content[:500],
            }
        else:
            return None