#friend.tech API Scraper
import requests
import time
from web3 import Web3
import json
from web3.middleware import geth_poa_middleware
import random
import logging
logging.basicConfig(level=logging.INFO)
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import click
import threading
import sys

#Add your own if this gets blocked one day
proxy_list = ["176.113.73.104:3128","176.113.73.99:3128","67.205.190.164:8080","46.21.153.16:3128","84.17.35.129:3128","104.248.59.38:80","12.156.45.155:3128","176.113.73.102:3128","147.182.142.189:80","66.152.169.73:1994","143.110.155.17:1994","191.101.1.116:80","96.75.48.93:8080","173.82.20.178:1994","170.64.137.67:1994","104.225.220.233:80","45.77.198.163:80","12.88.29.66:9080","38.45.242.12:999","170.64.128.216:1994","157.245.81.154:3128","141.148.163.150:3128","155.94.185.137:1994","128.14.27.141:80","198.211.55.167:1994","173.82.200.90:1994","52.88.105.39:80","198.74.101.82:1994","170.178.193.106:1994","108.166.203.110:1994","45.61.163.5:8080","104.129.41.2:1994","173.82.150.9:1994","66.128.123.114:8080","40.124.122.180:3128","100.42.70.109:1994","173.82.34.3:1994","104.194.228.118:1994","38.45.34.65:999","167.99.236.14:80","72.44.67.178:1994","34.135.0.68:80","31.220.109.82:80","170.64.134.155:1994","93.188.161.84:80","107.173.148.253:8080","104.194.227.12:1994","162.254.3.12:3128","143.198.150.120:1994","72.44.68.249:1994","162.240.75.37:80","173.82.102.194:1994","45.158.171.3:999","104.194.232.179:1994","198.74.98.18:1994","192.227.166.144:1994","100.42.79.61:1994","104.248.58.82:1994","77.247.126.194:3128","37.120.222.132:3128","89.249.65.191:3128","144.91.118.176:3128","85.214.94.28:3128","167.172.109.12:39452","95.111.226.235:3128","167.172.109.12:40825","185.189.112.157:3128","185.189.112.133:3128","85.214.244.174:3128","167.172.109.12:41491","167.172.109.12:39533","167.172.109.12:46249","88.99.10.252:1080","167.172.109.12:37355","47.254.152.98:80","82.180.163.163:80","157.230.127.125:8080","78.46.175.184:80","172.177.221.87:80","93.104.211.69:21","164.92.179.160:1994","130.61.186.129:8000","5.189.146.57:80","78.47.132.125:3128","88.198.117.95:3128","139.59.130.29:1994","46.101.156.40:1994","95.111.239.49:3128","104.248.40.5:1994","138.201.198.233:3128","13.229.107.106:80","13.229.47.109:80","119.81.71.27:80","119.81.71.27:8123","193.56.255.179:3128","139.180.140.254:1080","104.248.146.99:3128","18.141.177.23:80","193.56.255.181:3128","188.166.252.135:8080","156.67.217.159:80","52.74.49.91:80","182.55.48.187:80","143.198.195.106:1994","184.168.122.103:7890","165.22.57.238:443","139.180.145.113:1234","104.248.158.114:8080","128.199.131.215:1994","188.166.248.211:1994","206.189.130.107:8080","15.207.196.77:3128","159.89.166.232:1994","134.209.153.99:1994","103.207.1.82:8080","182.74.63.189:83","13.233.22.210:3000","159.89.171.241:1994","183.87.160.62:84","167.71.228.106:1994","43.243.174.3:83","103.149.195.33:80","103.242.119.88:80","103.243.114.206:8080","103.157.13.75:83","159.65.144.222:1994","121.200.49.204:8080","139.59.58.73:3111","51.158.68.133:8811","51.158.68.68:8811","159.8.114.37:80","35.180.188.216:80","51.158.172.165:8811","159.8.114.37:8123","141.95.127.15:3128","82.64.233.180:80","82.66.172.182:80","51.75.123.184:3128","51.38.191.151:80","193.70.102.210:8080","146.59.2.185:80","82.210.8.173:80","163.172.85.30:80","54.37.105.157:8080","119.81.189.194:80","119.81.189.194:8123","193.239.86.249:3128","193.239.86.247:3128","193.239.86.248:3128","8.210.223.21:80","8.210.52.87:8080","103.60.109.96:8888","103.172.135.53:80","218.250.67.85:80","123.202.159.203:80","103.234.55.173:80","45.142.106.133:80","8.210.150.202:24001","42.98.75.138:80","37.120.133.137:3128","84.17.51.235:3128","84.17.51.241:3128","84.17.51.240:3128","140.238.96.232:3128","144.126.194.20:1994","134.209.29.32:1994","46.101.19.131:80","138.68.149.125:8080","143.110.172.248:1994","165.22.119.104:1994","82.102.11.74:443","167.99.90.120:1994","134.209.180.166:1994","79.122.230.20:8080","37.232.145.221:53281","81.177.6.68:3128","95.188.78.101:8081","95.68.247.132:8080","95.154.76.20:3128","188.133.139.219:1256","46.229.73.19:8080","91.143.175.57:8080","176.192.80.10:3128","45.89.52.212:3128","46.72.56.78:8080","188.116.173.198:3128","94.73.239.124:55443","180.183.97.16:8080","113.53.53.7:8080","183.88.223.17:8081","183.89.11.135:8080","182.52.68.216:8080","110.164.15.182:8080","1.0.205.87:8080","171.6.104.8:8000","14.207.121.166:8080","183.88.235.50:8080","81.12.119.171:8080","217.172.122.14:8080","5.160.175.226:8383","80.249.112.162:80","46.249.122.1:8080","185.211.57.166:3128","185.118.155.202:8080","188.136.154.38:8080","91.221.240.254:1515","89.43.10.141:80","185.123.101.174:3128","93.180.135.243:3128","176.88.65.186:8080","185.123.101.174:4443","185.74.20.28:9090","176.236.85.246:9090","176.236.141.30:10001","88.255.65.119:8080","195.174.142.76:8080","159.89.113.155:8080","134.122.46.33:1994","107.175.96.34:1994","143.110.221.71:1994","68.183.207.173:1994","159.203.22.85:1994","167.114.19.195:8050","107.6.27.132:80","188.166.30.17:8888","79.110.52.252:3128","94.100.18.111:3128","206.189.108.245:1994","164.92.209.89:1994","20.31.129.113:3128","161.35.91.95:80","41.65.55.10:1981","41.65.174.34:1981","196.204.24.251:8080","41.65.236.35:1981","154.239.1.77:1981","154.236.168.141:1976","181.129.71.36:8080","200.32.80.54:999","177.93.51.168:999","177.93.50.106:999","190.121.157.142:999","181.48.107.26:999","45.172.111.89:999","181.209.113.99:999","45.229.205.191:55555","181.209.116.20:999","170.210.121.190:8080","200.123.157.37:8080","161.202.226.194:8123","35.200.4.163:3128","34.84.72.91:3128","153.127.25.97:3128","164.70.122.6:3128","186.166.138.51:999","186.24.9.118:999","181.191.226.1:999","186.167.67.99:999","38.41.0.91:999","14.170.154.193:19132","123.30.154.38:2008","103.176.179.84:3128","113.161.131.43:80","42.96.47.158:3128","185.123.143.251:3128","185.123.143.247:3128","37.120.140.158:3128","89.238.212.34:8080","103.130.141.98:8080","167.179.45.50:55443","111.90.188.206:8080","45.115.211.14:587","194.31.53.250:80","178.212.54.137:8080","89.230.94.115:8080","89.234.199.22:41258","201.222.45.2:999","45.160.74.1:999","190.110.99.188:999","200.54.194.12:53281","59.15.28.113:3128","119.192.76.54:80","121.139.218.165:31409","115.144.101.200:10000","45.229.87.233:999","45.173.231.153:999","186.3.38.205:999","181.198.115.179:999","3.24.178.81:80","103.1.184.238:3128","139.99.233.154:8888","185.236.202.205:3128","185.236.202.170:3128","86.56.167.154:80","193.34.95.110:8080","109.254.30.70:9090","109.254.219.40:9090","201.131.239.233:999","45.174.87.18:999","186.96.56.9:999","124.107.145.59:8081","58.69.175.99:8080","115.147.33.61:8081","190.119.151.163:999","179.43.94.238:999","200.123.15.122:999","95.216.17.79:3888","37.219.150.208:80","118.99.108.4:8080","103.114.53.2:8080","169.57.157.148:80","169.57.157.146:8123","103.28.121.58:3128","103.28.121.58:80","198.52.241.12:999","23.143.160.21:999","212.23.217.71:8080","185.65.253.161:8081","176.101.179.17:8080","87.197.99.79:8088","190.113.41.201:999","148.101.52.27:8080","190.128.129.10:8080","190.128.241.102:80","36.229.87.75:80","210.201.86.72:8080","196.216.132.199:8080","197.245.230.122:41026","79.121.102.227:8080","79.172.212.99:3128","181.115.93.75:999","200.229.147.2:999","185.236.203.208:3128","185.38.111.1:8080","195.158.3.103:8080","88.119.139.237:53281","186.1.206.154:3128","196.207.16.22:8080","165.154.241.143:80","160.119.148.190:8080","178.169.139.180:8080","154.118.228.212:80","200.85.169.18:47548","43.245.85.252:80","14.198.21.70:80","120.82.174.128:9091","117.160.250.131:8899","117.160.250.131:8080","5.75.171.241:1080","103.197.251.202:80","42.228.61.245:9091","114.239.152.243:9002","117.160.250.134:8080","64.56.150.102:3128","155.248.197.241:9898","103.111.122.2:80","223.84.240.36:9091","36.34.244.130:9091","47.88.87.74:1080","116.63.130.30:1080","183.234.218.202:9002","1.224.3.122:3888","8.210.37.63:8888","120.236.66.134:9002","89.218.186.133:3128","47.243.86.12:443","117.160.250.132:9999","192.81.128.182:8089","117.160.250.130:8081","117.160.250.130:8828","117.159.37.40:9091","116.117.253.212:9002","183.221.242.104:8443","60.12.168.114:9002","181.205.61.115:999","117.158.173.216:9091","117.160.250.133:82","212.112.113.178:3128","148.76.97.250:80","195.201.57.62:3128","111.59.4.88:9002","216.137.184.253:80","178.151.205.154:45099","103.77.60.14:80","222.88.167.22:9002","62.193.108.130:1981","111.21.183.58:9091","54.86.198.153:80","117.159.97.46:9002","41.65.55.2:1981","80.154.30.180:80","117.160.250.132:8081","142.129.238.249:8888","139.162.78.109:8080","112.51.96.118:9091","181.225.101.14:999","117.160.250.132:81","190.92.239.132:8080","151.232.72.20:80","112.44.126.88:9091","8.219.97.248:80","8.210.37.63:80","122.3.41.154:8090","183.237.222.51:9002","130.41.101.105:8080","124.107.145.59:8081","117.160.250.133:9999","41.33.254.190:1976","158.69.71.245:9300","117.160.250.133:8081","213.230.108.161:8080","38.41.0.92:999","220.248.111.194:9002","117.160.250.137:8081","203.142.69.250:8080","161.35.70.249:3128","221.214.246.76:8989","188.235.0.207:8282","200.187.70.223:3128","103.69.2.79:999","113.53.231.133:3129","123.130.115.217:9091","103.165.253.133:3125","103.105.126.2:82","86.98.2.41:8080","222.89.237.101:9002","103.145.212.242:80","170.187.138.40:8009","117.160.132.37:9091","183.238.163.8:9002","179.1.192.9:999","135.181.15.198:3128","43.255.113.232:82","120.237.142.198:9091","188.32.241.34:81","50.201.51.216:8080","87.255.6.218:8080","49.231.0.178:58023","95.216.33.21:80","154.16.180.182:3128","138.219.246.240:9999","117.160.250.134:8828","198.52.115.114:1994","117.160.250.138:8899","103.36.8.244:8080","186.3.38.206:999","103.159.195.43:8080","174.70.1.210:8080","183.233.169.226:9091","24.230.33.96:3128","111.225.152.69:8089","103.85.114.240:8080","112.78.168.122:8080","154.118.228.212:80","91.224.168.22:8080","183.239.188.250:9002","218.252.244.104:80","196.251.222.174:8104","81.162.74.10:8080","8.134.140.97:8080","112.53.167.29:9091","46.105.87.167:53281","34.77.204.1:3128","61.28.224.211:3128","41.57.138.30:8080","117.251.103.186:8080","182.55.48.187:80","117.160.250.132:80","111.225.152.157:8089","43.255.113.232:8084","45.188.166.50:1994","117.160.250.163:80","185.135.157.89:8080"]

