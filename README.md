# Case Study (Wiki Summarisation & Paraphrasing)

This project is a Streamlit app deployed on Streamlit Cloud that allows users to select a Wikipedia page, choose a section from that page, and then summarizes and paraphrases the content of that section using OpenAI's GPT-3.5-turbo model.

## Table of Contents

- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

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


git clone <repository-url>
cd wikipedia-section-summarizer


pip install -r requirements.txt


streamlit run app.py


## Deployment

The app is deployed on Streamlit Cloud. You can access the app [here](<https://indexpy-mukmokjngnrrq3p2el377f.streamlit.app>).

Replace `<https://indexpy-mukmokjngnrrq3p2el377f.streamlit.app>` with the URL to your deployed Streamlit app. Additionally, replace `<repository-url>` with the URL of your GitHub repository if you're planning to publish it.
