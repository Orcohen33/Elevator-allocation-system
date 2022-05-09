

## Explanation of the problem space :  
The problem : to move people from source floor to their destination within minimum time is possible in consideration for all the calls ,  
in this project we gave our best solution to this problem and tried to minimized the average waiting time and to take calls as much as     possible in the giving time.  

## Literature review:  
The first thing we've learned from it this video that shows us the elevator problem and what algorithm we should use to cover all the cases   up . this video has nice animation and very helpful to watch :  
The Science Behind Elevators - YouTube:  
https://www.youtube.com/watch?v=xOayymoIl8U  

The Wikipedia website is a great tool to know information about something you research about ,  
In this article there is a lot of information about elevators include little bit explanation of the algorithm.  
Elevator - Wikipedia:  
https://en.wikipedia.org/wiki/Elevator  

The hidden science of elevators by Jesse Dunietz is a useful and full of information article that explain the elevator problem , shows us an   algorithm and in addition gives us refer to links photos and videos about this topic .  
The Hidden Science of Elevators (popularmechanics.com):  
https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/  

## Algorithm explanation:

1. for call in calls_list {  
2. list_of_times <- []  
3. for elev in elevs_list {  
4. elev_time <- 0  
5. elev_time <- check elev ride time to call  
6. elev_time <- check elev ride time to complete the call  
7. append it to list_of_times  
8. } end for  
9. take the index of the minimum time in list_of_times  
10. update the curr floor of this elevator and enter it to the csv out put  
11. } end for  

## Executing the project :

**Two ways to run this program:**

**_1. First way:_**
  - Open cmd in project folder
    - Use the following code template to run Ex1: 
      ` py Ex1.py <Building json> <Calls csv> <output name>`
    - Running the algorithm example :
      `py Ex1.py B3.json Calls_b.csv out.csv`
  The output file is the result of executing the program.
  
 **_2. Second way:_**
  - Open pycharm
  - Right click on Ex1.py
  - Click on `Modifiy Run Configuration...`
    - Write in `Parameters:`  -> `<Building json> <Calls csv> <output name>`
    - Writing `Parameters :` for example : `B3.json Calls_b.csv out.csv`
  - Click `Apply` then `Ok`
  - Execute Ex1.py

## Executing the checker:

- Go to the `checker` folder then run the code according to the building files and calls you want. (As I showed above).
   - Then a file named out.csv will be added. If it already existed, after running the code, the code would overwrite what had been written before.

**_Two ways to run the checker:_**

**_1. First way:_**

- Use terminal on pycharm and write the following template:
<details><summary>CLICK ME</summary>
<p>   
  
      java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json out.csv out.log 
  
</p>
</details>


 

**_2. Second way:_**

- Open cmd in project folder
- Write the following template:
<details><summary>CLICK ME</summary>
<p>   
  
      java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json out.csv out.log 
  
</p>
</details>
 
- '1111,2222,3333' -> Write your id
 - 'B2.json' Is the building and elevators file that you want to run the checker on -> Write building file
 - 'out.csv' Is the output file that you allocated the elevators to calls -> Write down the CSV file you want to check
 - 'out.log' Is a log file showing the allocation of elevators and all other data such as: total operation time, average waiting time per person, uncompleted number of calls -> Enter the name of the log file you want to save for the checker











## UML Diagram

![UML5](https://user-images.githubusercontent.com/92351152/142615279-da823d6b-0ef1-4d50-82f0-971ae7e16017.jpg)



