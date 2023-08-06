import numpy as np

#############################
#### Lexicographic Sort #####
#############################

def L_binarysearch(A, T, L=0, R=None):
    """
    np.searchsorted has no contraints, i.e. L nor R
    GIVEN:  A (1d sorted numpy.array)
            T (searched for entry)
            *L (lowest  index to search for)
            *R (highest index to search for)
    GET:    L (left-(lowest) most index of entry)
    """
    if R is None:
        R = len(A)
    while L < R:
        m = (L + R) // 2
        if A[m] < T:
            L = m + 1
        else:
            R = m
    return L

def R_binarysearch(A, T, L=0, R=None):
    """
    np.searchsorted has no contraints, i.e. L nor R
    GIVEN:  A (1d sorted numpy.array)
            T (searched for entry)
            *L (lowest  index to search for)
            *R (highest index to search for)
    GET:    R (right-(highest) most index of entry)
    """
    if R is None:
        R = len(A)
    while L < R:
        m = (L + R) // 2
        if A[m] > T:
            R = m
        else:
            L = m + 1
    return R

def interval_binarysearch(A, value, L=0, R=None):
    return L_binarysearch(A, value, L=L, R=R), R_binarysearch(A, value, L=L, R=R)

def tuplebsearch_interval(B, value, L=0, R=None):
    for columns in range(B.shape[0]): ### over entries/columns of the tuple
        L, R = interval_binarysearch(B[columns,:], value[columns], L=L, R=R)
    return L, R

def tuple_greater(A, B): ## A > B ?
    ## O ~ n + n + n + 1 + 1 ~ 3n + 2, 
    ## (1) subtract (2) comparison (nonzero) (3) find argmax (4) subindex (5) compare to 0
    BA = B - A
    return BA[np.argmax( BA!=0 )] < 0

def log_domain(A):
    """
    GIVEN:  A (sorted 1d numpy array)
    GET:    domains (sorted 1d numpy array, ranges of unique elements)
    """
    domain = [0]
    while domain[-1]!=len(A):
        domain.append( R_binarysearch(A, A[domain[-1]], L=domain[-1], R=None) )
    return np.asarray(domain)

def R_tbs(A, T, L=0, R=None):
    """ tbs = tuple-binary-search
    GIVEN:  A (2d lsorted np.array dtype=int16/32/64)
            T (tuple/1d-array/list : searched for entry)
            *L (int : lowest  index bound)
            *R (int : highest index bound)
    GET:    R (right-(highest) most index of entry)
    """
    if R is None:
        R = (A.shape[1])
    while L < R:
        m = (L + R) // 2
        if tuple_greater(A[:,m], T): ##A[m] > T 
            R = m
        else:
            L = m + 1
    return R

def tuple_domain(A):
    """
    GIVEN:  A (lexicographically-sorted 2d numpy array (columns, rows))
    GET:    domains (sorted 1d numpy array, ranges of unique elements)
    """
    domain = [0]
    while domain[-1]!=(A.shape[1]):
        domain.append( R_tbs(A, A[:,domain[-1]], L=domain[-1], R=None) )
    return np.asarray(domain)

#############################
### Sparse Array Object #####
#############################

