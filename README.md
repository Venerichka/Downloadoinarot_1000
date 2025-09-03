
<p align="center">
  <a href="https://github.com/yt-dlp/yt-dlp"><img alt="yt-dlp" src="https://img.shields.io/badge/yt-dlp-GitHub-black?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://pypi.org/project/yt-dlp/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/yt-dlp?style=for-the-badge"/></a>
  <a href="https://pypi.org/project/yt-dlp/"><img alt="Install" src="https://img.shields.io/badge/Install-pip%20install-blue?style=for-the-badge&logo=pypi&logoColor=white"/></a>
</p>
<h1 align="center">Downloadoinator_1000_CLI</h1>


## Описание
CLI Cкрипт для скачивания видео,аудио,плейлистов видео с выбором форматов,качества и поддержкой множества сайтов за счёт использования yt-dlp([список поддерживаемых сайтов,попробуйте найти любимый:3](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)) 
## Требования

- Python **3.10+**
- yt-dlp
- ffmpeg(не Python-пакет и устанавливается отдельно)

## Установка

Не забудьте установить [ffmpeg](https://www.ffmpeg.org/download.html), сделать это можно либо по ссылке или через пакетные менеджеры,ниже будут показаны способы для пакетных менеджеров,ведь они сразу добавляют FFmpeg в PATH

### Windows:
```
# winget
winget install --id=Gyan.FFmpeg -e

# или Chocolatey
choco install ffmpeg

# или Scoop
scoop install ffmpeg

ffmpeg -version
ffprobe -version

git clone https://github.com/Venerichka/Downloadoinarot_1000.git
cd Downloadoinarot_1000
python -m pip install --upgrade pip
pip install -r requirements.txt

yt-dlp --version
#или
python -m yt_dlp --version

python main.py
```

### Linux and MacOS

- Debian/Ubuntu:
```
sudo apt update
sudo apt install -y ffmpeg
```
- Arch:
```
sudo pacman -S ffmpeg
```
- Fedora:
```
sudo dnf install ffmpeg
```
 - MacOS:
```
brew install ffmpeg
```

##### Важное примечание:
На Unix-подобных лучше создавать venv для установки Python пакетов, поэтому:
```
git clone https://github.com/Venerichka/Downloadoinarot_1000.git
cd Downloadoinarot_1000

python3 -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```


### Последний шаг
Чтобы получить доступ к контенту который доступен лишь при наличии аккаунта;
```
# из папки проекта: создаёт ./cookies.txt, взяв куки из вашего браузера
python -m yt_dlp --cookies cookies.txt --cookies-from-browser (варианты :brave, chrome,chromium,edge,firefox,opera,safari,vivaldi,whale)  
```
Или же уберите/закомментируйте эту строчку из кода downloader.py(15 строка):
```
'cookiefile' :'cookies.txt'
```
