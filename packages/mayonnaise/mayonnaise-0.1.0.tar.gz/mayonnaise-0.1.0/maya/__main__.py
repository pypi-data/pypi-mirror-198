from os import makedirs, path
from tqdm import tqdm

from pytube.contrib.playlist import Playlist
from pytube import YouTube
from click import group, option, argument


@group()
def main():
    pass


@main.command()
@argument('playlist', type = str)
@option('--output-path', '-o', type = str, required = True)
@option('--authenticate', '-a', is_flag = True)
@option('--audio', '-u', is_flag = True)
@option('--bit-rate', '-b', type = int, default = 160)
def pull(playlist: str, output_path: str, authenticate: bool, audio: bool, bit_rate: int):
    playlist = Playlist(playlist)

    abr = f'{bit_rate}kbps' if audio else None  # abr = audio bit rate

    for url in tqdm(playlist, desc = 'Downloading media from playlist'):
        yt = YouTube(url, use_oauth = authenticate, allow_oauth_cache = True)

        filename = f'{yt.title}.mp{"3" if audio else "4"}'.replace('/', '__slash__')
        filepath = path.join(output_path, filename)

        if path.isfile(filepath):
            continue

        makedirs(output_path, exist_ok = True)

        if audio:
            (
                yt.streams
                .filter(only_audio = True, abr = abr)
                .first()
                .download(output_path = output_path, filename = filename)
            )
        else:
            (
                yt.streams
                .filter(progressive = True, file_extension = 'mp4')
                .order_by('resolution')
                .desc()
                .first()
                .download(output_path = output_path, filename = filename)
            )


if __name__ == '__main__':
    main()
