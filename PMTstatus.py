# https://www.samsung.com/uk/tvs/personalize-my-tv/?sku=QE65QN900BTXXU&type=apps


import requests
import streamlit as st
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align: center; color: #F95700;'>Personalize My TV STATUS</h1>", unsafe_allow_html=True)

cntrList = ['UK', 'ID', 'MY', 'EG', 'HU', 'LEVANT', 'ES', 'LEVANT_AR', 'HK_EN', 'HK', 'RO', 'SE', 'NO', 'DK', 'FI', 'AT', 'CH', 'VN', 'CH_FR', 'TW', 'IT', 'DE', 'PH', 'BR', 'CZ', 'SK', 
 'FR', 'N_AFRICA', 'PT', 'KZ_KZ', 'KZ_RU', 'AU', 'ZA', 'EE', 'LV', 'LT', 'CA', 'PY', 'AR', 'SI', 'HR', 'AE', 'TH', 'NL', 'BE', 'BE_FR', 'SG', 'CL', 'CO', 'MX', 'CA_FR', 'PL', 'UA', 'PK', 'PE', 'AE_AR', 'RU', 'UY']

# cntrList = ['UK']

def statusYn(num):
    result = False
    if num == 200:
        result = True
    return result


def getStatus(cntr):
    r = requests.get("https://www.samsung.com/{}/tvs/personalize-my-tv/?sku=QE65QN900BTXXU&type=apps".format(cntr))
    num = -1
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
        
    elem = soup.find('div', attrs={'class' : 'customize__header'})
    try : 
        title = elem.text.split('Depending')[0]
        num = 200
    except:
        num = -1
    
    return num

col1, col2 = st.columns(2)

with col1:
    for i in range(len(cntrList)):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))

st.success(body="Check Done!")
