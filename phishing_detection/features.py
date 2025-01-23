import pandas as pd
import re
from urllib.parse import urlparse

def extract_features(url):
    """Extract features from a given URL."""
    features = {}

    # Presence of IP Address in URL
    features["Have_IP"] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

    # Presence of '@' Symbol in URL
    features["Have_At"] = 1 if "@" in url else 0

    # URL Length
    features["URL_Length"] = len(url)

    # URL Depth (Number of '/' in the path)
    features["URL_Depth"] = url.count('/')

    # Presence of Redirection '//'
    features["Redirection"] = 1 if "//" in urlparse(url).path else 0

    # HTTPS in Domain
    features["https_Domain"] = 1 if "https" in urlparse(url).netloc else 0

    # Presence of TinyURL (URL Shortening Services)
    shorteners = ["bit.ly", "goo.gl", "tinyurl", "ow.ly", "is.gd", "buff.ly"]
    features["TinyURL"] = 1 if any(shortener in url for shortener in shorteners) else 0

    # Prefix/Suffix in Domain
    features["Prefix/Suffix"] = 1 if "-" in urlparse(url).netloc else 0

    return pd.DataFrame([features])  # Convert dictionary to DataFrame
