---
layout: archive
permalink: /HIGH-HOPeS/
#mathjax: true comment in to enable math
#Possible further headers: Events, Projects/Results, Communication/Presentation, News
---
<script>addBackToTop({
  backgroundColor: '#fff',
  innerHTML: 'Back to Top',
  textColor: '#333'
})</script>
<style>
  #back-to-top {
    border: 1px solid #ccc;
    border-radius: 0;
    font-family: sans-serif;
    font-size: 14px;
    width: 100px;
    text-align: center;
    line-height: 30px;
    height: 30px;
  }
</style>

## HIGH-HOPeS: Higher-Order Hodge Laplacians for Processing of multi-way Signals
![image-right](/images/ERC-FLAG_FP.png){: .align-right}{: width="250"}
[ERC Starting Grant](https://cordis.europa.eu/project/id/101039827){:target="_blank"}  
(ERC StG --  Grant agreement ID: 101039827)   

This project has received funding by the European Union (ERC, HIGH-HOPeS, 101039827). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.

## Overview
Network analysis has revolutionized our understanding of complex systems, and graph-based methods have emerged as powerful tools to process signals on non-Euclidean domains via graph signal processing and graph neural networks. The graph Laplacian and related matrices are pivotal to such analyses: i) the Laplacian serves as algebraic descriptor of the relationships between nodes; moreover, it is key for the analysis of network structure, for local operations such as averaging over connected nodes, and for network dynamics like diffusion and consensus; ii) Laplacian eigenvectors are natural basis-functions for data on graphs and endowed with meaningful variability notions for graph signals, akin to Fourier analysis in Euclidean domains. However, graphs are ill-equipped to encode multi-way and higher-order relations that are becoming increasingly important to comprehend complex datasets and systems in many applications, e.g. to understand group-dynamics in social systems, multi-gene interactions in genetic data, or multi-way drug interactions.
{: .text-justify}

The goal of this project is to develop methods that can utilize such higher-order relations, going from mathematical models to efficient algorithms and software. Specifically, we will focus on ideas from algebraic topology and discrete calculus, according to which the graph Laplacian can be seen as part of a hierarchy of Hodge-Laplacians that emerge from treating graphs as instances of more general cell complexes that systematically encode couplings between node-tuples of any size. Our ambition is to i) provide more informative ways to represent and analyze the structure of complex systems, paying special attention to computational efficiency; ii) translate the success of graph-based signal processing to data on general topological spaces defined by cell complexes; and iii) by generalizing from graphs to neural networks on complexes, gain deeper theoretical insights on the principles of graph neural networks as special case.
{: .text-justify}

