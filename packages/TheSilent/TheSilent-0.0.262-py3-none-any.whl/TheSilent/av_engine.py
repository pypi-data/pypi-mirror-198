from TheSilent.clear import *
from TheSilent.form_scanner import *
from TheSilent.return_user_agent import *

import os
import re
import requests

cyan = "\033[1;36m"
red = "\033[1;31m"

def av_engine(file = " ", url = " ", secure = True):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    my_url = my_secure + url
    
    if url != " ":
        clear()
        
        identity_theft = ["social.*security", "ssn"]
        suspicious = ["atob.*\(", "free\s+movie", "movie\s+free", "under\s+construction"]
        tech_support_scam = ["hack", "infect", "trojan", "virus"]

        try:
            result = requests.get(my_url, headers = {"User-Agent":return_user_agent()}, timeout = (5,30)).text.lower()

        except requests.exceptions.SSLError:
            print(red + "")
            clear()
            return "suspicious (invalid certificate)"
        
        except:
            print(red + "")
            clear()
            return "ERROR!"

        for i in identity_theft:
            form_result = form_scanner(url, secure = secure)
            scan = re.search(i, str(form_result))
            
            if scan:
                print(red + "")
                clear()
                return "identity theft"

        for i in suspicious:
            scan = re.search(i, result)
            if scan:
                print(red + "")
                clear()
                return "suspicious"

        accuracy = 0
        for i in tech_support_scam:
            scan = re.search(i, result)

            if accuracy == 2:
                print(red + "")
                clear()
                return "tech support scam"

            if scan:
                accuracy += 1

        print(cyan + "")
        clear()
        return False

    if file != " ":
        mal_list = []

        ransomware_file_boolean = False
        ransomware_keyword_boolean = False
        ransomware_payment_boolean = False

        ransomware_file_list = ["document", "download", "jpeg", "jpg", "pdf", "picture", "txt"]
        ransomware_keyword_list = ["\d\.\d\.\d\.d", "b64", "base64", "crypt", "decode", "http", "socket"]
        ransomware_payment_list = ["bitcoin", "ethereum", "monero"]

        if os.path.isfile(file):
            clear()

            try:
                with open(file, "rb") as f:
                    for i in f:
                        result = i.decode(errors = "ignore").lower()

                        for ii in ransomware_file_list:
                            parse = re.search(ii, result)
                            if parse:
                                ransomware_file_boolean = True
                                break

                        for ii in ransomware_keyword_list:
                            parse = re.search(ii, result)
                            if parse:
                                ransomware_keyword_boolean = True
                                break

                        for ii in ransomware_payment_list:
                            parse = re.search(ii, result)
                            if parse:
                                ransomware_payment_boolean = True
                                break

                        if ransomware_file_boolean and ransomware_keyword_boolean and ransomware_payment_boolean:
                            print(cyan + "")
                            clear()
                            return True

                        else:
                            print(cyan + "")
                            clear()
                            return False
                        
            except:
                print(red + "can't open: " + str(os.path.join(path, i)))

        if os.path.isdir(file):
            clear()
            for path, current_directory, files in os.walk(file):
                for i in files:
                    new_file = os.path.join(path, i)
                    print(cyan + "checking: " + new_file)
                    try:
                        ransomware_file_boolean = False
                        ransomware_keyword_boolean = False
                        ransomware_payment_boolean = False
                        
                        with open(new_file, "rb") as f:
                            for ii in f:
                                result = ii.decode(errors = "ignore").lower()
                                

                                for iii in ransomware_file_list:
                                    parse = re.search(iii, result)
                                    if parse:
                                        ransomware_file_boolean = True

                                for iii in ransomware_keyword_list:
                                    parse = re.search(iii, result)
                                    if parse:
                                        ransomware_keyword_boolean = True

                                for iii in ransomware_payment_list:
                                    parse = re.search(iii, result)
                                    if parse:
                                        ransomware_payment_boolean = True

                                if ransomware_file_boolean and ransomware_keyword_boolean and ransomware_payment_boolean:
                                    mal_list.append("ransomware: " + new_file)
                                    break

                    except:
                        print(red + "can't open: " + new_file)
            
        mal_list.sort()
        clear()
        
        print(cyan + "threats:")
        for mal in mal_list:
            print(cyan + mal)