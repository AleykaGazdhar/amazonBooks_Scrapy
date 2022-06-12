# amazonBooks_Scrapy
I have scraped Amazon-Book Section using ScrapyFramework(2.6.1), Python(3.10.0 version) and have stored the scraped data in MongoDB(5.0.9) using Pymongo(4.1.1) library of python.



Create a folder for project, you want to scrap and go inside that to create a virtual Env by following command :
" Virtualenv ."

and activate it by following command: 
" .\scripts\activate "

Virtual Environment is mostly preferd as it keeps the project isolated, whatever packages and libraries needed for that particular project are inside the env. and we can directly deploy them on github by keeping them isolated from whole system.



Then Install Scrapy by typing this command in cmd :
" pip install Scrapy" , you can also specify the version of scrapy while installing.

Start Project by typing this command in terminal :
" scrapy startproject <project-name> and this will create a number of files and folders that includes a basic skeleton to get started quickly:
  
  
  
![Startproject](https://user-images.githubusercontent.com/86855712/173240434-98265aa2-4ca3-4399-ad37-38d606268e83.png)
  
  
  
In above picture-
Settings.py : Contains setting of spider, it has BOT_NAME which is your project name, USER_AGENT: Identification of yours, ROBOTSTXT_OBEY crawl by obeying this.
  
Items.py : Here we specify the website items or categories(like product_name, product_author, product_price, product_imagelink) etc to be scraped.
  
Pipelines.py : This is used to save data, which is scraped in database.
  
middleware.py: This is used to make changes to data before storing & also used as a proxy to request.
  
  
  
Now we will create first Spider named "website_spider.py", inside amazonwebsite/amazonwebsite/spiders,  we can name the spider anything we want.
  
Now in website_spider.py file we will write the Scraping Code of spider to scrap the pages. 
  
  
  
I have used CSS SELECTOR to extract particular items or code from source code. 

Scrapy Shell is same as cmd prompt in windows to help control scrapy in command line mode, here you can see wether the selector you have selected is extracting the correct item or not by typing following commond:"Scrapy Shell" and fetch("paste URL of website")
  
Instead of CSS SELECTOR, XPATH SELECTOR can also be used.
  
  
  
After the data is scraped and stored in temporary containers known as ITEMS. We can now store them in JSON, XML or CSV format by following command: 
scrapy crawl <name of your spider> -o items.json, or scrapy crawl <name of your spider> -o items.xml or scrapy crawl <name of your spider> -o items.csv
  
In PIPELINES.py file, we develop the pipeline to store the crawled data stored in temporary containers known as ITEMS to a database(MYsql, SQLite, MONGODB etc).
  
  
  
Big Websites like Amazon, Flipcart etc, put restrictions to crawl their website and scrap the data. We can Bypass this Restrictions using 2 ways:
  
User Agents are strings that let the website you are scraping identify the application, operating system (OSX/Windows/Linux), browser (Chrome/Firefox/Internet Explorer), etc. of the user sending a request to their website.
  
So you can use GOOGLE'S GOOGLEBOT, Web servers/websites can give bots special treatment, for example, by allowing them through mandatory registration screens, bypassing CAPTCHA etc. 
  
You can also use CHANGE USER AGENT.As popular website, have some level of blocking mechanism in place based on the user agents it sees you using.
We can get around this by rotating through multiple user agents, that appear like real visitors to their site by using scrapy-user-agents download middleware, which I have used in my project.
  
  
  
Second way can be by using PROXIES. Even when rotating your user agents, most websites will still refuse to serve your requests if you only specify User-Agent in the headers as they are also keeping track of the IP address.

When a site sees to many requests coming from one IP Address/User Agent combination they usually limit/throttle the requests coming from that IP address.To bypass this rate limiting/throttling the easiest thing we can do is to change the IP address from which we are sending our scraping requests.This is done using proxies.
  
That is why we also will need to look at using proxies in combination with the random user agents to provide a much more reliable way of bypassing the restrictions placed on our spiders. Their are Scrapy middlewares to take care of this problen for us. One such middleware is the scrapy_proxy_pool middleware project, which allows  to use free proxy pools.
  
The MongoDB Database will look like: 
  
![database](https://user-images.githubusercontent.com/86855712/173247524-ebde5238-1317-4462-8125-b239520d81a5.png)
