# **Documentation: Development  Yaziji**

## **Project Overview**

**Yaziji** is a web-based tool designed to help beginner learners of Arabic (especially foreign language learners) construct well-structured Arabic phrases with full diacritics. It aims to simplify the learning process by providing an interactive platform for phrase generation and grammatical guidance.

Yaziji uses Python Flask as its backend framework. The project consists of two main components:

1. **Web Interface**: The front-end interface that interacts with users.
2. **Core Yaziji**: The back-end core responsible for processing phrase generation and grammar logic.

## Key Features

- **Phrase Generator**: Helps users construct grammatically correct Arabic phrases with full diacritics.
- **Localization**: Designed to assist in teaching Arabic to non-native speakers, Yaziji supports multiple languages and provides localization features to cater to a wider user base.
- **License**:  Yaziji is licensed under the GNU GPL License. Feel free to contribute and modify the project as needed!

## Usage Instructions

### 1. **Setting Up the Environment**

- Install dependencies from `requirements.txt`.
- Configure the environment using files in the **`config/`** directory (if applicable).

### 2. **Adding a New Language**

- Follow the **Translation Guide** for adding new languages.
- Language files are stored as JSON in the **`static/resources/json`** directory for use in the web project.

### 3. **Customizing the Interface**

- Modify HTML templates in the **`templates/`** directory.
- Update static resources (CSS, images, etc.) in the **`static/`** directory as needed.

## Getting Started with Yaziji

To get started with Yaziji development, follow these steps:

1. #### **Set up the Development Environment**

- Install the required dependencies for Yaziji, including Python libraries and system dependencies.
- Install the necessary tools for data conversion and translation management by running the utility scripts in the **`tools/`** directory.
- Configure the environment using files in the **`config/`** directory (if applicable).

2. #### **Understand the Core Workflow**

The core workflow of Yaziji involves generating phrases based on predefined patterns and word relationships. Familiarize yourself with the key modules:

- **`phrase_generator.py`**: Coordinates the phrase generation process.
- **`phrase_pattern.py`** and **`stream_pattern.py`**: Define and handle phrase patterns.
- **`wordnode.py`**: Manages individual words and their relationships in the phrase generation system.
- **`data/`**: Contains the main data used by Yaziji, including word attributes and relationships.

3. **Setting Up Translation Support**

To add support for new languages:

- Refer to the **Translation Guide** for details on adding languages.
- The web project uses language JSON files stored in the **`static/resources/json`** directory.
- Use the **`data_to_translate_csv.py`** and **`translate_json_from_po.py`** scripts to convert translation data and integrate it into the system.

4. **Testing the Application**

- Run unit tests located in the **`tests/`** directory to ensure the system behaves as expected.
- Debug issues using logs from the **`logs/`** directory.
- Modify or add new tests if necessary, following the structure used in the test files.

5. **Contribute to the Codebase**

- Fork the repository or create a local branch for development.
- Modify or add new components as necessary, ensuring that all new code follows the coding style and guidelines.
- Run tests to validate your changes.
- Submit pull requests for code reviews and integration into the main codebase.

------

## Future Enhancements

- Add support for more languages and translation files.
- Improve database performance with advanced indexing.
- Enhance the user interface for better accessibility and user experience.

## Additional Resources

- **API Documentation**: For detailed information on the internal API and class references, check the API documentation in the **`docs/`** directory.
- **Translation Guide**: For guidance on managing translations in Yaziji, refer to the Translation guide in the **`docs/`** directory.

---

## ** Project Directory Structure**

Below is the directory structure of the Yaziji project, along with a description of each component:

```
├── yaziji
│   ├── data
│   │   └── data.json
│   ├── phrase_generator.py
│   ├── phrase_pattern.py
│   ├── stream_pattern.py
│   ├── wordnode.py
│   ├── components_set.py
│   ├── worddictionary.py
│   ├── validator.py
│   ├── inflector.py
│   ├── error_listener.py
│   ├── yaziji_const.py
│   └── yz_utils.py
├── data-source
│   └── yaziji-data_features.ods
├── tools
│   ├── data_to_json.py
│   ├── data_to_translate_csv.py
│   ├── translate_json_from_po.py
│   ├── get_json_lang_from_server.py
│   ├── generate_features_sample.py
│   └── convert_list.py
├── translations
│   ├── existing.pot
│   ├── main.pot
│   ├── work/*.csv
│   └── ...
├── tests
├── web
├── web-frontend
│   ├── index.html
│   └── resources 
├── wsgi.py
└── yaziji.cgi
```

---



## Yaziji Core Directory and File Descriptions

The **Yaziji** project is organized into several core directories and files, each serving a specific purpose in the phrase generation and translation pipeline.

Main **Core Yaziji Components**

- **`yaziji/`**: Core logic for phrase generation, including grammar rules and error handling.

