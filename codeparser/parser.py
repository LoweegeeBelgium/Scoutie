import json
import sys
import os
import re

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Now you can import the scraper module
from codescraper import scraper



def remove_comments(code_content):
    # Use regular expression to remove comments
    code_content = re.sub(r'#.*?\n', '\n', code_content)
    code_content = re.sub(r'\'\'\'.*?\'\'\'', '', code_content, flags=re.DOTALL)
    code_content = re.sub(r'\"\"\".*?\"\"\"', '', code_content, flags=re.DOTALL)
    return code_content

def vectorize(code_content):
    # Remove comments from the code content
    code_content = remove_comments(code_content)

    # Split the code content into words
    words = code_content.split()
    
    return words

def add_entry_to_json_file(link, vector, filename="dataset.json"):
    """
    Add a new entry to a JSON file of objects with members 'link' and 'vector'.
    If the file does not exist, it creates the file and adds the object.

    Args:
    link (str): The link to be added.
    vector (str): The vector to be added.
    filename (str): The name of the JSON file.
    """

    if os.path.exists(filename):

        with open(filename, 'r') as file:
            data = json.load(file)
    else:

        data = []


    new_entry = {"link": link, "vector": vector}

  
    data.append(new_entry)


    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
