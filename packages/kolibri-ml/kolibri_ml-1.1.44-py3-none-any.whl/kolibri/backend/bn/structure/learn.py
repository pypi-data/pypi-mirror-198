import bnlearn as bn

def learn_structure_from_data(data, method_type='constraints'):

    if method_type == 'constraints':
        return bn.structure_learning.fit(data, methodtype='cs', scoretype='bdeu')
