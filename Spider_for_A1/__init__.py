import collector
import finalize
import price_spider
import info_spider

# Collect the website links where data are needed to collect, and save them in "historical.txt" and "snapshot.txt"
collector.collect_web_info()
info_spider.scrap_info_link()
# Scrap price and info for each bond, and save them in "prices.txt" and "infos.txt" respectively
price_spider.scrap_data()
# Combine the info and price for each bond, and save it as "results.txt" and "results.csv" for future usage
finalize.finalize()

