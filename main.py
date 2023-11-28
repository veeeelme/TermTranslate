import googletrans
from sys import argv
from pyperclip import copy


def words_translate(words, lang):
    """text_translator

    Args:
        text (str): enter sentence or word that you want to translate
        lang (str): enter language
    """

    if lang not in googletrans.LANGUAGES:
        print('maybe there is no language you wrote')

    translator = googletrans.Translator()
    return translator.translate(words, dest=lang)


def detect_lang(words):
    """detect_lang

    Args:
        words (str or list): enter word/s whose language/s you want to detect
    """

    translator = googletrans.Translator()
    if words == str:
        translator.detect(words)
    return translator.detect(words)


def all_langs():
    return print(googletrans.LANGUAGES)


if len(argv) == 1:
    print(
        'Welcome to TermTranslate! \nHere, you can freely and easilly translate text.\n')
    print('______HELP_______\n'
          "python (or python3) [your path to main.py] [functions] [options]\n"
          "functions:\n"
          "   --wordtran: translate words and texts:\n"
          "       options:\n"
          "           'your word or text' [language that you want]\n"
          "   --dctlang: detect language/s of words\n"
          "       options:\n"
          "           [your word]\n"
          "   --langs: all available langs\n"
          "CAUTION: all texts or few word would be in ''\n")

if argv[1] == '--wordtran':
    translation = words_translate(words=argv[2], lang=argv[3])
    print(translation.text)
    if len(translation.text) > 10:
        copy_choice = input('Copy this text? y/n: ')
        if copy_choice == 'y':
            copy(translation.text)


if argv[1] == '--dctlang':
    detector = detect_lang(words=argv[2])
    print(f'Language: {detector.lang}')

if argv[1] == '--langs':
    all_langs()
