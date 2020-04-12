import os
from shutil import copy2
import time

CopyCatConfig = "CopyCatConfig.txt"

def config_handler(start_text, end_text, config_file):

    # The following code is designed to import text from a config file.
    # It's designed to do this line by line.
    # start_text: The program will start importing after this point.
    # end_text: The program will stop importing when it reaches this point.
    # config_file: location where config file is stored.

    fr = open(config_file, 'r')
    text = fr.read()
    start = text.find(start_text) + len(start_text + "\n")
    end = text.find("\n" + end_text)
    substring = text[start:end]
    fr.close()

    return substring


source = config_handler("File to Monitor:", "File to Copy:", CopyCatConfig)
destination = config_handler("File to Copy:", "Refresh Time in Seconds:", CopyCatConfig)
refresh_time = config_handler("Refresh Time in Seconds:", "End of config", CopyCatConfig)


run = True
while run:

    source_file_count = sum([len(files) for r, d, files in os.walk(source)])
    destination_file_count = sum([len(files) for r, d, files in os.walk(destination)])

    # check if source and destination have the same amount of files
    if source_file_count != destination_file_count:

        for file in os.listdir(source):

            # Check if file is in path.
            path = file
            isFile = os.path.isfile(destination)

            # If File is not in path, the copy it.
            if isFile == False:

                # The below should not be necessary
                # if file.endswith(".txt") or file.endswith(".ps1") or file.endswith(".doc") or file.endswith(".docx")\
                #         or file.endswith(".csv") or file.endswith(".xlsx") or file.endswith(".exe") \
                #         or file.endswith(".out") or file.endswith(".pptx") or file.endswith(".pdf"):

                    file = source + "\\" + file
                    # print(os.path.join("/mydir", file))

                    copy2(file , destination)
    time.sleep(int(refresh_time))


