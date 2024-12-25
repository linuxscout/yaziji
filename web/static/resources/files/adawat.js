


/**
 * Handles the phrase click event to validate input and send data via AJAX.
 * @param {Event} e - The event object.
 */
const phraseClick = (e) => {
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
        //text: subject.value || "",
        action: "phrase",
        subject: subject.value || "",
        object: document.NewForm.object.value || "",
        verb: document.NewForm.verb.value || "",
        time: document.NewForm.time.value || "",
        place: document.NewForm.place.value || "",
        tense: tense.value || "",
        voice: document.NewForm.voice.value || "",
        auxiliary: document.NewForm.auxiliary.value || "",
        negative: document.NewForm.negative.value || "",
        phrase_type: document.NewForm.phrase_type.value || "",
    };

    // Send data via GET request
    $.getJSON(`${prefix}/ajaxGet`, formData, (response) => {
        if (response?.result) {
            $("#result").html(`<div class='tashkeel'>${response.result}</div>`);
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
        subject: subject.value || "",
        object: document.NewForm.object.value || "",
        verb: document.NewForm.verb.value || "",
        time: document.NewForm.time.value || "",
        place: document.NewForm.place.value || "",
        tense: tense.value || "",
        voice: document.NewForm.voice.value || "",
        auxiliary: document.NewForm.auxiliary.value || "",
        negative: document.NewForm.negative.value || "",
        phrase_type: document.NewForm.phrase_type.value || "",
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
        subject: document.NewForm.subject.value || "",
        object: document.NewForm.object.value || "",
        verb: document.NewForm.verb.value || "",
        time: document.NewForm.time.value || "",
        place: document.NewForm.place.value || "",
        tense: document.NewForm.tense.value || "",
        voice: document.NewForm.voice.value || "",
        auxiliary: document.NewForm.auxiliary.value || "",
        negative: document.NewForm.negative.value || "",
        phrase_type: document.NewForm.phrase_type.value || "",
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
        "#voice",
        "#subject"
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
    console.log("Rating Element:", this, "Rating Value:", rating);
    // Collecting form data
    const formData = {
        text: document.NewForm.subject.value,
        action: "rating",
        subject: document.NewForm.subject.value,
        object: document.NewForm.object.value,
        verb: document.NewForm.verb.value,
        time: document.NewForm.time.value,
        place: document.NewForm.place.value,
        tense: document.NewForm.tense.value,
        voice: document.NewForm.voice.value,
        auxiliary: document.NewForm.auxiliary.value,
        negative: document.NewForm.negative.value,
        phrase_type: document.NewForm.phrase_type.value,
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


// a class to draw form with translation
class DrawForm {
    constructor(language_url) {
        this.language_url = language_url;
        this.translations = {};
    }

    // Load translations from JSON files
    load_languages() {
        const lang = getLang();
        $.ajax({
            url: `${this.language_url}${lang}.json`,
            method: 'GET',
            dataType: 'json',
            success: (data) => {
                this.translations[lang] = data;
                console.log("Translation", data);
            },
            error: (xhr, status, error) => {
                console.error('Error1:', error);
            }
        });
    }

    // Translate label based on the loaded translations
    translate_label(label, lang) {
        if (this.translations[lang] && this.translations[lang]["web-labels"]) {
            return this.translations[lang]["web-labels"][label] || label;  // Fallback to original label if not found
        }
        return label;  // Fallback to original label if translations are not available
    }

    // Translate value based on the loaded translations
    translate_value(field, key, lang) {
        return this.translations[lang]?.[field]?.[key] || key;  // Fallback to key if translation is not available
    }

    // Draw the form with translated values
    draw() {
        const lang = getLang();
        const prefix = getPrefixPath();

        $.getJSON(`${prefix}/selectGet`, {
            text: '',
            action: "RandomText"
        }, (data) => {
            if (!data) {
                console.log("Nothing from selectGet");
                return;
            }

            const selectValues = data;

            selectValues.fields.forEach(field => {
                const fieldLabel = $(`#${field}_label`);
                const ar_label = fieldLabel.text();
                const tr_label = this.translate_label(ar_label, lang);

                if (lang !== "ar") {
                    fieldLabel.append(`[${tr_label}]`);
                }

                $.each(selectValues[field], (key, value) => {
                    const translatedValue = lang !== "ar"
                        ? `${key} [${this.translate_value(field, key, lang)}]`
                        : value;

                    $(`#${field}`).append($("<option></option>").attr("value", key).text(translatedValue));
                });
            });
        });
    }
}

$(document).ready(() => {
    // Initialize the DrawForm instance
    const myDraw = new DrawForm(language_url);
    myDraw.load_languages();
    myDraw.draw();

    // Event bindings
    $(document)
        .on('click', '#phrase', phraseClick)
        .on('click', '#sample', sampleClick)
        .on('click', '#random_select', randomSelectClick)
        .on('click', '#copy', copyToClipboard)
        .on('click', '#signal', reportClick)
        .on('change', '.rating input', ratingChange);
});

