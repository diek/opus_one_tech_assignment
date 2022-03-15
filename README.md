# Software Developer Technical Test

Hello, and welcome to the final stages of the interview process with Opus One Solutions! 

Attached to this document, you will find two files:  
 
-   power-calc.py  

-   data1.json  

Please open power-calc.py to obtain instruction for the exercise. You will also need to use data1.json to complete the exercise. 

Upon completion, please email your code back to us as an attachment. A discussion and dissection of your code will serve as the base for part of your final in-person interview. This exercise should take no more than an hour to complete. 

### Notes: 

-   To satisfy step 2, you can use the function we’ve provided  

-   **That function doesn’t include code to implement calculation of q.** We’ve attached a picture showing the relationship between p, q and s in a right-angle triangle  

-   Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9  

![triangle](../assets/triangle.png)

### Requirements
- Step 1: Read in the file "data1.json" and clean it so that we semantically understand and have known quantities for voltage, current, and power factor  

- Step 2: Create a new dictionary that has the same location as the primary key, but the value is three new calculated quantities:  
	1. 	s = apparent power  
	1. 	p = real power  
	1. 	q = reactive power  
    
    Can use the "calc_power" function to help with this job

- Step 3: Print out this new dictionary
