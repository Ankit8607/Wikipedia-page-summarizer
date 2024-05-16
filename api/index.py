import streamlit as st  # to create frontend
import wikipediaapi  # to access wikipedia content
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv  # to load environment variables
import os

_ = load_dotenv(find_dotenv()) # read local .env file

OpenAI.api_key  = os.environ['OPENAI_API_KEY']  # set openai_api key
client=OpenAI()

# fucntion to summarize the section
def summarizer(s):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You will summarize the given text"},
            {"role": "user", "content": s}
        ]
    )
    return response.choices[0].message.content

# function for paraphrasing
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

    # User will enter the page name
    page_title = st.text_input("Enter the title of the Wikipedia page:")
    # page_title = "albert_einstein"
    
    if page_title:
        wiki_wiki = wikipediaapi.Wikipedia('ankitsuthar8607@gmail.com','en')
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
                    selected_section = sections[int(section_number) - 1]
                    wiki_wiki = wikipediaapi.Wikipedia('ankitsuthar8607@gmai.com','en')
                    page = wiki_wiki.page(page_title)
                    selected_section = page.sections[section_number - 1]
                    selected_section_text=""
                    if selected_section.sections:
                        for sub_section in selected_section.sections:
                                selected_section_text+=(f"- {sub_section.text}")
                                if len(selected_section_text)>300: 
                                    break
                    else: selected_section_text=selected_section.text[:300]
                    st.write(f"\n--- {selected_section} ---\n")
                    st.write(selected_section_text[:100])

                    # Summarize the content of selected section
                    st.write(f"\n--- Summarization of \"{selected_section}\" ---\n")
                    summary = summarizer(selected_section_text)
                    st.write(summary[:200])

                    # Paraphrase the summary
                    st.write(f"\n--- Paraphrasing of summary ---\n")
                    paraphrase = paraphraser(selected_section_text)
                    st.write(paraphrase[:200])
                    
                except:
                    st.error("Data is missing in this section.")
        else:
            st.error(f"The page '{page_title}' does not exist on Wikipedia.")

if __name__ == "__main__":
    main()