def init_passwordless_sms(phone_number):
    """
    Initializes a passwordless SMS authentication for the given phone number.

    Parameters:
        phone_number (str): The phone number to which the SMS authentication code should be sent.

    Returns:
        dict: The JSON response containing the result of the API call.
    """
    session = requests.Session()
    # Initialize Passwordless SMS
    url = "https://auth.privy.io/api/v1/passwordless_sms/init"
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin' : 'https://www.friend.tech',
        'Privy-App-Id':"cll35818200cek208tedmjvqp",
    }
    data = {"phoneNumber": phone_number}
    response = session.post(url, headers=headers, json=data)
    # Save session cookies for later use
    with open("session_cookies.json", "w") as f:
        json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
    return response.json()

def authenticate_with_mfa(phone_number, mfa_code, ft_wallet_addr):
    """
    Authenticates the user with multi-factor authentication (MFA).

    Args:
        phone_number (str): The phone number of the user.
        mfa_code (str): The MFA code for authentication.
        ft_wallet_addr (str): The address of the FT wallet.

    Returns:
        tuple: A tuple containing the token result and the authentication token.

    Raises:
        None.
    """
    session = requests.Session()
    # Load saved session cookies
    with open("session_cookies.json", "r") as f:
        cookies = json.load(f)
    session.cookies = requests.utils.cookiejar_from_dict(cookies)
    # Authenticate via SMS code
    url = "https://auth.privy.io/api/v1/passwordless_sms/authenticate"
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin' : 'https://www.friend.tech',
        'privy-app-id':"cll35818200cek208tedmjvqp",
    }
    data = {"phoneNumber": phone_number, "code": mfa_code}
    response = session.post(url, headers=headers, json=data)
    mfa_result = response.json()
    auth_token = mfa_result['token']
    ##################################
    ##  Get Signature URL TOKEN
    ##################################
    url_signing = "https://prod-api.kosetto.com/signature"
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin' : 'https://www.friend.tech',
        'privy-app-id':"cll35818200cek208tedmjvqp",
        "Authorization": auth_token
    }
    data = {"address":ft_wallet_addr}
    response = session.post(url_signing, headers=headers, json=data)
    token_result = response.json()
    return token_result['token'],auth_token