- **`data-source/`**: Contains raw data and feature definitions for phrase generation. This data contains:

  - List of fields and their word values
  - A dictionary of words attributes used to build phrases.
  - Labels and features to use and translate
  - A dictionary of words' relationships

- **`docs/`**: Documentation files, including API references, development notes and translation guide.

- **`tools/`**: Utility scripts for data conversion and translation management.

  

  ### Details 

#### 1. **`yaziji/`** - Core Logic

The `yaziji/` directory contains the main components responsible for generating phrases, handling grammar rules, and managing errors. Below are the key files in this directory:

- **`data/`**: Contains raw data files used for phrase generation, including word values, feature definitions, and relationships.
- **`phrase_generator.py`**: Central module that coordinates the phrase generation process. It uses patterns and word attributes to generate meaningful phrases.
- **`phrase_pattern.py`**: Manages the definition of phrase patterns, specifying how different word categories can be combined to form valid phrases.
- **`stream_pattern.py`**: Handles word stream processing, ensuring words are combined in the correct order according to grammar rules.
- **`wordnode.py`**: Implements the **WordNode** class, which represents individual words or word components. Each word can have multiple attributes and relationships with other words in a phrase.
- **`components_set.py`**: Manages sets of available components (word types, attributes, etc.) for use in phrase generation.
- **`worddictionary.py`**: Manage words informations and attributes, data structure, word semantic fields.
- **`validator.py`**: is a comprehensive utility for validating and ensuring the grammatical correctness and semantic compatibility of Arabic phrases input parts. This class leverages predefined rules to perform various checks on sentence components.
- **`inflector.py`**:  class which generate إعراب Arabic word inflection for phrase generated by `phrase_generator`.
- **`error_listener.py`**: Listens for errors during the phrase generation process, logging and reporting issues that occur.
- **`yaziji_const.py`**: Contains constant values, configuration settings, and default parameters used throughout the Yaziji system.
- **`yz_utils.py`**: Provides utility functions for common tasks such as data manipulation, transformations, and other helper operations.

#### 2. **`data-source/`** - Data Files

This directory contains data sources used for phrase generation:

- **`yaziji-data_features.ods`**: Contains feature definitions and relationships between words. It contains raw data, including words and their attributes.
- This spread sheet is organized as sheets:
  - **`words`**:  a list of phrase components (like verb, subject, object,), with their word values
  - **`features`**:  a list of phrase features like (phrase_type, tense, affirmative, tense voice) , with their predefined values like (phrase_type [verbal, nominal], voice[active, passive], tense[par, present, imperative])
  - **`relationships`**:  a list of configuration and relationships between words, for example:
    - acceptable verb and subject tuples, for example: (أكل، الولد, valid), (أكل، طاولة، invalid)
    - acceptable verb and object tuples, for example: (أكل، الطعام, valid), (أكل، طاولة، invalid)
    - Verb and place connection, for example: (أكل, في), (سافر، إلى)
  - **`labels`**:  a list of labels used in interface, to be translated.

#### 3. **`tools/`** - Utility Scripts

The `tools/` directory holds several scripts used for data conversion, language handling, and translation management. Some important scripts include:

- **`data_to_json.py`**: This script is used to build a JSON file containing a dictionary of data for the phrase generator. The resulting JSON file serves multiple purposes, including:

  - Storing **word attributes**, **phrase components features**, and **fields** required for phrase generation.
  - Generating a **"data" structure** (components and their values) that can be used in the user interface without directly modifying the core data.
  - The output JSON file will be used by the **`PhraseGenerator`** class as a dictionary to facilitate phrase generation.
  - It allows you to use the data in the **web API** or other interfaces, ensuring that the core data remains unaltered.

  Parameters:

  - **Input file**: The input data file contains all the necessary words, labels, and components used for Yaziji phrase generation.
  - **Output file**: Specifies the file path for the resulting JSON file.

- **`data_to_translate_csv.py`**: This script is used to generate a CSV file that contains the data required for translation. The resulting CSV file is designed for contributors who prefer working with spreadsheets (such as Excel or Google Docs) to handle the translation process.

  The CSV file will include: **Arabic words** and corresponding **translation fields**. Any additional properties needed specifically for translation purposes.

  Parameters:

  - **Input file**: The input data file contains all the necessary words, labels, and components used for Yaziji phrase generation. 

    The used part is  **"data"** which set (components and their values) that can be utilized in the user interface for translation work.

  - **Output file**: Specifies the file path for the resulting CSV file, formatted for translation purposes.

  

- **`translate_json_from_po.py`**: This script is used to generate a JSON file based on translations from **PO/MO compiled files**. It extracts the translations and applies them to the corresponding data structure for use in the Yaziji phrase generation system.

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

    

- **``generate_features_sample.py``**: A script that generates a sample dataset for features list, used to test ``validator.py``.

- **`get_json_lang_from_server.py`**: This script to generate json lang file by calling yaziji server, It uses babel flask

  > [!WARNING]
  >
  > to be removed

