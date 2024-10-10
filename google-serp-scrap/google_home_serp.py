import requests
from bs4 import BeautifulSoup as bs

quary = 'best cat breeds in the world'
data =quary.replace(' ', '+')
url = f'https://www.google.com/search?q={data}'

headers = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie' : 'OTZ=6849194_32_32__32_; AEC=ARSKqsJ1SwgWEuqGeiQRR9nBNtE_qIsIEeNc7yettHcZ7j0AhTuW-NmIVg; OGPC=19022552-1:19022519-1:; OGP=-19022552:-19022519:; SEARCH_SAMESITE=CgQIq5cB; SID=SwhSPc3mrS3IK3ZUCZ6LqziMfsgeOgtbnImOpmCffT3Dfm4iZxo5-Zgr5bkByTVdzR4rkw.; __Secure-1PSID=SwhSPc3mrS3IK3ZUCZ6LqziMfsgeOgtbnImOpmCffT3Dfm4iv1PUndgLVKbAIo8o2Z88Ig.; __Secure-3PSID=SwhSPc3mrS3IK3ZUCZ6LqziMfsgeOgtbnImOpmCffT3Dfm4iGfVBttwFZFhKUUS-uz-HWQ.; HSID=ACffZEoXgx7uBtRbm; SSID=A66Z5pS6KL1r7qd8r; APISID=CRfGhrKRcg_AOZ-p/Au193g90W_NEJDOuC; SAPISID=XfEDrWstPSDDRt8s/ALW4bpY1oFjCXa1k1; __Secure-1PAPISID=XfEDrWstPSDDRt8s/ALW4bpY1oFjCXa1k1; __Secure-3PAPISID=XfEDrWstPSDDRt8s/ALW4bpY1oFjCXa1k1; NID=511=Zp1OQJsIaYV58TcpUNqCo3uiNDAoswBeeiZeyBtajH0TQt--T5tAk7mTelXobH7ZiNJvw0DY20rgbzMtWEhnS9F6z3ilNxPn1vaaF3PHFS7O88attaxg-wOFuQhYXRqISnb2Zs5XJneyNjuYQ0SgdHxg9aOdwW_lGawd5kCjMMJhkjp0a0ipULV-7twGRqvR9EFws9G-vLHlkV7Jt0MDd-v1JK5MWFCJ_1ED29wTbik0ZnSTxHtoyLwOwmt69xePD3CIqlNgtw57mOOOR9fhsaN15yyvcGPKtpIgI-rnRwPDzwJyqoR4xAi5uvqAAdnlDQhF0-k30wHgtQmuz8kurupv3IFA6XXUAeNCKcGpV4mkopAtgksNW_-ga8vhip9H-T5iyJb30szwAWRAOUC3lL69TAKa3tQytkJc7LJEkWgekfCPp3CwANPF89LSals8fe8IlOLlz9riluBUMQRr3ZfZ69EFhtvOkSsG4o7xcQDTXA0I2zDt3O9FMA; DV=MzPn7iExqx5WwEtSPKiaEko6bjbwWphvU3dyzytn9AEAAIBHfY3ypUEuhAAAAFQ5Rwsg6qLjIgAAAKaqsXzyEc3TCwAAAA; 1P_JAR=2023-01-14-06; SIDCC=AIKkIs2DUJQLGU_lFY3rjOiacGjefOZv74J3S5wDyLIAwyujOQEnSh4qyIJIRfblBHfjAKFIOQ; __Secure-1PSIDCC=AIKkIs0rI8cZUxfti3eiD5dZh-7iWB81NiKDILHf5wMflA-WjykM3GRyTQHFWclMiXWMK1dde8g; __Secure-3PSIDCC=AIKkIs3kd1MZHVuCJeCkXkLlSStMI9tYhUCVY5OPtpAqmMjMTDX2T_AbbrYyyvximAJgGCKUxA' 
}

s = requests.session()

res = s.get(url, headers= headers)
soup = bs(res.text, 'html.parser')
Link_div = soup.findAll('div', {'class':'kvH3mc BToiNc UK95Uc'})
for link in Link_div:
    link_list = link.find('a').get('href')
    with open('link.txt', 'a+')as file:
        file.writelines(link_list+'\n')
        




