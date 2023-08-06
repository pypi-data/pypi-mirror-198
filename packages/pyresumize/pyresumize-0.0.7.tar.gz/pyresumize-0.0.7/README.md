
![](https://github.com/karthagokul/pyresumize/blob/main/logo.png)

# Introduction
pyresumize is a python module to extract useful information from resume and generate a json string out of it. Currently it supports only pdf file as input . 

### Todo
* Implement a Skill Fetcher
* Support for other formats
* Performance Improvements
* Bug Fixes
* Custom configuration of input data

## Usage
    python -m spacy download en_core_web_sm
    python -m nltk.downloader words
    python -m nltk.downloader stopwords
    from  pyresumize  import ResumeProcessor
    r_parser=ResumeProcessor()
    json=r_parser.process_resume(file)
    print(json)