class sparse_array():
    def __init__(self, indices=np.array([[]]), data=np.array([]), shape=np.array([0]), idx_dtype=np.int32, wellordered=False):
        self.indices     = indices
        self.data        = data
        self.shape       = shape
        self.wellordered = wellordered
        self.run()

    def sparsity(self):
        return len(self.data)/np.prod(self.shape)

    def wellorder(self):
        if self.wellordered:
            return None
        if (len(self.data)>0) and not self.wellordered:
            ### order (lexsort)
            args = np.lexsort(np.flip(self.indices, axis=0), axis=0)
            self.indices = self.indices[:,args]
            self.data    = self.data[args]  

            ### well-order (sum-over duplicates)
            i,k=0,0
            while k!=self.indices.shape[1]: ## find unique-domains (sections of sorted arrays that are unique)
                LR      = tuplebsearch_interval(self.indices, self.indices[:,k], L=k) ## only need tuple_R_bsearch()
                self.data[i]      = np.sum(self.data[LR[0]:LR[1]])
                self.indices[:,i] = self.indices[:,LR[0]]
                i+=1
                k=1*LR[1] ## deep-copy    
            self.indices = self.indices[:,:i]
            self.data    = self.data[:i]
            self.wellordered = True
            return None

    def Sparse_to_Dense(self):
        out = np.zeros(self.shape, dtype=self.data.dtype)
        out[tuple( self.indices )] = self.data
        return out

    def remove(self, tol=0.):
        keep = (np.abs(self.data) >= tol)
        self.data    = self.data[keep]
        self.indices = self.indices[:,keep]
        return None

    def run(self):
        ### input checks
        if isinstance(self.data, np.ndarray) and isinstance(self.indices, np.ndarray):
            if self.indices.ndim==2: # and self.data.ndim==1
                if self.indices.shape[0] > self.indices.shape[1] and self.indices.shape[0]>30:
                    self.indices = self.indices.swapaxes(0,1)
                if self.indices.shape[0]==len(self.shape) and self.indices.shape[1]==self.data.size:
                    None
                else:
                    raise Exception("Data & Index_array size or shape & Index_array not compatible")
            else:
                raise Exception("Index Array must be 2d")   
        else:
            raise Exception("Indices and Data-values must be np.arrays")   
        ###

        self.wellorder() ## wellorder indices
        return None

def Dense_to_Sparse(A, tol=1.E-8):
    """
    Given:  A (arbitrary dimensional numpy.array)
            tol (tolerance, range of values which may be set to "0")
    Get:    sparse_array_object
    """
    indices=np.asarray(np.where(np.abs(A) >= tol))
    return sparse_array(indices=indices, data=A[tuple( indices )], shape=np.asarray(A.shape), wellordered=True)

#############################
### sparse-tensor-product ###
#############################

def cartesian_product(a,b):
    ab = (a[:,:,None]*np.ones(b.shape[1],dtype=a.dtype)[None,:]).reshape((a.shape[0], a.shape[1]*b.shape[1]))
    ba = (b[:,None,:]*np.ones(a.shape[1],dtype=b.dtype)[:,None]).reshape((b.shape[0], a.shape[1]*b.shape[1]))
    return np.concatenate((ab, ba))

def sparse_tensor_product(A, B):
    ## check if wellordered
    if not A.wellordered:
        A.wellorder()
    if not B.wellordered:
        B.wellorder()

    C = sparse_array()
    C.shape   = np.concatenate(( A.shape, B.shape ))
    C.indices = cartesian_product( A.indices, B.indices )
    C.data    = np.outer( A.data, B.data ).reshape(-1)
    C.wellordered = True
    return C

#############################
### einsum-rule to labels ###
#############################

def Ord(s):
    """
    convert a collection of strings (word) str into int-np.array
    """
    return np.asarray( [ord(i) for i in s] )

def decompose_einsum(einsum_rule):
    """
    decompose an np.einsum rule/Rx into numerical list-of-1d.np.arrays and RHS array
    """
    LHSRHS = einsum_rule.replace(" ", "").split("->")
    if len(LHSRHS)==2: ## with "->" divider
        LHS    = LHSRHS[0]
        RHS    = Ord( LHSRHS[1] )
        labels = [ Ord(i) for i in LHS.split(",") ]
        if not np.all(np.bitwise_or.reduce(np.unique(np.concatenate(labels))[None,:]==RHS[:,None],1)):
           raise Exception("entires on RHS must be on the LHS") 
    else: ## no "->" divider
        LHS    = LHSRHS
        RHS    = None
        labels = [ Ord(i) for i in LHS.split(",") ]
    return labels, RHS

#############################
#### intra-intersection #####
#############################

def unique_in_og_order(X):
    """ 
    get uniques in X, in its order (unsorted)
    EXAMPLE: [4, -1, -1, -2, 4, -2, 3, -1, 3, 1, -1, -2, -3, -1] -> [ 4, -1, -2,  3,  1, -3]
    """
    x = np.argsort(X)
    u = np.where( np.diff( X[x] , prepend=X[x][0]-1) > 0)[0]
    return X[np.sort( x[u] )], np.sort( x[u] )

