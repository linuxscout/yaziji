

//var random_click = function(e) {
//    e.preventDefault()
//    $.getJSON(script + "/ajaxGet", {
//      text: '',
//      action: "RandomText"
//    }, function(data) {
//      if (data) document.NewForm.InputText.value = data.result;
//      else document.NewForm.InputText.value = "TZA";
//    });
//  }


//var csv2data_click = function(e) {
//        e.preventDefault()
//    $.getJSON(script + ")s/ajaxGet", {
//      text: document.NewForm.InputText.value,
//      action: "CsvToData"
//    }, function(d) {
//      $("#result").html("<pre>" + d.result + "</pre>");
//      //"#result").text(d.time);
//    });
//  }





//----------Tabs----------------------
//var more_click = function(e) {
//      e.preventDefault()
//    $("#moresection").slideToggle();
//  }

//  var vocalize_group_click = function(e) {
//        e.preventDefault()
//    $("#vocalizesection").slideToggle();
//    $("#moresection").hide();
//  }

  //copy result into clipboard
//  var copy_click = function(e) {
//        e.preventDefault()
//    $(".txkl").change();
//    var $temp = $("<input>");
//    $("body").append($temp);
//    $temp.val($("#result").text()).select();
//    document.execCommand("copy");
//    $temp.remove();
//    //document.NewForm.InputText.value = $("#result").text();
//  }


//    var phrase_click = function(e) {
//        e.preventDefault()
//    if((document.NewForm.tense.value == "الأمر")&&(document.NewForm.subject.value.indexOf("أنت") == -1))
//     {
//         alert("خطأ في الضمير ["+document.NewForm.subject.value+"] غير متطابق مع التصريف في الأمر");
//     return  0;
//     }
//    var prefix = getPrefixPath();
//    //console.log("phrase_click:"+prefix+"/ajaxGet")
//    $.getJSON(prefix+ "/ajaxGet", {
//
//      text: document.NewForm.subject.value,
//      action: "phrase",
//      "subject":document.NewForm.subject.value,
//      "object":document.NewForm.object.value,
//      "verb":document.NewForm.verb.value,
//      "time":document.NewForm.time.value,
//      "place":document.NewForm.place.value,
//      "tense":document.NewForm.tense.value,
//      "voice":document.NewForm.voice.value,
//      "auxiliary":document.NewForm.auxiliary.value,
//      "negative":document.NewForm.negative.value,
//      "phrase_type":document.NewForm.phrase_type.value,
//    }, function(d) {
//      $("#result").html("<div class=\'tashkeel\'>" + d.result + "</div>");
//
//    });
//  }

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
        text: subject.value || "",
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


//    var sample_click = function(e) {
//        e.preventDefault()
//    if((document.NewForm.tense.value == "الأمر")&&(document.NewForm.subject.value.indexOf("أنت") == -1))
//     {
//         alert("خطأ في الضمير ["+document.NewForm.subject.value+"] غير متطابق مع التصريف في الأمر");
//     return  0;
//     }
//     var prefix = getPrefixPath();
//     //~ var prefix = script;
//    $.getJSON(prefix+ "/ajaxGet", {
//      text: document.NewForm.subject.value,
//      action: "sample",
//      "subject":document.NewForm.subject.value,
//      "object":document.NewForm.object.value,
//      "verb":document.NewForm.verb.value,
//      "time":document.NewForm.time.value,
//      "place":document.NewForm.place.value,
//      "tense":document.NewForm.tense.value,
//      "voice":document.NewForm.voice.value,
//      "auxiliary":document.NewForm.auxiliary.value,
//      "negative":document.NewForm.negative.value,
//      "phrase_type":document.NewForm.phrase_type.value,
//    }, function(d) {
//      $("#result").html( d.result);
//
//    });
//  }

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



//    var report_click = function(e) {
//        e.preventDefault()
//     var prefix = getPrefixPath();
//     //~ var prefix = script;
//    $.getJSON(prefix+ "/ajaxGet", {
//      text: document.NewForm.subject.value,
//      action: "report",
//      "subject":document.NewForm.subject.value,
//      "object":document.NewForm.object.value,
//      "verb":document.NewForm.verb.value,
//      "time":document.NewForm.time.value,
//      "place":document.NewForm.place.value,
//      "tense":document.NewForm.tense.value,
//      "voice":document.NewForm.voice.value,
//      "auxiliary":document.NewForm.auxiliary.value,
//      "negative":document.NewForm.negative.value,
//      "phrase_type":document.NewForm.phrase_type.value,
//      "result":$("#result").text(),
//    }, function(d) {
//      $("#result").html(d.result);
//    alert("شكرا لإبلاغنا بالمشكلة..");
//    });
//  }


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



