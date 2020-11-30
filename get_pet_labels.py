#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Jared Teller
# DATE CREATED: 11/30/2020                       
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Create the filename list using listdir
    filename_list = listdir(image_dir)

    # create our empty results_dic dictionary for use later
    results_dic = dict()

    # we need to fix the format of the pet image image labels here
    for idx in range(0, len(filename_list), 1):
        
        # skip bad file names
        if filename_list[idx][0] != ".":

            pet_label = ""
            pet_label = strip_label(filename_list[idx])

            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_label]
            else:
                print("** Warning: Key=", filename_list[idx], "already exists in results_dic with value =", results_dic[filename_list[idx]])

    # For testing
    #Iterating through a dictionary printing all keys & their associated values
    #print("\nPrinting all key-value pairs in dictionary results_dic:")
    #for key, value in results_dic.items():
     #  print("Filename=", key, "   Pet Label=", value)

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

# Custom function to strip down the pet image labels
def strip_label(lbl_to_strip):
    """
    Strips a pet label down to the required format.

    Params:
        lbl_to_strip - the word to be processed
        Type (str)

    Returns:
        pet_name - the resulting pet name after everything has been stripped down
        Type (str)
    """
    # set to lower case
    lower_pet_label = lbl_to_strip.lower()

    # split lower case string by _ to break into words
    split_pet_label = lower_pet_label.split("_")

    # blank pet name
    blank_pet_name = ""

    # Loops to check if word in pet name is only aplhabetic characters, if true append word
    for word in split_pet_label:
        if word.isalpha():
            blank_pet_name += word + " "

    # remove whitespace that is trailing or at the beginning
    pet_name = blank_pet_name.strip()

    return pet_name