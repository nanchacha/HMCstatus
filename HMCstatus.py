import requests
import streamlit as st
from bs4 import BeautifulSoup
import time

st.markdown("<h1 style='text-align: center; color: #F95700;'>HELP ME CHOOSE STATUS</h1>", unsafe_allow_html=True)

cntrList = ['GR', 'UK', 'ID', 'MY', 'EG', 'HU', 'LEVANT', 'ES', 'LEVANT_AR', 'HK_EN', 'HK', 'RO', 'SE', 'NO', 'DK', 'FI', 'AT', 'CH', 'VN', 'CH_FR', 
            'TW', 'IT', 'DE', 'PH', 'BR', 'CZ', 'SK', 'FR', 'N_AFRICA', 'PT', 'KZ_KZ', 'KZ_RU', 'AU', 'ZA', 'EE', 'LV', 'LT', 'CA', 'PY', 'AR', 'SI', 
            'HR', 'AE', 'TH', 'NL', 'BE', 'BE_FR', 'SG', 'CL', 'CO', 'MX', 'CA_FR', 'PL', 'UA', 'PK', 'PE', 'AE_AR', 'RU', 'UY', 'SA', 'SA_EN']

# cntrList = ['GR']

# cntrList = ['UK']

def statusYn(num):
    result = False
    if num == 200:
        result = True
    return result


def getStatus(cntr):
    r = requests.get("https://www.samsung.com/{}/tvs/help-me-choose".format(cntr))
    num = -1
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    elem = soup.find('div', attrs={'class' : 'find-my-tv__header'})
    if (cntr=='GR'):
        num = 200
        return num
    try : 
        title = elem.text.split('Depending')[0]
        num = 200
    except:
        num = -1
    
    return num


div = round(len(cntrList)/3)
sectionA = div
sectionB = div*2
sectionC = len(cntrList)


col1, col2, col3 = st.columns(3)

with col1:
    for i in range(sectionA):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

with col2:
    for i in range(sectionA,sectionB):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

with col3:
       for i in range(sectionB,len(cntrList)):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

st.success(body="Check Done!")
