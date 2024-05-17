
def section_text(selected_section):
    selected_section_text = ""
    # selected_section_text=page.sections[int(section_number)-1].text[:300]
    if selected_section.sections:
        for sub_section in selected_section.sections:
                selected_section_text+=(f"- {sub_section.text}")
                if len(selected_section_text)>2000: 
                    break
    else: selected_section_text=selected_section.text[:2000]  # Make sure that GPT-3.5-turbo has limit of 4096
    return selected_section_text