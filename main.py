from auth import Auth
from spotify_data_fetcher import SpotifyDataFetcher
from data_storage import DataStorage

def main():
    auth = Auth()
    token = auth.get_token()

    fetcher = SpotifyDataFetcher(token)

    # Obtener datos de Spotify
    top_artists = fetcher.get_top_artists()
    top_tracks = fetcher.get_top_tracks()
    playlist_info = fetcher.get_playlist_info('37i9dQZF1DWWGFQLoP9qlv')

    # Continuación de main.py

    # Procesar los 10 artistas más escuchados
    artist_names = [artist['name'] for artist in top_artists]
    artist_genres = set()
    for artist in top_artists:
        artist_genres.update(artist['genres'])

    # Seleccionar los 5 géneros más comunes
    top_genres = list(artist_genres)[:5]

    # Procesar las 10 canciones más escuchadas
    track_names = [track['name'] for track in top_tracks]
    track_artists = [track['artists'][0]['name'] for track in top_tracks]

    # Procesar información de la playlist
    playlist_tracks = playlist_info['tracks']['items']
    track_ids = [track['track']['id'] for track in playlist_tracks]

    # Obtener características de audio de las canciones de la playlist
    audio_features = fetcher.get_audio_features(track_ids)

    # Calcular promedios de las características de audio
    # Asumimos que todas las características de audio son numéricas, excepto aquellas que se deben excluir
    features_to_exclude = ['type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    average_features = {key: 0 for key in audio_features[track_ids[0]].keys() if key not in features_to_exclude}

    for track_id in track_ids:
        for feature in average_features:
            # Asegúrate de que el valor es numérico antes de sumarlo
            if isinstance(audio_features[track_id][feature], (int, float)):
                average_features[feature] += audio_features[track_id][feature]

    # Calcular el promedio
    for feature in average_features:
        average_features[feature] /= len(track_ids)


    # Datos a guardar
    your_data = {
        'Top Artists': artist_names,
        'Top Genres': top_genres,
        'Top Tracks': list(zip(track_names, track_artists)),
        'Playlist Audio Features': average_features
    }

    # Continúa con la parte de guardar datos...


    # Guardar datos en un archivo
    DataStorage.save_to_json(your_data, 'spotify_data.json')
    DataStorage.save_image(playlist_info['images'][0]['url'], 'playlist_cover.jpg')

if __name__ == "__main__":
    main()