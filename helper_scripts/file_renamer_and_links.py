import os
import pandas as pd

link_list = []
for filename in os.listdir("new_records"):
    old_name_parsed = filename.split("_", 1) 
    new_name = old_name_parsed[0] + '.' + old_name_parsed[1]
    os.rename("new_records/" + filename, "new_records/" + new_name)
    link_http_half = "https://github.com/"
    link_http_full = link_http_half + old_name_parsed[0] + "/" + old_name_parsed[1].replace(".md", "")
    link_list.append(link_http_full)

df = pd.DataFrame(link_list)
df.to_csv("new_records_links.csv")


