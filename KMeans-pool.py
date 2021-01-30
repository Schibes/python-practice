from multiprocessing import Pool
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
import time

def do_kmeans(n_samples):
    """KMeans clustering on generated data"""

    X,_ = make_blobs(n_samples=100000, centers=3, n_features=10,
                random_state=0)
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
    print(f"KMeans cluster fit in {time.time()-t0}")

def main():
    """Run Everything"""

    count=10
    t0 = time.time()
    with Pool(count) as p:
        p.map(do_kmeans, [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000])
        
    print(f"Performed {count} KMeans in total time: {time.time()-t0}")

if __name__ == "__main__":
    main()