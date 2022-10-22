# Import the required modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def getAnswer():
    while(True):
        print("Inserez O pour Oui ou N pour Non")
        answer=input().upper()
        if(answer=='O'):
            return True
        elif(answer=='N'):
            return False

def check_through_mairies():
    i=28
    driver.get('https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointment&view=getViewAppointmentCalendar&id_form='+str(i)+'&nbPlacesToTake=1')
    while(check_exists_by_class_name("fc-event-container")==False):
        if(i>=45):
            i=28
        else:
            i+=1
        driver.get('https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointment&view=getViewAppointmentCalendar&id_form='+str(i)+'&nbPlacesToTake=1')

    driver.find_element_by_class_name("fc-event-container").click()
    appointment_fill_infos()

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

def appointment_fill_infos():
    driver.find_element_by_name('lastname').send_keys(lastname)
    driver.find_element_by_name('firstname').send_keys(firstname)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('emailConfirm').send_keys(email)

    i=0
    while(check_exists_by_id('attribute'+str(i)) == False):
        i+=1
    driver.find_element_by_name('attribute'+str(i)).send_keys(phone)
    i+=1
    while(check_exists_by_id('attribute'+str(i)) == False):
        i+=1
    driver.find_element_by_name('attribute'+str(i)).send_keys(postalCode)

    driver.find_element_by_name("save").click()


# Main Function
if __name__ == '__main__':

    firstname='Jean'
    lastname='DUPONT'
    postalCode='75001'
    email='mail.example@mail.fr'
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

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe", options = options)
    driver.set_window_size(1920,1080)

    check_through_mairies()

    # Quits the driver
    #driver.close()
    #driver.quit()