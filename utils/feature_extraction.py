import tldextract

def extract_features(url):
    features = []

    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in url else 0)
    features.append(url.count("."))
    features.append(1 if url.startswith("https") else 0)

    ext = tldextract.extract(url)
    features.append(len(ext.domain))

    return features