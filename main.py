import time
import requests
import yadisk
from pprint import pprint
from datetime import date
from progress.bar import IncrementalBar


class VK_Photos:
    url = "https://api.vk.com/method/"
    def __init__(self, TOKEN, version, USER_ID):
        self.params = {
        'owner_id': USER_ID,
        'v': version,
        'access_token': TOKEN,
    }

    def create_folder_name(self):
        create_folder_name_url = self.url +"users.get"
        resp = requests.get(url=create_folder_name_url, params=self.params)
        folder_json = resp.json()['response']
        return f"{folder_json[0].get('first_name')}_{folder_json[0].get('last_name')}_{date.today()}"
         
        
    def get_json_photos(self):
        json_url = self.url + "photos.get"
        json_params = {
                'album_id':'profile',
                'extended': '1',
                'photo_sizes':'1'
    }
        resp = requests.get(url=json_url, params={**self.params, **json_params})
        return resp.json()['response']['items']

    def get_biggest_px (self, size_dict):
        if size_dict['width']>= size_dict['height']:
            return size_dict['width']
        else:
            return size_dict['height']
    
def upload_photos():
    bar = IncrementalBar('Countdown', max = len(vk.get_json_photos()))
    for photo in vk.get_json_photos():
        bar.next()
        time.sleep(1)
        sizes = photo['sizes']
        max_size_url = max(sizes, key=vk.get_biggest_px)['url']
        file_name = f"/{vk.create_folder_name()}/likes_{photo['likes'].get('count')}"
        y.upload_url(max_size_url, file_name)
    bar.finish()
    print("Successfully uploaded")


if __name__ == '__main__':
    TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    USER_ID = '552934290'
    token_yd = 'AQAAAAAi7pwUAADLW9-DYE8jcUHYrzx-rc1e80k'

    vk = VK_Photos(TOKEN=TOKEN, version='5.131', USER_ID=USER_ID)
    y = yadisk.YaDisk(token=token_yd)

    y.mkdir(vk.create_folder_name())
    upload_photos()



    

