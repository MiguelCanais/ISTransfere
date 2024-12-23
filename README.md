# ISTransferido
Download the files of all your courses in a brief <br/>
Redoit it, and only the new ones will be added;<br/>
All new files will be in the inbox folder 📥 <br/>
Uses <a href="https://scrapy.org/">Scrapy's library</a>. <br/>
<br/>
Disclaimer: optimized for Fenix's pages, but easily customizable with other XPaths.

## Configuration
1. Prepare the virtual environment
```bash
bash install.sh
```
2. Create the file with credentials
```bash
touch .env
echo IST_ID="istxxxxx" >> .env
echo FENIX_SPIDER="your_password" >> .env
```

3. Chose which courses to download
```bash
vim config.yaml # maintain the base URL as used (it's the main link from each course page)
```

## Running
Download ALL the files + organize the inbox
```bash
# Run spider, RUN!
scrapy crawl fenix_spider && python src/filter_inbox.py
```


## Extra notes
- Please, do not change the download delay to something that can create too much requests to the servers
