import requests
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import warnings

## supressing depracation warnings just for less clutter - has no effect on program
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def header():
    print("""
============================================================================

                    GOOGLE INURL QUERYING
                          by: AJH                        

============================================================================
""")

## also supresses warning logs that have no effect on program
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

## Installs Chrome Driver Manage - added this for a pathing quick fix in the meantime
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

## Runs selected queries, opens web browser to show results
def run_query(query):
    driver.get("https://www.google.com/search?q=inurl:" + query)   
    print("----------------------------------------------------------------------------")
    print("")
    print("Loading Web Results in Chrome Window") 
    main_menu()
    return

## List of premade inurl queries
def presets_menu():
    header()
    query = input("""
                1. 2082/frontend -demo
                2. /shop.cgi/page= | /shop.pl/page=
                3. "robot.txt" | "robots.txt"  intext:disallow filetype:txt
                4. "auth_user_file.txt"
                5. passlist.txt
                6./view.shtml
                7./view/index.shtml
                8./mjpg/video.mjpg
                9./cgi-bin/camera?resolution=
                10. go back
                """)
    if query == "1":
        ## Makes sure only one browser window is open 
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("2082/frontend -demo")
    elif query == "2":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("/shop.cgi/page= | /shop.pl/page=")
        presets_menu()
    elif query == "3":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("""robot.txt" | "robots.txt" intext:disallow filetype:txt""")
        presets_menu()
    elif query == "4":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("auth_user_file.txt")
        presets_menu()
    elif query == "5":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("passlist.txt")
        presets_menu()
    elif query == "6":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("/view.shtml")
        presets_menu()
    elif query == "7":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("/view/index.shtml")
        presets_menu()
    elif query == "8":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("/mjpg/video.mjpg")
        presets_menu()
    elif query == "9":
        if len(driver.window_handles) > 1:
            driver.close()
        run_query("/cgi-bin/camera?resolution=")
        presets_menu()
    elif query == "10":
        main_menu()
    else:
        presets_menu()
    return

def main_menu():
    header()
    select = input("""  
            Select an Option to begin:
            1. Choose a premade query string.
            2. Craft a custom query string.
            3. Exit
            """)
    if select == "1":
        presets_menu()
    elif select == "2":
        custom = input("""
        Enter custom query string, or type 2 to go back.
        """)
        if custom == "2":
            main_menu()
        else:
            run_query(str(custom))
    elif select == "2":
        os._exit(0)
    return
try:
    main_menu()
except KeyboardInterrupt:
    os._exit(0)
