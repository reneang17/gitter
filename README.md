# Giter

My friend [Tom McClintock](https://github.com/tmcclintock) gives a seminar on his best 10 commits, that help
him start a data oriented project using best practices. I typed a script to execute these authomatically,
this way you can jump straight to action!

This repo is supose to give you a template for projects to develope a python package, using some good engineering practices: test, setup.py, requirements.txt, and travis continuous integration support.

## Instributions 

1 .- Create a repo e.g. https://github.com/git_username/git_repo_name

2 .- (Optional) Added to the programs follow by travis (https://travis-ci.com/account/repositories)

3 .- (Change only once) Clone this repo to your local computer, 
open _git_starter.py, customize the following settings

git_username = 'your_github_username'

travis_user = 'your_travis_username'

author = 'your_name'

author_email = 'your_email'

add, commit, push. 

4. - Finally run _git_starter.py parsing the following arguments

| Parameter  | Description | Default |
| ------------- | ------------- | ------------- |
| --git_repo_name | Repo name to commit to | No default |
| --git_username | Your github user name | No default | 
| --add_travis | Add .yml | True |
| --add_template | add notebooks and data dirs | True |

e.g $python _git_starter.py --git_repo_name a_git_repo_name --git_username reneang17

voilà! 
