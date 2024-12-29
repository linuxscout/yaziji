# **API Documentation for Yaziji: Arabic Sentence Generator**

## **Overview**

The Yaziji API provides endpoints for dynamically generating Arabic sentences. It is designed to support sentence generation and future features like inflection (`إعراب`). The backend is implemented using Flask, with support for AJAX requests for seamless interaction with the provided HTML interface.

The Yaziji-web frontend provides a user-friendly interface for interacting with the API. It allows users to generate sentences, select linguistic elements, and explore Arabic grammar dynamically.

------

## **Base URL**

```
http://127.0.0.1:5000/
```

------

## **Endpoints**

### 1. `/ajaxGet`

#### **Description**

Handles AJAX requests for generating sentences, performing actions, or retrieving random text.

#### **Methods**

- `POST`
- `GET`

#### **Parameters**

| **Parameter**      | **Type** | **Description**                                              |
| ------------------ | -------- | ------------------------------------------------------------ |
| `lang`             | String   | The language code (default: `ar`).                           |
| `text`             | String   | Input text for processing (optional).                        |
| `action`           | String   | Action to perform (`phrase`, `randomtext`, `sample`, `rating`). |
| `response_type`    | String   | Type of response (`get_random_text`).                        |
| Additional Options | JSON     | Extra parameters depending on the action.                    |

#### **Actions**

- **`phrase`**: Generates a fully diacritized Arabic sentence (e.g., جملة عربية مشكولة).
- **`randomtext`**: Returns a random Arabic text.
- **`sample`**: Generates a JSON sample for debugging purposes.
- **`report`**: Logs an issue with a generated sentence.
- **`rating`**: Records a user rating for a generated sentence.

#### **Example Request**

```http
POST /ajaxGet
Content-Type: application/json

{
  "text": "",
  "action": "phrase",
  "options": {
    "subject": "أنا",
    "verb": "أكتب",
    "tense": "الماضي"
  }
}
```

#### **Example Response**

```json
{
  "result": "أنا كتبت.",
  "order": 0
}
```

------

### **Build a Phrase with Given Inputs**

#### **Example Request**

```
GET /en/ajaxGet?text=فَرَاشَةٌ&action=phrase&subject=فَرَاشَةٌ&verb=لَعِبَ&time=بَعْدَ غَدٍ&tense=المضارع المعلوم&voice=معلوم&auxiliary=كَادَ&negative=مثبت&phrase_type=جملة فعلية
```

#### **Example Response**

```json
{
  "order": 0,
  "result": "يَكَادُ الْفَرَاشَةُ أَنْ يَلْعَبَ بَعْدَ غَدٍ[جملة فعلية]"
}
```

------

### 2. `/selectGet`

#### **Description**

Returns JSON data for populating dropdown values in the sentence generation form.

#### **Methods**

- `POST`
- `GET`

#### **Parameters**

| **Parameter** | **Type** | **Description**                    |
| ------------- | -------- | ---------------------------------- |
| `lang`        | String   | The language code (default: `ar`). |

#### **Example Request**

```
GET /selectGet
```

#### **Example Response**

```json
{
   "fields": ["subject", "verb", "auxiliary", "tense", "voice", "negative", "object", "time", "place", "phrase_type"],
   "web-labels": {
      "الاستضافة بدعم من شركة": "Supported by",
      "بناء": "Build",
      "جملة اسمية": "Nominal Phrase",
      "جملة فعلية": "Verbal phrase"
   },
   "auxiliary": {
      "أَرَادَ": "Want",
      "اِسْتَطَاعَ": "Can",
      "كَادَ": "May"
   },
   "verb": {
      "أَخَذَ": "to take",
      "أَخْبَرَ": "to tell"
   },
   "subject": {
      "أنا": "I",
      "أَحْمَدُ": "Ahmed"
   }
}
```

#### **Key Explanation**

- **`fields`**: Input field names used in the form.
- **`web-labels`**: Translated strings for frontend display.
- **Other Fields (e.g., `verb`, `subject`)**: Provide a list of values for respective dropdown fields.

------

### 3. **Static Files**

#### **Description**

Serves static assets like CSS, JavaScript, and images.

#### **URL Pattern**

```
/static/<path-to-static-file>
```

#### **Example**

- CSS: `/static/resources/files/adawatstyle.css`
- JS: `/static/resources/files/adawat.js`
- Images: `/static/resources/files/logo.png`

------

## **Configuration**

- **Logging**: Logs are written to the file specified in the configuration (`LOGGING_FILE`).
- **Debug Mode**: Controlled via the `MODE_DEBUG` setting in the configuration.

------

## **Notes**

- Ensure correct permissions for log files.
- Use UTF-8 encoding for compatibility with Arabic text.
- For extended functionalities, update the `Adaat` class in the backend.