def get_friend_account_details(twitter_username,auth_token):
    """
    Retrieves the account details of a friend on Twitter.

    Args:
        twitter_username (str): The username of the friend on Twitter.
        auth_token (str): The authentication token for accessing the API.

    Returns:
        dict: The account details of the friend.

    Raises:
        Exception: If there is an error while making the API request.
    """
    url = f"https://prod-api.kosetto.com/search/users?username={twitter_username}"
    headers = {'accept': 'application/json',
               'Referer':'https://www.friend.tech/',
                'content-type':'application/json',
                "referrerPolicy": "strict-origin-when-cross-origin",
                "Authorization": auth_token}
    try:
        proxies = {
            'http': random.choice(proxy_list)
        }
        response = requests.get(url, headers=headers, proxies=proxies)
        data = response.json()
    except Exception as e:
        print(e)
    return data


def input_with_timeout(prompt, timeout):
    timer = threading.Timer(timeout, lambda: print('\nAuth Timeout. Hit Any Key To Start Again....', end=''), args=None)
    timer.start()
    try:
        answer = input(prompt)
    finally: 
        timer.cancel()
    if not answer:
        sys.exit("Exiting due to inactivity. If You MFA'ed more than 5 times, in an hour, you will be rate limited for 1 hour.")
    return answer

