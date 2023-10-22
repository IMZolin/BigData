import requests
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":
    base_url = "http://www.pogodaiklimat.ru/monitor.php?id=29645"
    with open("kemerovo.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        headers = ["Year", "MeanTemp"]
        writer.writerow(headers)

        for year in range(2000, 2023):
            total_mean_temp = 0.0
            count = 0
            for month in range(1, 13):
                url = f"{base_url}&month={month}&year={year}"
                response = requests.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    table = soup.find('table')
                    if table:
                        rows = table.find_all('tr')
                        for row in rows[2:]:
                            cells = row.find_all('td')
                            if len(cells) >= 3:
                                mean_temp_str = cells[2].get_text(strip=True)
                                if mean_temp_str:
                                    mean_temp = float(mean_temp_str.replace(",", ".")) 
                                    total_mean_temp += mean_temp
                                    count += 1
            if count > 0:
                yearly_mean_temp = total_mean_temp / count
                data = [year, yearly_mean_temp]
                writer.writerow(data)
            else:
                print(f"Could not get data for year={year}")

    print("The data is written to a file 'kemerovo.csv'.")
