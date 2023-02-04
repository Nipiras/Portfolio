import requests
from collections import Counter
import pandas as pd

class CrimeReport():
  def __init__(self, location, date, category = "all-crime"):
    self.location = location
    self.date = date
    self.category = category
    self.sherif = self.sherif()

  def sherif(self):
    crime_URL = "https://data.police.uk/api/crimes-no-location"
    payload = {
        "category": self.category,
        "force": self.location,
        "date": self.date}
    response = requests.get(crime_URL, params=payload)

    if response.status_code == 200:
      return response.json()
    else:
      return None

  def report_crimes(self):
    crimes_list = []

    if self.sherif is not None:
      for crime in self.sherif:
        crimes_list.append(crime["category"])
        final = Counter(crimes_list)
        final_df = pd.DataFrame.from_dict(final, orient="index").reset_index()
        final_df = final_df.rename(columns={"index":"Crime Category", 0:"Count"})
      return final_df