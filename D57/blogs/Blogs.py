import requests


class Blogs:
    blogs_endpoint = 'https://api.npoint.io/53b3cecf519823194f2e'

    def get_data(self):
        try:
            response = requests.get(self.blogs_endpoint)
            response.raise_for_status()
            data = response.json()
            print(data)
            return data
        except Exception as e:
            print(e)
            return None
