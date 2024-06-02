import glob
import os
import yaml

class Translator():
    def __init__(self, translations_folder, default_locale='en') -> None:
        self.data = {}
        self.locale = 'en'

        # get list of files with specific extensions
        files = glob.glob(os.path.join(translations_folder, f'*.yml'))
        for file in files:
            # get the name of the file without extension, will be used as locale name
            loc = os.path.splitext(os.path.basename(file))[0]
            with open(file, 'r', encoding='utf8') as f:
                self.data[loc] = yaml.safe_load(f)
    
    def set_locale(self, locale: str) -> None:
        self.locale = locale

    def translate(self, key: str, locale: str=None) -> str:
        loc = (locale, self.locale) [locale is None]
        return (self.data[loc].get(key), key)

if __name__ == '__main__':
    translator = Translator('data/')
    word = translator.translate('this side of the river', locale='darug')
    print(word)
    translator.set_locale('darug')
    word = translator.translate('this side of the river')
    print(word)
