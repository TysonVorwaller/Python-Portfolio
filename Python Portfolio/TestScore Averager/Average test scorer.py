#Tyson Vorwaller 4-5
#Average Test Score
import math
def average_test_score(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
    
    average = (int(t1)+int(t2)+int(t3)+int(t4)+int(t5)+int(t6)+int(t7)+int(t8)+int(t9)+int(t10))/10
    return average

t1 =input("enter test1 score")
t2 =input("enter test2 score")
t3 =input("enter test3 score")
t4 =input("enter test4 score")
t5 =input("enter test5 score")
t6 =input("enter test6 score")
t7 =input("enter test7 score")
t8 =input("enter test8 score")
t9 =input("enter test9 score")
t10 =input("enter test10 score")

average=average_test_score(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10)
print(average)

 
   
