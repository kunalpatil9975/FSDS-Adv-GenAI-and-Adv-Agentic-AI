import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64


# ============================================================
# READ LANGUAGE DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\kunal\Downloads\6th - NLP project\6th - NLP project\MULTIPLE LANGUAGE TRANSLATION\language.csv"
)

df.dropna(inplace=True)

lang = df["name"].tolist()
langlist = tuple(lang)

langcode = df["iso"].tolist()


# ============================================================
# CREATE DICTIONARY
# Language Name -> Language Code
# ============================================================

lang_array = {
    lang[i]: langcode[i]
    for i in range(len(langcode))
}


# ============================================================
# STREAMLIT LAYOUT
# ============================================================

st.title("🌐 Language Translation")

inputtext = st.text_area(
    "Hi! Please enter text here to translate",
    height=100
)


# ============================================================
# SELECT LANGUAGE
# ============================================================

choice = st.sidebar.radio(
    "SELECT LANGUAGE",
    langlist
)


# ============================================================
# TEXT-TO-SPEECH SUPPORTED LANGUAGES
# ============================================================

speech_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese",
    "or": "Odia"
}


# ============================================================
# AUDIO DOWNLOAD FUNCTION
# ============================================================

def get_binary_file_downloader_html(
    bin_file,
    file_label="File"
):

    with open(bin_file, "rb") as f:
        data = f.read()

    bin_str = base64.b64encode(data).decode()

    href = (
        f'<a href="data:audio/mp3;base64,{bin_str}" '
        f'download="{bin_file}">'
        f'📥 Download {file_label}'
        f'</a>'
    )

    return href


# ============================================================
# CREATE COLUMNS
# ============================================================

c1, c2 = st.columns([4, 3])


# ============================================================
# TRANSLATION
# ============================================================

if len(inputtext) > 0:

    try:

        # Get selected language code
        selected_lang_code = lang_array[choice]

        # Translate text
        output = translate(
            inputtext,
            selected_lang_code
        )

        # ----------------------------------------------------
        # DISPLAY TRANSLATED TEXT
        # ----------------------------------------------------

        with c1:

            st.text_area(
                "TRANSLATED TEXT",
                output,
                height=200
            )


        # ----------------------------------------------------
        # TEXT TO SPEECH
        # ----------------------------------------------------

        if selected_lang_code in speech_langs:

            with c2:

                audio_file = gTTS(
                    text=output,
                    lang=selected_lang_code,
                    slow=False
                )

                audio_file.save("lang.mp3")


                # Read audio
                with open("lang.mp3", "rb") as audio_file_read:

                    audio_bytes = audio_file_read.read()


                # Play audio
                st.audio(
                    audio_bytes,
                    format="audio/mp3"
                )


                # Download audio
                st.markdown(
                    get_binary_file_downloader_html(
                        "lang.mp3",
                        "Audio File"
                    ),
                    unsafe_allow_html=True
                )

    except Exception as e:

        st.error(f"Error: {e}")