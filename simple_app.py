import streamlit as st

# Konfiguration der Seite
st.set_page_config(
    page_title="Simple Input App",
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
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🎨 Simple Input App</h1>', unsafe_allow_html=True)
    
    # Eingabefelder
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.header("📝 Eingabefelder")
    
    # Erste Zeile
    col1, col2 = st.columns(2)
    
    with col1:
        mood = st.text_input("Mood", placeholder="z.B. fröhlich, melancholisch, energisch...")
        style = st.text_input("Style", placeholder="z.B. minimalistisch, vintage, modern...")
        shot_type = st.text_input("Shot Type", placeholder="z.B. Close-up, Wide Shot, Medium Shot...")
    
    with col2:
        subject = st.text_input("Subject", placeholder="z.B. Person, Objekt, Landschaft...")
        action = st.text_input("Action", placeholder="z.B. läuft, sitzt, springt...")
        environment = st.text_input("Environment", placeholder="z.B. Wald, Stadt, Strand...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generieren Button
    if st.button("🚀 Generieren", type="primary", use_container_width=True):
        # Überprüfen ob alle Felder ausgefüllt sind
        inputs = [mood, style, shot_type, subject, action, environment]
        if all(inputs):
            generate_result(mood, style, shot_type, subject, action, environment)
        else:
            st.error("Bitte füllen Sie alle Felder aus!")
    
    # Ergebnis anzeigen
    if 'result' in st.session_state:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.header("✨ Ergebnis")
        st.text_area(
            "Generierter Text:",
            value=st.session_state.result,
            height=200,
            key="display_result"
        )
        
        # Buttons für Aktionen
        col_copy, col_clear = st.columns(2)
        
        with col_copy:
            if st.button("📋 Kopieren", use_container_width=True):
                st.write("Text in Zwischenablage kopiert!")
        
        with col_clear:
            if st.button("🗑️ Löschen", use_container_width=True):
                del st.session_state.result
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def generate_result(mood, style, shot_type, subject, action, environment):
    """Generiert einen Text basierend auf den Eingaben"""
    
    result = f"""Mood: {mood}
Style: {style}
Shot Type: {shot_type}
Subject: {subject}
Action: {action}
Environment: {environment}

Kombinierter Text:
Ein {mood}er {style}er {shot_type} zeigt {subject}, der/die {action} in einer {environment} Umgebung."""
    
    # Ergebnis in Session State speichern
    st.session_state.result = result

if __name__ == "__main__":
    main() 