# News

News is news scapper designed for machine learning news classifier

### Technology

News uses a number of open source projects to work properly:

- [Scrapy](https://scrapy.org/) - For extracting data from websites!
- [Flask](http://flask.pocoo.org/) - API framework for serving data

And of course on Git and GitHub for versionin and progress tracking.

### Installation

News requires Linux, Python 2 and PIP to run. If you are in windows
you can run linux tools inside a given folder and continue with linux
steps below.

Install the dependencies and devDependencies and start the server.

```sh
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install virtualenv virtualenvwrapper
$ sudo pip install --upgrade pip
```

# Environment

Prepare the project folder

```sh
$ sudo virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then clone the project into folder with the followin command

```sh
$ git clone git@github.com:jasir99/News.git .
```

All the modules developed for News are site and league/sport
based and should be put inside the folder `[projectFolder]/News/News/spiders`
as seperate scrapy python module.

# Sample

Create parsers based on Scrapy guidelines and templates.
Ex tamplate:

```
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
```

# Testing

To test a specific module note the name of the scrapy spider defined in the first line of class initialization. Run the following steps to test it

1. Go to `[projectFolder]/News/News` folder.
2. Execute `scrapy crawl [moduleName]` ex:`scrapy crawl BingNews`
