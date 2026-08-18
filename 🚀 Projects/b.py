import streamlit as st
from mtranslate import translate
from gtts import gTTS
import pandas as pd
import base64
import os


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8fbff 0%,
            #eef5ff 50%,
            #ffffff 100%
        );
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-left: 5%;
        padding-right: 5%;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #1f3c88;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #64748b;
        margin-bottom: 30px;
    }

    /* Language label */
    .language-label {
        font-size: 15px;
        font-weight: 600;
        color: #475569;
        margin-bottom: 5px;
    }

    /* Translation cards */
    .card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0px 8px 25px rgba(31, 60, 136, 0.10);
        border: 1px solid #e2e8f0;
        min-height: 270px;
    }

    /* Input / output heading */
    .box-title {
        font-size: 19px;
        font-weight: 600;
        color: #334155;
        margin-bottom: 10px;
    }

    /* Swap button */
    .swap-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 35px;
    }

    /* Translate button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-size: 17px;
        font-weight: 600;
        border: none;
        background: linear-gradient(
            90deg,
            #2563eb,
            #4f46e5
        );
        color: white;
        box-shadow: 0px 5px 15px rgba(37, 99, 235, 0.25);
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #1d4ed8,
            #4338ca
        );
        color: white;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        border-radius: 12px;
        border: 1px solid #dbe3ef;
        background-color: white;
        min-height: 48px;
    }

    /* Text area */
    textarea {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        font-size: 18px !important;
        background-color: #ffffff !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 35px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌐 AI Language Translator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Translate text instantly into multiple languages'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOAD LANGUAGE DATASET
# ============================================================

csv_path = (
    r"C:\Users\kunal\Downloads\6th - NLP project\6th - NLP project\MULTIPLE LANGUAGE TRANSLATION\language.csv"
    
)

df = pd.read_csv(csv_path)

df.dropna(inplace=True)

languages = df["name"].tolist()
language_codes = df["iso"].tolist()

lang_array = {
    languages[i]: language_codes[i]
    for i in range(len(languages))
}


# ============================================================
# SESSION STATE
# ============================================================

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Marathi"

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""


# ============================================================
# LANGUAGE SELECTION
# ============================================================

col1, swap_col, col2 = st.columns([5, 1, 5])


with col1:

    st.markdown(
        '<div class="language-label">SOURCE LANGUAGE</div>',
        unsafe_allow_html=True
    )

    source_lang = st.selectbox(
        "Source",
        languages,
        index=(
            languages.index(st.session_state.source_lang)
            if st.session_state.source_lang in languages
            else 0
        ),
        label_visibility="collapsed"
    )


with swap_col:

    st.markdown(
        '<div class="swap-container">🔄</div>',
        unsafe_allow_html=True
    )

    swap = st.button(
        "⇄",
        key="swap"
    )


with col2:

    st.markdown(
        '<div class="language-label">TARGET LANGUAGE</div>',
        unsafe_allow_html=True
    )

    target_lang = st.selectbox(
        "Target",
        languages,
        index=(
            languages.index(st.session_state.target_lang)
            if st.session_state.target_lang in languages
            else 0
        ),
        label_visibility="collapsed"
    )


# ============================================================
# SWAP LANGUAGES
# ============================================================

if swap:

    st.session_state.source_lang = target_lang
    st.session_state.target_lang = source_lang

    st.rerun()


st.session_state.source_lang = source_lang
st.session_state.target_lang = target_lang


# ============================================================
# INPUT / OUTPUT
# ============================================================

left, right = st.columns(2)


with left:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="box-title">✍️ Enter Text</div>',
        unsafe_allow_html=True
    )

    input_text = st.text_area(
        "Input",
        placeholder="Type or paste your text here...",
        height=200,
        label_visibility="collapsed"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


with right:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="box-title">✨ Translation</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Output",
        value=st.session_state.translated_text,
        height=200,
        placeholder="Your translation will appear here...",
        disabled=True,
        label_visibility="collapsed"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TRANSLATE BUTTON
# ============================================================

st.write("")

translate_col1, translate_col2, translate_col3 = st.columns(
    [2, 2, 2]
)

with translate_col2:

    translate_button = st.button(
        "🚀 Translate",
        use_container_width=True
    )


# ============================================================
# TRANSLATION
# ============================================================

if translate_button:

    if not input_text.strip():

        st.warning("⚠️ Please enter some text first.")

    else:

        try:

            source_code = lang_array[source_lang]
            target_code = lang_array[target_lang]

            with st.spinner("Translating..."):

                translated = translate(
                    input_text,
                    target_code
                )

            st.session_state.translated_text = translated

            st.success("✅ Translation completed!")

            # Rerun to display result
            st.rerun()

        except Exception as e:

            st.error(f"❌ Translation Error: {e}")


# ============================================================
# AUDIO + DOWNLOAD
# ============================================================

if st.session_state.translated_text:

    st.markdown("---")

    audio_col, download_col = st.columns(2)


    # --------------------------------------------------------
    # TEXT TO SPEECH
    # --------------------------------------------------------

    with audio_col:

        try:

            target_code = lang_array[
                st.session_state.target_lang
            ]

            audio = gTTS(
                text=st.session_state.translated_text,
                lang=target_code,
                slow=False
            )

            audio_file = "translation.mp3"

            audio.save(audio_file)

            st.markdown(
                "### 🔊 Listen to Translation"
            )

            with open(audio_file, "rb") as f:

                audio_bytes = f.read()

            st.audio(
                audio_bytes,
                format="audio/mp3"
            )

        except Exception as e:

            st.warning(
                "Audio is not available for this language."
            )


    # --------------------------------------------------------
    # DOWNLOAD TEXT
    # --------------------------------------------------------

    with download_col:

        st.markdown(
            "### 📥 Download Translation"
        )

        st.download_button(
            label="Download Text",
            data=st.session_state.translated_text,
            file_name="translation.txt",
            mime="text/plain",
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Built with Python 🐍 + Streamlit + mTranslate + gTTS
    </div>
    """,
    unsafe_allow_html=True
)