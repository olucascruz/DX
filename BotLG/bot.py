# Import for the Web Bot
from botcity.web import WebBot, Browser, By
import os
import requests

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
def open_buttons(bot):
        with open(os.path.abspath("utilsJS\main.js"), "r") as code_js:
            bot.execute_javascript(code=code_js.read())


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    bot.driver_path = os.path.abspath("geckodriver-win\geckodriver.exe")
    path_download = os.path.abspath("downloads_reports")


    # Opens the BotCity website.
    bot.browse("https://www.lg.com/global/investor-relations-reports")

    # Implement here your logic...
    bot.scroll_down(4)
    
    unit_boxes = bot.find_elements("unit-box", By.CLASS_NAME)
    groups_links = unit_boxes[0].find_elements_by_class_name("day-timeline")
    
    dict_link_download = dict()
    list_link_download = list()
    open_buttons(bot)

    for group in groups_links:
        head_title = group.find_element_by_class_name("day-timeline-head")
        title_test = head_title.find_element_by_tag_name("h3")
        new_folder = f"{path_download}\{title_test.text}"
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
       
        links_download = group.find_elements_by_class_name("download-item")
        list_link_download = list()
        for link in links_download:
            try:
                a = link.find_element_by_tag_name("a")
                list_link_download.append(a.get_attribute("href"))
                
            except Exception: pass
        dict_link_download[title_test.text] = list_link_download
    bot.stop_browser()

    for year, links in dict_link_download.items():
        
        for link in links:
            name_file = link.split("/")[-1]
            response = requests.get(link)    

            if response.status_code == 200:
                try:
                    with open(f"{path_download}\{year}\{name_file}", 'wb') as file:
                        file.write(response.content)
                    print(f'Arquivo {name_file} baixado com sucesso.')
                except Exception as err:
                    print(err)
            else:
                print(f'Erro ao baixar o arquivo. Código de status: {response.status_code}')

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    # bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
