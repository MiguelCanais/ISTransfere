# ISTransferido
Download the files of all your courses in a brief (long time). 
Redo it, and only the new ones will be added.<br/>

All new files will be in the desired organized files folder 📥 <br/>
<br/>
Uses <a href="https://scrapy.org/">Scrapy's library</a>. <br/>


## Configuration
1. Prepare the virtual environment
```sh
source ./install.sh
```
2. Create the file with your credentials
```sh
touch .env
echo IST_ID=istxxxxx >> .env
echo FENIX_PASSWORD=your_password >> .env
```

3. Edit the configuration to your liking
```sh
vim config.toml
```


## Running
Download the files + organize the downloads into the organized folder
```bash
# Run spider, RUN!
scrapy crawl fenix_spider && python src/filter_downloads.py
```


## Extra notes
- Please do not change the download delay to something that can create too many requests to the servers
