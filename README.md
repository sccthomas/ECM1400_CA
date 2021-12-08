# **INSTRUCTIONS FOR COVID 19 DASHBOARD**

## **INTRODUCTION**

This program creates a COVID 19 dashboard with up-to-date information of current covid levels and relevant news on the status of the pandemic.
The numeric data shown on the dashboard will be the total 7 day cases in your selected area along with a separate amount for your country,
the current hospital admissions and the total number of deaths in you country. On the right-hand side of the dashboard will be a widget containing the
latest news that relates to COVID 19; and on the left and lower centre will be a scheduling widget for you to create update schedules so that the data shown on
the dashboard will update periodically.

## **PREREQUISITES:**

- Python 3.6 and above

Dependencies that are not in the installation are:

- Libraries
  - logging
  - datetime
  - time
  - sched
  - requests
- Internal modules
  - config
  - handlers_logging
  - covid_data_handler
  - covid_news_handling
  - covid_data_interface
- Files
  - config.json (stored in modules folder)
  - nation_2021-10-28.csv

## **MODULE INSTALLS FOR PROGRAM:**

- In the command terminal run these commands
- pip install Flask
- pip install uk-covid19
- pip install newsapi-python
- pip install pytest

## **USING THE DASHBOARD**

- EXECUTING CODE:
  In order to execute the code you must execute the covid_data_interface.py file and then go to http://127.0.0.1:5000/

  Use the command : python -m covid_data_interface (You run this with the correct rootdir)

- LOCATION:
  In-order to change the location used in the program and see relevant data to your location, you must edit the value for the key 'Location' in the config.json file.
  Once changed the appropriate data will appear after a restarting of the server (run code again).

- COUNTRY:
  In-order to change the country the dashboard shows you can edit the country label in the config.json file. \*Note these countries must be in the UK

- LANGUAGE:
  In-order to change the language of the articles in the articles widget you can change this in the config file under the key 'Language'

- ARTICLE RETURNED:
  Once an article has been removed you are able to undo your action by going in the config file removing the article from the file.
  You are also able to change the articles collected by changing the filter key in the config file so that other news is returned

- NEWS WIDGET:
  The news widget allows you the user to permanently remove news articles that you know longer want to see. once removed they will be stored in the config file for you
  to allow back in or view if you remain interested in that article.
  To remove an article click the 'X' icon of the article you want removed and it will immediately and permanently be deleted.

- SCHEDULES WIDGET:
  The schedules widget allows for updates to the dashboards data to be scheduled. Within this there are 5 components.

      1. Setting a time for your schedule; by clicking on the time entry field you can select a time for the future using the scroll wheel style provided
      2. Choosing a name for you schedule; by clicking on the name entry field and typing in the schedules name
      3. Selecting repeat; a schedule has the ability to repeat itself so that is occurs 24hours ahead of the previous one. Select this option by ticking its box or not
      4. Update covid data; a schedule can be selected to update the covid 19 data on the dashboard by selecting the tick box provided
      5. Update news data; a schedule can be selected to update the news data on the dashboard by selecting the tick box provided

- NOTE - You can select both news and covid to be updated

#### **HOW THE CODE IS STRUCTURED:**

The code is structured, where there are 5 modules, each with a purpose and job in the composition of the dashboard.

- covid_data_interface:
  This is the main module that combines all other modules to create a flask interface with the appropriate data. This module handles the presentation of news, creation/running/deletion of schedules
  and the presentation of COVID 19 data. I have used OOP structures so that variables can be passed through efficiently and so that I don't have many global variables.

- covid_data_handler:
  This is a module that will handle the collection and processing, along with executing of due schedules of covid 19 data. There is a key function called covid_API_request, this is the function that will call the request
  for collecting the latest covid 19 data from the uk_covid19 module. From there it is passed to another function that will process the data so that we get 3 key values, 7 day infection rate, total deaths
  and the current hospital admissions.

- news_data_handling:
  This is a module that will handle the collection and processing, along with executing of due schedules of api news data. There is a key function called news_API_request, whose purpose is to collect the current news related to
  covid 19 using the request module and the newAPi module. Once collected the articles will be passed onto a processing function that will remove the unwanted covid 19 news articles that the user has chosen to remove.

- config:
  This is a module that will handle the opening and handling of the conig.json file. At the start of the module it will collect the relevant data from the config file so that it can be used elsewhere in other modules
  There are two main functions, one for writing in the config file and the other for removing executed schedules from the scheduler in the config file. Firstly the writing of the config file works by having a large list that contains
  many other list in a dictionary format. When changing the config file you change one part of this list and it will be updated in the config file when it is overwritten.

- logging:
  This is a module that will handle the logging of events in the covid 19 dashboard. It will create logging files for each module so that they can record events

## **TESTING:**

For testing I am using the pytest module. You will be able to run testing by entering this command to the cmd. This must be ran in the files directory.

python -m pytest

## **APPENDIX**

- GitHub:
  link : https://github.com/sccthomas/ECM1400_CA

- COVID 19 MODULE:
  link : https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/pages/getting_started.html
- NEWS API MODULE:
  link : https://newsapi.org/docs/get-started