def intraintersect(A, rule):
    """
    IN-PLACE function to remove redundant degrees-of-freedom (columns)
    as determined by label/rule for a sparse_array
    Given : A (sparse_array)
            rule (string or array)
    Get :   rule' (of new sparse-array in intertrace)
    algorthim O ~ N, element-wise-search 
    """

    if len(rule) != len(A.indices):
        raise Exception("Error, indices' rules are inconsistent!")

    u_rule = np.unique(rule)
    if len(u_rule)==len(rule): ## no repeats so bypass
        return rule

    out=[]
    for element in np.unique(rule):  ## goes along each unique axis-type/letter, regardless free or dumb
        key = np.where(rule == element)[0]
        out.append(key[0])
        if len(key) < 2:
            continue

        ### find the indices if they match within a key, key = index
        idx_it    = np.all(np.diff( A.indices[key] , axis=0 ) == 0, axis=0)
        A.indices = A.indices[:, idx_it ]
        A.data    = A.data[ idx_it ]

    out = np.asarray(out)
    rule = rule[out]
    A.indices = A.indices[out]
    A.shape   = np.asarray(A.shape)[ out ]
    
    return rule

#############################
#### label-intersection #####
#############################

def label_intersection(A, B, labels, RHS, intersect): ### remove intradummies here?? A, B, 
    """
    Given : labels (list of arrays, with UNIQUE entries!)
            RHS
    Get :   labels (list of int-np.arrays)
            overlaps (list of boolean-np.arrays)
            frees (list of boolean-np.arrays)
            intradummies (list of boolean-np.arrays)
            RHS (list of int-np.arrays)
    """

    ### label-intersection (both intra-dummy & intra-frees) ##!! bring outside??
    #intersect = np.intersect1d(labels[0], labels[1]) ## intersection elements
    overlap_A = np.bitwise_or.reduce(labels[0][:,None]==intersect[None,:], 1)
    overlap_B = np.bitwise_or.reduce(labels[1][:,None]==intersect[None,:], 1)
    
    intra_indicesA = np.logical_not(overlap_A) ## bool-np.array, True="not in the overlap AnB"
    intra_indicesB = np.logical_not(overlap_B) ## bool-np.array, True="not in the overlap AnB"
    if RHS is None: ## no "->" divider
        ## indices-not in intersection are by-default free !in-order! Einstein-convention
        RHS = np.concatenate((labels[0][intra_indicesA], labels[1][intra_indicesB])) 

    labels[0][overlap_A] *= -1 ## (if-in-overlap) *(-1)
    labels[1][overlap_B] *= -1 ## (if-in-overlap) *(-1)

    ### frees
    freesA = np.bitwise_or.reduce(labels[0][:,None]==RHS[None,:], 1) ## bool np.array, True = dummy-index
    freesB = np.bitwise_or.reduce(labels[1][:,None]==RHS[None,:], 1) ## bool np.array, True = dummy-index

    ### freesB, if freesB is in overlapB do not include, in freesB
    freesB = np.logical_xor( freesB , np.logical_and(freesB, overlap_B) )

    ### find dummies....find indices for each label which are not in RHS
    dummiesA  = np.logical_not(freesA) ## bool np.array, True = dummy-index
    dummiesB  = np.logical_not(freesB) ## bool np.array, True = dummy-index

    ###### dummies which are not in the intersection....
    # dummies in both (not in intersection) & (dummy)....
    not_intradummiesA = np.logical_not(np.logical_and(dummiesA, intra_indicesA)) ## bool-np.array, False = intra-dummy-index
    not_intradummiesB = np.logical_not(np.logical_and(dummiesB, intra_indicesB)) ## bool-np.array, False = intra-dummy-index
    
    if not np.all(not_intradummiesA): ## if any "False" exists, i.e. logical-AND
        A.wellordered = False
        A.indices = A.indices[not_intradummiesA,:] ## remove intradummies
        A.shape   = A.shape[not_intradummiesA]
        labels[0] = labels[0][not_intradummiesA]
        freesA    = freesA[not_intradummiesA]
        overlap_A = overlap_A[not_intradummiesA]
    if not np.all(not_intradummiesB): ## if any "False" exists, i.e. logical-AND
        B.wellordered = False
        B.indices = B.indices[not_intradummiesB,:]
        B.shape   = B.shape[not_intradummiesB]
        labels[1] = labels[1][not_intradummiesB]
        freesB    = freesB[not_intradummiesB]
        overlap_B = overlap_B[not_intradummiesB]
    ######

    return labels, [overlap_A, overlap_B], [freesA, freesB], RHS

