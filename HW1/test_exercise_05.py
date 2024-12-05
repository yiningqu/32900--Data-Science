"""
In order to start mastering the many features of Github, 
please complete the following tutorials from the GitHub Skills page:
https://skills.github.com/
. 
Please make sure to use **public** repositories for this in your own GitHub user account. 
Please put the URL to the repository of the completed tutorial in the README file 
of this repository.


 - [Introduction to GitHub](https://github.com/skills/introduction-to-github)
 - [Communicate using Markdown](https://github.com/skills/communicate-using-markdown)
 - [GitHub Pages](https://github.com/skills/github-pages)

"""
import github_tutorials

i_completed_introduction_to_github = github_tutorials.i_completed_introduction_to_github
i_completed_communicate_using_markdown = github_tutorials.i_completed_communicate_using_markdown
i_completed_github_pages = github_tutorials.i_completed_github_pages

def test_introduction_to_github():
    assert i_completed_introduction_to_github == True

def test_communicate_using_markdown():
    assert i_completed_communicate_using_markdown == True

def test_github_pages():
    assert i_completed_github_pages == True
