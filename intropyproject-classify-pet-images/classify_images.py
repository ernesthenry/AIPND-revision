#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Kato Ernest Henry
# DATE CREATED: 29/08/2026                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the true pet labels. This function inputs:
#            -The Image Folder as images_dir within classify_images and as 
#             in_arg.dir for the function call within main. 
#            -The results dictionary as results_dic within classify_images and 
#             as results for the function call within main.
#            -The CNN model architecture as model within classify_images and  
#             as in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
import os
from classifier import classifier

# TODO 3: Define classify_images function below please be certain to replace None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading at the trailing whitespace characters from them.
    For example, the Classifier function returns = ' Collie ' so the classifier 
    label would be = 'collie'.
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    for filename in results_dic:
        # Construct full path to the image
        img_path = os.path.join(images_dir, filename)
        
        # Runs classifier function to classify the image
        model_label = classifier(img_path, model)
        
        # Formats the classifier label: lowercase and strip whitespace
        model_label = model_label.lower().strip()
        
        # Defines the true pet image label
        truth = results_dic[filename][0]
        
        # If the pet image label is found in the classifier label, it's a match
        # Check either exact substring match or term match
        if truth in model_label:
            match = 1
        else:
            match = 0
            
        # Extends results_dic with classifier label and match result
        results_dic[filename].extend([model_label, match])
