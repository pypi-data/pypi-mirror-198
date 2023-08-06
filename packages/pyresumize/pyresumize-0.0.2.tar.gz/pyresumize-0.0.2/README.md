
# Introduction
pyresumize is a python module to extract useful information from resume and generate a json string out of it. Currently it supports only pdf file as input . 

### Todo
* Implement a Skill Fetcher
* Support for other formats
* Performance Improvements
* Bug Fixes

## Usage

    from  pyresumize  import ResumeProcessor
    r_parser=ResumeProcessor()
    json=r_parser.process_resume(file)
    print(json)

 

##### Developer Notes

To Run the unit tests

python -m unittest discover tests\ -vvv

python -m build

twine upload -r pyresumize dist\* --config-file "C:\Users\Gokul Kartha\.pypirc" --repository pypi