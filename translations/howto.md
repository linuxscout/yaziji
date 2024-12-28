# **Guide: Preparing a New Language for Yaziji**

This guide provides detailed steps to integrate a new language into the Yaziji Arabic Sentence Generator. Follow the instructions carefully to ensure seamless integration.

---

## **1. Ways to Translate**
You can translate the required strings either by using PO files or by working with an Excel/Google Sheets file for translation.

### **1.1. Translate Text Using PO Files**
- Begin with the `main.pot` template file. Rename it according to your target language (e.g., `main_fr.pot` for French).
- Skip to step **5. Create a Language Folder** for further instructions on folder structure.

### **1.2. Translate Text Using Google Sheets**
- Open the shared **Google Sheet** provided for translation.
- Translate each Arabic text entry into the target language.
- Ensure that translations are accurate, clear, and contextually correct, preserving the original meaning.

---

## **2. Save Translations to a CSV File**
- Download the completed translations from Google Sheets in **CSV format**.
- The CSV file must have **two columns**:
  - **Arabic text (Source)** 
  - **Translated text (Target)**

---

## **3. Prepare a Three-Field CSV File**
Create a new CSV file with the following structure:
- **location**: Leave this field empty.
- **source**: Contains the Arabic text.
- **target**: Contains the translated text in the target language.

### Example CSV Format:
| location | source          | target       |
|----------|-----------------|--------------|
|          | مرحبًا          | Hello        |
|          | كيف حالك؟       | How are you? |

---

## **4. Convert CSV to PO File**
Use the `csv2po` command-line tool to convert the CSV file into a `.po` file format.

### Command:
```sh
csv2po <your_file>.csv -t ../main.pot -o <language_code>.po
```

- Replace `<your_file>` with the name of your CSV file.
- Replace `<language_code>` with the **two-letter language code** for the target language (e.g., `bn` for Bangla).

---

## **5. Create a Language Folder**
- Create a folder named after the target language code (e.g., `bn` for Bangla).

### Command:
```sh
mkdir bn
```

---

## **6. Rename and Copy PO File**
- Rename the `.po` file to follow the naming convention `main_<language_code>.po`.
- Move the renamed file to the newly created language folder.

### Command:
```sh
cp <language_code>.po <language_code>/main_<language_code>.po
```

Example for Bangla:
```sh
cp bn.po bn/main_bn.po
```

---

## **7. Create Locales Directory**
Inside the `web` folder, create the directory structure for the target language:

### Command:
```sh
mkdir -p web/locales/<language_code>/LC_MESSAGES/
```

Example for Bangla:
```sh
mkdir -p web/locales/bn/LC_MESSAGES/
```

---

## **8. Copy Files into Locales**
Run the following command to copy the translated files into the `locales` directory:

### Command:
```sh
make copy_locales
```

---

## **9. Compile MO Files**
Add the newly added language to the list of languages for MO file compilation. Then, run the following command:

### Command:
```sh
make mo
```

---

## **10. Generate JSON Translation Files**
After compiling the PO/MO files, generate a JSON data file for the translations:

### Command:
```sh
make build_lang_json
```

### Parameters:
- `-d`: Path to the data file that contains all words, labels, and phrases used for Yaziji phrase generation.
- `-t`: Path to the directory containing compiled PO/MO files.
- `-o`: Output directory for the generated files.

---

## **11. Copy JSON Translation Files**
Copy the generated JSON translation files, such as `ar.json`, `en.json`, to the correct directory.

### Command:
```sh
make update_lang_json
```

The JSON files will be copied to the `web/static/resources/json/` directory.

---

## **12. Update the Yaziji Web Page**
- Open the `web/templates/index.html` file.
- Add the new language code (`<language_code>`) to the `language_list`.

---

## **13. Verify the Integration**
- Test the application to ensure the new language is visible and functional.
- Verify that the translations display correctly in the user interface.

---

## **Reference: Native Language Names**
For accurate language names and codes, refer to:
[Omniglot Language Names](https://omniglot.com/language/names.htm)
