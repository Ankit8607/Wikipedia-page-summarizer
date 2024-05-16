import streamlit as st
import wikipediaapi
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv()) # read local .env file

OpenAI.api_key  = os.environ['OPENAI_API_KEY']
client=OpenAI()

def summarizer(s):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You will summarize the given text"},
            {"role": "user", "content": s}
        ]
    )
    return response.choices[0].message.content

def paraphraser(s):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You will paraphrase the given text"},
            {"role": "user", "content": s}
        ]
    )
    return response.choices[0].message.content

def main():
    st.title("Wikipedia Section Selector")
    page_title = st.text_input("Enter the title of the Wikipedia page:")
    # page_title = "albert_einstein"
    
    if page_title:
        wiki_wiki = wikipediaapi.Wikipedia('ankitsuthar8607@gmail.com','en')
        page = wiki_wiki.page(page_title)

        if page.exists():
            sections = [section.title for section in page.sections]
            st.write(f"Sections for '{page_title}':")
            for i, section in enumerate(sections):
                st.write(f"{i+1}. {section}")
            
            section_number = st.number_input("Enter the number of the section you want to read:", min_value=1, max_value=len(sections))
            
            if st.button("Fetch Section"):
                try:
                    selected_section = sections[int(section_number) - 1]
                    wiki_wiki = wikipediaapi.Wikipedia('ankitsuthar8607@gmai.com','en')
                    page = wiki_wiki.page(page_title)
                    selected_section_text = page.sections[int(section_number) - 1].text[:500]  # Displaying first 500 characters of the section text
                    st.write(f"\n--- {selected_section} ---\n")
                    st.write(selected_section_text)
                    st.write(f"\n--- Summarization of \"{selected_section}\" ---\n")
                    summary = summarizer(selected_section_text)
                    st.write(summary)
                    st.write(f"\n--- Paraphrasing of summary ---\n")
                    paraphrase = paraphraser(selected_section_text)
                    st.write(paraphrase)
                    
                except:
                    st.error("An error occurred while fetching the section.")
        else:
            st.error(f"The page '{page_title}' does not exist on Wikipedia.")

if __name__ == "__main__":
    main()