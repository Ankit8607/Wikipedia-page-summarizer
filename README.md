# Case Study (Wiki Summarisation & Paraphrasing)

This project is a Streamlit app deployed on Streamlit Cloud that allows users to select a Wikipedia page, choose a section from that page, and then summarizes and paraphrases the content of that section using OpenAI's GPT-3.5-turbo model.

## Table of Contents

- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Deployment](#deployment)

## Usage

To use the app, follow these steps:

1. Visit the Streamlit app [here](<https://indexpy-mukmokjngnrrq3p2el377f.streamlit.app>).
2. Enter the title of the Wikipedia page you're interested in.
3. Select a section from the dropdown menu.
4. Click on the "Fetch Section" button.
5. The selected section's content will be displayed along with its summarized version and a paraphrased version.

## Dependencies

This project relies on the following dependencies:

- Streamlit
- Wikipedia-API
- OpenAI
- Dotenv

## Installation

These dependencies can be installed via pip. For example:

```bash
pip install streamlit wikipedia-api openai python-dotenv


git clone <(https://github.com/Ankit8607/stream.git)>
cd api


Create virtual environment to install libraries (in macOS)

Create venv : python3 -m venv venv
Activate your venv : source venv/bin/activate


pip install -r requirements.txt


Set your OPENAI_API_KEY in local environment variable


streamlit run index.py
```

## Deployment

The app is deployed on Streamlit Cloud. You can access it [here](<https://indexpy-mukmokjngnrrq3p2el377f.streamlit.app>).
