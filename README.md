# My-Bet-Supremo

You might want to start be creating a python virtual environment to work in.

### Creating virtual environment
Linux

Install pip and virtualenv (if neccesary)  
```
>>> sudo apt-get install python3-pip
>>> sudo pip3 install virtualenv
``` 

Create and activate a virtualenv
```
>>> mkdir <your_virtual_env_dir_name>
>>> cd venv
>>> virtualenv python3 .
>>> source bin/activate
```

Your terminal should now look like this
```
(your_virtual_env_dir_name)$
```

Clone the repository
```
(your_virtual_env_dir_name)$ git clone https://github.com/ML-Project-2018/my-bet-supremo.git
cd my-bet-supremo
```

Install all the dependencies into the virtual environment
```
(your_virtual_env_dir_name)$ pip3 install -r requirements.txt
```

Create a branch to work on
```
git checkout -b <your_branch_name>
```

Make changes, push and create a pull request for review.

### NB: The process is the same for Windows except a difference in some of the commands.