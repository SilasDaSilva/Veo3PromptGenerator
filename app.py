import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

# Lade Umgebungsvariablen aus .env Datei
load_dotenv()

# Konfiguration der Seite
st.set_page_config(
    page_title="Veo3PromptGenerator",
    page_icon="🎨",
    layout="wide"
)

# CSS für besseres Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .input-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .result-box {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .gpt-result-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .env-success {
        background-color: #d4edda;
        color: #155724;
        padding: 0.5rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
    .loading-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }
    .spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #1f77b4;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin-right: 1rem;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🎨 Veo3PromptGenerator</h1>', unsafe_allow_html=True)
    
    # OpenAI API Key Verwaltung
    st.sidebar.header("🔑 OpenAI API Key")
    
    # Versuche zuerst Umgebungsvariable zu verwenden
    api_key_from_env = os.getenv('OPENAI_API_KEY')
    api_key_source = None
    
    if api_key_from_env and api_key_from_env.strip() and api_key_from_env != 'your_openai_api_key_here':
        api_key = api_key_from_env
        api_key_source = "env"
        st.sidebar.markdown('<div class="env-success">✅ API Key loaded from .env file</div>', unsafe_allow_html=True)
    else:
        # Falls keine Umgebungsvariable gesetzt ist, verwende Sidebar-Eingabe
        api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Your OpenAI API Key")
        api_key_source = "input"
    
    # Debug-Informationen (nur für Entwicklung)
    if st.sidebar.checkbox("🔧 Show Debug Info"):
        st.sidebar.write(f"API Key Source: {api_key_source}")
        st.sidebar.write(f"API Key Present: {bool(api_key)}")
        if api_key:
            st.sidebar.write(f"API Key Length: {len(api_key)}")
            st.sidebar.write(f"API Key Start: {api_key[:10]}...")
    
    # Eingabefelder
    st.header("📝 Input Fields")
    
    # Erste Zeile
    col1 = st.columns(1)
    mood = st.text_input("Mood", placeholder="e.g. happy, melancholic, energetic...")
    style = st.text_input("Style", placeholder="e.g. minimalist, vintage, modern...")
    shot_type = st.text_input("Shot Type", placeholder="e.g. Close-up, Wide Shot, Medium Shot...")
    subject = st.text_input("Subject", placeholder="e.g. Person, Object, Landscape...")
    action = st.text_input("Action", placeholder="e.g. walking, sitting, jumping...")
    environment = st.text_input("Environment", placeholder="e.g. forest, city, beach...")
    
    # Generieren Button
    if st.button("🚀 Generate", type="primary", use_container_width=True):
        # Überprüfen ob alle Felder ausgefüllt sind
        inputs = [mood, style, shot_type, subject, action, environment]
        if all(inputs):
            if api_key and api_key.strip():
                # Ladeanimation anzeigen
                with st.spinner("🔄 Generating prompt with GPT..."):
                    generate_result(mood, style, shot_type, subject, action, environment)
                    generate_gpt_prompt(api_key)
            else:
                st.error("❌ Please enter your OpenAI API Key!")
        else:
            st.error("❌ Please fill in all fields!")
    
    # Ergebnis anzeigen
    if 'result' in st.session_state:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.header("✨ Generated Input")
        st.text_area(
            "Input for GPT:",
            value=st.session_state.result,
            height=150,
            key="display_result"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # GPT Ergebnis anzeigen
    if 'gpt_result' in st.session_state:
        st.markdown('<div class="gpt-result-box">', unsafe_allow_html=True)
        st.header("🤖 GPT Generated Prompt")
        st.text_area(
            "Final Prompt:",
            value=st.session_state.gpt_result,
            height=200,
            key="display_gpt_result"
        )
        
        # Buttons für Aktionen
        col_copy, col_clear = st.columns(2)
        
        with col_copy:
            if st.button("📋 Copy", use_container_width=True):
                st.write("Prompt copied to clipboard!")
        
        with col_clear:
            if st.button("🗑️ Clear", use_container_width=True):
                del st.session_state.gpt_result
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def generate_result(mood, style, shot_type, subject, action, environment):
    """Generiert einen Text basierend auf den Eingaben"""
    
    result = f"""Mood: {mood}
Style: {style}
Shot Type: {shot_type}
Subject: {subject}
Action: {action}
Environment: {environment}"""
    
    # Ergebnis in Session State speichern
    st.session_state.result = result

def generate_gpt_prompt(api_key):
    """Sendet das Ergebnis an GPT und generiert einen finalen Prompt"""
    
    try:
        # OpenAI Client initialisieren
        client = OpenAI(api_key=api_key)
        
        # System-Prompt für GPT
        system_prompt = """You are a professional prompt engineer for Veo3. 
        Create a detailed, creative and precise prompt for Veo3 based on the given parameters. 
        The prompt should contain all important visual and stylistic elements and have a maximum of 300 tokens. 
        Leave out everything that cannot be used in Veo3 and is not meant to be a prompt for Veo3."""
        
        # User-Prompt mit den generierten Parametern
        user_prompt = f"""Create a detailed Veo3 prompt based on these parameters:

{st.session_state.result}

The prompt should:
- Integrate all parameters creatively and precisely
- Describe visual details and moods
- Be optimized for Veo3
- Read naturally and fluently
- Ensure the smoothest and most realistic output possible
- Have a maximum of 300 tokens
- be in english, even if the input is in another language"""
        
        # GPT API Aufruf mit neuer API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=300,
            temperature=0.8
        )
        
        # Ergebnis extrahieren und speichern
        gpt_result = response.choices[0].message.content.strip()
        st.session_state.gpt_result = gpt_result
        
        st.success("✅ GPT Prompt generated successfully!")
        
    except Exception as e:
        st.error(f"❌ Error generating GPT prompt: {str(e)}")

if __name__ == "__main__":
    main()