def account_search(twitter_account:str,auth_token:str):
    """
    Given a Twitter account and an authentication token, this function hunts for the account details of the specified Twitter account.
    
    Args:
        twitter_account (str): The Twitter account to be searched.
        auth_token (str): The authentication token required for the search.
        
    Returns:
        bool or dict: If the account is not found, the function returns False. Otherwise, it returns a dictionary containing the details of the found account.
    """
    account_lookup = get_friend_account_details(twitter_account,auth_token)
    if 'message' in list(account_lookup.keys()):
        logging.info(f"Account: {twitter_account} Not Found.... Continuing Search....")
        return False
    else:
        logging.info(f"Account Found!")
        return account_lookup['users'][0]

#launch chrome browser and get private key for buys later
def get_pv_key(phone_number):
    """
    Retrieves the private key for accessing the friend.tech wallet.

    :return: The private key as a string if successfully obtained, or -1 if failed.
    :rtype: Union[str, int]
    """
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--app=https://friend.tech")
    driver = webdriver.Chrome(options=options)
    try:
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        button = wait.until(EC.visibility_of_element_located((By.XPATH,'//button')))
        # Find the button element by its text content and click it
        # button = driver.find_element(By.XPATH,'//button')
        button.click()
        input_phone = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="phone-number-input"]')))
        input_phone.send_keys(phone_number)
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="privy-dialog"]/div/div/div[2]/div/div[1]/button')))
        login_button.click()
        driver.implicitly_wait(4)
        mfa_code = input("Enter the MFA code you received via SMS: ")
        input_mfa = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="privy-dialog"]/div/div/div[3]/div[2]/div[1]/div[2]/input[1]')))
        input_mfa.send_keys(mfa_code)
        driver.implicitly_wait(2)
        time.sleep(2)
        notfi_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div/div/div/main/div/div[5]/button')))
        notfi_button.click()
        profile_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="top-nav"]/div[2]/div/span[2]')))
        profile_button.click()
        export_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/div/div/div[2]/div[4]/div[8]/button')))
        export_button.click()
        driver.implicitly_wait(2)
        copy_key = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="privy-dialog"]/div/div/div[3]/div[3]/div/div/iframe')))
        time.sleep(4)
        copy_key.click()
        copy_key.click()
        copy_key.click()
        #copy private key and try again if it breaks
        time.sleep(3)
        priv_key = pyperclip.paste()
        if len(priv_key) < 60:
            time.sleep(3)
            copy_key.click()
            copy_key.click()
            copy_key.click()
            priv_key = pyperclip.paste()
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
    logging.info(f"KEY OBTAINED: {priv_key}")
    if len(priv_key) > 60:
        logging.info("FT_EXPORT.txt does not exist, Creating...")
        with open("FT_EXPORT.txt", "w") as f:
            f.write(priv_key)
        return priv_key
    else:
        logging.info("FAILED TO OBTAIN WALLET KEY. RE-RUN SCRIPT.")
        return -1

