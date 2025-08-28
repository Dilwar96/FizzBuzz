#!/usr/bin/env python3
"""
FizzBuzz Interview Solution

A simple, maintainable implementation that prints numbers from 1 to 100.
For multiples of 3, prints "Fizz"; for multiples of 5, prints "Buzz";
for multiples of both 3 and 5, prints "FizzBuzz".

Features:
- Easy to maintain and understand
- Flexible for future requirements
- Clean, readable code
- Proper error handling
"""

def fizzbuzz(n):
    """
    Returns FizzBuzz output for a given number.
    
    Args:
        n (int): The number to process
        
    Returns:
        str: "Fizz", "Buzz", "FizzBuzz", or the number as string
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    """Main function - user inputs custom range with retry on invalid input"""
    print("FizzBuzz - Custom Range")
    print("-" * 25)
    
    while True:
        try:
            start = int(input("Enter start number: "))
            end = int(input("Enter end number: "))
            
            if start > end:
                print("Error: Start number must be less than end number!")
                print("Please try again.\n")
                continue
                
            print(f"\nFizzBuzz from {start} to {end}:")
            print("-" * 30)
            
            for i in range(start, end + 1):
                print(fizzbuzz(i))
            
            break  # Exit loop on success
            
        except ValueError:
            print("Error: Please enter valid numbers!")
            print("Please try again.\n")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break


if __name__ == "__main__":
    main()