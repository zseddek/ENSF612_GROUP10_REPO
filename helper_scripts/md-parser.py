import markdown
from bs4 import BeautifulSoup
import regex as re
import pandas as pd
import os


def get_md_headers(id, md, link):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    md_headers_to_df(id, soup.find_all(re.compile('^h[1-6]$')), link)


def md_headers_to_df(id, arr, link):
    heading = []
    file_id = [id]*len(arr)
    link_list = [link]*len(arr)
    counter = 0
    for header in arr:
        counter += 1
        if header.name == "h1":
            heading.append("#"+header.text)
        elif header.name == "h2":
            heading.append("##"+header.text)
        elif header.name == "h3":
            heading.append("####"+header.text)
        elif header.name == "h4":
            heading.append("#####"+header.text)
        elif header.name == "h5":
            heading.append("#####"+header.text)
        else:
            heading.append("######"+header.text)

    dataset = pd.DataFrame(
        {'file-id': file_id, 'url': link_list, 'heading': heading},
        columns=['file-id', 'url', 'heading'])
    dataset.to_csv('new_records.csv', index=False, mode='a', header=False)

col_names = ['file-id', 'url', 'heading']
df = pd.DataFrame(columns=col_names)
df.to_csv('new_records.csv', index=False)

file_ID = 436
for root, dirs, file in os.walk('./new_records'):
    for name in file:
        with open('./new_records/'+name, 'r') as f:
            try:
                text = f.read()
            except:
                continue
        name_split = name.split(".", 1)
        repo_link = "https://github.com/" + name_split[0] + "/" + name_split[1].replace(".md", "")
        get_md_headers(file_ID, text, repo_link)
        file_ID += 1