//    var random_select_click = function(e) {
//        e.preventDefault()
//    var item;
//    // verb
//    var options = $("#verb > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#verb > option").attr('selected',false).eq(random).attr('selected',true);
//
//    // time
//    var options = $("#time > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#time > option").attr('selected',false).eq(random).attr('selected',true);
//    // place
//    var options = $("#place > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#place > option").attr('selected',false).eq(random).attr('selected',true);
//    // negative
//    var options = $("#negative > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#negative > option").attr('selected',false).eq(random).attr('selected',true);
//    // auxiliary
//    var options = $("#auxiliary > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#auxiliary > option").attr('selected',false).eq(random).attr('selected',true);
//    // phrase_type
//    var options = $("#phrase_type > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#phrase_type > option").attr('selected',false).eq(random).attr('selected',true);
//      // tense
//    var options = $("#tense > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#tense > option").attr('selected',false).eq(random).attr('selected',true);
//    // voice
//    var options = $("#voice > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#voice > option").attr('selected',false).eq(random).attr('selected',true);
//    // subject
//    var options = $("#subject > option");
//    var random = Math.floor(options.length * (Math.random() % 1));
//    $("#subject > option").attr('selected',false).eq(random).attr('selected',true);
//  }

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

/*
 * Return prerfix path according to  acutal script and language
 * */
//function getPrefixPath()
//{
//    //~ return script;
//var lang = getLang();
//var prefix = script;
//if(!lang) lang = "ar";
//// generate prefix path
//prefix +="/"+lang;
////console.log("current script path is: "+prefix)
////console.log("catched locale is: "+lang)
//return prefix;
//}

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


///*
// * Return language param
// * */
//function getLang()
//{
//const urlParams = new URLSearchParams(window.location.search);
//var lang = urlParams.get('locale');
//return lang;
//}

/**
 * Returns the language parameter from the URL.
 * @returns {string|null} The value of the 'locale' parameter or null if not present.
 */
const getLang = () => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('locale') || "ar";
};

//// load translations from json files
//function load_languages(url){
//var lang = getLang();
//
//    var translations={}
//    $.ajax({
//    url: url+lang+".json", // Path to the JSON file
//    method: 'GET',
//    dataType: 'json',
//    success: function (data) {
//    translations[lang]=data;
//    console.log("Translation",data);
//    },
//    error: function (xhr, status, error) {
//    console.error('Error1:', error);
//    }
//    });
//    return translations;
//}
//
//
//function translate_label(label, lang)
//{
//console.log("Translation inside function translate_label", translations)
//return translations[lang]["web-labels"][label];
//}
//
//function translate_value(field, key, lang)
//{
//return translations[lang][field][key];
//}
//
//
//function draw(){
//// this function call /selectget api to get data to be display on fields Select inputs
//// this fields are translated into target language
//// fill all select fields from translated strings
//// fill select fields
//// Catche the current locale
//
//var lang = getLang();
//var prefix = getPrefixPath();
//
////if(!lang || lang === "ar")
////    $("#NewForm").css("direction", "rtl");
////else
////    $("#NewForm").css("direction", "ltr");
////console.log("Select get :"+prefix+"/selectGet")
////console.log("Translate :"+translations);
//
//   $.getJSON(prefix+"/selectGet", {
//      text: '',
//      action: "RandomText"
//    }, function(data) {
//
//      if (!data) console.log("No thing, from selectGet");
//      else
//      {
//      //console.log(data);
//        var selectValues = data;
////    console.log("SELECT Values" + selectValues);
////      console.log("SELECT Values fields" + selectValues.fields);
//     for (x in selectValues.fields)
//        {
//        var field = selectValues.fields[x];
//        //console.log("field", selectValues.fields[x], field);
//        // show translation
//        if(lang != "ar")
//        {
//        var ar_label = $('#'+field+"_label").text();
//        var tr_label =  translate_label(ar_label, lang);
//        //console.log("ar_label", ar_label,"tr",tr_label, selectValues["web-labels"]);
//        $('#'+field+"_label").append("["+tr_label+"]");
//        }
//        // translate values
//        $.each(selectValues[field], function(key, value) {
//        if(lang != "ar")
//        {
//        var arabic_translated = key +"  ["+translate_value(field,key, lang)+"]";
//        $('#'+field).append($("<option></option>").attr("value", key).text(arabic_translated));
//        }
//        else
//        {$('#'+field).append($("<option></option>").attr("value", key).text(value));}
//        });
//        }
//
//       }
//    });
//
//
//}

//const rating_change = function(e) {
//        e.preventDefault()
//     const prefix = getPrefixPath();
//       const rating = $(this).val();
//      //~ var prefix = script;
//      const fromdata= {
//      text: document.NewForm.subject.value,
//      action: "rating",
//      "subject":document.NewForm.subject.value,
//      "object":document.NewForm.object.value,
//      "verb":document.NewForm.verb.value,
//      "time":document.NewForm.time.value,
//      "place":document.NewForm.place.value,
//      "tense":document.NewForm.tense.value,
//      "voice":document.NewForm.voice.value,
//      "auxiliary":document.NewForm.auxiliary.value,
//      "negative":document.NewForm.negative.value,
//      "phrase_type":document.NewForm.phrase_type.value,
//      "result":$("#result").text(),
//      "rating":`${rating}`,
//    }
//    $.getJSON(prefix+ "/ajaxGet", fromdata, function(d) {
//      $("#result").html(d.result);
//    alert("شكرا لتقييم هذه العملية.");
//    });
//  }
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


////copy result into clipboard
//  var copy_click = function(e) {
//        e.preventDefault()
//    var $temp = $("<input>");
//    $("body").append($temp);
//    $temp.val($("#result").text()).select();
//    document.execCommand("copy");
//    $temp.remove();
//    alert("نسخت البيانات في الحافظة.");
//    //document.NewForm.InputText.value = $("#result").text();
//  }
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

