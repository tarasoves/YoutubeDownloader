from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable


# скачиваем простое видео по ссылке
def download_simple_link(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
    return f'Было скачено видео {video.title}'


# cкачиваем все видео из плейлиста СПОСОБ №1
def download_playlist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
    return f'Был скачен плейлист {playlist.title}'


# cкачиваем все видео из плейлиста СПОСОБ №2 (с обработкой исключений)
def download_playlist_with_except(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist.video_urls:
        try:
            video = YouTube(url)
        except VideoUnavailable:
            print(f'Видео по ссылке {url} недоступно')
        else:
            video.streams.get_highest_resolution().download()
    return f'Был скачен плейлист {playlist.title}'


# скачиваем только аудиопоток в формате mp4
def only_audio(url):
    audio = YouTube(url)
    audio.streams.get_audio_only().download()
    return f'Была скачена аудиодорожка {audio.title}'


# скачиваем видео в нужном качестве, например "720p" или “480p”
def video_resoulution(resolution, url):
    video = YouTube(url)
    if video.streams.get_by_resolution(resolution):
        video.streams.get_by_resolution(resolution).download()
        return f'Было скачено видео {video.title} с качеством {resolution}'
    else:
        print(f'Данного видео НЕТ в качестве {resolution}')
        video.streams.get_highest_resolution().download()
        return f'Было скачено видео {video.title} с максимально доступным качеством'


link = input('Введите ссылку на видео или плейлист: ')
if '&list=' in link:
    # print(download_playlist(link))
    print(download_playlist_with_except(link))
else:
    print(download_simple_link(link))

