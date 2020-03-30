# MiniProject2

  NJIT IS60162 - Group Project for Statistical Calculator

### Contributors: Akmal Husanov (ahusanov) and Amanda Outar (amandaoutar)

[![Build Status](https://travis-ci.org/IS-601862/MiniProject2.svg?branch=master)](https://travis-ci.org/IS-601862/MiniProject2)


## Project structure and Contents

### 1. Source directory - [src](./src/)

  This is the source folder for all source code including packages like:
  
  - Utilities (decorators, csv helper, sql helper, random number helper)
  
  - Basic Calculations - [calculator](./src/calculator/):
    1.  - [x] Addition
    2.  - [x] Subtraction
    3.  - [x] Multiplication
    4.  - [x] Division
    5.  - [x] Square
    6.  - [x] Square Root
    
  - Descriptive Statistics functions - [statistics](./src/statistics/):
      1. - [x] Mean
      2. - [x] Median
      3. - [x] Mode
      4. - [x] Variance
      5. - [x] Standard Deviation
      6. - [ ] Quartiles
      7. - [ ] Skewness
      8. - [x] Sample Correlation
      9. - [x] Population Correlation
      10. - [x] Z-Score
      11. - [x] Mean Deviation / Mean Absolute Deviation
      
  - Unit Tests - [tests](./src/tests/):
      1. - [x] Tests for csv reader
      2. - [x] Tests for calculator using csv files
      3. - [x] Tests for statistic functions using csv files 
 
### 2. Data directory - [data](./data/)
  
   This folder includes CSV files for unit testing.
   
### 3. Necessary Documentations - [doc](./doc/)
  
   References and statistical function descriptions are located in this directory.

### 4. Project logs - [log](./log/)
  
  Project and changelogs are located here.

## References:
1. http://www.mbaexcel.com/excel/how-to-create-a-normally-distributed-set-of-random-numbers-in-excel/
2. https://www.geeksforgeeks.com
3. https://stattrek.com/statistics/formulas.aspx
4. https://www.statisticssolutions.com/common-statistical-formulas/
5. https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/z-score/

## Lincese:
Licensed under the [MIT Lincese](LICENSE)

## Changelog:
[changeLog.csv](./log/changelog.csv)

### Changelog:
[changeLog.csv](./log/changelog.csv)

|Hash    |User          |Date and Time                  |Change                                                             |
|--------|--------------|-------------------------------|-------------------------------------------------------------------|
|a1dee8e|ahusanov|2020-03-30T03:04:20-04:00|[akmal] task: readme updated													|			
|a54088a|Akmal Husanov|2020-03-30T02:54:51-04:00|[akmal] travis link is added												|			
|4ba098e|ahusanov|2020-03-30T02:48:47-04:00|[akmal] fix: all run time errors fixed											|					
|8d35ada|ahusanov|2020-03-30T02:33:05-04:00|[akmal] fix: run time errors													|						
|3365d3d|ahusanov|2020-03-30T02:31:51-04:00|[akmal] fix: run time errors													|					
|86b7396|ahusanov|2020-03-30T02:08:50-04:00|[akmal] fix: whitespace issue													|	
|17a5f43|ahusanov|2020-03-30T02:03:16-04:00|[akmal] fix: imports issue fixed												|		
|20eb628|ahusanov|2020-03-30T02:02:38-04:00|[akmal] fix: imports issue fixed												|		
|f1af3c6|ahusanov|2020-03-30T01:54:57-04:00|[akmal] fix: unittest														    |
|c11f8d9|ahusanov|2020-03-30T01:52:55-04:00|[akmal] Feature: travis yml is added											|			
|a3cbaa8|Akmal Husanov|2020-03-30T00:57:34-04:00|Merge pull request #5 from IS-601862/akmal									|					
|0abadba|ahusanov|2020-03-30T00:54:21-04:00|[akmal] Feature: added unittests for statistics functions						|	
|4bf8737|ahusanov|2020-03-30T00:53:07-04:00|[akmal] Fix: fixed circular error												|		
|30c2c0a|ahusanov|2020-03-30T00:52:19-04:00|[akmal] Fix: refactored mode due to tests										|				
|dba8fd9|ahusanov|2020-03-30T00:51:48-04:00|[akmal] Fix: fixed parameter order												|		
|aa3309a|ahusanov|2020-03-30T00:51:19-04:00|[akmal] Fix: updated imports													|	
|cf12319|ahusanov|2020-03-30T00:50:22-04:00|[akmal] Fix: renamed														    |
|6b12818|ahusanov|2020-03-30T00:48:15-04:00|[akmal] Fix: updated imports													|	
|2a4515f|ahusanov|2020-03-29T22:18:01-04:00|[akmal] Feature: calculator test cases are added								|						
|0a41417|ahusanov|2020-03-29T22:17:27-04:00|[akmal] Fix: subtraction and divisions corrected								|						
|3eaa5e8|ahusanov|2020-03-29T22:16:30-04:00|[akmal] Task: get & set properties are added									|					
|056c04d|ahusanov|2020-03-29T21:43:27-04:00|[akmal] Task: encapsulation applied in calculator & statistics					|					
|ee03238|ahusanov|2020-03-29T21:32:19-04:00|[akmal] Feature: csv reader test is added with data								|						
|068a848|ahusanov|2020-03-29T19:13:30-04:00|[akmal] Feature: requirements added												|		
|62c9b2b|ahusanov|2020-03-29T19:11:07-04:00|[akmal] Feature: setup added													|	
|960e903|ahusanov|2020-03-29T19:10:57-04:00|[akmal] Feature: Dockerfile added												|		
|79745fc|ahusanov|2020-03-29T18:32:06-04:00|[akmal] Fix: refactored utilities												|		
|2dfd2ad|ahusanov|2020-03-29T18:30:21-04:00|[akmal] Fix: refactored utilities												|		
|0183775|Akmal Husanov|2020-03-29T18:03:36-04:00|Merge pull request #4 from IS-601862/akmal									|					
|455335f|ahusanov|2020-03-29T18:00:54-04:00|[akmal] Fix: refactored median module											|			
|a468c13|ahusanov|2020-03-29T17:46:34-04:00|[akmal] Fix: refactored mean module												|		
|6560c4a|ahusanov|2020-03-29T17:36:04-04:00|[akmal] Feature: added square and squareroot									|					
|b7846fa|Akmal Husanov|2020-03-29T14:50:53-04:00|[akmal] status updated on readme											|			
|f394589|Akmal Husanov|2020-03-29T14:48:27-04:00|Merge pull request #3 from IS-601862/amanda								|						
|891a192|Akmal Husanov|2020-03-29T14:47:19-04:00|Merge branch 'master' into amanda											|			
|0157480|amanda|2020-03-29T14:29:10-04:00|[amanda] Fix: Project structure is updated										|				
|0eeb620|Akmal Husanov|2020-03-29T14:16:10-04:00|Merge pull request #2 from IS-601862/akmal									|					
|a1752a5|ahusanov|2020-03-29T14:04:36-04:00|Merge branch 'akmal' of https://github.com/IS-601862/MiniProject2 into akmal	|						
|85e7990|ahusanov|2020-03-29T14:02:06-04:00|[akmal] Task: added template changelog											|			
|b255fe9|ahusanov|2020-03-29T14:01:31-04:00|[akmal] Task: added md documentation files										|				
|8d54904|ahusanov|2020-03-29T14:01:12-04:00|[akmal] Task: added csv data files												|		
|03eb450|ahusanov|2020-03-29T13:56:35-04:00|[akmal] Task: updated project structure based on readme							|		
|ef7334c|Akmal Husanov|2020-03-29T13:55:48-04:00|[akmal] updated readme with new structure									|					
|1fba890|amanda|2020-03-28T18:07:08-04:00|[amanda] Updated readme														    |
|c077a23|amanda|2020-03-28T17:21:24-04:00|[amanda] Created variance referecne file											|			
|b6bc705|amanda|2020-03-28T17:19:23-04:00|[amanda] Updated files														    |
|8ae9b9c|amanda|2020-03-28T17:16:34-04:00|[amanda] Created mode reference file												|		
|d7bc0f8|amanda|2020-03-28T17:14:10-04:00|[amanda] Created median reference file											|			
|f9a768d|amanda|2020-03-28T16:36:42-04:00|[amanda] Updated statistics module												|		
|5b34058|amanda|2020-03-28T16:33:35-04:00|[amanda] Made significant changes to main stats file								|						
|f82568b|amanda|2020-03-28T16:28:34-04:00|[amanda] Created corr module														|
|cdf307f|amanda|2020-03-28T16:27:02-04:00|[amanda] Made changes to main statistics module									|					
|dd756d4|amanda|2020-03-28T16:26:45-04:00|[amanda] created proportion module												|		
|8dc1a50|amanda|2020-03-28T16:24:22-04:00|[amanda] Created varience module													|	
|1e86987|amanda|2020-03-28T16:22:32-04:00|[amanda] Updated mode module														|
|87673d4|amanda|2020-03-28T16:21:25-04:00|[amanda] created zscore module													|	
|415fb55|amanda|2020-03-28T16:21:04-04:00|[amanda] Created mode module														|
|631f387|amanda|2020-03-28T16:20:49-04:00|[amanda] Updated median module													|	
|39cc489|amanda|2020-03-28T16:18:20-04:00|[amanda] Updated ZScore module													|	
|8bd413b|amanda|2020-03-28T16:16:54-04:00|[amanda] Updated statistics modules												|		
|45ef0f5|amanda|2020-03-28T13:46:54-04:00|[amanda] Updated statistics module												|		
|36b28d2|amanda|2020-03-28T13:41:31-04:00|[amanda] - updated calculator module												|		
|907d432|amanda|2020-03-28T13:37:40-04:00|[amanda] created multiplication module											|			
|31ebc8b|amandaoutar|2020-03-27T00:39:29-04:00|Merge pull request #1 from IS-601862/amanda									|					
|c9cb722|amanda|2020-03-27T00:22:55-04:00|[amanda] Feature: added subtraction												|		
|a2e8e31|amanda|2020-03-27T00:22:22-04:00|Update .gitignore														            |
|06a6dc1|ahusanov|2020-03-26T02:15:14-04:00|[akmal] Feature: added utilities package with absolutepath						|		
|171a59e|ahusanov|2020-03-26T02:14:35-04:00|[akmal] Feature: added testing package											|			
|3561a36|ahusanov|2020-03-26T02:13:42-04:00|Feature: added statistics package mean & statistics getsample module			|		
|5fa0017|ahusanov|2020-03-26T02:11:37-04:00|Feature: added various decorators												|		
|1ffb188|ahusanov|2020-03-26T02:11:00-04:00|Feature: added csv reader package added											|			
|4316367|ahusanov|2020-03-26T02:10:26-04:00|Feature: added calculators with add & division									|					
|3c7964a|Akmal Husanov|2020-03-25T10:09:03-04:00|Initial commit																|

