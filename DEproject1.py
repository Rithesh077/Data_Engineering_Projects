import pandas as pd
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

response = requests.get(url)
print(response.json())
data = response.json()
print(data['items'])
repo_list = data['items']
print(len(repo_list))
print(type(repo_list))
new_list = []
for repo in repo_list:
    new_list.append({
        'name': repo['name'],
        'html_url': repo['html_url'],
        'description': repo['description'],
        'stargazers_count': repo['stargazers_count'],
        'owner': repo['owner']['login']
    })

df = pd.DataFrame(new_list)
df.to_csv("repo_data.csv", index=False)
