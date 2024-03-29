# Gitter

My friend [Tom McClintock](https://github.com/tmcclintock) gave me a seminar on his awesome [first 10 commits](https://docs.google.com/presentation/d/1rJyTpUZPaCXiz43ZHQmCiq-1rEsflbFS8aCv7bgBl7Q/edit?usp=sharing) to start a new data-oriented project using best practices. This is a script I wrote to automate these commits so you can jump straight to your project. Future improvements may include some data cleaning libraries and some basic exploratory data analysis.

Succinctly, clone this repo and run `_git_starter.py` to initialize a project with a MIT Licence, `REAME.md`, `notebooks` directory, `.gitignore`, a source directory, installation files (e.g. `setup.py`, `requirements.txt`), create a unit test directory with initial tests (smoke tests), and add [travis-CI](https://travis-ci.com/) support.

Enjoy!

## How to use

0. (Only once) Download this repo to your local computer,
open _git_starter.py, customize the following settings

```python
git_username = 'your_github_username'

travis_user = 'your_travis_username'

author = 'your_name'

author_email = 'your_email'
```

Then simply add, commit, and push to your repository.

Every time you want to start a new project follow the next steps

1. Create a repository e.g. https://<span></span>github.com/git_username/git_repo_name

2. (Optional) Tell [travis to track the repository](https://travis-ci.com/account/repositories)

3. Clone gitter `git clone git@github.com:your_github_username/gitter`

4. Finally run `_git_starter.py` parsing the following arguments

| Parameter       | Description                       | Default |
| -------------   | -------------                     | ------------- |
| --repo | Repo name to commit to            | No default |
| --pack  | The name you want for you package | No default |
| --travis    | Add .yml                          | True |
| --template  | add notebooks and data dirs       | True |

e.g.

```bash
$python _git_starter.py --repo Awesome_Repo --pack Awesome_Package
```

Voilà! You can go to https://<span></span>github.com/git_username/git_repo_name and will find something like this:


![library.](./images/_image_to_illustrate.png)
