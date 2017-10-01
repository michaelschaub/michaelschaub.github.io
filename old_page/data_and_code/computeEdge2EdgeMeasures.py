# LICENCSE (MIT)
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from pylab import *
def computeEdge2EdgeMeasures(A):
	#COMPUTEEDGE2EDGEMEASURES Given a adjacency matrix (weighted 
	# adjacency matrix) A, compute the flow-redistribution matrix, the
	# edge-to-edge transfer function matrix and the embeddedness vector
	# (c) M. Schaub, Imperial College London, mts09@ic.ac.uk
	# Converted to Python by Jeff Alstott, alstottjd@cam.ac.uk


    # If you make use of this code please cite the associated article:
    # "Structure of complex networks: Quantifying edge-to-edge relations by 
    #  failure-induced flow redistribution", Michael T. Schaub, Jörg Lehmann, 
    #  Sophia N. Yaliraki, Mauricio Barahona, Network Science 2(1), 2014, 
    #  pp. 66--89; see also arXiv:0707.0609

	# remove diagonal from matrix
    A[diag_indices_from(A)] = 0

	# compute number of links
    links = (A != 0).sum()


	# find all indices of nodes
    i, j = where(triu(A))
    v = A[i,j]
    print i
    print j
    print v

	#combinatorial Laplacian
    L = diag(A.sum(axis=1)) - A

    E = createIncidenceMatrix(A)

	#M = diag(v)*E'*pinv(full(L))*E
	# faster than above: compute pseudoinverse directly
	#Lp = (L- ones(size(L))/length(L))^-1 + ones(size(L))/length(L);
	#M = diag(v)*E'*Lp*E;

	# even faster: use Gaussian elimination, (note that constant matrix is in 
	# null space of incidence matrix, so can be neglected)
    X = (L- ones(shape(L))/len(L))
    Y = linalg.solve(X,E)
    M = diag(v).dot(E.T).dot(Y)

    epsilon = 1-diag(M)

	# optional: avoid infinite LODF due to tree like structure by thresholding 
	# out...
	# epsilon(abs(epsilon)<1e-12)=Inf;
	 
    K = linalg.solve(diag(epsilon).T, M.T).T

    return K, M, epsilon

def createIncidenceMatrix(A):
	# For a given (undirected) graph with adj matrix A
	# create node-edge incidence matrix E
	# Note that self loops are not taken into account here

	# compute number of links
    links = (A != 0).sum()/2
    nodes = len(A)

	# find all indices of nodes
    i, j = where(triu(A))
	# allocate incidence matrix
	# insert +1/-1 in both node rows and column given by edge id
    E = zeros((nodes, links))
    E[i, arange(links)] = -1
    E[j, arange(links)] = 1
    return E
