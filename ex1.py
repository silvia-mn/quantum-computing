import numpy as np
import math 

# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.
    
    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.
        
    Returns:
        array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    
    norm= ((alpha*alpha.conjugate()+ beta*beta.conjugate()).real)**(1/2)
    alpha_norm= alpha/norm
    beta_norm= beta/norm
    output= alpha_norm*ket_0+ beta_norm*ket_1
    print (output)

    return output
alpha = 2.0 + 1.0j
beta = -0.3 + 0.4j
normalize_state(alpha, beta)    