#!/usr/bin/env python3
#
#  gen_json_lang.py
#  
#  Copyright 2024 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import requests
import json

def fetch_and_display_json(url, output_file):
    try:
        # Get the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors
        
        # Parse the JSON content
        data = response.json()
        
        # Display the JSON content as Unicode
        print(json.dumps(data, ensure_ascii=False, indent=4))
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit()
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit()


def main(args):
    # Example usage
    languages = ['ar', 'bn', 'de', 'en', 'es', 'fr', 'id', 'ja', 'ku', 'zh']
    for lang in languages:
        url = "http://127.0.0.1:5000/{lang}/selectGet?text=&action=RandomText".format(lang=lang)  # Replace with your URL
        outfile = "outputs/{lang}.json".format(lang=lang)
        fetch_and_display_json(url, outfile)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
