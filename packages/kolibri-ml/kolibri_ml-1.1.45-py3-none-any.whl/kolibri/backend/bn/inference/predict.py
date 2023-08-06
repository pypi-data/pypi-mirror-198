import bnlearn


def predict(model, variable, evidence):

    return bnlearn.inference.fit(model, variables=variable, evidence=evidence)