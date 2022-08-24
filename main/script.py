def open_sourse():
    
    list_eng = []
    list_rus = []

    with open('main/resourse/sourse.txt') as t:
        
        for line in t:
            
            list_line = line.split('\t')
            eng = list_line[0].split(';')
            rus = list_line[1].split(';')

            for i in range(len(eng)):

                word_eng = eng[i].strip()
                list_eng.append(word_eng)
                

            for i in range(len(rus)):

                word_rus = rus[i].strip('\n').strip()
                list_rus.append(word_rus)

            main(list(set(list_eng)), list(set(list_rus)))
            list_eng.clear()
            list_rus.clear()


def main(list_eng,list_rus):

    for i in range(len(list_eng)):

        for j in range(len(list_rus)):

            with open('main/resourse/output_eng.txt', 'a') as f:

                f.write(f'{i}-{j}  ' + list_eng[i] + '\n')

            with open('main/resourse/output_rus.txt', 'a') as f:

                f.write(f'{i}-{j}  ' + list_rus[j] + '\n')


open_sourse()
