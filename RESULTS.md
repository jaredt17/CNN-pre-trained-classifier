# Results for Udacity Project 1: Pre-Trained CNN Dog Classifier
--- 
Please view this result document in a markdown viewer (or on GitHub)

## Results from check_images.py

```
*** Results Summary for CNN Model Architecture VGG ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10
pct_match Value: 87.5
pct_correct_dogs Value: 100.0
pct_correct_breed Value: 93.33333333333333
pct_correct_notdogs Value: 100.0

INCORRECT Dog Breed Assignment:
Real:                     beagle     Classifier:  walker hound, walker foxhound
Real:             great pyrenees     Classifier:                         kuvasz

** Total Elapsed Runtime: 0:0:5
```

```
*** Results Summary for CNN Model Architecture ALEXNET ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10
pct_match Value: 75.0
pct_correct_dogs Value: 100.0
pct_correct_breed Value: 80.0
pct_correct_notdogs Value: 100.0

INCORRECT Dog Breed Assignment:
Real:           golden retriever     Classifier:                tibetan mastiff
Real:                     beagle     Classifier:  walker hound, walker foxhound
Real:           golden retriever     Classifier:                 english setter
Real:             great pyrenees     Classifier:                         kuvasz
Real:             boston terrier     Classifier:                        basenji
Real:           golden retriever     Classifier:           afghan hound, afghan

** Total Elapsed Runtime: 0:0:1
```

```
*** Results Summary for CNN Model Architecture RESNET ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10
pct_match Value: 82.5
pct_correct_dogs Value: 100.0
pct_correct_breed Value: 90.0
pct_correct_notdogs Value: 90.0

INCORRECCT Dog/Not Dog Assignments:
Pet Image Label is NOT-a-Dog - Classified as a-DOG
Real:                        cat     Classifier:   norwegian elkhound, elkhound

INCORRECT Dog Breed Assignment:
Real:           golden retriever     Classifier:                       leonberg
Real:                     beagle     Classifier:  walker hound, walker foxhound
Real:             great pyrenees     Classifier:                         kuvasz

** Total Elapsed Runtime: 0:0:1
```

## Results Table
| # Total Images     	| 40 	|
|--------------------	|----	|
| # Dog Images       	| 30 	|
| # Not-a-Dog Images 	| 10 	|

| CNN Model Architecture 	| % Not-a_Dog Correct 	| % Dogs Correct 	| % Breeds Correct 	| % Match Labels 	|
|------------------------	|---------------------	|----------------	|------------------	|----------------	|
| ResNet                 	| 90                  	| 100            	| 90               	| 82.5           	|
| AlexNet                	| 100                 	| 100            	| 80               	| 75             	|
| VGG                    	| 100                 	| 100            	| 93.3             	| 87.5           	|

## Interpreting the Results

Based on our results, we can deduce that the "best" model architecture is VGG. VGG was able to classify dogs and not-dogs with 100% accuracy, and had the highest percentage of breed guesses correct at 93.33.

