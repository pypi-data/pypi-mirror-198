import bnlearn as bn

def learn_structure_from_data(data, method_type='cs', scoretype='k2'):

    return bn.structure_learning.fit(data, methodtype=method_type, scoretype=scoretype)
