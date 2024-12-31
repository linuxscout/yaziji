

function get_options()
{
    return {subject: subject.value || "",
        object: document.NewForm.object.value || "",
        verb: document.NewForm.verb.value || "",
        time: document.NewForm.time.value || "",
        place: document.NewForm.place.value || "",
        tense: tense.value || "",
        voice: document.NewForm.voice.value || "",
        auxiliary: document.NewForm.auxiliary.value || "",
        negative: document.NewForm.negative.value || "",
        phrase_type: document.NewForm.phrase_type.value || "",
        adjective: document.NewForm.adjective.value || "",
    };
}


function test_compatibility(options) {
    /**
     * Check if the sentence contains sufficient components (subject, verb, object, etc.).
     * @param {Object} options - The sentence components to check.
     * @return {boolean} - Returns true if the sentence is valid, false otherwise.
     */
    const PASSIVE_VOICE = "مبني للمجهول";
    const ACTIVE_VOICE = "معلوم";
    const VERBAL_PHRASE = "جملة فعلية";
    const NOMINAL_PHRASE = "جملة اسمية";
    const TenseImperative = "الأمر";

    const verb = options.verb || '';
    const subject = options.subject || '';
    const object = options.object || '';
    const place = options.place || '';
    const predicate = options.adjective || '';
    const activeVoice = options.voice === ACTIVE_VOICE;
    const passiveVoice = options.voice === PASSIVE_VOICE;
    const imperative = options.tense === TenseImperative;
    const verbal = options.phrase_type === VERBAL_PHRASE;
    const nominal = options.phrase_type === NOMINAL_PHRASE;

    // Verbal phrase without verb, return false
    if (verbal && !verb) {
        alert("غير صالح: جملة فعلية بدون فعل");
        return false;
    }

    // Nominal phrase without subject, or no subject, but object, within passive voice and verb
    if (nominal && !subject && !object) {
        alert("غير صالح: جملة اسمية بدون اسم (مبتدأ أو مفعول به)");
        return false;
    }

    // Verb without subject or object
    if (verb && !subject && !object) {
        alert("غير صالح: فعل بدون فاعل أو مفعول به");
        return false;
    }

    // Subject not starting with "أنت" and tense is imperative
    if (!subject.startsWith("أنت") && imperative) {
        alert(`غير صالح: فاعل[${subject}] غير متوافق مع زمن الأمر`);
        return false;
    }

    // Active voice without subject
    if (!subject && activeVoice) {
        alert("غير صالح: المبني للمعلوم بدون فاعل");
        return false;
    }

    // Minimal valid sentence: verb + subject
    if (verb && subject) {
        // alert("صالح: جملة فعلية تحتوي على فعل وفاعل");
        return true;
    }

    // Minimal valid nominal phrase: subject + place
    if (subject && place) {
        // alert("صالح: جملة اسمية تحتوي على مبتدأ ومكان");
        return true;
    }

    // Minimal valid nominal phrase: subject + predicate
    if (subject && predicate) {
        // alert("صالح: جملة اسمية تحتوي على مبتدأ وصفة");
        return true;
    }

    // Minimal valid passive sentence: verb + object + passive voice
//    alert(`الموضوع: ${subject}, الفعل: ${verb}, المفعول به: ${object}, الأمر: ${imperative}, المبني للمجهول: ${passiveVoice}`);
    if (!subject && verb && object && !imperative && passiveVoice) {
        // alert("صالح: جملة تحتوي على فعل ومفعول به ومبني للمجهول");
        return true;
    }

    alert("غير صالح: مكونات غير كافية لتكوين جملة مفيدة");
    return false;
}


/**
 * Handles the phrase click event to validate input and send data via AJAX.
 * @param {Event} e - The event object.
 */
const phraseClick = (e) => {
    e.preventDefault();
    options = get_options();
    // test compatiblity between phrase parts input
    if (!test_compatibility(options))
    {return;}


    const prefix = getPrefixPath();
    // Collect form data
    const formData = {
        //text: subject.value || "",
        action: "phrase",
        options :options,
    };

    // Send data via GET request
    $.getJSON(`${prefix}/ajaxGet`, formData, (response) => {
        if (response?.result) {
            $("#result").html(`<div class='tashkeel'>${response.result.phrase}</div>`);
            $("#extra").html(`<div class='tashkeel'>${response.result.phrase_type} <br/>
            ${response.result.inflection}<br/>
            ${response.result.errors}</div>`);
        } else {
            console.error("Unexpected response:", response);
        }
    }).fail((jqXHR, textStatus, errorThrown) => {
        console.error("Error during AJAX request:", textStatus, errorThrown);
        alert("حدث خطأ أثناء إنشاء العبارة. يرجى المحاولة مرة أخرى.");
    });
};



