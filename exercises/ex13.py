def frame_it(word_list):
    splitted_list= word_list.split()
    size_of_frame = max(len(word) for word in splitted_list)
    
    print('*'*(size_of_frame+4))
    
    for word in splitted_list:
        print('* {a:<{b}} *'.format(a=word, b=size_of_frame))
    print('*'*(size_of_frame+4))
        
