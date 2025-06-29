# Veo3PromptGenerator

Eine Streamlit-Anwendung zur Generierung professioneller Prompts für Veo3 mit OpenAI GPT-Integration.

## 🚀 Installation und Verwendung

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)
- OpenAI API Key

### Installation

1. Klonen Sie das Repository:
```bash
git clone <repository-url>
cd Veo3PromptGenerator
```

2. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

3. **Wichtiger Schritt: API Key konfigurieren**

   **Option A: Umgebungsvariable (empfohlen)**
   ```bash
   # Erstellen Sie eine .env Datei
   cp env_example.txt .env
   # Bearbeiten Sie .env und fügen Sie Ihren API Key ein
   ```

   **Option B: Direkt in der Anwendung**
   - Starten Sie die App und geben Sie Ihren API Key in der Sidebar ein

4. Starten Sie die Anwendung:
```bash
streamlit run app.py
```

Die Anwendung wird automatisch in Ihrem Standard-Webbrowser geöffnet (normalerweise unter http://localhost:8501).

## 🔐 Sicherheit

- **API Key**: Wird niemals im Code gespeichert oder ins Repository hochgeladen
- **Umgebungsvariablen**: Verwenden Sie eine `.env` Datei für lokale Entwicklung
- **Gitignore**: Die `.env` Datei ist bereits in `.gitignore` ausgeschlossen

## 📋 Funktionen

- **6 Eingabefelder**: Mood, Style, Shot Type, Subject, Action, Environment
- **OpenAI GPT-Integration**: Automatische Prompt-Generierung mit GPT-3.5-turbo
- **Sichere API Key Verwaltung**: Über Umgebungsvariablen oder Sidebar-Eingabe
- **Benutzerfreundliche Oberfläche**: Intuitive Bedienung
- **Speichern und Kopieren**: Generierte Prompts können kopiert werden
- **Responsive Design**: Funktioniert auf Desktop und mobilen Geräten

## 🎯 Verwendung

1. **API Key eingeben** (falls nicht über Umgebungsvariable gesetzt)
2. **Eingabefelder ausfüllen**:
   - Mood (Stimmung)
   - Style (Stil)
   - Shot Type (Aufnahmetyp)
   - Subject (Subjekt)
   - Action (Aktion)
   - Environment (Umgebung)
3. **"Generieren" klicken**
4. **GPT erstellt automatisch** einen professionellen Veo3-Prompt
5. **Prompt kopieren** und verwenden

## 📁 Projektstruktur

```
Veo3PromptGenerator/
├── app.py              # Hauptanwendung
├── requirements.txt    # Python-Abhängigkeiten
├── README.md          # Diese Datei
├── .gitignore         # Git-Ausschlüsse
├── env_example.txt    # Vorlage für .env Datei
└── prompts/           # Gespeicherte Prompts (wird automatisch erstellt)
```

## 🔧 Konfiguration

### OpenAI API Key erhalten
1. Besuchen Sie [OpenAI Platform](https://platform.openai.com/api-keys)
2. Erstellen Sie einen neuen API Key
3. Fügen Sie ihn in Ihre `.env` Datei ein oder geben Sie ihn in der App ein

### Umgebungsvariablen
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 🤝 Beitragen

Verbesserungsvorschläge und Pull Requests sind willkommen!

**Wichtig**: Teilen Sie niemals API Keys oder sensitive Daten im Code.