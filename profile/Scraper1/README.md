# Youtube Scraper 1

This scraper starts with a youtube video, prints it's stats and then chooses a video from it's recommended section, and keeps on doing that until a duplicate link is found.



* To generate `stats_python.prof` : `python -m cProfile -o stats_python.prof youtube.py`

* To generate `stats_python.txt` : `python -m cProfile -s cumtime youtube.py >> stats_python.txt`

* To generate `stats_scrapy.prof` : `scrapy runspider youtube.py --profile stats_scrapy.prof`

* To view the visualisation, `snakeviz` can be used.

		 * `pip install snakeviz`
		
		 * `snakeviz stats_python.prof`
		 
		 * `snakeviz stats_scrapy.prof`