- **`convert_list.py`**: Converts line text to list to be used on building data.

  > [!WARNING]
  >
  > to be removed

  

#### 4. **`translations/`** - Translation Files

This directory contains files for translation management, including:

- **`existing.pot`**: Template file for existing translations.

- **`main.pot`**: The main template file for translations.

- **`ar/main_ar.po, en/main_en.po`**:  po files

- **``work``**: contains csv and excel source files.

  > [!NOTE]
  >
  > For more details on translation please refer to [Translation Guide](translation_guide.md)

  

#### 5. **`web/`** (API) and **`web-frontend/`**

* The `web/` directory: directory contains files related to the web API of the Yaziji project, based on Flask.
* The web-frontend/` directory contains files related to the web interface of the Yaziji project, including HTML files and resources needed for the frontend interface.

#### 6. **`wsgi.py` and `yaziji.cgi`**

These files are used for deploying the Yaziji web interface using WSGI (Web Server Gateway Interface) and CGI (Common Gateway Interface) protocols.

### **Web API Directory and File Descriptions**

The web Yaziji  contains the web api interface to use yaziji,:

```
web
├── yaziji_webserver.py
├── adaat.py
├── babel.cfg
├── data
│   ├── data_const.py
│   ├── data.json
│   └── rating.db
├── db_manager
│   ├── db_mongo.py
│   ├── db_sqlite.py
│   └── db_tool.py
├── config
│   ├── __init__.py
│   ├── languages.py
│   ├── logging.cfg
│   └── yaziji_config.py
├── locales
│   ├── ar
│   ├── en
│   ├── main.po
│   └── ...
├── logs
│   └── demo.log
├── requirements.txt
├── static
│   └── resources
├── templates
│   ├── index.html
│   └── 404.html
└── tests
    ├── test_flask.py
    └── test_babel.py
```

---

**1. yaziji\_webserver.py** Main web server script for running the Yaziji application. Implements Flask routes and handles user interactions.

it call **`adaat.py`** to run requested actions.

 **2. adaat.py** Contains helper functions and utilities given by the web interface, it relay the code and the backend.

For more details Refer to [API Guide](api.md)

**3. config/** Configuration files and scripts for the application.

- **`yaziji_config.py`**: Core application settings and configurations.
- **`logging.cfg`**: Configuration for logging system behavior and errors.
- **`languages.py`**:  A list of languages and their native names.

**4. data/** Stores data and constants used by the application.

- **`data_const.py`**: Contains predefined data structure to be used by the web interface. It contains the main data displayed on the web page:
  - Fields and their word values,
  - Interface labels

- **`data.json`**: JSON file containing  It contains the main data displayed on the web page:
  - Mainly contains word index of word attributes:
    - noun (gender, number, defined, ...)
    - verb (transitive, future mark)
  - Fields and their word values,
  - Interface labels
  - **N.B.** This data json, called in `adaat.py` to replace default `phrase_generator` database.
- **`rating.db`**: Database file used to store and manage user ratings and feedback.

**5. db\_manager/** A package to handle database operations and interactions.

- **`db_tool.py`** : Helper functions for database management.

- **`db_sqlite.py`**: SQLite database integration.

- **`db_mongo.py`**: MongoDB database integration. 

  > [!NOTE]
  >
  > Not implemented

  

**6. locales/** Directory for localization files. To add translation, please refer to ["How to translate guide"](translation_guide.md).

> [!Note]
>
> The locales for web project are changed to be json files located in **web front end** : **`static/resources/json`**

- **`ar/, en/, zh/`**, : Language files.
- **`main.po`**: Primary template file for translations.
- **`static/resources/json`**: Directory for localization files.

**7. static/** Directory for static assets (e.g., JavaScript, CSS, and images).

- **`resources/`**: Folder for resource files used in the web interface.

- **`resources/json`**: Directory for localization files.

  > [!NOTE]
  >
  > Used here for test only, The concrete resources are in web frontend directory

  

**8. templates/** HTML templates for the web application.

- **`index.html`**: Main landing page of the application.

- **`400.html, 404.html, 500.html`**, : Custom error pages for bad requests, not found errors, server errors.

- > [!NOTE]
  >
  > Used here for test only, The concrete resources are in web frontend directory

**9. tests/** Directory for testing scripts and related files.

- **`test_flask.py`**: Tests for Flask routes and views.

- **`test_babel.py`**: Tests for the Babel translation system.

- > [!warning]
  >
  > To be removed later

**10. logs/** Contains log files for debugging and monitoring. 

**11. requirements.txt** Lists all dependencies and libraries required for the web project.

### **Web Front  End Directory and File Descriptions**

**1. static/** Directory for static assets (e.g., JavaScript, CSS, and images).

- **`resources/`**: Folder for resource files used in the web interface.
- **`resources/json`**: Directory for localization files.