/**
 * Handles the sample click event to validate the form and send data via AJAX.
 * @param {Event} e - The event object.
 */
const sampleClick = (e) => {
    e.preventDefault();

    // Validation: Ensure correct pronoun usage with imperative tense
    const { tense, subject } = document.NewForm;
    if (tense.value === "الأمر" && !subject.value.includes("أنت")) {
        alert(`خطأ في الضمير [${subject.value}] غير متطابق مع التصريف في الأمر`);
        return;
    }

    const prefix = getPrefixPath();

    // Collect form data
    const formData = {
        text: subject.value || "",
        action: "sample",
        options :get_options(),
    };

    // Send data via GET request
    $.getJSON(`${prefix}/ajaxGet`, formData, (response) => {
        if (response?.result) {
            $("#result").html(response.result);
        } else {
            console.error("Unexpected response:", response);
        }
    }).fail((jqXHR, textStatus, errorThrown) => {
        console.error("Error during AJAX request:", textStatus, errorThrown);
        alert("حدث خطأ أثناء تحميل العينة. يرجى المحاولة مرة أخرى.");
    });
};




/**
 * Handles the report click event to send form data via AJAX.
 * @param {Event} e - The event object.
 */
const reportClick = (e) => {
    e.preventDefault();

    const prefix = getPrefixPath();

    // Collect form data
    const formData = {
        text: document.NewForm.subject.value || "",
        action: "report",
        options :get_options(),
        result: $("#result").text() || "",
    };

    // Send data via GET request
    $.getJSON(`${prefix}/ajaxGet`, formData, (response) => {
        if (response?.result) {
            $("#result").html(response.result);
            alert("شكرا لإبلاغنا بالمشكلة.");
        } else {
            console.error("Unexpected response:", response);
        }
    }).fail((jqXHR, textStatus, errorThrown) => {
        console.error("Error during AJAX request:", textStatus, errorThrown);
        alert("حدث خطأ أثناء إرسال التقرير. يرجى المحاولة مرة أخرى.");
    });
};




/**
 * Randomly selects an option from a dropdown by its ID.
 * @param {string} dropdownId - The ID of the dropdown element.
 */
const selectRandomOption = (dropdownId) => {
    const options = $(`${dropdownId} > option`);
    const randomIndex = Math.floor(Math.random() * options.length);
    options.prop('selected', false).eq(randomIndex).prop('selected', true);
};

/**
 * Handles the random selection of options for multiple dropdowns.
 * @param {Event} e - The event object.
 */
const randomSelectClick = (e) => {
    e.preventDefault();

    // List of dropdown IDs to randomize
    const dropdowns = [
        "#verb",
        "#time",
        "#place",
        "#negative",
        "#auxiliary",
        "#phrase_type",
        "#tense",
        "#object",
        "#voice",
        "#subject",
        "#adjective"
    ];

    // Apply random selection to each dropdown
    dropdowns.forEach(selectRandomOption);
};


/**
 * Returns the prefix path based on the current script and language.
 * @returns {string} The prefix path.
 */
const getPrefixPath = () => {
    let lang = getLang() || "ar"; // Default to "ar" if no language is found
    let prefix = script;

    // Append the language to the prefix path
    prefix += `/${lang}`;

    // Debugging logs (uncomment if needed)
    // console.log(`Current script path is: ${prefix}`);
    // console.log(`Caught locale is: ${lang}`);

    return prefix;
};



/**
 * Returns the language parameter from the URL.
 * @returns {string|null} The value of the 'locale' parameter or null if not present.
 */
const getLang = () => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('locale') || "ar";
};

/**
 * Handles the change event for rating input fields.
 * Sends a GET request to submit the selected rating and other form data to the server.
 *
 * @param {Event} e - The event object triggered by the change event.
 *
 * Behavior:
 * - Prevents the default form submission behavior.
 * - Collects data from the form, including the selected rating and additional metadata.
 * - Sends the data via an AJAX GET request to the server.
 * - Updates the result element with the server response.
 * - Displays a thank-you alert upon successful submission.
 */
const ratingChange = function(e) {
    e.preventDefault();

    const prefix = getPrefixPath();
    const rating = $(this).val();
//    console.log("Rating Element:", this, "Rating Value:", rating);
    // Collecting form data
    const formData = {
        text: document.NewForm.subject.value,
        action: "rating",
        options :get_options(),
        result: $("#result").text(),
        rating: `${rating}`
    };

    // Sending data via GET request
    $.getJSON(`${prefix}/ajaxGet`, formData, (data) => {
        $("#result").html(data.result);
        alert("شكرا لتقييم هذه العملية.");
    });
};


