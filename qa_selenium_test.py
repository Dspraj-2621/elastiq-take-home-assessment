import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SELENIUM_PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
SEARCH_TERM = "New York"
EXPECTED_RESULT_COUNT = 1
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
def search_table(driver, search_term):
    driver.get(SELENIUM_PLAYGROUND_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
    )
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.send_keys(search_term)

    all_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    print(f"Total rows before filtering: {len(all_rows)}")


def validate_results(driver, expected_count):
    # Wait for rows to update
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table[@id='example']/tbody/tr"))
    )
    rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style, 'display: none'))]")
    actual_count = len(rows)

    print("Filtered Rows:")
    for row in rows:
        print(f"Visible Row: {row.text}")


    print(f"Expected results: {expected_count}, Actual results: {actual_count}")
    assert actual_count == expected_count, f"Test failed: Expected {expected_count} but got {actual_count}"



def main():
    driver = setup_driver()
    try:
        search_table(driver, SEARCH_TERM)
        validate_results(driver, EXPECTED_RESULT_COUNT)
        print("Test passed: The search results are correct.")
    except AssertionError as e:
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
