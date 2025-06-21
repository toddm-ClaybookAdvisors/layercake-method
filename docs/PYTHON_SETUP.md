# Installing Python and Managing Environments on macOS with pyenv and requirements.txt

1. **Check if Python 3 is installed**
   - Open Terminal and run:
     ```
     python3 --version
     ```
   - If you see a version number, Python 3 is already installed.

2. **Install Homebrew (if not already installed)**
   - Paste this into Terminal:
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Then update Homebrew:
     ```
     brew update
     ```

3. **Install pyenv and pyenv-virtualenv**
   - Run:
     ```
     brew install pyenv pyenv-virtualenv
     ```
   - (Optional but recommended) Add pyenv to your shell:
     - For **zsh** (default on new macOS):
       ```
       echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
       echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
       echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
       echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
       source ~/.zshrc
       ```
     - For **bash**:
       ```
       echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
       echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
       echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
       echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
       source ~/.bash_profile
       ```

4. **Install a Specific Python Version**
   - To see available versions:
     ```
     pyenv install --list
     ```
   - To install (replace `3.11.3` with your preferred version):
     ```
     pyenv install 3.11.3
     ```

5. **Create and Activate a Custom pyenv Virtual Environment**
   - Create a new virtual environment (replace `myenv` with your chosen name):
     ```
     pyenv virtualenv 3.11.3 myenv
     ```
   - Activate your environment:
     ```
     pyenv activate myenv
     ```
   - To deactivate:
     ```
     pyenv deactivate
     ```

6. **(Optional) Set Local Python Version for a Project**
   - In your project directory:
     ```
     pyenv local myenv
     ```

7. **Prepare a requirements.txt File**
   - Create a `requirements.txt` file in your project directory listing all needed packages, e.g.:
     ```
     requests
     numpy
     matplotlib
     ```
   - (You can generate this automatically later using `pip freeze > requirements.txt`.)

8. **Install All Requirements**
   - Make sure your custom environment is active, then run:
     ```
     pip install -r requirements.txt
     ```

9. **(Optional) Freeze Your Exact Package List**
   - After installing or updating packages:
     ```
     pip freeze > requirements.txt
     ```

---

**Notes:**
- Always activate your environment before running or developing your project.
- If you see errors about missing libraries, you may need to run:

- You may need to restart your terminal after installing pyenv or modifying your shell config.
- Use `pyenv versions` to see all installed versions and environments.

