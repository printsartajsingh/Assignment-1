def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    input_string = input("Enter a string of numbers separated by spaces: ")
    
    # Split the input string by spaces and convert the parts to integers
    input_list = [int(num) for num in input_string.split()]
    
    # Sort the list using selection sort
    selection_sort(input_list)
    
    # Display the sorted list
    print("Sorted list:", input_list)

if __name__ == "__main__":
    main()