---
layout: archive
title: Code
permalink: /Code/
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
Below you find brief descriptions and the links to code related to several projects.

* [Simplicial closure and higher-order link prediction](#SCCLOSURE)
* [Generalized Louvain algorithm](#GENLOUVAIN)
* [Creating slow switching cell assemblies](#SSA)
* [Detecting cell assemblies in neural data](#DETECTCA)
* [Quantifying Edge-to-Edge relationships in complex networks](#EDGETOEDGE)
* [Markov zooming map-equation](#MARKOVMAP)
* [Markov Stability](#MARKOVSTABILITY)

## Simplicial closure and higher-order link prediction
{: #SCCLOSURE}
Many complex systems includes interactions that take place among more than two nodes at once.
For example, communication within a group rather than person to person, col- laboration among a team rather than a pair of coauthors 
We study 19 datasets from biology, medicine, social networks, and the web and characterize how higher-order structure emerges and differs between domains. 
We further propose a framework for evaluating higher-order data models based on link prediction:the prediction of future interactions based on a system’s structure and past history.

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/SCexample.png){: .align-center}
</div>

The associated code and datasets can be found here:
[https://github.com/arbenson/ScHoLP-Tutorial](https://github.com/arbenson/ScHoLP-Tutorial){:target="_blank"}

\[1] Benson, A. R.; Abebe, R.; Schaub, M. T.; Jadbabaie, A. & Kleinberg, J.
" Simplicial closure and higher-order link prediction" 
*Proceedings of the National Academy of Sciences*, 2018, [DOI: 10.1073/pnas.1800683115](https://doi.org/10.1073/pnas.1800683115)   

-------------------------
## Dynamical Modules in Complex Systems / Generalized Louvain optimization
{: #GENLOUVAIN}

Complex systems and relational data are often abstracted as dynamical processes on networks. To understand, predict and control their behavior a crucial step is to extract reduced descriptions of such networks. Inspired by notions from Control Theory, we have proposed a time-dependent dynamical similarity measure between nodes, which quantifies the effect that a node input has on the network over time.
Using this embedding we can try to partition the graph into dynamical modules, capturing dynamic similarity between nodes at different time scales.


<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/GenLouvain.png){: .align-center}
</div>


Matlab/C++ code for the associated generalized Louvain optimization scheme can be found here:
[https://github.com/michaelschaub/generalizedLouvain](https://github.com/michaelschaub/generalizedLouvain){:target="_blank"}

Feel free to send me an email with any suggestions, questions etc. regarding the code.  

\[1] "Multiscale Dynamical Embeddings of Complex Networks", Michael T. Schaub, J.-C. Delvenne, R. Lambiotte, and Mauricio Barahona, https://arxiv.org/abs/1804.03733

-------------------------
## Slow Switching Assemblies in Structured networks
{: #SSA}

Understanding how the complex orchestration of neuronal firing activity is determined by the structure of the underlying network (i.e., its wiring) is an important step towards comprehending how neural computation is manifested, especially given the growing experimental access to temporal record- ings and connectomics. I a recent work \[1] we investigated the link between network structure and the dynamics of neuronal assemblies in the context of leaky-integrate-and-fire (LIF) networks. We show how structural features in the wiring of the network can introduce additional time-scales to the dynamics, and how such structured wiring can lead to spatio-temporally segregated, coherent activity of groups of neurons, including both inhibitory and excitatory neurons 

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/SlowDynamics.png){: .align-center}
</div>


Matlab code for reproducing our results can be found here:  
[https://github.com/CellAssembly/SSA-Dynamics](https://github.com/CellAssembly/SSA-Dynamics){:target="_blank"}

Feel free to send me an email with any suggestions, questions etc. regarding the code.  

\[1] "Emergence of Slow-Switching Assemblies in Structured Neuronal Networks", Michael T. Schaub*, Yazan N. Billeh*, Costas A. Anastassiou, Christof Koch and Mauricio Barahona, PLoS Computational Biology 11(7), 2015, pp. e1004196 (* denotes equal contribution); see also arXiv:1502.05656


-------------------------
## Detecting Cell Assemblies in Neural Spike trains
{: #DETECTCA}

Give a set of recorded spike trains, how can we detect possible structured activity in the data, possibly stemming from neural cell assemblies? Using the Markov stability framework in combination with a new functional connectivity measure, we have provided a tool for solving this problem in a recent publication \[1]. Our dynamics driven methodology is able to extract patterns in the spike trains a multiple scales, without any prior knowledge of their expected size. 

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/CellAssemblyDetect.png){: .align-center}
</div>

Matlab code can be found here: [https://github.com/CellAssembly/Detection](https://github.com/CellAssembly/Detection){:target="_blank"}

\[1] "Revealing cell assemblies at multiple levels of granularity", Yazan N. Billeh*, Michael T. Schaub*, Costas A. Anastassiou, Mauricio Barahona, and Christof Koch, Journal of Neuroscience Methods 236(0), 2014, pp. 92-106 (* denotes equal contribution); see also arXiv:1411.2103 

-----------------------
## Quantifying Edge-to-Edge relations
{: #EDGETOEDGE}

Most network analysis considers the nodes as the primary entities of importance. However, there are arguable a number of cases in which relations between edges are of interest, in particular if there is a flow occuring on th edges. In Ref. \[1], we have presented graph-theoretical measures to quantify edge-to-edge relations. Our measures can reveal the dynamical interplay between the edges of a network, including potentially non-local interactions.

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/FR_schematic2.png){: .align-center}
</div>

Matlab code implementing our edge-measures can be found [HERE](/old_page/data_and_code/computeEdge2EdgeMeasures.m).  
There is a python implementation available as well [HERE](/old_page/data_and_code/computeEdge2EdgeMeasures.py), thanks to Jeff Alstott (Cambridge)!  

Feel free to send me an email with any suggestions, questions etc. regarding the code.  

\[1] "Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution", Michael T. Schaub, Jörg Lehmann, Sophia N. Yaliraki, Mauricio Barahona, Network Science 2(1), 2014, pp. 66--89; see also arXiv:0707.0609 

--------------------------
## Markov Zooming Map Equation
{: #MARKOVMAP}

In some recent work we have presented a dynamical extension to the so called "map equation" framework by Rosvall and coworkers \[1]. Within this work \[2] we could show that the standard map equation is prone to show a so called field of view limit \[2,3], which effectively results in an overclustering of a network if the community structure is not sufficiently dense. By endowing the map equation with an explicitely time-dependent flow model one can scan across all scales in a natural manner and thus effectively evade the field of view problem \[2].

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/MarkovMap.jpg){: .align-center}
</div>

A recent zip archive of the code can be found [HERE](https://github.com/michaelschaub/MarkovZoomingMap/zipball/master). The code is hosted on github with an associated homepage here:  

[https://github.com/michaelschaub/MarkovZoomingMap](https://github.com/michaelschaub/MarkovZoomingMap){:target="_blank"} -- git repository  
[http://michaelschaub.github.com/MarkovZoomingMap/](http://michaelschaub.github.com/MarkovZoomingMap/){:target="_blank"} -- associated homepage  

Feel free to send me an email with any suggestions, questions etc. regarding the code or make use of the repository to contribute.  

\[1] "Maps of information flow reveal community structure in complex networks", Martin Rosvall and Carl T. Bergstrom, PNAS 105, 1118 (2008); see also arXiv:0707.0609  
\[2] "Encoding dynamics for multiscale community detection: Markov time sweeping for the Map equation", M.T. Schaub,
R. Lambiotte, M. Barahona, Phys. Rev. E., Aug, 2012. Vol. 86, pp. 026112. American Physical Society; see also arXiv:1109.6642  
\[3] "Markov dynamics as a zooming lens for multiscale community detection: non clique-like communities and the field-of-view limit", Schaub, M. T.; Delvenne, J.-C.; Yaliraki, S. N. & Barahona, M. PLoS ONE, Public Library of Science, 2012, 7, e32210  

----------------------------------
## Stability of a graph partition
{: #MARKOVSTABILITY}

Looking for code of the stability method?  
You can find it here:
[http://www2.imperial.ac.uk/~mpbara/Partition_Stability/](http://www2.imperial.ac.uk/~mpbara/Partition_Stability/){:target="_blank"}

<div style="border: 1px solid black; padding: 0px;" markdown="1">
![image-center](/images/screenshot.png){: .align-center}
</div>
