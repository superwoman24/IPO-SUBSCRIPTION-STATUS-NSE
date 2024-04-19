import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.nseindia.com/market-data/all-upcoming-issues-ipo")

# Wait for the table to be visible
wait = WebDriverWait(driver, 10)
table = wait.until(EC.visibility_of_element_located((By.ID, "publicIssuesCurrent")))

# Find all header cells in the table
header_cells = table.find_elements(By.TAG_NAME, "th")
headers = [cell.text for cell in header_cells if cell.text != "NSE BID DETAILS (ACROSS ALL CATEGORIES)"]

# Find all body rows in the table
body_rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Exclude the header row
data = []
for row in body_rows:
    # Find all cells in each row
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    data.append(row_data)

# Write data to CSV file
csv_filename = "ipo_data.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write headers
    csv_writer.writerows(data)  # Write data rows

print(f"Data has been written to {csv_filename}")

# Close the WebDriver
driver.quit()
