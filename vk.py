import requests
from datetime import datetime


class Vk:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.base_url = 'https://api.vk.com/method/'
        self.params = {'access_token': self.token, 'v': self.version}

    def photos(self, owner_id):
        url = self.base_url + 'photos.get'
        params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'photo_sizes': 1
        }
        response = requests.get(url, params={**self.params, **params})
        if response.status_code != 200:
            return response.status_code
        else:
            photos_info = []
            try:
                for photo in response.json()['response']['items']:
                    date = datetime.fromtimestamp(photo['date'])
                    photos_sizes = photo['sizes']
                    photo_url = photos_sizes[len(photos_sizes) - 1]['url']
                    photos_info.append({
                        'likes': photo['likes']['count'],
                        'date': date.strftime("(%y.%m.%d-%H.%M)"),
                        'url': photo_url
                    })
                return {'user': owner_id,
                        'photos': photos_info}
            except:
                return 0
