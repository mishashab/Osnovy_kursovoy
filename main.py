import json
from progress.bar import IncrementalBar
from vk import Vk
from yandexDisk import YaUploader
from datetime import datetime

access_token = ''
user_id = ''
ya_token = ''


def upload_from_vk():
    # loader_user_id = input('Введите id профиля для сохранения фотографий: ')
    loader_user_id = '98865615'
    vk = Vk(access_token, user_id)
    return vk.photos(loader_user_id)


def save_file_on_ydisk(folder_name, photo):
    ya = YaUploader(ya_token)
    ya.upload(folder_name, photo)


def reserved_coping():
    photos = upload_from_vk()
    log_file_name = 'logs/' + datetime.now().strftime("%y.%m.%d-%H.%M.%S") \
                    + '.json'

    if type(photos) == int:
        with open(log_file_name, 'w') as out_file:
            json.dump({'vk response status': photos}, out_file,
                      ensure_ascii=False, indent=2)
        return f'vk response status {photos}'

    with open(log_file_name, 'w') as out_file:
        json.dump(photos, out_file, ensure_ascii=False, indent=2)

    if photos['photos'] == 'No photo in profile':
        return "User  hasn't photos"

    folder_name = photos['user']
    photos = photos['photos']
    print(f'В профиле {len(photos)}')
    photos_count = int(input('Введите количество фотографий для сохранения: '))
    if photos_count <= 0 or photos_count > len(photos):
        photos_count = 5
    bar = IncrementalBar('Upload photo on Yandex disk', max=photos_count)
    for photo in photos[:photos_count]:
        save_file_on_ydisk(folder_name, photo)
        bar.next()
    bar.finish()
    return 0


if __name__ == '__main__':
    reserved_coping()
