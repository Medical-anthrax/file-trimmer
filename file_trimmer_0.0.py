
print(r'''
 ________ ___  ___       _______                                                
|\  _____\\  \|\  \     |\  ___ \                                               
\ \  \__/\ \  \ \  \    \ \   __/|                                              
 \ \   __\\ \  \ \  \    \ \  \_|/__                                            
  \ \  \_| \ \  \ \  \____\ \  \_|\ \                                           
   \ \__\   \ \__\ \_______\ \_______\                                          
    \|__|    \|__|\|_______|\|_______|                                          
                                                                                
                                                                                
                                                                                
 _________  ________  ___  _____ ______   _____ ______   _______   ________     
|\___   ___\\   __  \|\  \|\   _ \  _   \|\   _ \  _   \|\  ___ \ |\   __  \    
\|___ \  \_\ \  \|\  \ \  \ \  \\\__\ \  \ \  \\\__\ \  \ \   __/|\ \  \|\  \   
     \ \  \ \ \   _  _\ \  \ \  \\|__| \  \ \  \\|__| \  \ \  \_|/_\ \   _  _\  
      \ \  \ \ \  \\  \\ \  \ \  \    \ \  \ \  \    \ \  \ \  \_|\ \ \  \\  \| 
       \ \__\ \ \__\\ _\\ \__\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ _\ 
        \|__|  \|__|\|__|\|__|\|__|     \|__|\|__|     \|__|\|_______|\|__|\|__|
                                                                                
                                                                                
''')


print( '''Welcome to the file trimmer!  This python program trims entries out of your 
file based on certain criteria. File_trimmer can delete entries over/under x length,
delete entries based on the presence of x character

Please note- your original file will not be changed, but you will be given a new file

Please note- entries MUST be on seperate lines, File must be in UTF8, .TXT format.''')


print('''
Type in the name of the file you would like to edit in the format 'file.txt'.''')

filename=input()
file= open(filename, 'r', encoding='utf8')

print('''type in exactly how many lines your file contains''')
file_length=int(input())+10

print('''Type in the name you would like your new file to be called. 'newfilename.txt' ''')
new_file= input()
open(new_file, 'x', encoding='utf8')
new_file= open(new_file, 'a', encoding='utf8')
while 10==10:
        print('''\nOn what criteria would you like to edit your file? 'length', 'char'
        ''')
        global edit_choice
        edit_choice= input()


        if edit_choice== 'length':
                print('you have chosen to delete entries according to their length ')
                break

        elif edit_choice == 'char':
                print('''you have chosen to delete entries according to whether or not they contain
one or more certain characters.''')
                break

        else: print ('''please input one of the given commands''')

if edit_choice== 'length':# type: ignore
        print('''would you like to delete entries shorter than ____, or longer than____? 'shorter','longer' ''')

        length_choice= input()
        if length_choice=='shorter':
                print('''you have decided to delete all entries shorter than ____
                Please type in the minimum amount of characters allowed''')
                min_length=int(input())
                print('trimming all entries shorter than',min_length,'...')
                for i in range(file_length):
                        f=file.readline()
                        print(f)

                        if len(f) > min_length:
                                new_file.write(f)

        elif length_choice=='longer':
                print('''you have decided to delete all entries longer than ____
                Please type in the maximum amount of characters allowed ''')
                max_length=int(input())+1
                print('trimming all entries longer than', max_length,'...')
                for i in range(file_length):
                        f=file.readline()
                        print(f)

                        if len(f) <= max_length:
                                new_file.write(f)

        else:print('you stupid SHIT! You just cant type one fucking command correctly, can you.')
                








if edit_choice== 'char':# type: ignore
        print('''would you like to delete entries with_____, or delete entries without___? 'with','without' ''')
        char_pres= input()
        if char_pres== 'with':
                print('you have decided to delete all entries with a certain character')
                print('please type in your characters.  Example:a ')
                with_char= input()
                
                for i in range(file_length):
                        f=file.readline()
                        print (f)
                        if any(s not in f for s  in(with_char)):
                                new_file.write(f)

        elif char_pres=='without':
                print ('you have decided to delete all entries without a certain character')
                print('please type in your character.  Example:a ')
                without_char=input()

                for i in range(file_length):
                        f=file.readline()
                        print(f)
                        if any(s in f for s in (without_char)):
                                new_file.write(f)
