import requests
from bs4 import BeautifulSoup

class Scraping:
    def request_song_info(song_title,artist_name):
        base_url='https://api.genius.com'
        headers={'Authorization':'Bearer '+'UgkaGS1PQxxWgEzXvSbd49iPFP7glhYMwF66aFIQeNHmcanThUTYHhSgUpBOr_lk'}
        search_url=base_url+'/search'
        data={'q':song_title+' '+artist_name}
        response=requests.get(search_url,data=data,headers=headers)

        return response

    def find_url(song_title,artist_name):
        response=request_song_info(song_title,artist_name)
        json=response.json()
        remote_song_info=None
        print(response)
        print(json.keys())
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                remote_song_info=hit
                break
        return remote_song_info['result']['url']

    def scrape_url(url):
        page=requests.get(url)
        html=BeautifulSoup(page.text,'html.parser')
        lyrics=html.find('div',class_='lyrics').get_text()

        return lyrics
    
    def get_lyrics(song_title,artist_name):
        return scrape_url(find_url(song_title,artist_name))

print(get_lyrics('WAV Files','Lupe Fiasco'))