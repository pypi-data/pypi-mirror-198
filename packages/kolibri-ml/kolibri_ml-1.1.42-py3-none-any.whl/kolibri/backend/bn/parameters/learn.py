import bnlearn


def learn_parameters(model_structure, data):
     model_mle=  bnlearn.parameter_learning.fit(model_structure, data, methodtype='maximumlikelihood')
     bnlearn.print_CPD(model_mle)
     return model_mle