const copyToClipboard = (e) => {
    e.preventDefault();

    const resultText = document.getElementById('result').innerText;

    if (navigator.clipboard) {
        // Modern approach using the Clipboard API
        navigator.clipboard.writeText(resultText)
            .then(() => {
                alert("نسخت البيانات في الحافظة.");
            })
            .catch(err => {
                console.error('Failed to copy text: ', err);
            });
    } else {
        // Fallback for older browsers using document.execCommand
        const tempInput = document.createElement('input');
        document.body.appendChild(tempInput);
        tempInput.value = resultText;
        tempInput.select();
        document.execCommand('copy');
        tempInput.remove();

        alert("نسخت البيانات في الحافظة.");
    }
};


//// a class to draw form with translation
//class DrawForm {
//    constructor(language_url) {
//        this.language_url = language_url;
//        this.translations = {};
//    }
//
//    // Load translations from JSON files
//    load_languages() {
//        const lang = getLang();
//        $.ajax({
//            url: `${this.language_url}${lang}.json`,
//            method: 'GET',
//            dataType: 'json',
//            success: (data) => {
//                this.translations[lang] = data;
//                console.log("Translation", data);
//            },
//            error: (xhr, status, error) => {
//                console.error('Error1:', error);
//            }
//        });
//    }
//
//    // Translate label based on the loaded translations
//    translate_label(label, lang) {
//        if (this.translations[lang] && this.translations[lang]["web-labels"]) {
//            return this.translations[lang]["web-labels"][label] || label;  // Fallback to original label if not found
//        }
//        return label;  // Fallback to original label if translations are not available
//    }
//
//    // Translate value based on the loaded translations
//    translate_value(field, key, lang) {
//        return this.translations[lang]?.[field]?.[key] || key;  // Fallback to key if translation is not available
//    }
//
//    // Draw the form with translated values
//    draw_form() {
//        const lang = getLang();
//        const prefix = getPrefixPath();
//
//        $.getJSON(`${prefix}/selectGet`, {
//            text: '',
//            action: "RandomText"
//        }, (data) => {
//            if (!data) {
//                console.log("Nothing from selectGet");
//                return;
//            }
//
//            const selectValues = data;
//            selectValues.fields.forEach(field => {
//
//                const fieldLabel = $(`#${field}_label`);
//                const ar_label = fieldLabel.text();
//                const tr_label = this.translate_label(ar_label, lang);
//
//                if (lang !== "ar") {
//                    fieldLabel.append(`[${tr_label}]`);
//                }
//
//                $.each(selectValues[field], (key, value) => {
//                    const translatedValue = lang !== "ar"
//                        ? `${key} [${this.translate_value(field, key, lang)}]`
//                        : value;
//
//                    $(`#${field}`).append($("<option></option>").attr("value", key).text(translatedValue));
//                });
//            });
//        });
//    }
//}
//


// Object to store translations
let jsontrans = {};