def buy_key(ft_wallet_addr,account_found,keys2buy,top_of_block,friendtech_contract_addr,friends_contract,web3,friendtech_private_key):
    buy_price_after_fee = friends_contract.functions.getBuyPriceAfterFee(web3.to_checksum_address(account_found['address']),keys2buy).call()
    current_wallet_balance = web3.eth.get_balance(web3.to_checksum_address(account_found['address']))
    if buy_price_after_fee > current_wallet_balance:
        logging.error(f"ETH Required:{buy_price_after_fee}| ETH in Wallet: {current_wallet_balance} \nNot Enough in wallet for purchase!")
        exit()
    else:
        try:
            buy_price= (friends_contract.functions.getBuyPrice(web3.to_checksum_address(account_found['address']),keys2buy).call())
            print(f"{account_found['twitterName']} : {web3.from_wei(buy_price_after_fee,'ether')} ETH")
            current_nonce = web3.eth.get_transaction_count(ft_wallet_addr)
            print(f"Current Wallet Nonce: {current_nonce}")
            data_tx = friends_contract.encodeABI(fn_name='buyShares', args=[web3.to_checksum_address(account_found['address']),keys2buy])
            #build tx params. Value is what the value of the key is without fee. Required Input
            if top_of_block == True:
                gasfee = 1
            else:
                gasfee = 0.1
            tx_params = {
                            'from': ft_wallet_addr,
                            'to': friendtech_contract_addr,
                            'chainId': 8453,
                            'value': int(buy_price_after_fee),
                            'maxFeePerGas': web3.to_wei(gasfee, 'gwei'),
                            'maxPriorityFeePerGas': web3.to_wei(gasfee, 'gwei'),
                            'gas': 6500000,
                            'nonce': current_nonce,
                            'data': data_tx
                        }
            #Sign and send TX
            signed_txn = web3.eth.account.sign_transaction(tx_params, private_key=friendtech_private_key)
            tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"Sent Transaction: {tx_token.hex()}")
            print(f"---------------- {account_found['twitterUsername']} Buy Successful!------------------")
            return account_found['twitterUsername'], tx_token.hex()
        except Exception as e:
            print("Failed to Buy!")
            print(e)
            return -1
