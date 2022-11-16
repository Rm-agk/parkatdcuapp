# 2023-ca377-ejikec2-parkatdcu

CA377_2022_23 project 'Park at DCU'
## Description
The ParkAtDCU App is to allow access to realtime information about DCU carpark spaces.
I made this ParkAtDCU app with 3 main pages, the home page, maps page and Bus stops page.
In the home page users will be able to navigate to the realtime information about DCU carpark spaces, DCU social media links and DCU official footer links
In the Maps page, there is maps of the campuses in which the carparks are located and there is also a description of each campus background.
In the Bus stops page, there is a list of bustops located at dcu campuses with an interative map. It also displays a link to the real time dublin bus stops information.


## How to Install
### Dependencies
1. If you don't have python installed, go to [python.org](https://www.python.org/downloads/) and follow the installation instructions.
2. Open a command line and install the necessary python packages by running the following commands:
``pip install django``
``pip install requests``

### How to Run the App
1. Download the git repo by clicking the download button and choosing .zip as the file type.
2. Extract the zip file and navigate to **2023-ca377-ejikec2-parkatdcu\2023-ca377-ejikec2-parkatdcu\src\ca377**
3. Run the following commands to create an mySQL database and import data from the JSON files

<code>python manage.py migrate
python manage.py loaddata ../../data/campus.json
python manage.py loaddata ../../data/carpark.json
</code>

4. Open a command line and run ``python manage.py runserver``
The web application is now running, you can open it by going to  [localhost](127.0.0.1:8000)

### How to run the test cases
In the same directory as above, run the command ``python manage.py test parkatdcu``