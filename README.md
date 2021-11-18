# Ex1

## Explanation of the problem space :
The problem : to move people from source floor to their destanation with the minimum time is possible in consideration for all the calls ,
in this project we gave our best solution to this problem and tried to minimized the average waiting time and to take calls as much as possible in the giving time.

## Literature review:
The first thing we've learned from it this video that shows us the elevator problem and what algorithm we should use to cover all the cases up . this video has nice animation and very helpful to watch :
The Science Behind Elevators - YouTube:
https://www.youtube.com/watch?v=xOayymoIl8U

The Wikipedia website is a great tool to know information about something you research about ,
In this article there is a lot of information about elevators include little bit explanation of the algorithm.
Elevator - Wikipedia:
https://en.wikipedia.org/wiki/Elevator

The hidden science of elevators by Jesse Dunietz is a useful and full of information article that explain the elevator problem , shows us an algorithm and in addition gives us refer to links photos and videos about this topic .
The Hidden Science of Elevators (popularmechanics.com):
https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

# Algorithm explanation:

1.for call in calls_list {
2.list_of_times <- []
3.for elev in elevs_list {
4.elev_time <- 0
5.elev_time <- check elev ride time to call
6.elev_time <- check elev ride time to complete the call
7.append it to list_of_times
8.} end for
9.take the index of the minimum time in list_of_times
10.update the curr floor of this elevator and enter it to the csv out put
11.} end for

