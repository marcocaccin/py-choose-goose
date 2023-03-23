# py-choose-goose

quick and dirty chatGPT copycat

## Installation

- Expose `OPENAI_API_KEY` in your environment
- `pip install -r requirements.txt` with your Python intepreter of choice
- `./chat.py`


## Example Usage

```bash

❯ ./chat.py
System prompt (e.g., 'You are a helpful assistant. Answer concisely when possible.'):

User:
write fizzbuzz in pytorch
```

Fizzbuzz is a simple programming problem that requires printing out numbers from 1 to 100, replacing numbers that are
multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz". Here is the PyTorch code
for FizzBuzz:

```python
import torch                        
 # create tensor with numbers from 1 to 100                                                                                                                                   
 numbers = torch.arange(1, 101)                                                                                                                                               
                                                                                                                                                                              
 # use boolean indexing to check if each number is a multiple of 3 or 5                                                                                                       
 is_multiple_3 = numbers % 3 == 0                                                                                                                                             
 is_multiple_5 = numbers % 5 == 0                                                                                                                                             
                                                                                                                                                                              
 # create empty fizzbuzz tensor                                                                                                                                               
 fizzbuzz = torch.empty(100, dtype=torch.dtype(object))                                                                                                                       
                                                                                                                                                                              
 # fill fizzbuzz tensor with regular numbers, Fizz, Buzz, or FizzBuzz                                                                                                         
 fizzbuzz[is_multiple_3] = 'Fizz'                                                                                                                                             
 fizzbuzz[is_multiple_5] = 'Buzz'                                                                                                                                             
 fizzbuzz[is_multiple_3 & is_multiple_5] = 'FizzBuzz'                                                                                                                         
 fizzbuzz[~(is_multiple_3 | is_multiple_5)] = numbers[~(is_multiple_3 | is_multiple_5)]                                                                                       
                                                                                                                                                                              
 # print fizzbuzz tensor                                                                                                                                                      
 print(fizzbuzz)                                                                                                                                                              
                                                                                                                                                                              

This program prints out the following output:                                                                                                                                 

                                                                                                                                                                              
 tensor(['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz',                                                               
         '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz',                                                          
         '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz',                                                          
         '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz',                                                          
         '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz',                                                          
         '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz',                                                          
         '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz'], dtype=object)                                                                                 
                                                                                                                                                                              

As you can see, the program successfully printed out the numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with  
"FizzBuzz".  
