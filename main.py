from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    l =[]

    for i in int_list:
        if i%2 == 0:
            l.append(i)

    return l



# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:

        
#Main fuction
def main():
        #Example list
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_int_list = even_list(int_list)
        output = sum_of_squares_of_even(even_int_list)
        print(output)
