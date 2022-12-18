import requests
import streamlit as st

st.markdown("<h1 style='text-align: center; color: #F0EDCC;'>HELP ME CHOOSE STATUS</h1>", unsafe_allow_html=True)

cntrList = ['UK', 'ID', 'MY', 'EG', 'HU', 'LEVANT', 'ES', 'LEVANT_AR', 'HK_EN', 'HK', 'RO', 'SE', 'NO', 'DK', 'FI', 'AT', 'CH', 'VN', 'CH_FR', 'TW', 'IT', 'DE', 'PH', 'BR', 'CZ', 'SK', 
 'FR', 'N_AFRICA', 'PT', 'KZ_KZ', 'KZ_RU', 'AU', 'ZA', 'EE', 'LV', 'LT', 'CA', 'PY', 'AR', 'SI', 'HR', 'AE', 'TH', 'NL', 'BE', 'BE_FR', 'SG', 'CL', 'CO', 'MX', 'CA_FR', 'PL', 'UA', 'PK', 'PE', 'AE_AR', 'RU', 'UY']

def statusYn(num):
    result = False
    if num == 200:
        result = True
    return result


def getStatus(cntr):
    r = requests.get("https://www.samsung.com/{}/tvs/help-me-choose".format(cntr))
    num = r.status_code
    # print(cntr, num)
    return num

cnt = 1

# for i in range(len(cntrList)):
#     if (statusYn(getStatus(cntrList[i]))):
#         st.write("{} :smiley:".format(cntrList[i]))
#     else:
#         st.write("{} :rage:".format(cntrList[i]))

col1, col2, col3 = st.columns(3)

with col1:
    for i in range(19):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} ::red_circle:".format(cntrList[i]))

with col2:
    for i in range(20,39):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} ::red_circle:".format(cntrList[i]))

with col3:
       for i in range(40,len(cntrList)):
        if (statusYn(getStatus(cntrList[i]))):
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} ::red_circle:".format(cntrList[i]))

st.success(body="Check Done!")
