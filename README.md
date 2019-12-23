# BigTweet

The BigTweet tool was built out of the need to eliminate the barriers that the Twitter API imposes so as to help researchers, businesses and organizations get all the tweets data they need for various analysis in their different line of operations, with ease and from command line, meaning no prior extensive programming knowledge is required. 
BigTweet provides a means of getting old/backdated twitter data for analysis, bypassing the rate limits and restrictions from twitter API, giving you unlimited tweet textual data along with some other metadata such as; dates and time information, likes, retweets, replies, and permalinks (unique link to a tweet).



# Software Architecture for BigTweet 
**<p align="center"> class diagram showing modules and their member functions </p>**

![BigTweet Class Diagram](https://github.com/marquisvictor/BigTweet/blob/master/BigTweet/final%20class%20diagram.png)
              


This page provides the source code for running BigTweet and a [Wiki page](https://github.com/marquisvictor/BigTweet/wiki/BigTweet-Software-Wiki-page) with a guide for installation.


## System requirements and Specification

##### Operating system
BigTweet was tested on Ubuntu distribution of the Linux operating system and on Windows 7, 8, 10.

##### Programming Language
Python 3.5 or higher

##### Dependencies
- Pyquery
- Request
- urllib 


## Usage

The following are step by step procedures that would eventually ensure that tweets are downloaded and ready for analysis. 

1. Install any version of Python greater than 3.5

2. Create an environment variable path for python on your local machine such that you can interactively fire python from Command Prompt.
3. Download or `git-clone` the BigTweet repository to your local machine from github
4. Unzip the downloaded zip 
5. Navigate to the unzipped folder
6. While inside the unzipped folder, navigate to the BigTweet folder and open a command right in that same folder
7. Start mining Tweets with any of the command line arguments and one of or combination of the six “use cases” from the `README` file
8. The downloaded tweets would be saved as an `output.csv` file in your working directory. Although you can specify a name to save the downloaded tweets by passing a “name”.csv argument to the `--output` argument.


##### The following are the associated command line arguments

  - since (**str. "yyyy-mm-dd"**): A lower bound date to restrict search.
  - until **(str. "yyyy-mm-dd"**): An upper bound date to restrist search.
  - querysearch (**str**): A query text to be matched.
  - toptweets (**bool**): If True only the Top Tweets will be retrieved.
  - near (**str**): A reference location area from where tweets were generated.
  - within (**str**): A distance radius from "near" location (e.g. 25km)
  - lang (**str**): Filter tweets by language. (e.g `en` - english tweets,  `cn` - chinese tweets, `es` - spanish tweeets, etc.) 
  - maxtweets (**int**): The maximum number of tweets to be retrieved. If no number is set here or is lower than 1 all possible tweets will be retrieved.


For instance, if we needed a ten-year historic (old) Tweets. All the English tweets sent from `First of January 2009` till `First of January 2019` and from Hung Hum District in Hong Kong, the combination command line arguments below would be used. 

```
python BigTweet.py --near "22.3029, 114.1816" --within 4km --lang es --since 2009-01-01 --until 2019-01-01 --output hongkong.csv
```


When you run this command from command line, it typically returns the following as columns in a hongkong.csv that would be saved in your current working directory. 
  - permalink (str)
  - username (str)
  - text (str)
  - date (date)
  - retweets (int)
  - favorites (int)
  - mentions (str)
  - hashtags (str)
  - geo (str)



## Authors 
* [Mohammed Abdul-Rahman](https://www.linkedin.com/in/mohammed-abdul-rahman-73741869/)<sup>1a,b</sup>

* [Victor E. Irekponor](https://www.linkedin.com/in/veirekponor/)<sup>b</sup>

* [Maryam O. Abdul-Rahman](https://www.linkedin.com/in/maryam-abdul-rahman-74aab658/)<sup>b</sup>

* [Edwin H.W. Chan](https://scholar.google.com/citations?user=QHGVaJsAAAAJ&hl=en)<sup>a</sup>

* [Man Sing Wong](https://scholar.google.com.hk/citations?user=poqz28gAAAAJ&hl=en)<sup>c</sup>

a - [Department of Building and Real Estate, The Hong Kong Polytechnic University, Hong Kong](http://www.bre.polyu.edu.hk/)

b - [AI Africa Lab, Lagos, Nigeria](https://twitter.com/aiafricalab)

c - [Department of Land Surveying and Geo-informatics, The Hong Kong Polytechnic University, Hong Kong](http://www.lsgi.polyu.edu.hk/home/index.asp)
