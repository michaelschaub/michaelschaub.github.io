---
layout: archive
permalink: /Research/
mathjax: true 
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
# Research
My research interest are broad, but have one common denominator: the use of networks to analyse a variety of systems and data.
As networks have become an almost ubiquitous modeling tool in a range of different disciplines, this enables us to naturally connect to a wide range of applications.
The modeling perspective applied in these application areas can be quite different, however.
My work may be partitioned into the following (overlapping) themes.
For more details please also refer to [Publications]({{ site.baseurl }}{% link publications.md %}) and [Code]({{ site.baseurl }}{% link code.md %}).

### Interdisciplinary Applications
One of the strengths of network models is their versatility: networks have become ubiquitous abstractions for social, physical, biological and engineered systems. 
Facilitated by my multidisciplinary background, I have been fortunate to work with great collaborators on a range of applications.
I am particularly interested in biological problems, such as the analysis of neurophysiological data or the analysis of proteins and genetic data, but have also worked on applications concerning technical and social systems in the past.

![image-center](/images/applications.png){: .align-center}{:style="border: 1px solid black; padding: 10px"}

### Modeling and analysing relational data as networks
![image-right](/images/rel_data.png){: .align-right}{:style="border: 0px solid black; padding: 10px"}
One area in which networks have become prevalent is the modeling and analysis of relational data.
For instance, we may have data that measures social relations such as friendship between people.
Such data can be mapped into a network model by identifying people with nodes, and the (measured) relations between them as edges.
Since there is typically uncertainty about the present edges, we may have to adopt a statistical perspective towards the measured network topology and model it via a random graph model.
Many statistical challenges arise from the fact that we are typically confronted with $$n = 1$$ observed network samples.

Some problems we are interested in within this domain is the identification of salient features in such a network, such as the identification of important nodes via centrality measures, or the detection of clusters ("communities") and hierarchical structures potentially present in the network.  

<!--### Dimensionality reduction via graphs-->
<!--In the context of dimensionality reduction, we are often given high-dimensional data in a vector space, e.g., the levels of gene expression within different cells, and want to learn a lower-dimensional representation of such data ("manifold learning").-->

<!--Many popular techniques in this space (diffusion maps, isomap, etc.) are based on the idea of first constructing a graph that encodes the "shape of the data", and then using graph-based analysis to unravel the lower-dimensional geometry of the data.-->
<!--We are interested in exploring connections of this viewpoint to the analysis of relational data, topological data analysis, and the inference of dynamical systems.-->

### Dynamics and data on networks
![image-right](/images/neuro_dyn.png){: .align-left}{:style="border: 0px solid black; padding: 10px"}
In problems emerging from control theory and dynamical systems, we often consider a distributed dynamical system defined on a network structure. A similar view is also adopted in graph signal processing, in which the network defines the domain on which a signal is supported.
The object of interest is an (uncertain) signal defined on the nodes of the graph, e.g., a time-series for each node, or other types of measurements. 

Our work focuses on understanding such dynamics and data in a more principled way by taking into account the underlying network structure.
Problems of interest in this area include i) understanding the emergence of patterns in partially structured network, ii) model-order reduction and its links to graph clustering iii) inference of network structure from dynamics.

### Simplicial complexes and higher-order network models
![image-right](/images/SCexample.png){: .align-right}{:style="border: 0px solid black; padding: 10px"}
Thus far, networks are mostly represented mathematically via graphs.
However, while graphs can capture pairwise interactions between nodes, fundamental interactions in networks often take place between multiple nodes. 
For example, in a biochemical network a reaction often involves more than two species ($$A + B \rightarrow C + D$$), or two reagents might interact only in the presence of an enzyme. 

In this line of research our goal is to investigate new types of models such as hypergraphs and simplicial complexes that account for interactions between groups of nodes (triplets, quadruplets, etc.).
Questions of interest include:
* How can we analyse the effects of non-binary relationships on dynamical properties of networked systems? 
* How can we design decentralized control and optimization strategies, utilizing such non-binary interactions? 
* How can we utilize non-binary relationships for analysis of real world data, e.g., from biological networks?

Please also refer to my Marie Curie project [HIntNets]({{ site.baseurl }}{% link hintnets.md %}).
