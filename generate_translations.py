import os
import json
import re

# --- CONFIGURATION ---
CONTENT_DIR = "."
TRANSLATIONS_FILE = os.path.join(CONTENT_DIR, "translations.json")
# List of target languages to generate placeholders for. 
# English ('en') is treated as the source language from folder names.
TARGET_LANGUAGES = ["es"] 
# ---------------------

def parse_folder_name(folder_name):
    """Extracts code and title from folder name like '010 - Air Law'"""
    match = re.match(r"(\d+(?:-\d+)*)\s*-\s*(.*)", folder_name)
    if match:
        return match.group(1), match.group(2)
    return "", folder_name

def update_translation_entry(translations, code, title):
    """Updates or creates a translation entry for a given code."""
    if code not in translations:
        translations[code] = {}
    
    # Always ensure 'en' exists (Source of truth from folder structure)
    if "en" not in translations[code]:
        translations[code]["en"] = title
        
    # Add target languages if they don't exist yet
    for lang in TARGET_LANGUAGES:
        if lang not in translations[code]:
            translations[code][lang] = title # Use English title as placeholder

def generate_translations():
    translations = {}
    
    # Load existing translations to preserve manual edits
    if os.path.exists(TRANSLATIONS_FILE):
        try:
            with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
                translations = json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Warning: Existing translations.json is invalid. Starting fresh.")
            translations = {}

    root_path = os.path.abspath(CONTENT_DIR)
    if not os.path.exists(root_path):
        print(f"❌ Content directory {root_path} not found.")
        return

    print(f"Scanning directory: {root_path}")

    # 1. Scan Categories (Level 1)
    categories = sorted([d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d)) and not d.startswith('.')])
    
    for cat_folder in categories:
        cat_code, cat_title = parse_folder_name(cat_folder)
        if cat_code:
            update_translation_entry(translations, cat_code, cat_title)
            
            cat_path = os.path.join(root_path, cat_folder)
            
            # 2. Scan Subcategories (Level 2)
            subcategories = sorted([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d)) and not d.startswith('.')])
            
            for sub_folder in subcategories:
                sub_code, sub_title = parse_folder_name(sub_folder)
                if sub_code:
                    update_translation_entry(translations, sub_code, sub_title)
                    
                    sub_path = os.path.join(cat_path, sub_folder)
                    
                    # 3. Scan Topics (Level 3)
                    topics = sorted([d for d in os.listdir(sub_path) if os.path.isdir(os.path.join(sub_path, d)) and not d.startswith('.')])
                    
                    for topic_folder in topics:
                        topic_code, topic_title = parse_folder_name(topic_folder)
                        if topic_code:
                            update_translation_entry(translations, topic_code, topic_title)

    # Save back to JSON with nice formatting
    with open(TRANSLATIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(translations, f, indent=2, ensure_ascii=False, sort_keys=True)
    
    print(f"✅ Translations updated at {TRANSLATIONS_FILE}")
    print(f"   Target languages configured: {TARGET_LANGUAGES}")

if __name__ == "__main__":
    generate_translations()