#############################
### prepare-sparse-arrays ###
#############################

def get_uarg(u, I):
    """
    GIVEN:    I : 1d np.array : indices to sort array (argsort)
              u : 1d np.array : with unique entries (including the len(I))
    GET : surjective uarg : 1d np.array of len(I)
    """
    uarg = np.arange(u[-1])
    for i in range(len(u)-1):
        uarg[u[i]:u[i+1]] = i
    return uarg[I]

def iargsort(i):
    ## https://stackoverflow.com/questions/2483696/undo-or-reverse-argsort-python @jesse
    i_rev    = np.zeros(len(i), dtype=i.dtype)
    i_rev[i] = np.arange(len(i))
    return i_rev

def Prepare(A, B, labels, overlaps, frees):
    """
    In-place modify sparse-arrays: A, B (order along intersection)
    create sparse-array C (containing the frees indices \& data '= 0)
    """

    ### reorder columns to have overlap-dummies/overlap-frees/frees (sort overlap)
    I_A = np.argsort( labels[0] ) ## overlap frees need not be sorted!!!!!
    A.shape     = A.shape[I_A]
    labels[0]   = labels[0][I_A]
    overlaps[0] = overlaps[0][I_A]
    frees[0]    = frees[0][I_A]
    I_B = np.argsort( labels[1] ) ## overlap frees need not be sorted!!!!!
    B.shape     = B.shape[I_B]
    labels[1]   = labels[1][I_B]
    overlaps[1] = overlaps[1][I_B]
    frees[1]    = frees[1][I_B]
    A.indices   = A.indices[I_A,:]
    B.indices   = B.indices[I_B,:]
    A.wellordered=False
    B.wellordered=False
    A.wellorder() ## well-order in this new column-sequence (sum over intradummies) (including overlaps and free)
    B.wellorder() ## well-order in this new column-sequence

    ### extract frees (omit copy overlap-frees) and lexsort
    F_A = A.indices[frees[0]]
    F_B = B.indices[frees[1]] ## if freeB in overlapB do not include!!!
    if len(F_A)==0: ## if A does not have free indices
        F_A = np.array([np.zeros(1, dtype=A.indices.dtype)])
        i_A = np.zeros(A.indices.shape[1], dtype=A.indices.dtype)
        u_A = np.array([0,1])
        shapeA = np.array([1])
    else:
        i_A = np.lexsort(np.flip( F_A , axis=0), axis=0)
        F_A = F_A[:,i_A]
        i_A = iargsort(i_A)
        u_A = tuple_domain(F_A)
        i_A = get_uarg(u_A, i_A)
        shapeA = A.shape[frees[0]]
    if len(F_B)==0: ## if B does not have free indices
        F_B = np.array([np.zeros(1, dtype=B.indices.dtype)])
        i_B = np.zeros(B.indices.shape[1], dtype=B.indices.dtype)
        u_B = np.array([0,1])
        shapeB = np.array([1])
    else:  
        i_B = np.lexsort(np.flip( F_B , axis=0), axis=0)
        F_B = F_B[:,i_B]
        i_B = iargsort(i_B)
        u_B = tuple_domain(F_B)
        i_B = get_uarg(u_B, i_B)
        shapeB = B.shape[frees[1]]

    ### make C
    C = sparse_array()
    C.indices = cartesian_product( F_A[:,u_A[:-1]], F_B[:,u_B[:-1]] )
    C.data    = np.zeros( (len(u_A[:-1]), len(u_B[:-1])) , dtype=A.data.dtype)
    C.shape   = np.concatenate(( shapeA , shapeB ))
    C.wellordered = True
    C_label   = np.concatenate(( labels[0][frees[0]], labels[1][frees[1]] ))
    
    ### extract overlaps
    A.shape   = A.shape[overlaps[0]]
    A.indices = A.indices[overlaps[0],:]
    B.shape   = B.shape[overlaps[1]]
    B.indices = B.indices[overlaps[1],:]

    return C, C_label, i_A, i_B

#############################
#### direct-intersection ####
#############################

def kron1(a,b):
    return (a[:,None]*np.ones(b.shape[0],dtype=a.dtype)[None,:]).reshape(-1)

