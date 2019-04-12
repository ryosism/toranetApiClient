# requirements

- beautifulsoup4
- selenium
- chromedriver
    - `https://sites.google.com/a/chromium.org/chromedriver/downloads`
        - this code works with ChromeDriver 73.0.3683.20(https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/)
    - download and set PATH `export PATH="$PATH:/path/to/chromedriver"`
    - or just type `pip install chromedriver_binary`
- libgconf2-4
- libnss3-dev
- google-chrome
    ```
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
        sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
        apt-get update
        apt-get install google-chrome-stable
    ```
    
A Dockerfile builds compative environment. Just type `docker build .`

# setup
- setup gcloud to work `gcloud auth list`
- just type `main.py app.yaml`
