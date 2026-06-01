#!/usr/bin/env python3
"""Check which words from a list exist in the Hunspell dictionary."""
import sys

# Load the Hunspell dictionary
with open('el_GR.dic', 'r', encoding='utf-8') as f:
    lines = f.readlines()

hunspell_words = set()
for line in lines[1:]:  # skip count line
    word = line.strip().split('/')[0].strip()
    if len(word) == 4 and word.isalpha():
        hunspell_words.add(word.upper())

print(f"Total 4-letter words in Hunspell: {len(hunspell_words)}")
print()

# Test the words the user specified
target = [
    "ΑΥΓΟ", "ΜΗΛΟ", "ΤΑΜΑ", "ΜΑΜΑ", "ΓΟΠΑ", "ΦΕΡΕ", "ΤΥΡΙ", "ΤΑΠΑ",
    "ΦΑΠΑ", "ΒΑΝΑ", "ΓΟΜΑ", "ΦΑΤΟ", "ΠΑΜΕ", "ΚΑΛΟ", "ΛΑΠΑ", "ΗΤΤΑ",
    "ΤΩΡΑ", "ΦΑΚΑ", "ΔΑΔΑ", "ΔΟΡΙ", "ΧΕΡΙ", "ΨΩΜΙ", "ΩΡΕΣ", "ΝΥΧΙ",
    "ΖΑΡΙ", "ΣΥΡΕ"
]

print("=== Έλεγχος λέξεων ===")
for w in target:
    if w in hunspell_words:
        print(f"  {w}  ✓  Υπάρχει στο λεξικό")
    else:
        print(f"  {w}  ✗  ΔΕΝ υπάρχει στο λεξικό")

# Also check current dictionary.json words
import json
try:
    with open('dictionary.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    current_dict = set(data.get('dictionary', []))
    current_targets = set(data.get('targetWords', []))
    
    # Check which current dictionary words are actually in Hunspell
    valid = current_dict & hunspell_words
    invalid = current_dict - hunspell_words
    print(f"\n=== Στατιστικά τρέχοντος λεξικού ===")
    print(f"Λέξεις στο dictionary.json: {len(current_dict)}")
    print(f"Από αυτές, πραγματικές (Hunspell): {len(valid)} ({len(valid)/len(current_dict)*100:.1f}%)")
    print(f"Ανύπαρκτες: {len(invalid)} ({len(invalid)/len(current_dict)*100:.1f}%)")
    print(f"\nΜερικές ανύπαρκτες: {sorted(list(invalid))[:20]}")
except:
    pass
