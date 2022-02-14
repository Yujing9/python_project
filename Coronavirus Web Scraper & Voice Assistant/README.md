# Coronavirus Web Scraper & Voice Assistant


## Web Scraper

Step 1 : Using parsehub to scrap data

## Get data:

Using parsehub -API get data

api_key 	The API key for your account. - Just like personal verification

```python
import requests
import json
API_KEY = "taeFe__wat9F"
PROJECT_TOKEN = "tWwAoJA7SUUR"
RUN_TOKEN = "tS447j8_RqSH"
response = requests.get(f'https://parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key":API_KEY})
data = json.loads(response.text)
print(data['country'])
print(type(data))
```

But we want to look at data more nicely.

Using class：

- init function
- get_data function 

```python
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
data = Data(API_KEY,PROJECT_TOKEN)
print(data.data)
		
```

And then, I wanna get more detailed data like total_cases and total_deaths

- create total_cases function 
- create total_deaths function

```python
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
```

Next, i need to download some libraries:pyttsx3 speech_recognition

*pyttsx3* is a text-to-speech conversion library in Python.

Library for performing *speech recognition*

```python
def speak(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()
speak("hello  你好啊好哈哈哈哈,牛啊，太有意思了")
```

download pyaudio to get our audio

```python
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
		except Exception as e:
			print("Exception:", str(e))

	return said.lower()
print(get_audio())
```

Then we need to set the main function 

Aim to implement get audio!

```python
def main():
	print("Started Program")
	END_PHRASE = "stop"
	while True:
		print("Listening...")
		text = get_audio()
		if text.find(END_PHRASE) :  # stop loop
			print("Exit")
			break
```

Set a dictionary to store some questions.

[\W\S] means anything of words

For example: how many total cases?

how many total deaths?

```python
TOTAL_PATTERNS = {
					re.compile("[\w\s]+ total [\w\s]+ cases"):data.get_total_cases,
					re.compile("[\w\s]+ total cases"): data.get_total_cases,
                    re.compile("[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
                    re.compile("[\w\s]+ total deaths"): data.get_total_deaths
					}
```

Then  we need to find anything from  total_patterns and then match we told the text , if True:invoke total_patterns 's function. 

And then speak the result

```python
	while True:
		print("Listening...")
		text = get_audio()
		result = None
		for pattern, func in TOTAL_PATTERNS.items():
			if pattern.match(text):
				result = func()
				break
		if result:
			speak(result)
		if text.find(END_PHRASE) :  # stop loop
			print("Exit")
			break
```

And then I wanna get more detailed data, I wanna get total cases and total deaths of the country.

lambda country: takes one variable country so as a parameter and when it takes that it will call and return this value 

```python
	COUNTRY_PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
                    re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths'],
					}
```

We set country_patterns over. We have to use it  , same like total_pattern, say text , match the text in pattern and then invoke function . 

In order to save time,we store all country name in list(paragraph 1). And we use variable "words " split all text , and match every words

```python
country_list = data.get_list_of_countries()
for pattern, func in COUNTRY_PATTERNS.items():
			if pattern.match(text):
				words = set(text.split(" "))
				for country in country_list:
					if country in words:
						result = func(country)
						break
```

## update

We have almost finished everything. But if data update, we need to updata again. It is very troublesome and annoying.

So we have to use function updata.

```python
	def update_data(self):
		response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

```

We need to modify the link , because the last link transfer the later data.

Then,we define function poll. Aim to use loop get new data. When finish one loop .take the rest.  We can easily find get_data() that could return anything. So modify it and return data and init data.

```python
def poll():
			time.sleep(0.1)
			old_data = self.data
			while True:
				new_data = self.get_data()
				if new_data != old_data:
					self.data = new_data
					print("Data updated")
					break
				time.sleep(5)
```

We wanna guarantee update and listen at the same time. So we use thread to create two thread. They can work in the meanwhile.

```
t = threading.Thread(target=poll)
t.start()
```

Finally, we want to apply that we say "update", then system start working.

```python
UPDATE_COMMAND = "update"
if text == UPDATE_COMMAND:
			result = "Data is being updated. This may take a moment!"
			data.update_data()
```

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Everything is over. Good job!
