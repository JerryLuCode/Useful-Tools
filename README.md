# Useful Tools

## Table of Content

- [YouTube Downloader (yt\_down.py)](#youtube-downloader-yt_downpy)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
    - [Arguments](#arguments)
    - [Examples](#examples)
  - [How it Works](#how-it-works)
- [Chinese Converter (chinese\_converter.py)](#chinese-converter-chinese_converterpy)
  - [Dependencies](#dependencies-1)
  - [Usage](#usage-1)
    - [Convert a single EPUB file](#convert-a-single-epub-file)
    - [Convert a single text file](#convert-a-single-text-file)
    - [Convert all EPUB and text files in a directory](#convert-all-epub-and-text-files-in-a-directory)
  - [How it Works](#how-it-works-1)

## YouTube Downloader (yt_down.py)

This script allows you to download videos or audio from YouTube, either as a single video or as a playlist. It also provides the option to download subtitles for the videos.

### Dependencies

The script requires the following Python packages:

- `argparse`
- `pytube`

You can install these dependencies using pip:

```
pip install argparse pytube
```

### Usage

```
python yt_down.py [-s | -l] [-v | -a] [-c] [-o] <youtube_url>
```

#### Arguments

- `-s`, `--single`: Download a single video.
- `-l`, `--list`: Download a playlist.
- `-v`, `--video`: Download the video.
- `-a`, `--audio`: Download the audio.
- `-c`, `--subtitles`: Download subtitles.
- `-o`, `--only`: Download subtitles only.
- `<youtube_url>`: The URL of the YouTube video or playlist.

#### Examples

1. Download a single video as a video:
   ```
   python yt_down.py -s -v "https://youtu.be/dQw4w9WgXcQ?si=R60mVlzUdkIeGPDT"
   ```

2. Download a playlist as audio:
   ```
   python yt_down.py -l -a "https://youtube.com/playlist?list=PLCiNIjl_KpQhFwQA3G19w1nmhEOlZQsGF&si=TDDKF0DLgGXDrJqq"
   ```

3. Download a single video with subtitles:
   ```
   python yt_down.py -s -c "https://youtu.be/bknUn7yMwNI?si=4ll2qL6s2VLjsJ4a"
   ```

4. Download subtitles only for a single video:
   ```
   python yt_down.py -s -o https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

### How it Works

The script uses the `pytube` library to interact with the YouTube API and download the videos, audio, and subtitles. The `argparse` library is used to parse the command-line arguments and handle the different options.

The `download_youtube` function is the main function that handles the download process. It checks the provided URL and determines if it's a single video or a playlist. It then uses the appropriate `pytube` classes (`YouTube` or `Playlist`) to download the content.

The `progress_function` is a callback function that is registered with the `YouTube` object to display the download progress.

The script also handles age-restricted videos and replaces any invalid characters in the video titles to ensure proper file naming.

Note: the caption part is not working now, so you can omit example 3 and 4.


## Chinese Converter (chinese_converter.py)

This script is designed to convert Simplified Chinese content (EPUB books and text files) to Traditional Chinese.

### Dependencies

The script requires the following Python packages:

- `opencc-python-reimplemented`
- `ebooklib`

You can install these dependencies using pip:

```
pip install opencc-python-reimplemented ebooklib
```

### Usage

#### Convert a single EPUB file

```
python chinese_converter.py -e /path/to/your/file.epub
```

This will convert the EPUB file to Traditional Chinese and save the result as `file_traditional.epub` in the same directory.

#### Convert a single text file

```
python chinese_converter.py -f /path/to/your/file.txt
```

This will convert the text file from Simplified Chinese (GBK encoding) to Traditional Chinese (UTF-8 encoding) and save the result as `file_traditional.txt` in the same directory.

#### Convert all EPUB and text files in a directory

```
python chinese_converter.py -d /path/to/your/directory
```

This will convert all EPUB and text files in the specified directory to Traditional Chinese and save the results in the same directory, with `_traditional` appended to the filenames.

### How it Works

The script uses the following libraries:

- `opencc-python-reimplemented`: This library is used to convert the content from Simplified Chinese to Traditional Chinese.
- `ebooklib`: This library is used to read and write EPUB files.

The script has three main functions:

1. `convert_simplified_to_traditional_epub`: This function reads an EPUB file, converts the content from Simplified Chinese to Traditional Chinese, and writes the converted content to a new EPUB file.
2. `convert_simplified_to_traditional_text`: This function converts a text file from Simplified Chinese (GBK encoding) to Traditional Chinese (UTF-8 encoding).
3. `convert_directory`: This function iterates through all files in a directory, and calls the appropriate conversion function for EPUB and text files.

The script uses an argument parser to accept different command-line arguments for converting single files or directories.

