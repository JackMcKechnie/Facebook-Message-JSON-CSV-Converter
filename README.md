# Facebook-Message-JSON-CSV-Convertor

This is a tool to convert the JSON data obtained by downloading message data from Facebook. Saves the sender, timestamp and message content.

------------------------------
How to download Facebook data:
------------------------------

1. Navigate to https://www.facebook.com/dyi/?referrer=yfi_settings
2. Select the information that you wish to download and select JSON format 
3. Facebook will process your data and after some time allow you to download it 

-----------------------------------------------------
How to use the Facebook Message JSON to CSV convertor
-----------------------------------------------------

The convertor takes 3 command line arguments, these are: the folder in which the JSON files you wish to convert are, the destination you want the CSV to be saved in and the number of JSON files to convert (Facebook splits large conversations into individual files of 10k messages). 

Example:

JSON_Convertor.py C:\Users\your-name\Documents\Messenger Archive\facebook-yourname\messages\inbox\chatname C:\Users\your-name\Desktop

************************************
Created by Jack McKechnie - May 2020 - Thanks for using!
************************************
