import json
import re
def check_dollar_symbol_in_json(file_path):
    """
    This function checks for the '$' symbol in the description, conversation, and system sections
    of a JSON data structure, while ignoring pattern matching sections (like regex).
    """
    found_dollar_signs = False    
    def check_in_text_section(section_name, text):
        nonlocal found_dollar_signs
        # Check for the '$' symbol in the text, while avoiding lines that are regex patterns
        if '$' in text and not re.search(r'pattern.*:', text, re.IGNORECASE):
            found_dollar_signs = True
            print(f"Found '$' symbol in {section_name} section:")
            print(text.strip())
            print("-" * 50)
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)        
        # Iterate through the JSON structure and check the content
        for cell in json_data:
            if 'cells' in cell:
                for cell_content in cell['cells']:
                    if 'source' in cell_content:  # Ensure 'source' exists in cell content
                        source = "".join(cell_content['source'])  
                        # Check if the section is 'system', 'tools', 'description', or 'conversation'
                        if 'system' in source.lower():
                            check_in_text_section("System", source)
                        elif 'tools' in source.lower() or 'description' in source.lower():
                            check_in_text_section("Tool Description", source)
                        elif '[conversation]' in source.lower():
                            check_in_text_section("Conversation", source)
                        elif '[user]' in source.lower():  # Check for '$' in user sections too
                            check_in_text_section("User", source)
        if not found_dollar_signs:
            print("No '$' symbols found in description, conversation, system, or user sections.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'combined_payload (1).json'
check_dollar_symbol_in_json(file_path)
