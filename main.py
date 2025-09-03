from downloader import download_content, list_formats



def prompt_yes_no(prompt: str) -> bool:
    return input(f"{prompt} (y/n): ").strip().lower().startswith('y')
def main():
    url = input("Введите ссылочку:")
    custom = prompt_yes_no("Х-х-хочешь..сам выбрать формат (кодик потока)?")
    if custom:
        print("\n=== Доступные форматити ===")
        list_formats(url)
        fmt = input("Введите код формата (пример: '137' или '248+251'): ").strip()
        options = {
            'custom_format': fmt,
            'output_path': input("Папочка для сохранения: ").strip(),
            'embed_thumbnail': prompt_yes_no("Встраивать обложечку?"),
            'add_metadata': prompt_yes_no("Добавить метаданные?")
        }
        mode = 'custom'
    else:
        mode = input("Выбери режимчик (audio/video/playlist): ").strip().lower()
        options = {
            'output_path': input("Папочка для сохранения: ").strip(),
            'quality': input("Желаемое качество (best/worst или Enter): ").strip() or 'best',
            'embed_thumbnail': prompt_yes_no("Встраивать обложечку?"),
            'add_metadata': prompt_yes_no("Добавить метаданные?")
        }
    print("\nЗапуск загрузки…пуки...каки\n")
    success = download_content(url, mode, options)
    print("\nГотово НЯЯ!" if success else "\nПроизошла ошибочка дурачок")



if __name__ == "__main__":
    main()