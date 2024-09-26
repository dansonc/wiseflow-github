# 将目录core 添加到sys.path中
import sys
sys.path.append('core')
from scrapers.general_crawler import general_crawler
from insights import logger


url = "https://www.baidu.com"
logger.info(f"applying {url}")
flag, result = general_crawler(url, logger)
# show the result
print(result)


