import pickle

def display_menu():
    print('---- Menu ----') 
    print('1) Add suspect')
    print('2) Add accomplice')
    print('3) Display all suspects') 
    print('4) Find potential accomplices')
    print('F) Find key players.')
    print('E) Exit')

def display_suspect(suspect,graph):
    print(f'{suspect}:')
    for name in graph.get(suspect, set()) :
        print(f'    {name}')


def display_all_suspects(graph):
    print('---- All suspects ----')
    for name in graph:
        display_suspect(name , graph)   

def find_potential_accomplices(suspect, graph):
    accomplices =set()
    for name in graph.get(suspect, set()):
        accomplices.update(graph.get(name, set()))
#akhane suspect thaika jai nam gula pamu abar ta key hisabe use koira sobar name save kormo
    accomplices.discard(suspect)
    for name in graph.get(suspect , set()):
        accomplices.discard(name)
    return {suspect : accomplices}
    
def display_potential_accomplices(suspect, graph):
    print('---- Potential accomplices ----')
    print('Already known accomplices:')
    display_suspect(suspect,graph)
    print()


    print('Potential new accomplices:')
    potential = find_potential_accomplices(suspect,graph)
    display_suspect(suspect ,potential)

def load_from_file(filename):

    with open(filename,'rb') as f:
        return pickle.load(f)


def save_to_file(graph, filename):
    with open(filename, 'wb') as f:
        pickle.dump(graph,f)



def main():
    filename =input('Enter filename for social graph: ')
    print()

    try:
        graph = load_from_file(filename)
        print('*** Graph loaded from file. ***')
        print()

    except:
        graph ={}
        print('*** File not found. Starting with empty graph. ***')
        print()

    while True:
        display_menu()
        choice =(input('Enter your choice: '))
        
        if choice =='1' :
            sus_name = input('Enter suspect name: ')

            if sus_name not in graph:
                graph[sus_name] =set()
                
            save_to_file(graph,filename)

        elif choice == '2':
            sus_name = input("Enter suspect name: ")
            accomplice = input("Enter accomplice name: ")

            if sus_name not in graph:
                graph[sus_name] = set()
            
           
            if accomplice not in graph:
                graph[accomplice]=set()
            
            
            graph[sus_name].add(accomplice)
            graph[accomplice].add(sus_name)
            save_to_file(graph, filename)

        elif choice == '3':
            display_all_suspects(graph)

        elif choice == '4':
            sus_name = input('Enter suspect name:')
            display_potential_accomplices(sus_name, graph)

        elif choice == 'F':
            x = int(input('X: '))
            for suspect in graph:
                if len(graph[suspect]) > x:
                    num = len(graph[suspect])
                    print(f'{suspect:<15}:{num:>10} accomplice(s)')
            
        elif choice.upper() == 'E':
            break

if __name__ == '__main__':
    main()