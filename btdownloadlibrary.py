import BitTorrent.download
from threading import Event

def download(url, file):
    return BitTorrent.download.download(['--url=' + url, '--saveas=' + file], 
        lambda x: x, lambda a, b: None, Event(), 80)
