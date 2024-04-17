# Welcome to the Web Scraper Project 4
## This project was made for CS325. Test cases by Logan Holland and Joshua Caley

### Step 1: Setting up the environment
Install Miniconda and download the file webscraperp3.yaml. Once you have done that, use the command "conda env create -f webscraperp3.yaml" to create your environment.

Once you have made your environment, run the command "conda activate CS325_Proj3", unless you gave the environment a custom name.

### Step 2: Setting up the API Key
Once your environment is set up, you need to make an OpenAI API Key. First, however, you may need to make an account. 

#### Step 2.1: Setting up account
To make an account go to platform.openai.com, then create yourself an account.

#### Step 2.2: Checking for credits
If you already have an account, make sure you have credits available to run the API. 

To do this, go to the tab labeled Usage on the side bar, and see if you have credits available.

#### Step 2.3: Making API Key
So, you have enough credits and you have an account to make an API key with.

To make an API Key, go to the tab API keys on the side bar, and click it.

Once on that page, click the button labeled "Create new secret key".

Put this key somewhere you can find it again if needed, but you will need it in your computer's clipboard (ctrl + c) for the next part.

#### Step 2.4: Adding API Key
To add your API Key run the following command: setx OPENAI_API_KEY "your-api-key-here"
    Replace "your-api-key-here" with your API key that is in your clipboard, but leave the quotation marks there, because your API key needs to be inside quotation marks.

To test that this worked, you will have to close miniconda, reopen it, reactivate your environment, and then run this command: echo %OPENAI_API_KEY%
    This command should tell you the API key that you are to use.

The above commands only work for Windows computers. For MacOS, use the following instructions:
Use the command
    'nano ~/.bash_profile'
or
    'nano ~/.zshrc'
to open the profile file in a text editor. Then, the editor, add the line
    export OPENAI_API_KEY='your-api-key-here'
while replacing "your-api-key-here" with your actual API key.

Then save and exit the text editor using Ctrl+O, followed by Ctrl+X

Next, load your profile using
    'source ~/.bash_profile'
or
    'source ~/.zshrc'
to load the updated profile. Finally, verify that it works by using the command echo $OPENAI_API_KEY

-Please note, I used Windows when making this program, and I just rewrote the instructions from the OpenAI website here just to make it easier to find.
 If you want to look at the instructions directly on the webpage, the link is: https://platform.openai.com/docs/quickstart?context=python.

 ### Step 3: Setting up the file folders
 Once all of the above is done, you will need to download the files run.py and articles.txt, and the folders module_1, module_2, module_3, and Data. All of these folders should be in the same folder as run.py and articles.txt, or else the program will not work.

 ### Step 4: Running the program
 If you want to run the example articles, go into Miniconda and change the directory to the folder that run.py is in using the command cd "FolderPath", where "FolderPath" is the path structure to where run.py is.
 
 Next, use the command: python run.py articles.txt
 
 Running this command will generate 3 different files per article. A "article_X_raw.txt", "article_X_full.txt", and a "article_X.txt", where X is the number of the article in the list of articles in article.txt.
 A summarized article will be in article_X.txt, and will have a title in quotation marks at the top. All of the example articles are pulled from the news outlet CNN, with the link being https://www.cnn.com/business/tech

 ### Warnings:
 This Web Scraper only works for CNN articles, and has only been tested on articles gathered through this link: https://www.cnn.com/business/tech.
 This Web Scraper may work on other CNN articles, but not on any other website unless they use the exact same structure and classes as the CNN website does.

 ## TEST CASES:
 ### Test Case 1:
 To run Test Case 1, use the command python tc1.py "articles.txt"
 You can replace the file with the file you want, as long as it is a .txt file. The output should be "Line # is a URL" if the line is a URL, or "Line # is not a URL" if the line is not a URL

 ### Test Case 2:
 To run Test Case 2, use the command python tc2.py "articles.txt"
 You can replace the file with any file you like, as long as it is a .txt file. The output should be "Article #: 200" if the webpage is working.

 ### Test Case 3:

 ### Test Case 4:

 ### Test Case 5:

 ### Test Case 6:

 ### Test Case 7:
 To run Test Case 7, use the command python tc7.py
 All you need to run this test case is to make sure your API key is set inside of your environment. It should output "Yes." or "Yes" if the API responds.

 ### Test Case 8:
 To run Test Case 8, use the command python tc8.py "articles.txt"
 You can replace the file with any .txt file that passes Test Case 1 and 2. It will then output the total number of articles, the number of articles processed, and if the two match it will say "Accurate number of articles processed".