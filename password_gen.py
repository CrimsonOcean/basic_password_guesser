def enter_password(attempt):
    password = "pswd"
    if password == attempt:
        return True
    else:
        return False

def increment_trial(trial,place,min_index,max_index):
    if place >= len(trial):
        trial.append(min_index)
    elif trial[place] > max_index - 1:
        trial[place] = min_index
        increment_trial(trial,place+1,min_index,max_index)
    else:
        trial[place] += 1

def password_cracker(entry_function):
    min_char = 32
    max_char = 126
    num_valid_symbols = max_char - min_char + 1
    trial = []
    string = ''

    print("Processing...")
    flag = False
    itteration = 0 #debug
    while flag == False:
        increment_trial(trial,0,min_char,max_char)
        string = ''.join(map(chr,trial))
        flag = entry_function(string)
        
        #debug
        itteration += 1
        if itteration % 10000000 == 0:
            print("attempts: ",itteration," string: ",string)


    print("Correct Password:",string)
    print("Number of itterations:",itteration)


password_cracker(enter_password)
