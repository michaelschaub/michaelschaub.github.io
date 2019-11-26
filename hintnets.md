---
layout: archive
permalink: /HIntNets/
#mathjax: true comment in to enable math
#Possible further headers: Events, Projects/Results, Communication/Presentation, News
---

## HIntNets: Higher-order interactions and Laplacian dynamics in complex networks: structure, dynamics and control
![image-right](/images/EuropeFlag.png){: .align-right}
[Marie Skłodowska-Curie Individual Fellowships](http://cordis.europa.eu/project/rcn/207743_en.html){:target="_blank"}  
(MSCA-IF-GF - Global Fellowships, Project ID: 702410)   

This page collects information about the project "HIntNets".  
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant agreement No 702410.

## Overview
Complex networks are an essential ingredient of modern life, and underpin integral parts of our biological, physical, technological and socio-economic universe. 
Thus far, such networks have been mainly represented as graphs. 
However, while graphs can capture pairwise interactions between nodes, fundamental interactions in networks often take place between multiple nodes. 
For example, in socio-economic networks, the joint coordinated activity of several agents (e.g., buyer, seller, broker); the formation and interactions of coalitions; the emergence of peer pressure; and the existence of triadic closure are all prevalent.

To investigate such group interactions in complex networks and their dynamical implications is the main objective of this interdisciplinary project.
Specifically, we will investigate how such interactions can be taken into account for modelling, analysis and design of complex networks, and will investigate generalized network models.
While in some cases data about group interactions is readily available, in many cases the groupings or even the network of interactions might be unknown.
We will thus further investigate techniques to infer (generalized) networks and group structures from available interaction data.

The overarching goal of this research is to elucidate relations between structure, dynamics and function in complex systems.

## Events
**Sep 9 - 11, 2019**, Workshop on Higher-Order Interaction Networks: [Dynamics, Structure, Data](https://www.maths.ox.ac.uk/groups/networks/events/higher-order-interaction-workshop)  
**May 28, 2019**, Workshop on Higher-Order Models in Network Science [HONS 2019](https://uzhdag.github.io/hons_web) (part of Netsci 2019).  
**June 12, 2018**, Workshop on Higher-Order Models in Network Science [HONS 2018](https://uzhdag.github.io/hons_web/2018/index.html) (part of Netsci 2018).  

--------------
## Selected Projects

### Simplicial Complexes as modelling tools for complex systems

![image-right](/images/SCexample.png){: .align-right}
To integrate higher order interactions into network models, a framework is needed to extend standard graph based approaches.
Hypergraphs can provide such a general framework. 
We concentrate on a particular form of hypergraphs called simplicial complexes (SCs), i.e., finite collections of simplices (nodes, edges, triangular faces, etc.) closed under intersections.
We show how simplicial complexes can be used as a natural data model for a variety of systems, study their temporal evolution, and introduce higher-order link prediction as a benchmark problem to assess models and algorithms that predict higher-order structure [1].  

Compared to generic hypergraphs, SC have favourable additional algebraic structure, which we aim to exploit in this project.
A key ingredient in this context is the hierarchy of the so-called boundary maps and their adjoint co-boundary maps which couple higher-order to lower-order entities (e.g. edges to vertices). Combining these maps in an appropriate manner gives rise to higher-order Laplacian operators. 
The first order operator is the well-known graph Laplacian matrix, which is paramount for the analysis of networked systems. 
Like the graph Laplacian in the node domain, its higher order equivalents enable the rigorous definition of diffusive processes (random walks and consensus dynamics) in the domain of edges (node-pairs) and higher order entities [2].

#### Related Publications
\[1] Benson, A. R.; Abebe, R.; Schaub, M. T.; Jadbabaie, A. & Kleinberg, J.
" Simplicial closure and higher-order link prediction" 
*Proceedings of the National Academy of Sciences*, 2018, [DOI: 10.1073/pnas.1800683115](https://doi.org/10.1073/pnas.1800683115)   
\[2] Schaub, M. T.; Benson, A. R.; Horn, P.; Lippner, G. & Jadbabaie, A. "Random walks on simplicial complexes and the normalized Hodge Laplacian", 2018,
[arXiv:1807.05044](https://arxiv.org/abs/1807.05044)     

### Flow decompositions, machine learning and signal processing on graphs and simplicial complexes

![image-right](/images/ToyExampleFlowFiltering.png){: .align-left}
In many problems modeled using graphs, the data of interest is located on the edges (as opposed to the nodes). A typical scenario of practical interest is a flow on the edges – signal, mass, energy, information – of a graph that is measured and has to be analyzed further, such as traffic flow associated with the edges of a traffic network.

To analyze these types of signal we have developed techniques for analyzing the edge-space of graphs and simplicial complexes in more detail [1,2]
An important tool in this context is the Hodge decomposition, a decomposition of edge flows into intuitively interpretable components that are analogous to notions such as gradient flows or rotational flows from vector calculus. 
We have demonstrated how this decomposition can be leveraged for data analytics that extract information about the edge-space that complements and extends typical graph-based analysis.

#### Related Publications
\[1] Schaub, M. T.; Benson, A. R.; Horn, P.; Lippner, G. & Jadbabaie, A. "Random walks on simplicial complexes and the normalized Hodge Laplacian", 2018,
[arXiv:1807.05044](https://arxiv.org/abs/1807.05044)     
\[2] Schaub M. T.; Segarra, S. "Flow smoothing and denoising: graph signal processing in the edge-space". 2018 IEEE Global Conference on Signal and Information Processing (GlobalSIP), Anaheim, CA, USA, 2018, pp. 735-739. [DOI: 10.1109/GlobalSIP.2018.8646701](https://doi.org/10.1109/GlobalSIP.2018.8646701)   
\[3] Jia, J.; Segarra, S.; Schaub, M. T. & Benson, A. R. "Graph-based Semi-Supervised & Active Learning for Edge Flows". Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2019), ACM, 2019 [DOI: 10.1145/3292500.3330872](https://doi.org/10.1145/3292500.3330872)     


---------------
## Presentations and Communication 
Research related to the present project was presented at the following places / events.

* Control and Optimization Journal Club, University of Oxford, UK, October 2019
* Networks Seminar, Mathematical Institute, University of Oxford, UK, October 2019
* Algebra Statistics and Optimization Seminar, MIT, Cambridge MA, USA, April 2019
* University Utrecht, Netherlands, April 2019.
* University of Oxford, United Kingdom, March 2019.
* Institute for Computational Biology, Helmholtz Zentrum München, Germany. February 2019. 
* FZ Juelich, Germany. December 2018.
* Complex Networks 2018, Cambridge, United Kingdom, December 2018
* Growth Lab Seminar, Center for International Development, Harvard University, Cambridge, USA, September 2018
* PostDoc Lunch Seminar, Institute of Data, Systems and Society, MIT, Cambridge MA, USA, August 2018
* International Conference on Complex Networks (ICCS) 2018, Boston MA, USA, July 2018
* Imperial College London, Biomathematics Seminar, United Kingdom, November 2017
* Netsci 2018 - Machine Learning in Network Science Workshop, Paris, France, June 2018
* Netsci 2018, Paris, France, June 2018
* Complenet 2018, Boston MA, USA, March 2018
* University of Oxford, SysSoS group seminar, United Kingdom, November 2017
* Université catholique de Louvain, Applied Mathematics Seminar / ICTEAM, Belgium, November 2017


## Outreach
* MIT Spark Programme, Cambridge, MA, March 2018
* St. Ursula Gymnasium Bruehl, Outreach Talk, Germany, November 2017

## Contact
**@MIT**   
Institute for Data, Systems, and Society  
Massachusetts Institute of Technology  
77 Massachusetts Avenue,  
Office: E18-425C  
Cambridge, MA, 02139 

**@Oxford**   
Department of Engineering Science   
University of Oxford   
Parks Road   
Oxford, OX1 3PJ 
