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

|Hash    |User          |Date and Time                  |Change                                                                                                                            |
|--------|--------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|af6d687 |ahusanov         |3/26/2020 2:13 AM|Feature: added statistics package mean, statistics getsample module     
