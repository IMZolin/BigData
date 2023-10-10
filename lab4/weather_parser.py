import requests
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":
    base_url = "http://www.pogodaiklimat.ru/monitor.php?id=29645"
    with open("kemerovo.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Headers CSV
        headers = ["FullDate", "MeanTemp"]
        writer.writerow(headers)

        # Yaers and months in cycles
        for year in range(2021, 2023):
            for month in range(1, 13):
                url = f"{base_url}&month={month}&year={year}"
                
                # Send GET request
                response = requests.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    table = soup.find('table')
                    if table:
                        rows = table.find_all('tr')
                        for row in rows[2:]:
                            cells = row.find_all('td')
                            if len(cells) >= 3:
                                date = cells[0].get_text(strip=True)
                                mean_temp = cells[2].get_text(strip=True)
                                full_date = f"{year}-{month}-{date}"
                                data = [full_date, mean_temp]
                                writer.writerow(data)  
                else:
                    print(f"Could not get data for year={year} и month={month}")

    print("The data is written to a file 'kemerovo.csv'.")