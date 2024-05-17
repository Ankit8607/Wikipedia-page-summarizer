import streamlit as st  # to create frontend
import wikipediaapi  # to access wikipedia content
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv  # to load environment variables
import os

from sectionExtractor import section_text  # function to extract the section text
from summarization import summarizer  # fucntion to summarize the section
from paraphrasing import paraphraser  # fucntion to paraphrase the summary

_ = load_dotenv(find_dotenv()) # read local .env file

OpenAI.api_key  = os.environ['OPENAI_API_KEY']  # set openai_api key
client=OpenAI()

def main():
    st.title("Wikipedia Section Selector")

    # User will enter the page name
    page_title = st.text_input("Enter the title of the Wikipedia page:")
    # page_title = "albert_einstein"
    
    if page_title:
        wiki_wiki = wikipediaapi.Wikipedia('application','en')
        page = wiki_wiki.page(page_title)  # stored the information of page_title

        if page.exists():
            sections = [section.title for section in page.sections]  # extracted the sections from page
            # this will write the sections in frontend
            st.write(f"Sections for '{page_title}':")  
            for i, section in enumerate(sections):
                st.write(f"{i+1}. {section}")
            
            # Take the section number from user from frontend
            section_number = st.number_input("Enter the number of the section you want to read:", min_value=1, max_value=len(sections))
            
            if st.button("Fetch Section"):
                try:
                    # extract the content of selected section
                    selected_section = page.sections[int(section_number) - 1]
                    wiki_wiki = wikipediaapi.Wikipedia('application','en')
                    page = wiki_wiki.page(page_title)


                    # Extract the text of selected section
                    selected_section_text = section_text(selected_section)
                    st.write(f"\n--- {selected_section.title} ---\n")
                    st.write(selected_section_text[:500])


                    # Summarize the content of selected section
                    st.write(f"\n--- Summarization of section \"{ selected_section.title}\" ---\n")
                    summary = summarizer(selected_section_text)
                    st.write(summary[:500])


                    # Paraphrase the summary
                    st.write(f"\n--- Paraphrasing of summary ---\n")
                    paraphrase = paraphraser(summary)
                    st.write(paraphrase[:500])
                    
                except:
                    st.error("Data is missing in this section.")
        else:
            st.error(f"The page '{page_title}' does not exist on Wikipedia.")

if __name__ == "__main__":
    main()