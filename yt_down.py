import argparse
from pytube import YouTube, Playlist, exceptions

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (bytes_downloaded / total_size) * 100
    print(f'Downloading {stream.title}... {liveprogress:.1f}% complete', end='\r')

def download_youtube(url, download_type, is_playlist, download_subtitles, subtitles_only):
    if is_playlist:
        playlist = Playlist(url)
        for url in playlist.video_urls:
            download_youtube(url, download_type, False, download_subtitles, subtitles_only)
    else:
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            yt.register_on_progress_callback(progress_function)
            if not subtitles_only:
                # check file name, if it contains invalid characters, replace them
                invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
                for char in invalid_chars:
                    yt.title = yt.title.replace(char, '_')
                if download_type == 'v':
                    yt.streams.get_highest_resolution().download()
                elif download_type == 'a':
                    yt.streams.get_audio_only().download(filename=f"{yt.title} - {yt.author}.mp3")
            if download_subtitles or subtitles_only:
                # caption = yt.captions.get_by_language_code('en')
                # if caption is not None:
                #     with open(f"{yt.title} - {yt.author}.srt", "w") as f:
                #         f.write(caption.generate_srt_captions())
                caption = yt.captions
                next(c for c in caption if c.code == 'en').download(output_path="subtitles")
                # yt.captions.get_by_language_code('en').download(output_path="subtitles")
        except exceptions.AgeRestrictedError:
            print(f"Skipping age-restricted video: {yt.title}")
            print(f"URL: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YouTube Downloader')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--single', action='store_true', help='Download single video')
    group.add_argument('-l', '--list', action='store_true', help='Download playlist')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--video', action='store_true', help='Download as video')
    group.add_argument('-a', '--audio', action='store_true', help='Download as audio')
    parser.add_argument('-c', '--subtitles', action='store_true', help='Download subtitles')
    parser.add_argument('-o', '--only', action='store_true', help='Download subtitles only')
    parser.add_argument('url', type=str, help='YouTube URL')
    args = parser.parse_args()

    download_type = 'v'
    if args.audio:
        download_type = 'a'

    is_playlist = False
    if args.list:
        is_playlist = True

    download_subtitles = False
    if args.subtitles:
        download_subtitles = True

    subtitles_only = False
    if args.only:
        subtitles_only = True

    download_youtube(args.url, download_type, is_playlist, download_subtitles, subtitles_only)
