from requests import get

url = input("Digite o seu alvo: \n >:")

wordlist_file = "wordlist.txt"
with open(wordlist_file) as f:
    wordlist = f.readlines()
wordlist = [x.replace('\n', "") for x in wordlist]
if url[-1] != '/':url = url+'/'
for word in wordlist:
    new_url= f'{url}{word}'
    print(f'Scanning: {new_url}')
    response = get(f"{new_url}")
    if response.status_code != 404:
        if response.history:
            print(f'{response.url}')
            for r in response.history:
                print(f"\t{r} -> {r.status_code}")
        else:
            print(f"\t{new_url} -> {response.status_code}")
        
    
