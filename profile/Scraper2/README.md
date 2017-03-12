# Youtube Scraper 2

This scraper just takes a youtube link and prints out it's stats.

* To generate `stats_python.prof` : `python -m cProfile -o stats_python.prof youtube2.py`

* To generate `stats_python.txt` : `python -m cProfile -s cumtime youtube2.py >> stats_python.txt`

* To generate `stats_scrapy.prof` : `scrapy runspider youtube2.py --profile stats_scrapy.prof`

* To view the visualisation, `snakeviz` can be used.

 * `pip install snakeviz`

 * `snakeviz stats_python.prof`
 
 * `snakeviz stats_scrapy.prof`