def sendTGMessage(text,bot_father_token,channel_name):
    token = bot_father_token
    channel_name = channel_name
    telAPIurl = "https://api.telegram.org/bot{}/sendMessage".format(token)
    channel_url = telAPIurl + "?chat_id={}&text={}".format(channel_name,text)
    while True:
        try:
            request = requests.post(channel_url)
            if(request.status_code == 200):
                break
            else:
                continue
        except:
            continue


@click.group()
def cli():
    pass
#init Account and save data
@cli.command()
@click.argument('phone_number')
@click.argument('ft_wallet_addr')
@click.option('--auth_token_file', default='auth_token.txt', help="The file to save the auth token. Default is 'auth_token.txt'.")
@click.option('--ft_key_file', default='FT_EXPORT.txt', help="The file to save the FT key. Default is 'FT_EXPORT.txt'.")
@click.option('--enable_buy', default=False, type=bool, help="Whether to enable buying, requires wallet key. Default is False.")
def save_account_data(phone_number,ft_wallet_addr,auth_token_file='auth_token.txt',ft_key_file="FT_EXPORT.txt",enable_buy=False):
    """Save account data after MFA authentication and optional wallet key retrieval for buying.

    Arguments:
        phone_number: The phone number used for MFA.
        ft_wallet_addr: The FT wallet address.
        auth_token_file: The file to save the auth token. Default is 'auth_token.txt'.
        ft_key_file: The file to save the FT key. Default is 'FT_EXPORT.txt'.
        enable_buy: Whether to enable buying, requires wallet key. Default is False.
    """
    if os.path.exists(auth_token_file):
        logging.info("auth_token.txt exists, reading token.")
        with open(auth_token_file, "r") as f:
            auth_token = f.read().strip()
    else:
        logging.info("If You MFA more than 5 times, in an hour, you will be rate limited for 1 hour.")
        logging.info("auth_token.txt does not exist, proceeding with MFA.")
        result_init = init_passwordless_sms(phone_number)
        mfa_code= input_with_timeout("Enter the MFA code you received via SMS: ", 60)
        auth_token, privy_auth = authenticate_with_mfa(phone_number, mfa_code, ft_wallet_addr)
        logging.info("Authentication successful.")
        with open("auth_token.txt", "w") as f:
            f.write(auth_token)
        logging.info("Auth token written to auth_token.txt.")
        
    if enable_buy:
        if os.path.exists(ft_key_file):
            logging.info(f"{ft_key_file} exists, reading key.")
            with open(ft_key_file, "r") as f:
                friendtech_private_key = f.read().strip()
        else:
            logging.warning("DO NOT TOUCH THE CHROME SESSION!\nYOU WILL BREAK THE AUTOMATION AND HAVE TO START OVER!\nWait for MFA Prompt to show up in python terminal, only enter MFA Auth in terminal!\n\n\n")
            logging.info("DO NOT TOUCH THE CHROME SESSION!\nYOU WILL BREAK THE AUTOMATION AND HAVE TO START OVER!\nWait for MFA Prompt to show up in python terminal, only enter MFA Auth in terminal!\n\n\n")
            time.sleep(5)
            friendtech_private_key = get_pv_key(phone_number)
            if friendtech_private_key == -1:
                exit()
                
#account Hunter
@cli.command()
@click.argument('twitter_account')
@click.argument('ft_wallet_addr')
@click.option('--provider_rpc', default="https://mainnet.base.org", help="Provider RPC URL. Default is 'https://mainnet.base.org'.")
@click.option('--friendtech_private_key', default=None, help="Friendtech private key. Default is None.")
@click.option('--auth_token_file', default='auth_token.txt', help="The file to read the auth token from. Default is 'auth_token.txt'.")
@click.option('--ft_key_file', default='FT_EXPORT.txt', help="The file to read the FT key from. Default is 'FT_EXPORT.txt'.")
@click.option('--enable_buy', default=False, type=bool, help="Whether to enable buying. Default is False.")
@click.option('--top_of_block', default=False, type=bool, help="Top of block option. Default is False.")
@click.option('--check_interval', default=1, type=int, help="Check interval in seconds. Default is 1.")
@click.option('--keys2buy', default=1, type=int, help="Number of keys to buy. Default is 1.")
@click.option('--phone_number', default=None, help="Phone number for authentication. Default is None.")
@click.option('--bot_father_token', default=None, help="TG Bot Father Auth token to post to channel. Default is None.")
@click.option('--channel_name', default=None, help="TG Channel Name to post to ex: @FT_Alerts. Default is None.")

