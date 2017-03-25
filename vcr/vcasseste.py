import urllib2
import vcr

with vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml'):
    response = urllib2.urlopen('http://quotes.toscrape.com/').read()
    assert 'Example domains' in response

