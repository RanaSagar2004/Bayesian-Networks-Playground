
# Basic Bayesian Network Inference (simplified)
class Node:
    def __init__(self, name, parents=[], cpt={}):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def probability(self, value, evidence):
        if not self.parents:
            return self.cpt[value]
        key = tuple(evidence[parent] for parent in self.parents)
        return self.cpt[key][value]

# Example: Rain → Sprinkler, Rain + Sprinkler → WetGrass
rain = Node('Rain', [], {True: 0.2, False: 0.8})
sprinkler = Node('Sprinkler', ['Rain'], {
    (True,): {True: 0.01, False: 0.99},
    (False,): {True: 0.4, False: 0.6}
})
wet_grass = Node('WetGrass', ['Sprinkler', 'Rain'], {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.9, False: 0.1},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0}
})

print("P(WetGrass=True | Rain=True, Sprinkler=True):", wet_grass.probability(True, {'Rain': True, 'Sprinkler': True}))