def hunt_account(ft_wallet_addr,twitter_account,provider_rpc,friendtech_private_key=None,auth_token_file='auth_token.txt',ft_key_file="FT_EXPORT.txt",enable_buy=False,top_of_block=False,check_interval=1,keys2buy=1,phone_number=None,bot_father_token=None,channel_name=None):
    """Hunt for a Twitter account and optionally buy shares.

        Arguments:
            ft_wallet_addr: The FT wallet address.
            twitter_account: The Twitter account to hunt.
            provider_rpc: The RPC provider URL. Default is 'https://mainnet.base.org'.
            friendtech_private_key: The FriendTech private key for signing transactions. Default is None.
            auth_token_file: The file containing the auth token. Default is 'auth_token.txt'.
            ft_key_file: The file containing the FT key. Default is 'FT_EXPORT.txt'.
            enable_buy: Whether to enable buying upon account finding. Default is False.
            top_of_block: Whether to set a higher gas fee for top-of-block inclusion. Default is False.
            check_interval: The interval in seconds between account hunt attempts. Default is 1.
            keys2buy: The number of keys to buy. Default is 1.
            phone_number: The phone number for headless MFA if auth_token is missing. Default is None.
    """
    web3 = Web3(Web3.HTTPProvider(provider_rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # Pre-stage web3 init for later purchase
    friendtech_contract_addr = web3.to_checksum_address("0xcf205808ed36593aa40a44f10c7f7c2f67d4a4d4")
    friends_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"trader","type":"address"},{"indexed":false,"internalType":"address","name":"subject","type":"address"},{"indexed":false,"internalType":"bool","name":"isBuy","type":"bool"},{"indexed":false,"internalType":"uint256","name":"shareAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"subjectEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"supply","type":"uint256"}],"name":"Trade","type":"event"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"supply","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeeDestination","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"sellShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeDestination","type":"address"}],"name":"setFeeDestination","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setProtocolFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setSubjectFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"sharesBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"sharesSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"subjectFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    friends_contract = web3.eth.contract(web3.to_checksum_address(friendtech_contract_addr), abi=friends_abi)

    # Check for buy scenario
    if os.path.exists(auth_token_file) and os.path.exists(ft_key_file) and enable_buy is True:
        logging.info("auth_token.txt exists, reading token.")
        with open(auth_token_file, "r") as f:
            auth_token = f.read().strip()
        with open(ft_key_file, "r") as f:
            friendtech_private_key = f.read().strip()
    #check for non-buy and no auth token
    elif os.path.exists(auth_token_file) and enable_buy is False and phone_number is not None:
        logging.info("Attempting Headless MFA.")
        result_init = init_passwordless_sms(phone_number)
        mfa_code = input("Enter the MFA code you received via SMS: ")
        auth_token, privy_auth = authenticate_with_mfa(phone_number, mfa_code, ft_wallet_addr)
        logging.info("Authentication successful.")
        with open("auth_token.txt", "w") as f:
            f.write(auth_token)
        logging.info("Auth token written to auth_token.txt.")
    #just hunting 
    elif os.path.exists(auth_token_file) and enable_buy is False:
        logging.info("auth_token.txt exists, reading token.")
        with open(auth_token_file, "r") as f:
            auth_token = f.read().strip()
        logging.info("auth_token.txt successfully read.")
    #error if no scenario exists
    else:
        logging.error("Missing AUTH TOKEN or FT_KEY file! Run (python friend_sniper.py --save_account_data) before starting.")
        exit(1)
    #Looking for account. Waiting....
    account_found = False        
    while account_found == False:
        account_found = account_search(twitter_account,auth_token)
        time.sleep(check_interval)

    ## TIME FOR BUY ##
    if account_found != False and enable_buy == True:
        account_name, tx_hash= buy_key(ft_wallet_addr,account_found,keys2buy,top_of_block,friendtech_contract_addr,friends_contract,web3,friendtech_private_key)
        if tx_hash and (bot_father_token is not None and channel_name is not None):
            message = f"Buy Alert! \n\
Accounts Bought: {account_name} \n\
Key Count: {keys2buy} \n\
TX: {tx_hash}\n"
        sendTGMessage(message,bot_father_token,channel_name)
        exit()

if __name__ == "__main__":
    cli()  