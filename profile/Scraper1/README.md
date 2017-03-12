# Youtube Scraper 1

This scraper starts with a youtube video, prints it's stats and then chooses a video from it's recommended section, and keeps on doing that until a duplicate link is found.



* To generate `stats_python.prof` : `python -m cProfile -o stats_python.prof youtube.py`

* To generate `stats_python.txt` : `python -m cProfile -s cumtime youtube.py >> stats_python.txt`

* To generate `stats_scrapy.prof` : `scrapy runspider youtube.py --profile stats_scrapy.prof`

* To view the visualisation, `snakeviz` can be used.

 * `pip install snakeviz`

 * `snakeviz stats_python.prof`
 
 * `snakeviz stats_scrapy.prof`


* Snakeviz results

Shows the relative cumulative time usage by each function

![Sunburst](https://github.com/Parth-Vader/ScrapyBenchmark/blob/master/profile/Scraper1/images/Sunburst.png?raw=true "Shows the relative cumulative time usage by each function")

Shows the total time usage by each function

![Tottime](https://github.com/Parth-Vader/ScrapyBenchmark/blob/master/profile/Scraper1/images/tottime.png?raw=true "Shows the total time usage by each function")

Shows the cumulative time usage by each function

![Cumtime](https://github.com/Parth-Vader/ScrapyBenchmark/blob/master/profile/Scraper1/images/tottime.png?raw=true "Shows the cumulative time usage by each function")
