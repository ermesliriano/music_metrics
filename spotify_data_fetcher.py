import requests

class SpotifyDataFetcher:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.headers = {'Authorization': f'Bearer {self.auth_token}'}
        self.base_url = 'https://api.spotify.com/v1/'

    def get_top_artists(self):
        response = requests.get(f'{self.base_url}me/top/artists?limit=10', headers=self.headers)
        return response.json()['items']

    def get_top_tracks(self):
        response = requests.get(f'{self.base_url}me/top/tracks?limit=10', headers=self.headers)
        return response.json()['items']

    def get_playlist_info(self, playlist_id):
        response = requests.get(f'{self.base_url}playlists/{playlist_id}', headers=self.headers)
        return response.json()

    def get_audio_features(self, track_ids):
        features = {}
        for track_id in track_ids:
            response = requests.get(f'{self.base_url}audio-features/{track_id}', headers=self.headers)
            features[track_id] = response.json()
        return features