import requests
import json
API_KEY = "taeFe__wat9F"
PROJECT_TOKEN = "tWwAoJA7SUUR"
RUN_TOKEN = "tS447j8_RqSH"
class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.get_data()
	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		self.data = json.loads(response.text)
	def get_total_cases(self):
		data = self.data['total']
		for content in data:
			if content['name'] == "Coronavirus Cases:":
				return content['value']
	def get_total_deaths(self):
		data = self.data['total']
		for content in data:
			if content['name'] == "Deaths:":
				return content['value']
    def __init__(self):
        return False
data = Data(API_KEY,PROJECT_TOKEN)


