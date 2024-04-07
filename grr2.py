import requests
from bs4 import BeautifulSoup

def eposta_bul(username):
    url = f'https://www.instagram.com/{username}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tags = soup.find_all('meta')
    
    for tag in meta_tags:
        if 'property' in tag.attrs and tag.attrs['property'] == 'og:description':
            content = tag.attrs['content']
            eposta = content.split(' ')[0]
            if '@' in eposta:
                return eposta
    return None

# Kullanıcı adını gir ve e-postayı bul
username = input("İzleyeceğin kişinin Instagram kullanıcı adını gir: ")
eposta = eposta_bul(username)

if eposta:
    print(f"{username}'nin e-postası: {eposta}")
else:
    print("E-posta bulunamadı.")

if not eposta:
    print("Başarısız oldu? Öfkelenme, belki de kullanıcının e-postası gizlidir ya da bulunamamıştır. Bu durumda, öfkelenmek yerine daha iyi bir plan yapman gerekir.")
