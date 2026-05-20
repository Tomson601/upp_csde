decision_tree = {
    'start': {
        'type': 'decision',
        'question': 'Czy widoczne są okrągłe ciemne plamy?',
        'tak': 'plamy_ciemne',
        'nie': 'brak_plam'
    },
    'plamy_ciemne': {
        'type': 'decision',
        'question': 'Czy w środku plamy widoczne są paski?',
        'tak': 'paski',
        'nie': 'bez_pasków'
    },
    'bez_pasków': {
        'type': 'decision',
        'question': 'Czy plamy mają zółte krawędzie?',
        'tak': 'choroba_bakteryjna',
        'nie': 'pleśnioza'
    },
    'paski': {
        'type': 'conclusion',
        'result': 'Podejrzenie: paskoza ciemna!'
    },
    'choroba_bakteryjna': {
        'type': 'conclusion',
        'result': 'Podejrzenie: Bakterioza'
    },
    'pleśnioza': {
        'type': 'conclusion',
        'result': 'Podejrzenie: pleśnioza!'
    },
    'brak_plam': {
        'type': 'decision',
        'question': 'Czy na liściach widoczny jest szary nalot?',
        'tak': 'nalot_widoczny',
        'nie': 'brak_nalotu'
    },
    'nalot_widoczny': {
        'type': 'decision',
        'question': 'Czy nalot łatwo ściera się z liścia?',
        'tak': 'mąka',
        'nie': 'trudniak'
    },
    'mąka': {
        'type': 'conclusion',
        'result': 'Podejrzenie: Mąka na liściu!'
    },
    'trudniak': {
        'type': 'conclusion',
        'result': 'Podejrzenie: trudniak plamisty!'
    },
    'brak_nalotu': {
        'type': 'decision',
        'question': 'Czy liście są wysychające?',
        'tak': 'susznik',
        'nie': 'normalny_stan'
    },
    'susznik': {
        'type': 'conclusion',
        'result': 'Podejrzenie: susznik liściowy, za dużo słońca!'
    },
    'normalny_stan': {
        'type': 'conclusion',
        'result': 'Roślina zdrowa'
    }
}

def run_diagnosis(tree, current_node='start'):
    while True:
        node = tree[current_node]
        
        if node['type'] == 'conclusion':
            print(f"\n*** DIAGNOZA ***")
            print(f"Wynik: {node['result']}")
            break
        
        elif node['type'] == 'decision':
            print(f"\n{node['question']}")
            answer = input("Odpowiedź (tak/nie): ").lower().strip()
            
            if answer in ['tak', 't']:
                current_node = node['tak']
            elif answer in ['nie', 'n']:
                current_node = node['nie']
            else:
                print("Proszę wpisać 'tak' lub 'nie'")
                continue

if __name__ == "__main__":
    run_diagnosis(decision_tree)
