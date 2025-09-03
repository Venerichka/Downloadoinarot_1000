import yt_dlp
import os

from pathlib import Path


def download_content(url:str, mode:str , options:dict) -> bool:
    ydl_opts = {
        "outtmpl" : os.path.join(options['output_path'], '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': False,
        'noplaylist': (mode != 'playlist'),
        
        
        'cookiefile' :'cookies.txt'
    }
    if options.get('custom_format'):
        ydl_opts['format'] = options['custom_format']
        ydl_opts.pop('merge_output_format', None)
        ydl_opts.pop('recode_video', None)
    else: 
        if mode == 'audio':
            ydl_opts['format'] = f"bestaudio/{options.get('quality', 'best')}"
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        elif mode == 'video':
            ydl_opts['format'] = f"bestvideo+bestaudio/{options.get('quality','best')}"
            ydl_opts['recode_video'] = 'mp4'
        else:
            ydl_opts['outtmpl'] = os.path.join(
                options['output_path'],
                '%(playlist_index)s - %(title)s.%(ext)s'
            )
        # ВСТРАИВАНИЕ ОБЛОЖКИ
    if options.get('embed_thumbnail'):
        ydl_opts.setdefault('postprocessors', []).append({
            'key': 'EmbedThumbnail'
        })

    # ВСТРАИВАНИЕ МЕТАДАННЫХ
    if options.get('add_metadata'):
        ydl_opts.setdefault('postprocessors', []).append({
            'key': 'FFmpegMetadata'
        })
    
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"[Ошибкочка мя] {e}")
        return False

def list_formats(url: str) -> None:
    ydl_opts = {'quiet': False}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    formats = info.get('formats', [])
    print(f"Доступные форматики для «{info.get('title', '')}» (код — расширение — разрешение — заметка):")
    for f in formats:
        code = f.get('format_id', '')
        ext = f.get('ext', '')
        res = f.get('resolution') or f.get('format_note', '')
        note = f.get('format_note', '')
        print(f"{code:<8} {ext:<6} {res:<12} {note}")