# 🐾 Zootopia

This Python script processes a JSON file containing animal data and generates an HTML file that displays a list of animals filtered by their skin type.

## 🔧 How It Works

The script performs the following steps:

1. **Loads animal data** from a JSON file (`animals_data.json`)
2. **Prompts the user** to optionally filter animals by skin type
3. **Generates an HTML list** of the filtered animal information
4. **Replaces a placeholder** in the HTML template (`animals_template.html`) with the generated HTML content
5. **Saves the final HTML file** as `animals.html`

## 📋 Requirements

- Python 3.x
- A JSON file (`animals_data.json`) containing structured animal data
- An HTML template file (`animals_template.html`) including a placeholder like `__REPLACE_ANIMALS_INFO__`

## 🚀 Installation

1. Make sure Python 3 is installed on your system.
2. Place the files `animals_data.json` and `animals_template.html` in the same directory as the Python script.