# CHATGPT ON Linux Terminal

Here we will be using the chatgpt api to send prompts and receive answer which will be displayed on the terminal.
<br>
### Step 1:<br> 
Go to openai's website and login to your account (create an account if you don't have one) and then go to this <a href="https://platform.openai.com/account/api-keys" target="_blank">website</a> <br>

### Step 2: <br>
Generate an API key by clicking on the Create new secret key button. Copy the key and store it in a text file say api.txt

### Step 3: <br>
Run the following command: <b>echo "api-key=$(cat api.txt) >> .bashrc</b>

### Step 4: <br>
git clone this repo with the command: <b>git clone https://github.com/n1haldev/gpt_on_cli</b>

### Step 5: <br>
enter the directory using: <b>cd gpt_on_cli</b> <br>
and then run the command: <b>chmod +x gpt</b>

### Step 6: <br>
copy the file to /usr/bin by running the command: <b>sudo cp gpt /usr/bin</b>

## That's it. Run the 'gpt' command to enter active query mode and type exit as query to exit the query mode.
Hope you had fun setting this up :)
