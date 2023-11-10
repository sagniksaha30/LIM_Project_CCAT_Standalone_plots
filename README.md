# Code to make standalone plots using the LIM_Project_CCAT repository.
### (Author: Sagnik Saha)

This repository is based on the LIM_Project_CCAT repository. 
Basically, it contains Python scripts that serve as standalone plotting files
for results obtained using the LIM_Project_CCAT code. In addition to plotting,
it also SAVES the essential data files, which can be used for other purposes. 

For this set of files, we have used the following specifications:
1. We used specifications created for the actual EoR-Spec modules.
2. The specification contained 140 data points, containing central frequencies, along with their corresponding number of detectors (Nfeeds). We split them into groups of 35 each (i.e. 4 bands).
3. We calculated a representative frequency and frequency step for each group. Then, we ensured that the number of channels in each band was equal to 35. That is, we used Delta_nu = dnu * 35.
4.  We also ran the code for 2xNfeeds and 7xNfeeds, for future possibilities. 
