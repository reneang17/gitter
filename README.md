# Giter

My friend [Tom McClintock](https://github.com/tmcclintock) gave me a seminar on his awesome first 10 commits to start a new data-oriented project using best practices. This is a script I wrote to authomate these commits so you can jump straight to your project. Future improvements will include some data cleaning libraries and some basic exploratory data analysis, for structure and un-structured data.

Succincly, clone this repo and run, se detailed instructions below, _git_starter.py, to initialize a project, with a MIT Licence, REAME.md, notebooks, .gitnore, a package, installed (setup.py, requirements.txt), create a test module, smoke test package, and add travis continuous integration support.

Enjoy!

## How to use. 

0 .- (Only once) Fork and clone this repo to your local computer, 
open _git_starter.py, customize the following settings

git_username = 'your_github_username'

travis_user = 'your_travis_username'

author = 'your_name'

author_email = 'your_email'

add, commit, push. 

Every time you want to start a new project follow the next steps

1 .- Create a repo e.g. https://github.com/git_username/git_repo_name

2 .- (Optional) Added to the programs follow by travis (https://travis-ci.com/account/repositories)

3 .- Clone giter $git cone https://github.com/your_github_username/giter

4.- Finally run _git_starter.py parsing the following arguments

| Parameter  | Description | Default |
| ------------- | ------------- | ------------- |
| --git_repo_name | Repo name to commit to | No default |
| --package_name | The name you want for you package | No default | 
| --add_travis | Add .yml | True |
| --add_template | add notebooks and data dirs | True |

e.g.

$python _git_starter.py --git_repo_name Awesome_Repo --package_name Awesome_Package

voilà! you can go to https://github.com/git_username/git_repo_name and will find 
something like this:


![library.](./_image_to_illustrate.png)
