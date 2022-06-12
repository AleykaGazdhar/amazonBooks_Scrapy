# amazonBooks_Scrapy
I have scraped Amazon Book Section using Scrapy(2.6.1) Framework, Python(3.10.0 version) and have stored the scraped data in MongoDB(5.0.9) using Pymongo(4.1.1) library of python
Create a folder for project, you want to scrap and go inside that to create a virtual Env by following command :" Virtualenv ." and activate it by following command: " .\scripts\activate
Virtual Environment is mostly preferd as it keeps the project isolated, whatever packages and libraries needed for that particular project are inside the env. and we can directly deploy them on github by keeping them isolated from whole system.
Then Install Scrapy by typing this command in cmd :" pip install Scrapy" , you can also specify the version of scrapy while installing.
Start Project by typing this command in terminal :" srapy startproject <project-name> and this will create a number of files and folders that includes a basic skeleton to get started quickly:
  
                       ![Startproject](https://user-images.githubusercontent.com/86855712/173240434-98265aa2-4ca3-4399-ad37-38d606268e83.png)
In above picture-
Settings.py : Contains setting of spider, it has BOT_NAME which is your project name, USER_AGENT: Identification of yours, ROBOTSTXT_OBEY crawl by obeying this.
Items.py : Here we specify the website items or categories(like product_name, product_author, product_price, product_imagelink) etc to be scraped.
Pipelines.py : This is used to save data, which is scraped in database.
middleware.py: This is used to make changes to data before storing & also used as a proxy to request.
Now we will create first Spider named "website_spider.py", inside amazonwebsite/amazonwebsite/spiders,  we can name the spider anything we want.
Now in website_spider.py file we will write the Scraping Code of spider to scrap the pages. 
I have used CSS SELECTOR to extract particular items or code from source code. Scrapy Shell is same as cmd prompt in windows to help control scrapy in command line mode, here you can see wether the selector you have selected is extracting the correct item or not by typing following commond:"Scrapy Shell" and fetch("paste URL of website")
Instead of CSS SELECTOR, XPATH SELECTOR can also be used.
After the data is scraped and stored in temporary containers known as ITEMS. We can now store them in JSON, XML or CSV format by following command: scrapy crawl <name of your spider> -o items.json, or scrapy crawl <name of your spider> -o items.xml or scrapy crawl <name of your spider> -o items.csv.
In PIPELINES.py file, we store the crawled data stored in temporary containers known as ITEMS to a database(MYSQL, SQLite, MONGODB etc)  