def kron2(a,b):
    return (b[None,:]*np.ones(a.shape[0],dtype=b.dtype)[:,None]).reshape(-1)

def direct_intersection(A, B, C, i_a, i_b):
    """
    INPLACE modification of C (sparse-array)
    Given : A, B, C  sparse-arrays (C being the output)
            i_a & i_b : surjective dumb-to-free mapping
    Get : C 
    """
    X_   = np.zeros( (2,2) , dtype=np.int64)
    END1,END2=0,0
    while END1 < A.indices.shape[1]: 

        X_[0] = tuplebsearch_interval(A.indices, A.indices[:,END1], L=END1) ## I_tbs tuplebsearch_interval
        X_[1] = tuplebsearch_interval(B.indices, A.indices[:,END1], L=END2)
        if X_[1][0]==X_[1][1]: ### not-found!
            END2 = X_[1][1]
        else: ## found
            a  = np.arange(X_[0,0], X_[0,1])
            b  = np.arange(X_[1,0], X_[1,1])
            aa = i_a[ kron1(a,b) ] ##! i_a composed direct_sum 1st column (uarg of F_a)
            bb = i_b[ kron2(a,b) ] ##! i_b composed direct_sum 2nd column (uarg of F_b)
            C.data[ aa, bb ] += np.outer( A.data[a], B.data[b]).reshape(-1)
            END2 = X_[1][1]

        if END2 >= B.indices.shape[1]:
            break

        X_[0] = tuplebsearch_interval(A.indices, B.indices[:,END2], L=END1)
        X_[1] = tuplebsearch_interval(B.indices, B.indices[:,END2], L=END2) ## I_tbs tuplebsearch_interval
        if X_[0][0]==X_[0][1]: ### not-found!
            END1 = X_[0][1]
        else: ## found
            a  = np.arange(X_[0,0], X_[0,1])
            b  = np.arange(X_[1,0], X_[1,1])
            aa = i_a[ kron1(a,b) ] ##! i_a composed direct_sum 1st column (uarg of F_a)
            bb = i_b[ kron2(a,b) ] ##! i_b composed direct_sum 2nd column (uarg of F_b)
            C.data[ aa, bb ] += np.outer( A.data[a], B.data[b]).reshape(-1)
            END1 = X_[0][1]
    C.data = C.data.reshape(-1)
    return C

#############################
###### final-transpose ######
#############################

def reorder_if_needed(C, C_label, RHS):
    """
    ***IN-PLACE function for C***
    Goal :  change C_label until: RHS == C_label (a change columns accoridng to C_label)
    
    for each element in RHS, build output, if RHS==C_label: do nothing....
    """
    if np.all(RHS==C_label): ## logical-AND
        return None
    else:
        emptyarray = np.empty((len(RHS), C.indices.shape[1]), dtype=C.indices.dtype) 
        for i in range(len(RHS)):
            j=np.where(C_label==RHS[i])[0]
            emptyarray[i,:] = C.indices[j,:]
        C.indices     = emptyarray
        C.wellordered = False
        C.wellorder()
    C_label = RHS
    return None

#############################
##### fast-tensor-trace #####
#############################

def ftt(einsum_rule, A, B):
    """
    Given : 2 sparse
    """

    ## listize the string-type einsum_rule
    LHS, RHS = decompose_einsum(einsum_rule)

    ## remove duplicates in own-label, i.e. intraintersect
    # we need to bypass this if-not needed very-expensive
    LHS[0] = intraintersect(A, LHS[0]) 
    LHS[1] = intraintersect(B, LHS[1])

    ## get label overlaps (inter-duplicates)
    intersect = np.intersect1d(LHS[0], LHS[1]) ## intersection elements
    LHS, overlaps, frees, RHS = label_intersection(A, B, LHS, RHS, intersect)

    #if np.any(overlaps[0]): ## if overlaps exist do direct-intersection
    if len(intersect)!=0:
        C, C_label, i_a, i_b = Prepare(A, B, LHS, overlaps, frees)
        C = direct_intersection(A, B, C, i_a, i_b)
        C.remove()
    else: 
        C = sparse_tensor_product(A, B)
        C_label = np.concatenate(LHS)

    reorder_if_needed(C, C_label, RHS)
    return C