// Load translation file dynamically based on ISO code
async function loadTranslationFile(lang) {
    const fileName = `${language_url}${lang}.json`; // File name based on ISO code
    try {
        const response = await fetch(fileName);
        if (!response.ok) {
            throw new Error(`Error loading ${fileName}: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Failed to load translation file:", error);
        return null; // Return null in case of an error
    }
}

// Select language change event handler
const selectLanguage = function () {
    const lang = this.value;
//    console.log("Selected language:", lang);
    translateUI(lang); // Translate UI elements
};

// Main function to translate UI elements
async function translateUI(lang) {
    // Load the translation for the selected language
    jsontrans[lang] = await loadTranslationFile(lang);

    // If translation is not found, log a warning and exit
    if (!jsontrans[lang]) {
        console.warn(`No translations found for language: ${lang}`);
        return;
    }

    // Translate select options based on loaded translation
    const list = ["phrase_type", "subject", "object", "verb", "time", "place", "tense", "negative", "voice", "auxiliary", "adjective"];
    list.forEach(part => {
        translateSelect(lang, part); // Translate each part
    });
    const listLabel = ["phrase_type_label", "subject_label", "object_label", "verb_label", "time_label",
     "place_label", "tense_label", "negative_label", "voice_label", "auxiliary_label","adjective_label",
     // buttons
     "phrase","random_select", "sample","LastMark_label"];
    listLabel.forEach(part => {
        translateLabel(lang, part);
    });
}

// Function to translate the options of select elements
function translateSelect(lang, part) {
    const partSelect = document.querySelector(`#${part}`);

    // Ensure the select element exists
    if (!partSelect) {
        console.warn(`Select element with ID "${part}" not found.`);
        return;
    }

    // Get the translations for the current part
    const partTranslations = jsontrans[lang][part];

    // Ensure translations exist for the part
    if (!partTranslations) {
        console.warn(`No translations found for part: "${part}" in language: ${lang}`);
        return;
    }

    // Loop through the options and translate their text content
//    console.log("PART select", part, partSelect.length, typeof(partTranslations));
//    console.log("PART select translation", partTranslations);
    // if options are not empty, translate
    // else draw
    if(partSelect.length <= 1)
    {
    Object.keys(partTranslations).forEach(value => {
    const translatedValue = partTranslations[value];

//    console.log("PART select translation-value", value);

    if (lang === "ar") {
        // For Arabic, only display the value (original text)
         $(`#${part}`).append($("<option></option>").attr("value", value).text(value));
    } else {
        // For other languages, display the translated value if available
        if (translatedValue) {
            $(`#${part}`).append($("<option></option>")
                .attr("value", value)
                .text(`${value} [${translatedValue}]`)
                  );
        } else {
           $(`#${part}`).append($("<option></option>").attr("value", value).text(value));
            console.warn(`Translation missing for: ${value}`);
        }
    }
   });

//    Array.from(partTranslations).forEach(value => {
//        const translatedValue =  partTranslations[value]
//        // For Arabic, only display the value
//        console.log("PART select translation-value", value);
//        if (lang === "ar") {
//            partSelect.append($("<option></option>").attr("value", value).text(value));
//        } else {
//            // Translate the option text and append it with the translation
////            if (translatedValue) {
//            partSelect.append($("<option></option>").attr("value", value).text(translatedValue));
////            }
//        }
//    });
    }
    else
    {   // draw instead of translate
//    console.log()
       Array.from(partSelect.options).forEach(option => {
        const value = option.value; // Use the option's value as a key

        // For Arabic, only display the value
        if (lang === "ar") {
            option.textContent = value;
        } else {
            // Translate the option text and append it with the translation
            if (partTranslations[value]) {
                option.textContent = `${value} [${partTranslations[value]}]`;
            }
        }
    });
    }
}

// Function to translate the labels of HTML elements
function translateLabel(lang, part) {
    const partLabel = document.querySelector(`#${part}`);

    // Ensure the label element exists
    if (!partLabel) {
        console.warn(`Label element with ID "${part}" not found.`);
        return;
    }

    // Get the translations for the current part
    const labelTranslations = jsontrans[lang]["web-labels"];
//    console.log("labelTranslations", labelTranslations);

    // Ensure translations exist for the part
    if (!labelTranslations) {
        console.warn(`No translations found for labels in language: ${lang}`);
        return;
    }

    // Access the original label's text (assuming you're using `textContent`)
//    const originalText = partLabel.textContent.trim();  // Text in the label, e.g., "Username"
    const originalText = partLabel.getAttribute('data-original-text');  // Text in the label, e.g., "Username"
//    console.log("Original label text:", originalText);

    // If translation for this label exists in the selected language
    if (labelTranslations[originalText]) {
        const translatedText = labelTranslations[originalText];
//        console.log("Translated label text:", translatedText);

        // Update the label's text content with the translation
                // For Arabic, only display the value
        if (lang === "ar") {
        partLabel.textContent = `${originalText}`;
        }
        else
        {
        partLabel.textContent = `${originalText} [${translatedText}]`;
        }
    } else {
        console.warn(`No translation found for "${originalText}" in language: ${lang}`);
    }
}

// Initialize the app by loading the Arabic translations as default
loadTranslationFile("ar").then(translations => {
    if (translations) {
        jsontrans["ar"] = translations; // Store the Arabic translations
    }
});

function get_lang2()
{
const lang = $("#language").val() || "ar";
//console.log("Get_lang", lang);
return lang;
}
$(document).ready(() => {
    // Initialize the DrawForm instance
//    const myDraw = new DrawForm(language_url);
//    myDraw.load_languages();
//    myDraw.draw_form();
    const lang = get_lang2();
     translateUI(lang);
    if(!CONFIG_DEBUG_MODE)
    { // hide some buttons

    $("#random_select").hide();
    $("#sample").hide();
    }
    // Event bindings
    $(document)
        .on('click', '#phrase', phraseClick)
        .on('click', '#sample', sampleClick)
        .on('click', '#random_select', randomSelectClick)
        .on('click', '#copy', copyToClipboard)
        .on('click', '#signal', reportClick)
        .on('change', '.rating input', ratingChange)
        .on('change', '#language', selectLanguage);

});

