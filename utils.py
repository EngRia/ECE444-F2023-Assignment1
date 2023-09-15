class utils:
    def reversed(self, num):
        if type(num) == float:
            raise TypeError('Invalid Input! Float input is not allowed, Enter Integers only')
        
        if type(num) == str:
            raise TypeError('Invalid Input! String input is not allowed, Enter Integers only')
        
        if type(num) == int:
            rev_num = 0 
            while num > 0:
                rem = num%10
                rev_num = rem + (rev_num*10)
                num = num//10
            print(f'The Reversed Number Is:', rev_num)
            return rev_num
        else:
            print(f'Invalid Input!')
    
    def formatter(self, num):
        if type(num) == float:
            raise TypeError('Invalid Input! Float input is not allowed, Enter Integers only')
        
        if type(num) == str:
            raise TypeError('Invalid Input! String input is not allowed, Enter Integers only')
        
        if type(num) == int:
            binary = bin(num)
            octal = oct(num)
            print(f'Binary:', binary, 'Octal:', octal)
            return binary, octal
        else:
            print(f'Invalid Input!')
