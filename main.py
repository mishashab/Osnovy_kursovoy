
from vk import Vk
from yandexDisk import YaUploader

access_token = ''
user_id = ''
ya_token = ''


def upload_from_vk():
    loader_user_id = input('Введите id профиля для сохранения фотографий: ')
    # loader_user_id = '397729647'
    vk = Vk(access_token, user_id)
    return vk.photos(loader_user_id)


def save_file_on_ydisk(folder_name, photo):
    ya = YaUploader(ya_token)
    ya.upload(folder_name, photo)


def reserved_coping():
    photos = upload_from_vk()
    if photos == 0:
        return "User  hasn't photos"
    if type(photos) == int:
        return f'Error {photos}'
    folder_name = photos['user']
    photos = photos['photos']
    print(f'В профиле {len(photos)}')
    photos_count = int(input('Введите количество фотографий для сохранения: '))
    if photos_count <= 0 or photos_count > len(photos):
        photos_count = 5
    for photo in photos[:photos_count - 1]:
        save_file_on_ydisk(folder_name, photo)


if __name__ == '__main__':
    reserved_coping()