<!--## Events-->
<!--**Sep 9 - 11, 2019**, Workshop on Higher-Order Interaction Networks: [Dynamics, Structure, Data](https://www.maths.ox.ac.uk/groups/networks/events/higher-order-interaction-workshop)  -->

<!------------------>
<!--## Selected Projects-->

<!--### Simplicial Complexes as modelling tools for complex systems-->

<!--![image-right](/images/SCexample.png){: .align-right}-->
<!--To integrate higher order interactions into network models, a framework is needed to extend standard graph based approaches.-->
<!--Hypergraphs can provide such a general framework. -->
<!--We concentrate on a particular form of hypergraphs called simplicial complexes (SCs), i.e., finite collections of simplices (nodes, edges, triangular faces, etc.) closed under intersections.-->
<!--We show how simplicial complexes can be used as a natural data model for a variety of systems, study their temporal evolution, and introduce higher-order link prediction as a benchmark problem to assess models and algorithms that predict higher-order structure [1].  -->

<!--Compared to generic hypergraphs, SC have favourable additional algebraic structure, which we aim to exploit in this project.-->
<!--A key ingredient in this context is the hierarchy of the so-called boundary maps and their adjoint co-boundary maps which couple higher-order to lower-order entities (e.g. edges to vertices). Combining these maps in an appropriate manner gives rise to higher-order Laplacian operators. -->
<!--The first order operator is the well-known graph Laplacian matrix, which is paramount for the analysis of networked systems. -->
<!--Like the graph Laplacian in the node domain, its higher order equivalents enable the rigorous definition of diffusive processes (random walks and consensus dynamics) in the domain of edges (node-pairs) and higher order entities [2].-->

<!--#### Related Publications-->
<!--\[1] Benson, A. R.; Abebe, R.; Schaub, M. T.; Jadbabaie, A. & Kleinberg, J.-->
<!--" Simplicial closure and higher-order link prediction" -->
<!--*Proceedings of the National Academy of Sciences*, 2018, [DOI: 10.1073/pnas.1800683115](https://doi.org/10.1073/pnas.1800683115)   -->
<!--\[2] Schaub, M. T.; Benson, A. R.; Horn, P.; Lippner, G. & Jadbabaie, A. "Random walks on simplicial complexes and the normalized Hodge 1-Laplacian", *SIAM Review*, 2020. -->
<!--[DOI: 10.1137/18M1201019](https://doi.org/10.1137/18M1201019)     -->

<!--### Flow decompositions, machine learning and signal processing on graphs and simplicial complexes-->

<!--![image-right](/images/ToyExampleFlowFiltering.png){: .align-left}-->
<!--In many problems modeled using graphs, the data of interest is located on the edges (as opposed to the nodes). A typical scenario of practical interest is a flow on the edges – signal, mass, energy, information – of a graph that is measured and has to be analyzed further, such as traffic flow associated with the edges of a traffic network.-->

<!--To analyze these types of signal we have developed techniques for analyzing the edge-space of graphs and simplicial complexes in more detail [1,2]-->
<!--An important tool in this context is the Hodge decomposition, a decomposition of edge flows into intuitively interpretable components that are analogous to notions such as gradient flows or rotational flows from vector calculus. -->
<!--We have demonstrated how this decomposition can be leveraged for data analytics that extract information about the edge-space that complements and extends typical graph-based analysis.-->

<!--#### Related Publications-->
<!--\[1] Schaub, M. T.; Benson, A. R.; Horn, P.; Lippner, G. & Jadbabaie, A. "Random walks on simplicial complexes and the normalized Hodge 1-Laplacian", *SIAM Review*, 2020. -->
<!--[DOI: 10.1137/18M1201019](https://doi.org/10.1137/18M1201019)     -->
<!--\[2] Schaub M. T.; Segarra, S. "Flow smoothing and denoising: graph signal processing in the edge-space". 2018 IEEE Global Conference on Signal and Information Processing (GlobalSIP), Anaheim, CA, USA, 2018, pp. 735-739. [DOI: 10.1109/GlobalSIP.2018.8646701](https://doi.org/10.1109/GlobalSIP.2018.8646701)   -->
<!--\[3] Jia, J.; Segarra, S.; Schaub, M. T. & Benson, A. R. "Graph-based Semi-Supervised & Active Learning for Edge Flows". Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2019), ACM, 2019 [DOI: 10.1145/3292500.3330872](https://doi.org/10.1145/3292500.3330872)     -->


---------------
## Presentations and Communication 
Research related to the present project was presented at the following places / events.

* Autumn school on hypergraphs, Bernoulli Society Committee on Statistical Network Science, Online, October 2023
* ELLIIT Focus Period Network Dynamics and Control, Linköping, Sweden, September 2023 
* International Congress on Industrial and Applied Mathematics (ICIAM 2023) -- Minisymposium on Higher order networks for complex systems, Tokyo, Japan, August 2023
* Seminar at Chair of Data Analytics and Machine Learning, TUM, Munich, Germany, August 2023
* School lectures: Signal Processing on Networks, NetSci 2023, Vienna, Austria, July 2023
* Applications of Hodge Theory on Networks Workshop, Banff, Canada, February 2023 

<!--## Outreach-->
<!--* MIT Spark Programme, Cambridge, MA, March 2018-->
<!--* St. Ursula Gymnasium Bruehl, Outreach Talk, Germany, November 2017-->

-------------
## Complete Publication list
A list of all publications associated with this project is provided below:

* Hoppe, J. & Schaub, M. T., Representing Edge Flows on Graphs via Sparse Cell Complexes, Learning on Graphs 2023, 2023 (**Best Paper Award**)
* Grande, V. P. & Schaub, M. T.,  Non-isotropic Persistent Homology: Leveraging the Metric Dependency of PH, Learning on Graphs 2023, 2023 
{: .text-justify}

-------------

## Contact
Computational Network Science Group     
Department of Computer Science     
RWTH Aachen University     
Ahornstrasse 50      
52074 Aachen      
Germany
