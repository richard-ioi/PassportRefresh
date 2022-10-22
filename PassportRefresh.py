# Import the required modules
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def getAnswer():
    while(True):
        print("Inserez O pour Oui ou N pour Non")
        answer=input().upper()
        if(answer=='O'):
            return True
        elif(answer=='N'):
            return False

def connect():
    driver.get('https://v70-auth.paris.fr/auth/realms/paris/protocol/openid-connect/auth?client_id=W78-PROD&response_type=code&redirect_uri=https%3A%2F%2Fteleservices.paris.fr%2Frdvtitres%2Fservlet%2Fplugins%2Foauth2%2Fcallback%3Fdata_client%3DauthData&scope=openid+profile+email+address+phone&state=238de4c1cb588&nonce=1be04a38f9f20')
    driver.find_element(By.NAME,'username').send_keys(login)
    driver.find_element(By.NAME,'password').send_keys(password)
    driver.find_element(By.NAME,'Submit').click()
    

def check_through_mairies():
    i=28
    driver.get('https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointment&view=getViewAppointmentCalendar&id_form='+str(i)+'&nbPlacesToTake=1')
    while(check_exists_by_class_name("fc-event-container")==False):
        if(i>=45):
            i=28
            time.sleep(10)
        else:
            i+=1
        driver.get('https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointment&view=getViewAppointmentCalendar&id_form='+str(i)+'&nbPlacesToTake=1')

    driver.find_element(By.CLASS_NAME,'fc-event-container').click()
    appointment_fill_infos()

def check_exists_by_id(id):
    try:
        driver.find_element(By.ID,id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(class_name):
    try:
        driver.find_element(By.CLASS_NAME,class_name)
    except NoSuchElementException:
        return False
    return True

def appointment_fill_infos():

    i=0
    while(check_exists_by_id('attribute'+str(i)) == False):
        i+=1
    driver.find_element(By.NAME,'attribute'+str(i)).send_keys(phone)
    i+=1
    while(check_exists_by_id('attribute'+str(i)) == False):
        i+=1
    driver.find_element(By.NAME,'attribute'+str(i)).send_keys(postalCode)

    driver.find_element(By.NAME,"save").click()
    


# Main Function
if __name__ == '__main__':

    login="LOGIN"
    password="PASSWORD"
    postalCode="75012"
    phone='0612345678'
    
    # print("=========")

    # print("Prenom ?")
    # firstname=input().capitalize()
    # print("OK, votre prenom est " + firstname)

    # print("=========")

    # print("Nom de famille ?")
    # lastname=input().upper()
    # print("OK, votre nom est " + lastname)

    # print("=========")

    # print("Code postal ?")
    # postalCode=''
    # while(len(postalCode)!=5):
    #     print("Le format doit etre 00000")
    #     postalCode=input().upper()
    # print("OK, votre code postal est " + postalCode)

    # print("=========")

    # print("e-mail ?")
    # email=input().lower()
    # print("OK, votre e-mail est " + email)

    # print("=========")

    # print("Numero de telephone ?")
    # phone=''
    # while((len(phone)!=10) or (phone.isnumeric()==False)):
    #     print("Le format doit etre 0612345678")
    #     phone=input()

    # print("=========")


    print("=========")

    print("\nMerci pour ces informations, lancement de la recherche...")

    print("\n=========")

    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Edge(executable_path="Drivers/msedgedriver.exe", options = options)
    driver.set_window_size(1920,1080)

    connect()
    check_through_mairies()

    # Quits the driver
    #driver.close()
    #driver.quit()