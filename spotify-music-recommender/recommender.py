import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load and preprocess dataset
# df = pd.read_csv("SpotifyFeatures.csv")
df = pd.read_csv(r'D:\spotify-music-recommender\SpotifyFeatures.csv')

audio_features = ['acousticness', 'danceability', 'duration_ms', 'energy',
                  'instrumentalness', 'liveness', 'loudness', 'speechiness',
                  'tempo', 'valence']

X = df[audio_features].dropna()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=10, random_state=42)
df['KMeans_Cluster'] = kmeans.fit_predict(X_scaled)

# Optional: PCA for visual features (not used here)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

def recommend_songs(song_name, model='KMeans_Cluster', n=5):
    index = df[df['track_name'].str.lower() == song_name.lower()].index
    if len(index) == 0:
        return df[['track_name', 'artist_name', 'genre']].sample(n)
    index = index[0]
    cluster_label = df.loc[index, model]
    cluster_songs = df[(df[model] == cluster_label) & (df.index != index)]
    return cluster_songs[['track_name', 'artist_name', 'genre']].sample(n)