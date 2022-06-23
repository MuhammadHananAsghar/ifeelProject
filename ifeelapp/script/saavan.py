from bs4 import BeautifulSoup
import requests



class JioSaavn:
  def __init__(self):
    self.header = {
        'authority': 'www.jiosaavn.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.jiosaavn.com/search/',
        'accept-language': 'en-US,en;q=0.9',
    }

  def search(self, query):
    params = {
      'p': '1',
      'q': f'{query}',
      '_format': 'json',
      '_marker': '0',
      'api_version': '4',
      'ctx': 'web6dot0',
      'n': '20',
      '__call': 'search.getResults',
    }

    response = requests.get('https://www.jiosaavn.com/api.php', params=params, headers=self.header).json()
    return response['results']

  def slice(self, string):
    if len(string) > 20:
      string = string[:20]+"...."
    return string

  def details(self, json):
    return {
        "lyrics_id": json["id"],
        "title": self.slice(json['title']),
        "subtitle": json['subtitle'],
        "type": json['type'],
        "image": json['image'],
        "language": json['language'],
        "perma_url": json['perma_url'],
        "year": json['year'],
        "id": json['perma_url'].split("/")[-1],
        "encrypted_media_url": json['more_info']["encrypted_media_url"],
        "duration": round(int(json['more_info']['duration'])/60, 2),
        'album': json['more_info']['album'],
        'has_lyrics': json['more_info']['has_lyrics']
    }
  
  def song(self, ID, URL):
    params = {
      '__call': 'song.generateAuthToken',
      'url': f'{URL}',
      'bitrate': '128',
      'api_version': '4',
      '_format': 'json',
      'ctx': f'{ID}',
      '_marker': '0',
    }
    response = requests.get('https://www.jiosaavn.com/api.php', params=params, headers=self.header)
    return response.json()['auth_url']
  
  def lyrics(self, lyrics_id):
    params = {
        '__call': 'lyrics.getLyrics',
        'lyrics_id': f'{lyrics_id}',
        'ctx': 'web6dot0',
        'api_version': '4',
        '_format': 'json',
        '_marker': '0',
    }
    response = requests.get('https://www.jiosaavn.com/api.php', params=params, headers=self.header)
    return response.json()['lyrics']