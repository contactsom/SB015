import rlcompleter

my_completer= rlcompleter.Completer()

parse_list = ['co','cal','asser','contain','exec','final','abc']

for parse in  parse_list:
    print(parse+' (TAB) ', end='')

    try:
        for i in range(50):
            terms=my_completer.complete(parse,i)
            if terms is None:
                break
            print(terms,end='\t')
        print()
    except:
        pass
