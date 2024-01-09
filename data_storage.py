import requests
import json

class DataStorage:
    @staticmethod
    def save_to_json(data, filename):
        with open('spotify_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    @staticmethod
    def save_image(url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

#with open('spotify_data.json', 'w', encoding='utf-8') as f:
#    json.dump(your_data, f, ensure_ascii=False, indent=4)
