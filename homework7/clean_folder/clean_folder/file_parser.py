import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_MEDIA = []
MP4_MEDIA = []
MOV_MEDIA = []
MKV_MEDIA = []
DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT =[]
PDF_DOCUMENT =[]
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []


OTHER = []
ZIP_ARCHIVES = []
GZ_ARCHIVES =  []
TAR_ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_MEDIA,
    'MP4': MP4_MEDIA,
    'MOV': MOV_MEDIA,
    'MKV': MKV_MEDIA,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,

    'ZIP': ZIP_ARCHIVES,
    'GZ' : GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # превращаем расширение файла в название папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Если это папка то добавляем ее в список FOLDERS и преходим к следующему элементу папки
        if item.is_dir():
            # проверяем, чтобы папка не была той в которую мы складываем уже файлы
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                #  сканируем эту вложенную папку - рекурсия
                scan(item)
            #  перейти к следующему элементу в сканируемой папке
            continue

        #  Пошла работа с файлом
        ext = get_extension(item.name)  # взять расширение
        fullname = folder / item.name  # взять полный путь к файлу
        if not ext:  # если у файла нет расширения добавить к неизвестным
            OTHER.append(fullname)
        else:
            try:
                # взять список куда положить полный путь к файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Если мы не регистрировали расширение в REGISTER_EXTENSIONS, то добавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')
    print(f'Media mp4: {MP4_MEDIA}')
    print(f'Media avi: {AVI_MEDIA}')
    print(f'Media mov: {MOV_MEDIA}')
    print(f'Media mkv: {MKV_MEDIA}')
    print(f'Document doc: {DOC_DOCUMENT}')
    print(f'Document docx: {DOCX_DOCUMENT}')
    print(f'Document txt: {TXT_DOCUMENT}')
    print(f'Document pdf: {PDF_DOCUMENT}')
    print(f'Document xlsx: {XLSX_DOCUMENT}')
    print(f'Document pptx: {PPTX_DOCUMENT}')


    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')


    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
