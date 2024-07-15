from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.keys import Keys
import os
import time

start_time = time.time()

def find_element(driver, method, identifier):
    try:
        if method == "id":
            element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, identifier)))
        elif method == "name":
            element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, identifier)))
        else:
            raise ValueError("Invalid method provided")
        return element
    except NoSuchElementException:
        print(f"Element with {method} '{identifier}' not found.")
        return None
    except Exception as ex:
        print(f"Error occurred while finding element with {method} '{identifier}': {ex}")
        return None

def click_radio_button(driver, name_value=None, value=None):
    try:
        if name_value and value:
            locator = (By.XPATH, f"//input[@type='radio' and @name='{name_value}' and @value='{value}']")
            radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
            radio_button.click()
            print(f"Successfully clicked radio button for '{name_value}'.")
        else:
            print("Invalid name_value or value provided.")
    except Exception as ex:
        print(f"Error occurred while clicking radio button for '{name_value}': {ex}")

def click_checkbox(driver, name_value=None, value=None):
    try:
        if name_value and value:
            locator = (By.XPATH, f"//input[@type='checkbox' and @name='{name_value}' and @value='{value}']")
            checkbox_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
            checkbox_button.click()
            print(f"Successfully clicked checkbox button for '{name_value}'.")
        else:
            print("Invalid name_value or value provided.")
    except Exception as ex:
        print(f"Error occurred while clicking checkbox button for '{name_value}': {ex}")

def close_modal(driver):
    try:
        modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "modal-fullscreen")))
        close_btn = modal.find_element(By.CLASS_NAME, "close")
        close_btn.click()
        print("Closed the modal dialog.")
    except Exception as ex:
        print("Error occurred while closing the modal dialog:", ex)

def fill_select2_dropdown(driver, field_id, value):
    try:
        input_field = driver.find_element(By.ID, field_id)
        input_field.click()
        time.sleep(1)
        search_field = driver.find_element(By.CLASS_NAME, "select2-search__field")

        search_field.send_keys(value)
        time.sleep(1)
        search_field.send_keys(Keys.ARROW_DOWN)
        search_field.send_keys(Keys.ENTER)
    except Exception as ex:
        print(f"Failed to find or fill '{field_id}':", ex)

def fill_form(driver, url, field_data):
    driver.get(url)
    invalid = []
    result = []
    
    try:
        time.sleep(1)
        
        for field, value in field_data.items():
            time.sleep(1)
            try:
                if field.startswith("Next"):
                    
                    print("--- %s seconds ---" % (time.time() - start_time))
                    next_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/ul/li[2]/a")))
                    next_link.click()
                    print("Successfully clicked 'Next' link.")
                    try:
                        toast_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]')))
                        
                        toast_message_element = WebDriverWait(toast_element, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'igrowl-message')))
                        
                        if toast_message_element:
                            errortoast = toast_message_element.text
                            invalid.append(errortoast)
                            print("Toastify notification:", toast_message_element.text)
                            break
                    
                    except:
                        pass
                    error_tags = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.sfError")))
                    if error_tags:
                        for error_tag in error_tags:
                            error_for = error_tag.get_attribute("for")
                            invalid.append(error_for)
                        print("Invalid fields:", invalid)
                    break
                    
    
                elif field == "submissionCode":
                    submission_code_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "submissionCode")))
                    email_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "emailAddress")))
                    submission_code = submission_code_element.text
                    email = email_element.text
                    x = {"submission": submission_code, "email": email}
                    result.append(x)

                if field.startswith("VideoKyc"):
                    print("--- %s seconds ---" % (time.time() - start_time))
                    videoKyc_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/div/div/form/div/div[2]/section[7]/div/div/div/div[1]/div/span/img")))
                    videoKyc_link.click()
                    print("Successfully clicked 'videoKyc' link.")
                    print(f"Popping '{field}' from field_data.")
                    # field_data.pop(field)
                if field.startswith("finish"):
                    print("--- %s seconds ---" % (time.time() - start_time))
                    finish_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/ul/li[3]/a")))
                    finish_link.click()
                    print("Successfully clicked 'finish' link.")
                if field.startswith("Ok"):
                    print("--- %s seconds ---" % (time.time() - start_time))
                    ok_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/button[1]")))
                    ok_link.click()
                    print("Successfully clicked 'ok' link.")
                    print(f"Popping '{field}' from field_data.")
                    
                if field == ("finalok"):
                    print("--- %s seconds ---" % (time.time() - start_time))
                    ok_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/button")))
                    ok_link.click()
                    print("Successfully clicked 'ok' link.")
                    print(f"Popping '{field}' from field_data.")
                    
                elif field == "isMinor" and value:
                    input_field = find_element(driver, "id", field)
                    if input_field:
                        input_field.click()
                        time.sleep(1)
                        print("Selected 'isMinor'.")
                    
                elif field.startswith("select2"):
                    fill_select2_dropdown(driver, field, value)
                    
                elif field == "isPermanentAddressSameAsCurrentAddress" and value:
                    input_field = find_element(driver, "id", field) or find_element(driver, "name", field)
                    if input_field:
                        input_field.click()
                        print("--- %s seconds ---" % (time.time() - start_time))
                        time.sleep(1)
                   

                elif field.startswith("file"):
                    file_field = value.get("field")
                    file_path = value.get("value")

                    if file_field and file_path:
                        print(f"Attempting to fill '{file_field}'...")
                        input_field = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, file_field)))
                        abs_file_path = os.path.abspath(file_path)
                        input_field.send_keys(abs_file_path)
                        print(f"Successfully filled '{file_field}' with '{file_path}'.")
                        
                    else:
                        print(f"Missing field or file path for '{field}'.")

                else:
                    input_field = find_element(driver, "name", field)
                    if input_field:
                        input_type = input_field.get_attribute("type")
                        if input_type == "text":
                            input_field.clear()
                            input_field.send_keys(value)
                            print(f"Successfully filled '{field}' with value '{value}'.")
                        elif input_field.tag_name == "input" and input_type == "radio":
                            click_radio_button(driver, field, value)
                        elif input_field.tag_name == "input" and input_type == "checkbox":
                            click_checkbox(driver, field, value)
                        elif input_field.tag_name == "select":
                            input_field.send_keys(value)
                            print("--- %s seconds ---" % (time.time() - start_time))
                        
                    else:
                        input_field.click()
            except NoSuchElementException:
                close_modal(driver)  # Close the modal dialog if element not found
                continue
            except ElementClickInterceptedException:
                print("Element is not clickable, trying again...")
                time.sleep(2)
                continue
            except WebDriverException as e:
                error_message = e.msg
                print("Error message:", error_message)
            except Exception as ex:
                print(f"Failed to find or fill '{field}':", ex)

    except Exception as e:
        print("An error occurred:", e)
        pass
    

    return {'invalid': invalid, 'submissionNo': result}
