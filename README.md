# APM466_A1 V.1.0 

updated:
  1. fixed the bug in price_spider.py.
  2. make it more effecient for each .py spider file.

To use this project, what you need to do is open the file Spider_for_A1 and you may start as follows:

  1. Download the chromedriver.exe from url: https://chromedriver.chromium.org/downloads based your chorme version. (You may get the info from the "about" section in your google)
  2. Copy the path of your chromedriver.exe, and past it to EXACUTABLE_PATH under the an_li.py.
  3. Run the module collector.py to get the web links.
  4. Run the module price_spider.py to get the price data based on the web links.
  5. Run the module info_spider.py to get the bond info data based on the web links.
  6. Run the module finalize.py to combine the 2 data into one as results.txt and results.csv.

Notice:

* Warm_1: there might have some error when you do the Step 1. The reson is I am using write("historical", "a") instead of "w". The file may not exist. But anyway, you may be able to fix it by yourself, right? ^-^

* Warm_2: to make sure the project is able to run smoothly, I would highly recommand to make sure that you have your labtop's speaker on. Or, if you are in the library for example, you may use your ear phone instead.

* This project uses too many for-loop. Thus for step 1, 2 and 3, it will take nearly 5 min for each module. However, you may make it more efficient if you want. I am not gonna to do it, tho. ^-^
  
  1. Try
      driver_i = webDriver.Chorme(), for i \in {1,2, ... ,32}. 
  Thus, you will collect data from 32 websites, instead of what I did, which collect the data one web by one.
    
  2. In step 1, I should have record the web links for historical data and snapshot data. But when I am writing that code, I haven't got the assignment, thus not knowing that we need the data from snapshot. 
  By doing so, you may skip step 3.
  
  3. You may use BeatifulSoup instead. BS can be run behind the screen. The problem is the HTML BS read in our assignment is kind of wried for some reason I don't know. Therefore, I simply give it up. 
