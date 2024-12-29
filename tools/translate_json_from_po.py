#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This script generate json file fro languages,
#based on Babel,
# From po and mo files
"""
**`translate_json_from_po.py`**: This script is used to generate a JSON file based on translations from **PO/MO compiled files**. It extracts the translations and applies them to the corresponding data structure for use in the Yaziji phrase generation system.

### Parameters:

- **`-d`**: Specifies the data file that contains all the words, labels, and components used for Yaziji phrase generation.
- **`-t`**: Specifies the directory containing the compiled **PO/MO** translation files.
- **`-o`**: Specifies the output directory where the resulting JSON file will be saved.

Usage:

- The script processes the **PO/MO** compiled files, extracting translations and applying them to the relevant components and fields from the input data file.

- The resulting JSON file can then be used in the phrase generation system, ensuring that translations are integrated without altering the core data.

- > [!NOTE]
  >
  > For more details on translation please refer to [Translation Guide](translation_guide.md)
"""

import os
import json
from babel.support import Translations
import argparse

class Translator:
    def __init__(self, translation_directory, locale="ar"):
        """
        Initialize the Translator object with a directory for translations and a locale.
        Defaults to 'ar' (Arabic) if no locale is specified.
        """
        self.translation_directory = translation_directory
        self.locale = locale
        self.translations = self.load_translations()

    def load_translations(self):
        """
        Load translation files based on the locale.
        """
        return Translations.load(dirname=self.translation_directory, locales=self.locale)

    def set_locale(self, new_locale):
        """
        Dynamically change the locale and reload translations.
        """
        self.locale = new_locale
        self.translations = self.load_translations()  # Reload translations for the new locale

    def translate_dict_dict(self, input_dict):
        """
        Translate the values of a dictionary using Babel.
        """
        _ = self.translations.gettext  # Get the translation function
        translated_dict = {"fields": input_dict.get("fields", [])}

        for field in input_dict.get("fields", []):
            field_dict = input_dict[field]
            translated_dict[field] = {key: _(value) for key, value in field_dict.items()}

        return translated_dict

    def translate_dict_list(self, input_dict):
        """
        Translate the values of a dictionary with list values using Babel.
        """
        _ = self.translations.gettext  # Get the translation function
        translated_dict = {"fields": input_dict.get("fields", [])}
        # translate also labels
        for field in input_dict.get("fields", []):
            field_list = input_dict[field]
            translated_dict[field] = {value: _(value) for value in field_list if value}
        return translated_dict

    def translate_list(self, input_list):
        """
        Translate the values of a dictionary with list values using Babel.
        """
        _ = self.translations.gettext  # Get the translation function
        # translate also labels
        translated_dict = {value: _(value) for value in input_list if value}
        return translated_dict

    @staticmethod
    def open_json(file_path):
        """
        Open and load a JSON file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                print("Data loaded successfully.")
                return data
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
    @staticmethod
    def save_json(data, outfile):
        """
        Save data to a JSON file.

        :param data: Data to be written to the JSON file.
        :param outfile: Path to the output file.
        """
        try:
            # Open a file for writing
            with open(outfile, 'w', encoding='utf-8') as f:
                # Serialize the data and write it to the file
                json.dump(data, f, ensure_ascii=False, indent=4)  # `indent=4` for better formatting
            print(f"Data successfully saved to {outfile}")
        except Exception as e:
            print(f"Error saving data to {outfile}: {e}")

    def translate_web_data(self,data):
        """

        :param dict_path:
        :return:
        """
        if data:
            # the field data contains field :[term1, term2]
            webdata = data.get("data", {})
            weblabels = data.get("labels", {}).get("label",[])
            fields = data.get("fields", [])
            translated_data ={"project":"Yaziji Arabic Phrase Generator",
                              "lang":f"{self.locale}",
                "fields": fields,
                              # translate labels
                              "web-labels":self.translate_list(weblabels),
                              }
            # translate field value_list
            for field in fields:
                translated_data[field] = self.translate_list(webdata[field])
            # Translate dictionary with list values
            return translated_data
        return {}
def parse_args():
    """

    :return:
    """
# Initialize the argument parser
    parser = argparse.ArgumentParser(description="Process parameters for translation.")

    # Add arguments
    parser.add_argument(
        "-d", "--data-file",
        type=str,
        required=True,
        help="Path to the input data file."
    )
    parser.add_argument(
        "-t", "--translation-dir",
        type=str,
        required=True,
        help="Path to the translation directory."
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        required=True,
        help="Path to the output directory."
    )

    # Parse the arguments
    args = parser.parse_args()
    return args

def maintest():
    # Set up translation directory and initial locale (default is 'ar')
    translation_directory = os.path.join(os.path.dirname(__file__), "../web/locales")

    # Initialize Translator with default locale 'ar'
    translator = Translator(translation_directory, "ar")

    # Test translation strings for the default locale
    print("Default Locale (ar):", translator.translations.gettext("أَسَدٌ"))
    print("Default Locale (ar):", translator.translations.gettext("كَرِيمٌ"))
    print("Default Locale (ar):", translator.translations.gettext("سُوقٌ"))

    # Open JSON file
    dict_path = os.path.join(os.path.dirname(__file__), "../web/data/data.new.json")
    data = translator.open_json(dict_path)


    translated_data = translator.translate_web_data(data)
    print("Translated Data (ar):", translated_data)
    print("Translated Data (ar):", translated_data)
    # Change locale dynamically and translate again
    print("\nChanging locale to 'en'...")
    translator.set_locale("en")

    # Test translation strings for the new locale
    print("New Locale (en):", translator.translations.gettext("أَسَدٌ"))
    print("New Locale (en):", translator.translations.gettext("كَرِيمٌ"))
    print("New Locale (en):", translator.translations.gettext("سُوقٌ"))

    # Translate the same data after changing the locale
    if data:
        translated_data_en =     translated_data = translator.translate_web_data(data)
        print("Translated Data (en):", translated_data_en)


def mainjson():
    # Set up translation directory and initial locale (default is 'ar')
    translation_directory = os.path.join(os.path.dirname(__file__), "../web/locales")

    # Initialize Translator with default locale 'ar'
    translator = Translator(translation_directory, "ar")

    # Open JSON file
    dict_path = os.path.join(os.path.dirname(__file__), "../web/data/data.new.json")
    data = translator.open_json(dict_path)

    # Change locale dynamically and translate again
    print("\nChanging locale to 'en'...")
    translator.set_locale("en")

    # Test translation strings for the new locale
    print("New Locale (en):", translator.translations.gettext("أَسَدٌ"))
    print("New Locale (en):", translator.translations.gettext("كَرِيمٌ"))
    print("New Locale (en):", translator.translations.gettext("سُوقٌ"))

    # Translate the same data after changing the locale
    if data:
        translated_data_en =     translated_data = translator.translate_web_data(data)
        print("Translated Data (en):", translated_data_en)
        translator.save_json(translated_data_en, "../tests/output/bn.json")

def generate_lang_json(dict_path, translation_directory, output_directory):
    # Set up translation directory and initial locale (default is 'ar')
    # translation_directory = os.path.join(os.path.dirname(__file__), "../web/locales")

    # Initialize Translator with default locale 'ar'
    translator = Translator(translation_directory, "ar")

    # Open JSON file
    # dict_path = os.path.join(os.path.dirname(__file__), "../web/data/data.new.json")
    data = translator.open_json(dict_path)

    # Change locale dynamically and translate again
    languages = "ar,bn,de,en,es,fr,id,ja,ku,zh,he".split(',')
    for lang in languages:
        print("\nChanging locale to 'en'...")
        translator.set_locale(lang)

        # Test translation strings for the new locale
        print(f"New Locale {lang}:", translator.translations.gettext("أَسَدٌ"))
        print(f"New Locale {lang}:", translator.translations.gettext("كَرِيمٌ"))
        print(f"New Locale {lang}:", translator.translations.gettext("سُوقٌ"))

        # Translate the same data after changing the locale
        if data:
            translated_data_en =     translated_data = translator.translate_web_data(data)
            print(f"Translated Data {lang}:", translated_data_en)
            translator.save_json(translated_data_en, output_directory+f"/{lang}.json")
if __name__ == "__main__":
    # maintest()
    # mainjson()
    args = parse_args()
    # Output the parsed arguments
    # dict_path = args.data_file
    # translation_directory args.translation_dir, output_directory
    # print("Data file:", args.data_file)
    # print("Translation directory:", args.translation_dir)
    # print("Output directory:", args.output_dir)
    generate_lang_json(args.data_file, args.translation_dir, args.output_dir)