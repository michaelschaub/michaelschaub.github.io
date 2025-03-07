---
layout: publications
title: Publications
permalink: /Publications/
#mathjax: true comment in to enable math
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

Finished publications and public preprints are listed below. 
Click on \[Abstract] to obtain more information. 
Bibliographical information is available by clicking on \[BibTeX].

You can search in the abstracts using the quicksearch box above.
The official publication pages can be accessed through the link given \[DOI]. 
If a preprint version is available it can be found by clicking on \[URL].
Links to press coverage are listed under \[Comment].

A list of my publications is also available on [Google Scholar](https://scholar.google.com/citations?hl=en&user=FCGOxvYAAAAJ&view_op=list_works){:target="_blank"}. 

------------------

<!--BEGIN PUBLICATIOON INSERT HERE-->
<table id="qs_table" border="1">
<tbody>
<tr id="Savostianov2025" class="entry">
	<td> [1] Savostianov A, Schaub MT, Guglielmi N and Tudisco F (2025), <i>"Efficient Sparsification of Simplicial Complexes via Local Densities of States"</i>. February, 2025.
	<p class="infolinks">[<a href="javascript:toggleInfo('Savostianov2025','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Savostianov2025','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2502.07558" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Savostianov2025" class="abstract noshow">
	<td><b>Abstract</b>: Simplicial complexes (SCs), a generalization of graph models for relational data that account for higher-order relations between data items, have become a popular abstraction for analyzing complex data using tools from topological data analysis or topological signal processing. However, the analysis of many real-world datasets leads to dense SCs with a large number of higher-order interactions. Unfortunately, analyzing such large SCs often has a prohibitive cost in terms of computation time and memory consumption. The sparsification of such complexes, i.e., the approximation of an original SC with a sparser simplicial complex with only a log-linear number of high-order simplices while maintaining a spectrum close to the original SC, is of broad interest.<br>In this work, we develop a novel method for a probabilistic sparsifaction of SCs. At its core lies the efficient computation of sparsifying sampling probability through local densities of states as functional descriptors of the spectral information. To avoid pathological structures in the spectrum of the corresponding Hodge Laplacian operators, we suggest a "kernel-ignoring" decomposition for approximating the sampling probability; additionally, we exploit error estimates to show asymptotically prevailing algorithmic complexity of the developed method. The performance of the framework is demonstrated on the family of Vietoris--Rips filtered simplicial complexes.</td>
</tr>
<tr id="bib_Savostianov2025" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Savostianov2025,
  author = {Anton Savostianov and Michael T. Schaub and Nicola Guglielmi and Francesco Tudisco},
  title = {Efficient Sparsification of Simplicial Complexes via Local Densities of States},
  year = {2025},
  url = {https://arxiv.org/abs/2502.07558}
}
</pre></td>
</tr>
<tr id="Patel2025" class="entry">
	<td> [2] Patel D, Savostianov A and Schaub MT (2025), <i>"Convergence of gradient based training for linear Graph Neural Networks"</i>. January, 2025.
	<p class="infolinks">[<a href="javascript:toggleInfo('Patel2025','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Patel2025','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2501.14440" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Patel2025" class="abstract noshow">
	<td><b>Abstract</b>: Graph Neural Networks (GNNs) are powerful tools for addressing learning problems on graph structures, with a wide range of applications in molecular biology and social networks. However, the theoretical foundations underlying their empirical performance are not well understood. In this article, we examine the convergence of gradient dynamics in the training of linear GNNs. Specifically, we prove that the gradient flow training of a linear GNN with mean squared loss converges to the global minimum at an exponential rate. The convergence rate depends explicitly on the initial weights and the graph shift operator, which we validate on synthetic datasets from well-known graph models and real-world datasets. Furthermore, we discuss the gradient flow that minimizes the total weights at the global minimum. In addition to the gradient flow, we study the convergence of linear GNNs under gradient descent training, an iterative scheme viewed as a discretization of gradient flow.</td>
</tr>
<tr id="bib_Patel2025" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Patel2025,
  author = {Dhiraj Patel and Anton Savostianov and Michael T. Schaub},
  title = {Convergence of gradient based training for linear Graph Neural Networks},
  year = {2025},
  url = {https://arxiv.org/abs/2501.14440}
}
</pre></td>
</tr>
<tr id="Epping2024" class="entry">
    <td> [3] Epping, B.; René, A.; Helias, M. &amp; Schaub, M.T. (2024), <i>"Graph Neural Networks Do Not Always Oversmooth"</i>, In Advances in Neural Information Processing Systems., December, 2024.  Vol. 37, pp. 48164-48188. Curran Associates, Inc..
        <p class="infolinks">[<a href="javascript:toggleInfo('Epping2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Epping2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.48550/arXiv.2406.02269" target="_blank">DOI</a>] [<a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/5623c35f3ab5e2c72aeb3abce27dc28f-Paper-Conference.pdf" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Epping2024" class="abstract noshow">
    <td><b>Abstract</b>: Graph neural networks (GNNs) have emerged as powerful tools for processing relational data in applications. However, GNNs suffer from the problem of oversmoothing, the property that the features of all nodes exponentially converge to the same vector over layers, prohibiting the design of deep GNNs. In this work we study oversmoothing in graph convolutional networks (GCNs) by using their Gaussian process (GP) equivalence in the limit of infinitely many hidden features. By generalizing methods from conventional deep neural networks (DNNs), we can describe the distribution of features at the output layer of deep GCNs in terms of a GP: as expected, we find that typical parameter choices from the literature lead to oversmoothing. The theory, however, allows us to identify a new, nonoversmoothing phase: if the initial weights of the network have sufficiently large variance, GCNs do not oversmooth, and node features remain informative even at large depth. We demonstrate the validity of this prediction in finite-size GCNs by training a linear classifier on their output. Moreover, using the linearization of the GCN GP, we generalize the concept of propagation depth of information from DNNs to GCNs. This propagation depth diverges at the transition between the oversmoothing and non-oversmoothing phase. We test the predictions of our approach and find good agreement with finite-size GCNs. Initializing GCNs near the transition to the non-oversmoothing phase, we obtain networks which are both deep and expressive.</td>
</tr>
<tr id="bib_Epping2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Epping2024,
    author = {Bastian Epping and Alexandre René and Moritz Helias and Michael T. Schaub},
           editor = {A. Globerson and L. Mackey and D. Belgrave and A. Fan and U. Paquet and J. Tomczak and C. Zhang},
           title = {Graph Neural Networks Do Not Always Oversmooth},
           booktitle = {Advances in Neural Information Processing Systems},
           publisher = {Curran Associates, Inc.},
           year = {2024},
           volume = {37},
           pages = {48164--48188},
           url = {https://proceedings.neurips.cc/paper_files/paper/2024/file/5623c35f3ab5e2c72aeb3abce27dc28f-Paper-Conference.pdf},
           doi = {10.48550/arXiv.2406.02269}
}
    </pre></td>
</tr>
<tr id="Heck2024" class="entry">
	<td> [4] Heck L, Gelbrecht M, Schaub MT and Boers N (2024), <i>"Improving the Noise Estimation of Latent Neural Stochastic Differential Equations"</i>. December, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Heck2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Heck2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.48550/arXiv.2412.17499" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Heck2024" class="abstract noshow">
	<td><b>Abstract</b>: Latent neural stochastic differential equations (SDEs) have recently emerged as a promising approach for learning generative models from stochastic time series data. However, they systematically underestimate the noise level inherent in such data, limiting their ability to capture stochastic dynamics accurately. We investigate this underestimation in detail and propose a straightforward solution: by including an explicit additional noise regularization in the loss function, we are able to learn a model that accurately captures the diffusion component of the data. We demonstrate our results on a conceptual model system that highlights the improved latent neural SDE's capability to model stochastic bistable dynamics.</td>
</tr>
<tr id="bib_Heck2024" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Heck2024,
  author = {Heck, Linus and Gelbrecht, Maximilian and Schaub, Michael T and Boers, Niklas},
  title = {Improving the Noise Estimation of Latent Neural Stochastic Differential Equations},
  year = {2024},
  url = {https://doi.org/10.48550/arXiv.2412.17499}
}
</pre></td>
</tr>
<tr id="Witthaut2024" class="entry">
	<td> [5] Witthaut D, Kistinger D, Titz M, B&ouml;ttcher P, Schaub M and Venghaus S (2024), <i>"Revealing drivers of green technology adoption through explainable AI"</i>. December, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Witthaut2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Witthaut2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.21203/rs.3.rs-5367657/v1" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Witthaut2024" class="abstract noshow">
	<td><b>Abstract</b>: Effective governance of energy system transformations away from fossil resources requires a quantitative understanding of the diffusion of green technologies and its key influencing factors. In this article, we propose a novel machine learning approach to diffusion research focusing on actual decisions and spatial aspects complementing research on intentions and temporal dynamics. We develop machine learning models that predict regional differences in the accumulated peak power of household-scale photovoltaic systems and the share of battery electric vehicles from a large set of demographic, geographic, political, and socio-economic features. Tools from explainable artificial intelligence enable a consistent identification of the key influencing factors and quantify their impact. Focusing on data from German municipal associations, we identify common themes and differences in the diffusion of green technologies.</td>
</tr>
<tr id="bib_Witthaut2024" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Witthaut2024,
  author = {Witthaut, Dirk and Kistinger, Dorothea and Titz, Maurizio and B&ouml;ttcher, Philipp and Schaub, Michael and Venghaus, Sandra},
  title = {Revealing drivers of green technology adoption through explainable AI},
  year = {2024},
  url = {https://doi.org/10.21203/rs.3.rs-5367657/v1}
}
</pre></td>
</tr>
<tr id="Grande2024b" class="entry">
    <td> [6] Grande, V.P.; Hoppe, J.; Frantzen, F. &amp; Schaub, M.T. (2024), <i>"Topological Trajectory Classification and Landmark Inference on Simplicial Complexes"</i>, In 58th Annual Asilomar Conference on Signals, Systems, and Computers., December, 2024. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Grande2024b','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Grande2024b','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.48550/arXiv.2412.03145" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Grande2024b" class="abstract noshow">
    <td><b>Abstract</b>: We consider the problem of classifying trajectories on a discrete or discretised 2-dimensional manifold modelled by a simplicial complex. Previous works have proposed to project the trajectories into the harmonic eigenspace of the Hodge Laplacian, and then cluster the resulting embeddings. However, if the considered space has vanishing homology (i.e., no "holes"), then the harmonic space of the 1-Hodge Laplacian is trivial and thus the approach fails. Here we propose to view this issue akin to a sensor placement problem and present an algorithm that aims to learn "optimal holes" to distinguish a set of given trajectory classes. Specifically, given a set of labelled trajectories, which we interpret as edge-flows on the underlying simplicial complex, we search for 2-simplices whose deletion results in an optimal separation of the trajectory labels according to the corresponding spectral embedding of the trajectories into the harmonic space. Finally, we generalise this approach to the unsupervised setting.</td>
</tr>
<tr id="bib_Grande2024b" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Grande2024b,
    author = {Grande, Vincent P and Hoppe, Josef and Frantzen, Florian and Schaub, Michael T},
           title = {Topological Trajectory Classification and Landmark Inference on Simplicial Complexes},
           booktitle = {58th Annual Asilomar Conference on Signals, Systems, and Computers},
           year = {2024},
           url = {https://doi.org/10.48550/arXiv.2412.03145}
}
    </pre></td>
</tr>
<tr id="Hajij2024" class="entry">
    <td> [7] Hajij, M.; Papillon, M.; Frantzen, F.; Agerberg, J.; AlJabea, I.; Ballester, R.; Battiloro, C.; Bernárdez, G.; Birdal, T.; Brent, A.; Chin, P.; Escalera, S.; Fiorellino, S.; Gardaa, O.H.; Gopalakrishnan, G.; Govil, D.; Hoppe, J.; Karri, M.R.; Khouja, J.; Lecha, M.; Livesay, N.; Meißner, J.; Mukherjee, S.; Nikitin, A.; Papamarkou, T.; Prílepok, J.; Ramamurthy, K.N.; Rosen, P.; Guzmán-Sáenz, A.; Salatiello, A.; Samaga, S.N.; Scardapane, S.; Schaub, M.T.; Scofano, L.; Spinelli, I.; Telyatnikov, L.; Truong, Q.; Walters, R.; Yang, M.; Zaghen, O.; Zamzmi, G.; Zia, A. &amp; Miolane, N. (2024), <i>"TopoX: A Suite of Python Packages for Machine Learning on Topological Domains"</i>, Journal of Machine Learning Research., December, 2024.  Vol. 25(374), pp. 1-8.
        <p class="infolinks">[<a href="javascript:toggleInfo('Hajij2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Hajij2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.48550/arXiv.2402.02441" target="_blank">DOI</a>] [<a href="http://jmlr.org/papers/v25/24-0110.html" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Hajij2024" class="abstract noshow">
    <td><b>Abstract</b>: We introduce TopoX, a Python software suite that provides reliable and user-friendly building blocks for computing and machine learning on topological domains that extend graphs: hypergraphs, simplicial, cellular, path and combinatorial complexes. TopoX consists of three packages: TopoNetX facilitates constructing and computing on these domains, including working with nodes, edges and higher-order cells; TopoEmbedX provides methods to embed topological domains into vector spaces, akin to popular graph-based embedding algorithms such as node2vec; TopoModelx is built on top of PyTorch and offers a comprehensive toolbox of higher-order message passing functions for neural networks on topological domains. The extensively documented and unit-tested source code of TopoX is available under MIT license at this https URL.</td>
</tr>
<tr id="bib_Hajij2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Hajij2024,
    author = {Mustafa Hajij and Mathilde Papillon and Florian Frantzen and Jens Agerberg and Ibrahem AlJabea and Ruben Ballester and Claudio Battiloro and Guillermo Bernárdez and Tolga Birdal and Aiden Brent and Peter Chin and Sergio Escalera and Simone Fiorellino and Odin Hoff Gardaa and Gurusankar Gopalakrishnan and Devendra Govil and Josef Hoppe and Maneel Reddy Karri and Jude Khouja and Manuel Lecha and Neal Livesay and Jan Meißner and Soham Mukherjee and Alexander Nikitin and Theodore Papamarkou and Jaro Prílepok and Karthikeyan Natesan Ramamurthy and Paul Rosen and Aldo Guzmán-Sáenz and Alessandro Salatiello and Shreyas N. Samaga and Simone Scardapane and Michael T. Schaub and Luca Scofano and Indro Spinelli and Lev Telyatnikov and Quang Truong and Robin Walters and Maosheng Yang and Olga Zaghen and Ghada Zamzmi and Ali Zia and Nina Miolane},
           title = {TopoX: A Suite of Python Packages for Machine Learning on Topological Domains},
           journal = {Journal of Machine Learning Research},
           year = {2024},
           volume = {25},
           number = {374},
           pages = {1--8},
           url = {http://jmlr.org/papers/v25/24-0110.html},
           doi = {10.48550/arXiv.2402.02441}
}
    </pre></td>
</tr>
<tr id="Stamm2024" class="entry">
    <td> [8] Stamm, F.I. &amp; Schaub, M.T. (2024), <i>"Faster optimal univariate microgaggregation"</i>, Transactions on Machine Learning Research., October, 2024. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Stamm2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Stamm2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.48550/arXiv.2401.02381" target="_blank">DOI</a>] [<a href="https://openreview.net/forum?id=s5lEUtyVly" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Stamm2024" class="abstract noshow">
    <td><b>Abstract</b>: Microaggregation is a method to coarsen a dataset, by optimally clustering data points in groups of at least k points, thereby providing a k-anonymity type disclosure guarantee for each point in the dataset. Previous algorithms for univariate microaggregation had a O(kn) time complexity. By rephrasing microaggregation as an instance of the concave least weight subsequence problem, in this work we provide improved algorithms that provide an optimal univariate microaggregation on sorted data in O(n) time and space. We further show that our algorithms work not only for sum of squares cost functions, as typically considered, but seamlessly extend to many other cost functions used for univariate microaggregation tasks. In experiments we show that the presented algorithms lead to real world performance improvements.</td>
</tr>
<tr id="bib_Stamm2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Stamm2024,
    author = {Stamm, Felix I and Schaub, Michael T},
           title = {Faster optimal univariate microgaggregation},
           journal = {Transactions on Machine Learning Research},
           year = {2024},
           url = {https://openreview.net/forum?id=s5lEUtyVly},
           doi = {10.48550/arXiv.2401.02381}
}
    </pre></td>
</tr>
<tr id="Peel2024" class="entry">
    <td> [9] Peel, L. &amp; Schaub, M.T. (2024), <i>"Detectability of hierarchical communities in networks"</i>, Phys. Rev. E., September, 2024.  Vol. 110, pp. 034306. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Peel2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Peel2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevE.110.034306" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2009.07525" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Peel2024" class="abstract noshow">
    <td><b>Abstract</b>: We study the problem of recovering a planted hierarchy of partitions in a network. The detectability of a single planted partition has previously been analyzed in detail and a phase transition has been identified below which the partition cannot be detected. Here we show that, in the hierarchical setting, there exist additional phases in which the presence of multiple consistent partitions can either help or hinder detection. Accordingly, the detectability limit for nonhierarchical partitions typically provides insufficient information about the detectability of the complete hierarchical structure, as we highlight with several constructive examples.</td>
</tr>
<tr id="bib_Peel2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Peel2024,
    author = {Peel, Leto and Schaub, Michael T.},
           title = {Detectability of hierarchical communities in networks},
           journal = {Phys. Rev. E},
           publisher = {American Physical Society},
           year = {2024},
           volume = {110},
           pages = {034306},
           url = {https://arxiv.org/abs/2009.07525},
           doi = {10.1103/PhysRevE.110.034306}
}
    </pre></td>
</tr>
<tr id="Papamarkou2024" class="entry">
    <td> [10] Papamarkou, T.; Birdal, T.; Bronstein, M.; Carlsson, G.; Curry, J.; Gao, Y.; Hajij, M.; Kwitt, R.; Liò, P.; Lorenzo, P.D.; Maroulas, V.; Miolane, N.; Nasrin, F.; Ramamurthy, K.N.; Rieck, B.; Scardapane, S.; Schaub, M.T.; Veličković, P.; Wang, B.; Wang, Y.; Wei, G.-W. &amp; Zamzmi, G. (2024), <i>"Position: Topological Deep Learning is the New Frontier for Relational Learning"</i>, In Proceedings of the 41st International Conference on Machine Learning (ICML 2024)., July, 2024. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Papamarkou2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Papamarkou2024','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2402.08871" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Papamarkou2024" class="abstract noshow">
    <td><b>Abstract</b>: Topological deep learning (TDL) is a rapidly evolving field that uses topological features to understand and design deep learning models. This paper posits that TDL is the new frontier for relational learning. TDL may complement graph representation learning and geometric deep learning by incorporating topological concepts, and can thus provide a natural choice for various machine learning settings. To this end, this paper discusses open problems in TDL, ranging from practical benefits to theoretical foundations. For each problem, it outlines potential solutions and future research opportunities. At the same time, this paper serves as an invitation to the scientific community to actively participate in TDL research to unlock the potential of this emerging field.</td>
</tr>
<tr id="bib_Papamarkou2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Papamarkou2024,
    author = {Theodore Papamarkou and Tolga Birdal and Michael Bronstein and Gunnar Carlsson and Justin Curry and Yue Gao and Mustafa Hajij and Roland Kwitt and Pietro Liò and Paolo Di Lorenzo and Vasileios Maroulas and Nina Miolane and Farzana Nasrin and Karthikeyan Natesan Ramamurthy and Bastian Rieck and Simone Scardapane and Michael T. Schaub and Petar Veličković and Bei Wang and Yusu Wang and Guo-Wei Wei and Ghada Zamzmi},
           title = {Position: Topological Deep Learning is the New Frontier for Relational Learning},
           booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML 2024)},
           year = {2024},
           url = {https://arxiv.org/abs/2402.08871}
}
    </pre></td>
</tr>
<tr id="Arnaudon2024" class="entry">
    <td> [11] Arnaudon, A.; Schindler, D.J.; Peach, R.L.; Gosztolai, A.; Hodges, M.; Schaub, M.T. &amp; Barahona, M. (2024), <i>"Algorithm 1044: PyGenStability: Multiscale community detection with generalized Markov Stability"</i>, ACM Transactions on Mathematical Software. New York, NY, USA, June, 2024.  Association for Computing Machinery.
        <p class="infolinks">[<a href="javascript:toggleInfo('Arnaudon2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Arnaudon2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1145/3651225" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2303.05385" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Arnaudon2024" class="abstract noshow">
    <td><b>Abstract</b>: We present PyGenStability, a general-use Python software package that provides a suite of analysis and visualisation tools for unsupervised multiscale community detection in graphs. PyGenStability finds optimized partitions of a graph at different levels of resolution by maximizing the generalized Markov Stability quality function with the Louvain or Leiden algorithms. The package includes automatic detection of robust graph partitions and allows the flexibility to choose quality functions for weighted undirected, directed and signed graphs, and to include other user-defined quality functions. The code and documentation are hosted on GitHub under a GNU General Public License at this https URL.</td>
</tr>
<tr id="bib_Arnaudon2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Arnaudon2024,
    author = {Alexis Arnaudon and Dominik J Schindler and Robert L Peach and Adam Gosztolai and Maxwell Hodges and Michael T Schaub and Mauricio Barahona},
           title = {Algorithm 1044: PyGenStability: Multiscale community detection with generalized Markov Stability},
           journal = {ACM Transactions on Mathematical Software},
           publisher = {Association for Computing Machinery},
           year = {2024},
           url = {https://arxiv.org/abs/2303.05385},
           doi = {10.1145/3651225}
}
    </pre></td>
</tr>
<tr id="Grande2024a" class="entry">
	<td> [12] Grande VP and Schaub MT (2024), <i>"Node-Level Topological Representation Learning on Point Clouds"</i>. June, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Grande2024a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Grande2024a','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2406.02300" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Grande2024a" class="abstract noshow">
	<td><b>Abstract</b>: Topological Data Analysis (TDA) allows us to extract powerful topological and higher-order information on the global shape of a data set or point cloud. Tools like Persistent Homology or the Euler Transform give a single complex description of the global structure of the point cloud. However, common machine learning applications like classification require point-level information and features to be available. In this paper, we bridge this gap and propose a novel method to extract node-level topological features from complex point clouds using discrete variants of concepts from algebraic topology and differential geometry. We verify the effectiveness of these topological point features (TOPF) on both synthetic and real-world data and study their robustness under noise.</td>
</tr>
<tr id="bib_Grande2024a" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Grande2024a,
  author = {Vincent P. Grande and Michael T. Schaub},
  title = {Node-Level Topological Representation Learning on Point Clouds},
  year = {2024},
  url = {https://arxiv.org/abs/2406.02300}
}
</pre></td>
</tr>
<tr id="Grande2023a" class="entry">
    <td> [13] Grande, V.P. &amp; Schaub, M.T. (2024), <i>"Non-Isotropic Persistent Homology: Leveraging the Metric Dependency of PH"</i>, In Proceedings of the Second Learning on Graphs Conference., June, 2024.  Vol. 231, pp. 17:1-17:19. PMLR.
        <p class="infolinks">[<a href="javascript:toggleInfo('Grande2023a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Grande2023a','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2310.16437" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Grande2023a" class="abstract noshow">
    <td><b>Abstract</b>: Persistent Homology is a widely used topological data analysis tool that creates a concise description of the topological properties of a point cloud based on a specified filtration. Most filtrations used for persistent homology depend (implicitly) on a chosen metric, which is typically agnostically chosen as the standard Euclidean metric on textdollar &reals;&circ;ntextdollar . Recent work has tried to uncover the true metric on the point cloud using distance-to-measure functions, in order to obtain more meaningful persistent homology results. Here we propose an alternative look at this problem: we posit that information on the point cloud is lost when restricting persistent homology to a single (correct) distance function. Instead, we show how by varying the distance function on the underlying space and analysing the corresponding shifts in the persistence diagrams, we can extract additional topological and geometrical information. Finally, we numerically show that non-isotropic persistent homology can extract information on orientation, orientational variance, and scaling of randomly generated point clouds with good accuracy and conduct some experiments on real-world data.</td>
</tr>
<tr id="bib_Grande2023a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Grande2023a,
    author = {Grande, Vincent Peter and Schaub, Michael T},
           editor = {Villar, Soledad and Chamberlain, Benjamin},
           title = {Non-Isotropic Persistent Homology: Leveraging the Metric Dependency of PH},
           booktitle = {Proceedings of the Second Learning on Graphs Conference},
           publisher = {PMLR},
           year = {2024},
           volume = {231},
           pages = {17:1--17:19},
           url = {https://arxiv.org/abs/2310.16437}
}
    </pre></td>
</tr>
<tr id="Hoppe2024" class="entry">
	<td> [14] Hoppe J and Schaub MT (2024), <i>"Random Abstract Cell Complexes"</i>. June, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Hoppe2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Hoppe2024','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2406.01999" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Hoppe2024" class="abstract noshow">
	<td><b>Abstract</b>: We define a model for random (abstract) cell complexes (CCs), similiar to the well-known Erdős-Rényi model for graphs and its extensions for simplicial complexes. To build a random cell complex, we first draw from an Erdős-Rényi graph, and consecutively augment the graph with cells for each dimension with a specified probability. As the number of possible cells increases combinatorially -- e.g., 2-cells can be represented as cycles, or permutations -- we derive an approximate sampling algorithm for this model limited to two-dimensional abstract cell complexes. Since there is a large variance in the number of simple cycles on graphs drawn from the same configuration of ER, we also provide an efficient method to approximate that number, which is of independent interest. Moreover, it enables us to specify the expected number of 2-cells of each boundary length we want to sample. We provide some initial analysis into the properties of random CCs drawn from this model. We further showcase practical applications for our random CCs as null models, and in the context of (random) liftings of graphs to cell complexes. Both the sampling and cycle count estimation algorithms are available in the package `py-raccoon` on the Python Packaging Index.</td>
</tr>
<tr id="bib_Hoppe2024" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Hoppe2024,
  author = {Josef Hoppe and Michael T. Schaub},
  title = {Random Abstract Cell Complexes},
  year = {2024},
  note = {arxiv preprint},
  url = {https://arxiv.org/abs/2406.01999}
}
</pre></td>
</tr>
<tr id="Hoppe2023" class="entry">
    <td> [15] Hoppe, J. &amp; Schaub, M.T. (2024), <i>"Representing Edge Flows on Graphs via Sparse Cell Complexes"</i>, In Proceedings of the Second Learning on Graphs Conference., June, 2024.  Vol. 231, pp. 1:1-1:22. PMLR.
        <p class="infolinks">[<a href="javascript:toggleInfo('Hoppe2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Hoppe2023','comment')">Comment</a>]  [<a href="javascript:toggleInfo('Hoppe2023','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2309.01632" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Hoppe2023" class="abstract noshow">
    <td><b>Abstract</b>: Obtaining sparse, interpretable representations of observable data is crucial in many machine learning and signal processing tasks. For data representing flows along the edges of a graph, an intuitively interpretable way to obtain such representations is to lift the graph structure to a simplicial complex: The eigenvectors of the associated Hodge-Laplacian, respectively the incidence matrices of the corresponding simplicial complex then induce a Hodge decomposition, which can be used to represent the observed data in terms of gradient, curl, and harmonic flows. In this paper, we generalize this approach to cellular complexes and introduce the flow representation learning problem, i.e., the problem of augmenting the observed graph by a set of cells, such that the eigenvectors of the associated Hodge Laplacian provide a sparse, interpretable representation of the observed edge flows on the graph. We show that this problem is NP-hard and introduce an efficient approximation algorithm for its solution. Experiments on real-world and synthetic data demonstrate that our algorithm outperforms state-of-the-art methods with respect to approximation error, while being computationally efficient.</td>
</tr>
<tr id="rev_Hoppe2023" class="comment noshow">
    <td><b>Comment</b>: Best paper Award</td>
</tr>
<tr id="bib_Hoppe2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Hoppe2023,
    author = {Hoppe, Josef and Schaub, Michael T},
           editor = {Villar, Soledad and Chamberlain, Benjamin},
           title = {Representing Edge Flows on Graphs via Sparse Cell Complexes},
           booktitle = {Proceedings of the Second Learning on Graphs Conference},
           publisher = {PMLR},
           year = {2024},
           volume = {231},
           pages = {1:1--1:22},
           url = {https://arxiv.org/abs/2309.01632}
}
    </pre></td>
</tr>
<tr id="Scholkemper2024a" class="entry">
	<td> [16] Scholkemper M, Wu X, Jadbabaie A and Schaub M (2024), <i>"Residual Connections and Normalization Can Provably Prevent Oversmoothing in GNNs"</i>. June, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Scholkemper2024a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Scholkemper2024a','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2406.02997" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Scholkemper2024a" class="abstract noshow">
	<td><b>Abstract</b>: Residual connections and normalization layers have become standard design choices for graph neural networks (GNNs), and were proposed as solutions to the mitigate the oversmoothing problem in GNNs. However, how exactly these methods help alleviate the oversmoothing problem from a theoretical perspective is not well understood. In this work, we provide a formal and precise characterization of (linearized) GNNs with residual connections and normalization layers. We establish that (a) for residual connections, the incorporation of the initial features at each layer can prevent the signal from becoming too smooth, and determines the subspace of possible node representations; (b) batch normalization prevents a complete collapse of the output embedding space to a one-dimensional subspace through the individual rescaling of each column of the feature matrix. This results in the convergence of node representations to the top-k eigenspace of the message-passing operator; (c) moreover, we show that the centering step of a normalization layer -- which can be understood as a projection -- alters the graph signal in message-passing in such a way that relevant information can become harder to extract. We therefore introduce a novel, principled normalization layer called GraphNormv2 in which the centering step is learned such that it does not distort the original graph signal in an undesirable way. Experimental results confirm the effectiveness of our method.</td>
</tr>
<tr id="bib_Scholkemper2024a" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Scholkemper2024a,
  author = {Michael Scholkemper and Xinyi Wu and Ali Jadbabaie and Michael Schaub},
  title = {Residual Connections and Normalization Can Provably Prevent Oversmoothing in GNNs},
  year = {2024},
  url = {https://arxiv.org/abs/2406.02997}
}
</pre></td>
</tr>
<tr id="Telyatnikov2024" class="entry">
	<td> [17] Telyatnikov L, Bernardez G, Montagna M, Vasylenko P, Zamzmi G, Hajij M, Schaub MT, Miolane N, Scardapane S and Papamarkou T (2024), <i>"TopoBenchmarkX: A Framework for Benchmarking Topological Deep Learning"</i>. June, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Telyatnikov2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Telyatnikov2024','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2406.06642" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Telyatnikov2024" class="abstract noshow">
	<td><b>Abstract</b>: This work introduces TopoBenchmarkX, a modular open-source library designed to standardize benchmarking and accelerate research in Topological Deep Learning (TDL). TopoBenchmarkX maps the TDL pipeline into a sequence of independent and modular components for data loading and processing, as well as model training, optimization, and evaluation. This modular organization provides flexibility for modifications and facilitates the adaptation and optimization of various TDL pipelines. A key feature of TopoBenchmarkX is that it allows for the transformation and lifting between topological domains. This enables, for example, to obtain richer data representations and more fine-grained analyses by mapping the topology and features of a graph to higher-order topological domains such as simplicial and cell complexes. The range of applicability of TopoBenchmarkX is demonstrated by benchmarking several TDL architectures for various tasks and datasets.</td>
</tr>
<tr id="bib_Telyatnikov2024" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Telyatnikov2024,
  author = {Lev Telyatnikov and Guillermo Bernardez and Marco Montagna and Pavlo Vasylenko and Ghada Zamzmi and Mustafa Hajij and Michael T Schaub and Nina Miolane and Simone Scardapane and Theodore Papamarkou},
  title = {TopoBenchmarkX: A Framework for Benchmarking Topological Deep Learning},
  year = {2024},
  note = {arxiv preprint},
  url = {https://arxiv.org/abs/2406.06642}
}
</pre></td>
</tr>
<tr id="Neuhaeuser2024" class="entry">
    <td> [18] Neuhäuser, L.; Scholkemper, M.; Tudisco, F. &amp; Schaub, M.T. (2024), <i>"Learning the effective order of a hypergraph dynamical system"</i>, Science Advances., May, 2024.  Vol. 10(19), pp. eadh4053.
        <p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1126/sciadv.adh4053" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2306.01813" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Neuhaeuser2024" class="abstract noshow">
    <td><b>Abstract</b>: Dynamical systems on hypergraphs can display a rich set of behaviors not observable for systems with pairwise interactions. Given a distributed dynamical system with a putative hypergraph structure, an interesting question is thus how much of this hypergraph structure is actually necessary to faithfully replicate the observed dynamical behavior. To answer this question, we propose a method to determine the minimum order of a hypergraph necessary to approximate the corresponding dynamics accurately. Specifically, we develop a mathematical framework that allows us to determine this order when the type of dynamics is known. We use these ideas in conjunction with a hypergraph neural network to directly learn the dynamics itself and the resulting order of the hypergraph from both synthetic and real datasets consisting of observed system trajectories.</td>
</tr>
<tr id="bib_Neuhaeuser2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Neuhaeuser2024,
    author = {Leonie Neuhäuser and Michael Scholkemper and Francesco Tudisco and Michael T. Schaub},
           title = {Learning the effective order of a hypergraph dynamical system},
           journal = {Science Advances},
           year = {2024},
           volume = {10},
           number = {19},
           pages = {eadh4053},
           url = {https://arxiv.org/abs/2306.01813},
           doi = {10.1126/sciadv.adh4053}
}
    </pre></td>
</tr>
<tr id="Frantzen2024" class="entry">
    <td> [19] Frantzen, F. &amp; Schaub, M.T. (2024), <i>"Learning From Simplicial Data Based on Random Walks and 1D Convolutions"</i>, In International Conference on Learning Representations., April, 2024. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Frantzen2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Frantzen2024','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2404.03434" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Frantzen2024" class="abstract noshow">
    <td><b>Abstract</b>: Triggered by limitations of graph-based deep learning methods in terms of computational expressivity and model flexibility, recent years have seen a surge of interest in computational models that operate on higher-order topological domains such as hypergraphs and simplicial complexes. While the increased expressivity of these models can indeed lead to a better classification performance and a more faithful representation of the underlying system, the computational cost of these higher-order models can increase dramatically. To this end, we here explore a simplicial complex neural network learning architecture based on random walks and fast 1D convolutions (SCRaWl), in which we can adjust the increase in computational cost by varying the length and number of random walks considered while accounting for higher-order relationships. Importantly, due to the random walk-based design, the expressivity of the proposed architecture is provably incomparable to that of existing message-passing simplicial neural networks. We empirically evaluate SCRaWl on real-world datasets and show that it outperforms other simplicial neural networks.</td>
</tr>
<tr id="bib_Frantzen2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Frantzen2024,
    author = {Florian Frantzen and Michael T. Schaub},
           title = {Learning From Simplicial Data Based on Random Walks and 1D Convolutions},
           booktitle = {International Conference on Learning Representations},
           year = {2024},
           url = {https://arxiv.org/abs/2404.03434}
}
    </pre></td>
</tr>
<tr id="Scholkemper2024" class="entry">
    <td> [20] Scholkemper, M.; K&uuml;hn, D.; Nabbefeld, G.; Musall, S.; Kampa, B. &amp; Schaub, M.T. (2024), <i>"A Wasserstein Graph Distance Based on Distributions of Probabilistic Node Embeddings"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)., March, 2024. , pp. 9751-9755.
        <p class="infolinks">[<a href="javascript:toggleInfo('Scholkemper2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Scholkemper2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP48485.2024.10447922" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2401.03913" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Scholkemper2024" class="abstract noshow">
    <td><b>Abstract</b>: Distance measures between graphs are important primitives for a variety of learning tasks. In this work, we describe an unsupervised, optimal transport based approach to define a distance between graphs. Our idea is to derive representations of graphs as Gaussian mixture models, fitted to distributions of sampled node embeddings over the same space. The Wasserstein distance between these Gaussian mixture distributions then yields an interpretable and easily computable distance measure, which can further be tailored for the comparison at hand by choosing appropriate embeddings. We propose two embeddings for this framework and show that under certain assumptions about the shape of the resulting Gaussian mixture components, further computational improvements of this Wasserstein distance can be achieved. An empirical validation of our findings on synthetic data and real-world Functional Brain Connectivity networks shows promising performance compared to existing embedding methods.</td>
</tr>
<tr id="bib_Scholkemper2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Scholkemper2024,
    author = {Scholkemper, Michael and K&uuml;hn, Damin and Nabbefeld, Gerion and Musall, Simon and Kampa, Bj&ouml;rn and Schaub, Michael T},
           title = {A Wasserstein Graph Distance Based on Distributions of Probabilistic Node Embeddings},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)},
           year = {2024},
           pages = {9751-9755},
           url = {https://arxiv.org/abs/2401.03913},
           doi = {10.1109/ICASSP48485.2024.10447922}
}
    </pre></td>
</tr>
<tr id="Grande2024" class="entry">
    <td> [21] Grande, V. &amp; Schaub, M.T. (2024), <i>"Disentangling the Spectral Properties of the Hodge Laplacian: Not All Small Eigenvalues Are Equal"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)., March, 2024. , pp. 9896-9900.
        <p class="infolinks">[<a href="javascript:toggleInfo('Grande2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Grande2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP48485.2024.10446051" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2311.14427" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Grande2024" class="abstract noshow">
    <td><b>Abstract</b>: The rich spectral information of the graph Laplacian has been instrumental in graph theory, machine learning, and graph signal processing for applications such as graph classification, clustering, or eigenmode analysis. Recently, the Hodge Laplacian has come into focus as a generalisation of the ordinary Laplacian for higher-order graph models such as simplicial and cellular complexes. Akin to the traditional analysis of graph Laplacians, many authors analyse the smallest eigenvalues of the Hodge Laplacian, which are connected to important topological properties such as homology. However, small eigenvalues of the Hodge Laplacian can carry different information depending on whether they are related to curl or gradient eigenmodes, and thus may not be comparable. We therefore introduce the notion of persistent eigenvector similarity and provide a method to track individual harmonic, curl, and gradient eigenvectors/-values through the so-called persistence filtration, leveraging the full information contained in the Hodge-Laplacian spectrum across all possible scales of a point cloud. Finally, we use our insights (a) to introduce a novel form of topological spectral clustering and (b) to classify edges and higher-order simplices based on their relationship to the smallest harmonic, curl, and gradient eigenvectors.</td>
</tr>
<tr id="bib_Grande2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Grande2024,
    author = {Grande, Vincent and Schaub, Michael T.},
           title = {Disentangling the Spectral Properties of the Hodge Laplacian: Not All Small Eigenvalues Are Equal},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)},
           year = {2024},
           pages = {9896-9900},
           url = {https://arxiv.org/abs/2311.14427},
           doi = {10.1109/ICASSP48485.2024.10446051}
}
    </pre></td>
</tr>
<tr id="Fanuel2024" class="entry">
	<td> [22] Fanuel M, Aspeel A, Schaub MT and Delvenne J-C (2024), <i>"Ellipsoidal embeddings of graphs"</i>. March, 2024.
	<p class="infolinks">[<a href="javascript:toggleInfo('Fanuel2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Fanuel2024','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2403.15023" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Fanuel2024" class="abstract noshow">
	<td><b>Abstract</b>: Due to their flexibility to represent almost any kind of relational data, graph-based models have enjoyed a tremendous success over the past decades. While graphs are inherently only combinatorial objects, however, many prominent analysis tools are based on the algebraic representation of graphs via matrices such as the graph Laplacian, or on associated graph embeddings. Such embeddings associate to each node a set of coordinates in a vector space, a representation which can then be employed for learning tasks such as the classification or alignment of the nodes of the graph. As the geometric picture provided by embedding methods enables the use of a multitude of methods developed for vector space data, embeddings have thus gained interest both from a theoretical as well as a practical perspective. Inspired by trace-optimization problems, often encountered in the analysis of graph-based data, here we present a method to derive ellipsoidal embeddings of the nodes of a graph, in which each node is assigned a set of coordinates on the surface of a hyperellipsoid. Our method may be seen as an alternative to popular spectral embedding techniques, to which it shares certain similarities we discuss. To illustrate the utility of the embedding we conduct a case study in which we analyse synthetic and real world networks with modular structure, and compare the results obtained with known methods in the literature.</td>
</tr>
<tr id="bib_Fanuel2024" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Fanuel2024,
  author = {Michaël Fanuel and Antoine Aspeel and Michael T. Schaub and Jean-Charles Delvenne},
  title = {Ellipsoidal embeddings of graphs},
  year = {2024},
  note = {accepted for publication at SIAM Journal on Applied Mathematics},
  url = {https://arxiv.org/abs/2403.15023}
}
</pre></td>
</tr>
<tr id="Nagai2024" class="entry">
    <td> [23] Nagai, J.S.; Costa, I.G. &amp; Schaub, M.T. (2024), <i>"Optimal transport distances for directed, weighted graphs: a case study with cell-cell communication networks"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)., March, 2024. , pp. 9856-9860.
        <p class="infolinks">[<a href="javascript:toggleInfo('Nagai2024','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Nagai2024','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP48485.2024.10446503" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2309.07030" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Nagai2024" class="abstract noshow">
    <td><b>Abstract</b>: Comparing graphs by means of optimal transport has recently gained significant attention, as the distances induced by optimal transport provide both a principled metric between graphs as well as an interpretable description of the associated changes between graphs in terms of a transport plan. As the lack of symmetry introduces challenges in the typically considered formulations, optimal transport distances for graphs have mostly been developed for undirected graphs. Here, we propose two distance measures to compare directed graphs based on variants of optimal transport: (i) an earth movers distance (Wasserstein) and (ii) a Gromov-Wasserstein (GW) distance. We evaluate these two distances and discuss their relative performance for both simulated graph data and real-world directed cell-cell communication graphs, inferred from single-cell RNA-seq data.</td>
</tr>
<tr id="bib_Nagai2024" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Nagai2024,
    author = {James S. Nagai and Ivan G. Costa and Michael T. Schaub},
           title = {Optimal transport distances for directed, weighted graphs: a case study with cell-cell communication networks},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2024)},
           year = {2024},
           pages = {9856-9860},
           url = {https://arxiv.org/abs/2309.07030},
           doi = {10.1109/ICASSP48485.2024.10446503}
}
    </pre></td>
</tr>
<tr id="Scholkemper2023" class="entry">
    <td> [24] Scholkemper, M. &amp; Schaub, M.T. (2023), <i>"An Optimization-based Approach To Node Role Discovery in Networks: Approximating Equitable Partitions"</i>, In Advances in Neural Information Processing Systems (NeurIPS 2023)., December, 2023.  Vol. 36, pp. 71358-71374.
        <p class="infolinks">[<a href="javascript:toggleInfo('Scholkemper2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Scholkemper2023','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2305.19087" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Scholkemper2023" class="abstract noshow">
    <td><b>Abstract</b>: Similar to community detection, partitioning the nodes of a network according to their structural roles aims to identify fundamental building blocks of a network. The found partitions can be used, e.g., to simplify descriptions of the network connectivity, to derive reduced order models for dynamical processes unfolding on processes, or as ingredients for various graph mining tasks. In this work, we offer a fresh look on the problem of role extraction and its differences to community detection and present a definition of node roles related to graph-isomorphism tests, the Weisfeiler-Leman algorithm and equitable partitions. We study two associated optimization problems (cost functions) grounded in ideas from graph isomorphism testing, and present theoretical guarantees associated to the solutions of these problems. Finally, we validate our approach via a novel "role-infused partition benchmark", a network model from which we can sample networks in which nodes are endowed with different roles in a stochastic way.</td>
</tr>
<tr id="bib_Scholkemper2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Scholkemper2023,
    author = {Michael Scholkemper and Michael T. Schaub},
           title = {An Optimization-based Approach To Node Role Discovery in Networks: Approximating Equitable Partitions},
           booktitle = {Advances in Neural Information Processing Systems (NeurIPS 2023)},
           year = {2023},
           volume = {36},
           pages = {71358--71374},
           url = {https://arxiv.org/abs/2305.19087}
}
    </pre></td>
</tr>
<tr id="Hajij2023a" class="entry">
    <td> [25] Hajij, M.; Zamzmi, G.; Papamarkou, T.; Guzmán-Sáenz, A.; Birdal, T. &amp; Schaub, M.T. (2023), <i>"Combinatorial Complexes: Bridging the Gap Between Cell Complexes and Hypergraphs"</i>, In 57th Asilomar Conference on Signals, Systems, and Computers., December, 2023. , pp. 799-803.
        <p class="infolinks">[<a href="javascript:toggleInfo('Hajij2023a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Hajij2023a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/IEEECONF59524.2023.10477018" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2312.09504" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Hajij2023a" class="abstract noshow">
    <td><b>Abstract</b>: Graph-based signal processing techniques have become essential for handling data in non-Euclidean spaces. However, there is a growing awareness that these graph models might need to be expanded into `higher-order' domains to effectively represent the complex relations found in high-dimensional data. Such higher-order domains are typically modeled either as hypergraphs, or as simplicial, cubical or other cell complexes. In this context, cell complexes are often seen as a subclass of hypergraphs with additional algebraic structure that can be exploited, e.g., to develop a spectral theory. In this article, we promote an alternative perspective. We argue that hypergraphs and cell complexes emphasize <em>different</em> types of relations, which may have different utility depending on the application context. Whereas hypergraphs are effective in modeling set-type, multi-body relations between entities, cell complexes provide an effective means to model hierarchical, interior-to-boundary type relations. We discuss the relative advantages of these two choices and elaborate on the previously introduced concept of a combinatorial complex that enables co-existing set-type and hierarchical relations. Finally, we provide a brief numerical experiment to demonstrate that this modelling flexibility can be advantageous in learning tasks.</td>
</tr>
<tr id="bib_Hajij2023a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Hajij2023a,
    author = {Mustafa Hajij and Ghada Zamzmi and Theodore Papamarkou and Aldo Guzmán-Sáenz and Tolga Birdal and Michael T. Schaub},
           title = {Combinatorial Complexes: Bridging the Gap Between Cell Complexes and Hypergraphs},
           booktitle = {57th Asilomar Conference on Signals, Systems, and Computers},
           year = {2023},
           pages = {799-803},
           url = {https://arxiv.org/abs/2312.09504},
           doi = {10.1109/IEEECONF59524.2023.10477018}
}
    </pre></td>
</tr>
<tr id="Loveland2023" class="entry">
    <td> [26] Loveland, D.; Zhu, J.; Heimann, M.; Fish, B.; Schaub, M.T. &amp; Koutra, D. (2023), <i>"On Performance Discrepancies Across Local Homophily Levels in Graph Neural Networks"</i>, In Proceedings of the Second Learning on Graphs Conference., November, 2023.  Vol. 231, pp. 6:1-6:30. PMLR.
        <p class="infolinks">[<a href="javascript:toggleInfo('Loveland2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Loveland2023','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2306.05557v3" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Loveland2023" class="abstract noshow">
    <td><b>Abstract</b>: Graph Neural Network (GNN) research has highlighted a relationship between high homophily (i.e., the tendency of nodes of the same class to connect) and strong predictive performance in node classification. However, recent work has found the relationship to be more nuanced, demonstrating that simple GNNs can learn in certain heterophilous settings. To resolve these conflicting findings and align closer to real-world datasets, we go beyond the assumption of a global graph homophily level and study the performance of GNNs when the local homophily level of a node deviates from the global homophily level. Through theoretical and empirical analysis, we systematically demonstrate how shifts in local homophily can introduce performance degradation, leading to performance discrepancies across local homophily levels. We ground the practical implications of this work through granular analysis on five real-world datasets with varying global homophily levels, demonstrating that (a) GNNs can fail to generalize to test nodes that deviate from the global homophily of a graph, and (b) high local homophily does not necessarily confer high performance for a node. We further show that GNNs designed for globally heterophilous graphs can alleviate performance discrepancy by improving performance across local homophily levels, offering a new perspective on how these GNNs achieve stronger global performance.</td>
</tr>
<tr id="bib_Loveland2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Loveland2023,
    author = {Loveland, Donald and Zhu, Jiong and Heimann, Mark and Fish, Benjamin and Schaub, Michael T and Koutra, Danai},
           editor = {Villar, Soledad and Chamberlain, Benjamin},
           title = {On Performance Discrepancies Across Local Homophily Levels in Graph Neural Networks},
           booktitle = {Proceedings of the Second Learning on Graphs Conference},
           publisher = {PMLR},
           year = {2023},
           volume = {231},
           pages = {6:1--6:30},
           url = {https://arxiv.org/abs/2306.05557v3}
}
    </pre></td>
</tr>
<tr id="Calmon2023" class="entry">
    <td> [27] Calmon, L.; Schaub, M.T. &amp; Bianconi, G. (2023), <i>"Dirac signal processing of higher-order topological signals"</i>, New Journal of Physics., September, 2023.  Vol. 25(9), pp. 093013.
        <p class="infolinks">[<a href="javascript:toggleInfo('Calmon2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Calmon2023','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1088/1367-2630/acf33c" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2301.10137" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Calmon2023" class="abstract noshow">
    <td><b>Abstract</b>: We consider topological signals corresponding to variables supported on nodes, links and triangles of higher-order networks and simplicial complexes. So far such signals are typically processed independently of each other, and algorithms that can enforce a consistent processing of topological signals across different levels are largely lacking. Here we propose Dirac signal processing, an adaptive, unsupervised signal processing algorithm that learns to jointly filter topological signals supported on nodes, links and (filled) triangles of simplicial complexes in a consistent way. The proposed Dirac signal processing algorithm is rooted in algebraic topology and formulated in terms of the discrete Dirac operator which can be interpreted as ``square root" of a higher-order (Hodge) Laplacian matrix acting on nodes, links and triangles of simplicial complexes. We test our algorithms on noisy synthetic data and noisy data of drifters in the ocean and find that the algorithm can learn to efficiently reconstruct the true signals outperforming algorithms based exclusively on the Hodge Laplacian.</td>
</tr>
<tr id="bib_Calmon2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Calmon2023,
    author = {Lucille Calmon and Michael T. Schaub and Ginestra Bianconi},
           title = {Dirac signal processing of higher-order topological signals},
           journal = {New Journal of Physics},
           year = {2023},
           volume = {25},
           number = {9},
           pages = {093013},
           url = {https://arxiv.org/abs/2301.10137},
           doi = {10.1088/1367-2630/acf33c}
}
    </pre></td>
</tr>
<tr id="Bick2023" class="entry">
    <td> [28] Bick, C.; Gross, E.; Harrington, H.A. &amp; Schaub, M.T. (2023), <i>"What are higher-order networks?"</i>, SIAM Review., August, 2023.  Vol. 65(3), pp. 686-731.
        <p class="infolinks">[<a href="javascript:toggleInfo('Bick2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Bick2023','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1137/21M1414024" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2104.11329" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Bick2023" class="abstract noshow">
    <td><b>Abstract</b>: Modeling complex systems and data using the language of graphs and networks has become an essential topic across a range of different disciplines. Arguably, this network-based perspective derives is success from the relative simplicity of graphs: A graph consists of nothing more than a set of vertices and a set of edges, describing relationships between pairs of such vertices. This simple combinatorial structure makes graphs interpretable and flexible modeling tools. The simplicity of graphs as system models, however, has been scrutinized in the literature recently. Specifically, it has been argued from a variety of different angles that there is a need for higher-order networks, which go beyond the paradigm of modeling pairwise relationships, as encapsulated by graphs. In this survey article we take stock of these recent developments. Our goals are to clarify (i) what higher-order networks are, (ii) why these are interesting objects of study, and (iii) how they can be used in applications.</td>
</tr>
<tr id="bib_Bick2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Bick2023,
    author = {Christian Bick and Elizabeth Gross and Heather A. Harrington and Michael T. Schaub},
           title = {What are higher-order networks?},
           journal = {SIAM Review},
           year = {2023},
           volume = {65},
           number = {3},
           pages = {686-731},
           url = {https://arxiv.org/abs/2104.11329},
           doi = {10.1137/21M1414024}
}
    </pre></td>
</tr>
<tr id="Grande2023" class="entry">
    <td> [29] Grande, V.P. &amp; Schaub, M.T. (2023), <i>"Topological Point Cloud Clustering"</i>, In Proceedings of the 40th International Conference on Machine Learning (ICML 2023)., July, 2023.  Vol. 202, pp. 11683-11697. PMLR.
        <p class="infolinks">[<a href="javascript:toggleInfo('Grande2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Grande2023','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2303.16716" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Grande2023" class="abstract noshow">
    <td><b>Abstract</b>: We present Topological Point Cloud Clustering (TPCC), a new method to cluster points in an arbitrary point cloud based on their contribution to global topological features. TPCC synthesizes desirable features from spectral clustering and topological data analysis and is based on considering the spectral properties of a simplicial complex associated to the considered point cloud. As it is based on considering sparse eigenvector computations, TPCC is similarly easy to interpret and implement as spectral clustering. However, by focusing not just on a single matrix associated to a graph created from the point cloud data, but on a whole set of Hodge-Laplacians associated to an appropriately constructed simplicial complex, we can leverage a far richer set of topological features to characterize the data points within the point cloud and benefit from the relative robustness of topological techniques against noise. We test the performance of TPCC on both synthetic and real-world data and compare it with classical spectral clustering.</td>
</tr>
<tr id="bib_Grande2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Grande2023,
    author = {Grande, Vincent Peter and Schaub, Michael T},
           editor = {Krause, Andreas and Brunskill, Emma and Cho, Kyunghyun and Engelhardt, Barbara and Sabato, Sivan and Scarlett, Jonathan},
           title = {Topological Point Cloud Clustering},
           booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML 2023)},
           publisher = {PMLR},
           year = {2023},
           volume = {202},
           pages = {11683--11697},
           url = {https://arxiv.org/abs/2303.16716}
}
    </pre></td>
</tr>
<tr id="Schaub2023" class="entry">
    <td> [30] Schaub, M.T.; Li, J. &amp; Peel, L. (2023), <i>"Hierarchical community structure in networks"</i>, Phys. Rev. E., May, 2023.  Vol. 107, pp. 054305. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2023','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevE.107.054305" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2009.07196" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2023" class="abstract noshow">
    <td><b>Abstract</b>: Modular and hierarchical structures are pervasive in real-world complex systems. A great deal of effort has gone into trying to detect and study these structures. Important theoretical advances in the detection of modular, or "community", structures have included identifying fundamental limits of detectability by formally defining community structure using probabilistic generative models. Detecting hierarchical community structure introduces additional challenges alongside those inherited from community detection. Here we present a theoretical study on hierarchical community structure in networks, which has thus far not received the same rigorous attention. We address the following questions: 1)&nbsp;How should we define a valid hierarchy of communities? 2)&nbsp;How should we determine if a hierarchical structure exists in a network? and 3)&nbsp;how can we detect hierarchical structure efficiently? We approach these questions by introducing a definition of hierarchy based on the concept of stochastic externally equitable partitions and their relation to probabilistic models, such as the popular stochastic block model. We enumerate the challenges involved in detecting hierarchies and, by studying the spectral properties of hierarchical structure, present an efficient and principled method for detecting them.</td>
</tr>
<tr id="bib_Schaub2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2023,
    author = {Schaub, Michael T. and Li, Jiaze and Peel, Leto},
           title = {Hierarchical community structure in networks},
           journal = {Phys. Rev. E},
           publisher = {American Physical Society},
           year = {2023},
           volume = {107},
           pages = {054305},
           url = {https://arxiv.org/abs/2009.07196},
           doi = {10.1103/PhysRevE.107.054305}
}
    </pre></td>
</tr>
<tr id="Neuhaeuser2022a" class="entry">
    <td> [31] Neuhäuser, L.; Karimi, F.; Bachmann, J.; Strohmaier, M. &amp; Schaub, M.T. (2023), <i>"Improving the visibility of minorities through network growth interventions"</i>, Communication Physics., May, 2023.  Vol. 6(108)
        <p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2022a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2022a','comment')">Comment</a>]  [<a href="javascript:toggleInfo('Neuhaeuser2022a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1038/s42005-023-01218-9" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2208.03263" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Neuhaeuser2022a" class="abstract noshow">
    <td><b>Abstract</b>: Improving the position of minorities in networks via interventions is a challenge of high theoretical and societal importance. In this work, we examine how different network growth interventions impact the position of minority nodes in degree rankings over time. We distinguish between two kinds of interventions: (i) group size interventions, such as introducing quotas, that regulate the ratio of incoming minority and majority nodes; and (ii) behavioural interventions, such as homophily, i.e. varying how groups interact and connect to each other. We find that even extreme group size interventions do not have a strong effect on the position of minorities in rankings if certain behavioural changes do not manifest at the same time. For example, minority representation in rankings is not increased by high quotas if the actors in the network do not adopt homophilic behaviour. As a result, a key finding of our research is that in order for the visibility of minorities to improve, group size and behavioural interventions need to be coordinated. Moreover, their potential benefit is highly dependent on pre-intervention conditions in social networks. In a real-world case study, we explore the effectiveness of interventions to reach gender parity in academia. Our work lays a theoretical and computational foundation for further studies aiming to explore the effectiveness of interventions in growing networks.</td>
</tr>
<tr id="rev_Neuhaeuser2022a" class="comment noshow">
    <td><b>Comment</b>: Highlighted as research highlight in editorial https://www.nature.com/articles/s42254-023-00627-7</td>
</tr>
<tr id="bib_Neuhaeuser2022a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Neuhaeuser2022a,
    author = {Leonie Neuhäuser and Fariba Karimi and Jan Bachmann and Markus Strohmaier and Michael T. Schaub},
           title = {Improving the visibility of minorities through network growth interventions},
           journal = {Communication Physics},
           year = {2023},
           volume = {6},
           number = {108},
           url = {https://arxiv.org/abs/2208.03263},
           doi = {10.1038/s42005-023-01218-9}
}
    </pre></td>
</tr>
<tr id="Stamm2023" class="entry">
    <td> [32] Stamm, F.I.; Scholkemper, M.; Strohmaier, M. &amp; Schaub, M.T. (2023), <i>"Neighborhood Structure Configuration Models"</i>, In The Web Conference. New York, NY, USA, April, 2023. , pp. 210–220. Association for Computing Machinery.
        <p class="infolinks">[<a href="javascript:toggleInfo('Stamm2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Stamm2023','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1145/3543507.3583266" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2210.06843" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Stamm2023" class="abstract noshow">
    <td><b>Abstract</b>: We develop a new method to efficiently sample synthetic networks that preserve the d-hop neighborhood structure of a given network for any given d. The proposed algorithm trades off the diversity in network samples against the depth of the neighborhood structure that is preserved. Our key innovation is to employ a colored Configuration Model with colors derived from iterations of the so-called Color Refinement algorithm. We prove that with increasing iterations the preserved structural information increases: the generated synthetic networks and the original network become more and more similar, and are eventually indistinguishable in terms of centrality measures such as PageRank, HITS, Katz centrality and eigenvector centrality. Our work enables to efficiently generate samples with a precisely controlled similarity to the original network, especially for large networks.</td>
</tr>
<tr id="bib_Stamm2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Stamm2023,
    author = {Felix I. Stamm and Michael Scholkemper and Markus Strohmaier and Michael T. Schaub},
           title = {Neighborhood Structure Configuration Models},
           booktitle = {The Web Conference},
           publisher = {Association for Computing Machinery},
           year = {2023},
           pages = {210–220},
           url = {https://arxiv.org/abs/2210.06843},
           doi = {10.1145/3543507.3583266}
}
    </pre></td>
</tr>
<tr id="Hajij2023" class="entry">
	<td> [33] Hajij M, Zamzmi G, Papamarkou T, Miolane N, Guzm&aacute;n-S&aacute;enz A, Ramamurthy KN, Birdal T, Dey TK, Mukherjee S, Samaga SN and others (2023), <i>"Topological Deep Learning: Going Beyond Graph Data"</i>. April, 2023.
	<p class="infolinks">[<a href="javascript:toggleInfo('Hajij2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Hajij2023','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2206.00606" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Hajij2023" class="abstract noshow">
	<td><b>Abstract</b>: Topological deep learning is a rapidly growing field that pertains to the development of deep learning models for data supported on topological domains such as simplicial complexes, cell complexes, and hypergraphs, which generalize many domains encountered in scientific computations. In this paper, we present a unifying deep learning framework built upon a richer data structure that includes widely adopted topological domains.<br>Specifically, we first introduce combinatorial complexes, a novel type of topological domain. Combinatorial complexes can be seen as generalizations of graphs that maintain certain desirable properties. Similar to hypergraphs, combinatorial complexes impose no constraints on the set of relations. In addition, combinatorial complexes permit the construction of hierarchical higher-order relations, analogous to those found in simplicial and cell complexes. Thus, combinatorial complexes generalize and combine useful traits of both hypergraphs and cell complexes, which have emerged as two promising abstractions that facilitate the generalization of graph neural networks to topological spaces.<br>Second, building upon combinatorial complexes and their rich combinatorial and algebraic structure, we develop a general class of message-passing combinatorial complex neural networks (CCNNs), focusing primarily on attention-based CCNNs. We characterize permutation and orientation equivariances of CCNNs, and discuss pooling and unpooling operations within CCNNs in detail.<br>Third, we evaluate the performance of CCNNs on tasks related to mesh shape analysis and graph learning. Our experiments demonstrate that CCNNs have competitive performance as compared to state-of-the-art deep learning models specifically tailored to the same tasks. Our findings demonstrate the advantages of incorporating higher-order relations into deep learning models in different applications.</td>
</tr>
<tr id="bib_Hajij2023" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Hajij2023,
  author = {Hajij, Mustafa and Zamzmi, Ghada and Papamarkou, Theodore and Miolane, Nina and Guzm&aacute;n-S&aacute;enz, Aldo and Ramamurthy, Karthikeyan Natesan and Birdal, Tolga and Dey, Tamal K and Mukherjee, Soham and Samaga, Shreyas N and others},
  title = {Topological Deep Learning: Going Beyond Graph Data},
  year = {2023},
  url = {https://arxiv.org/abs/2206.00606}
}
</pre></td>
</tr>
<tr id="Roddenberry2023" class="entry">
    <td> [34] Roddenberry, T.M.; Grande, V.P.; Frantzen, F.; Schaub, M.T. &amp; Segarra, S. (2023), <i>"Signal Processing on Product Spaces"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)., March, 2023. , pp. 1-5. IEEE.
        <p class="infolinks">[<a href="javascript:toggleInfo('Roddenberry2023','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Roddenberry2023','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP49357.2023.10095735" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2303.10495" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Roddenberry2023" class="abstract noshow">
    <td><b>Abstract</b>: We establish a framework for signal processing on product spaces of simplicial and cellular complexes. For simplicity, we focus on the product of two complexes representing time and space, although our results generalize naturally to products of simplicial complexes of arbitrary dimension. Our framework leverages the structure of the eigenmodes of the Hodge Laplacian of the product space to jointly filter along time and space. To this end, we provide a decomposition theorem of the Hodge Laplacian of the product space, which highlights how the product structure induces a decomposition of each eigenmode into a spatial and temporal component. Finally, we apply our method to real world data, specifically for interpolating trajectories of buoys in the ocean from a limited set of observed trajectories.</td>
</tr>
<tr id="bib_Roddenberry2023" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Roddenberry2023,
    author = {T. Mitchell Roddenberry and Vincent P. Grande and Florian Frantzen and Michael T. Schaub and Santiago Segarra},
           title = {Signal Processing on Product Spaces},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
           publisher = {IEEE},
           year = {2023},
           pages = {1-5},
           url = {https://arxiv.org/abs/2303.10495},
           doi = {10.1109/ICASSP49357.2023.10095735}
}
    </pre></td>
</tr>
<tr id="Klimm2022" class="entry">
    <td> [35] Klimm, F.; Jones, N.S. &amp; Schaub, M.T. (2022), <i>"Modularity Maximization for Graphons"</i>, SIAM Journal on Applied Mathematics., December, 2022.  Vol. 82(6), pp. 1930-1952. SIAM.
        <p class="infolinks">[<a href="javascript:toggleInfo('Klimm2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Klimm2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1137/22M1492003" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2101.00503" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Klimm2022" class="abstract noshow">
    <td><b>Abstract</b>: Networks are a widely-used tool to investigate the large-scale connectivity structure in complex systems and graphons have been proposed as an infinite size limit of dense networks. The detection of communities or other meso-scale structures is a prominent topic in network science as it allows the identification of functional building blocks in complex systems. When such building blocks may be present in graphons is an open question. In this paper, we define a graphon-modularity and demonstrate that it can be maximised to detect communities in graphons. We then investigate specific synthetic graphons and show that they may show a wide range of different community structures. We also reformulate the graphon-modularity maximisation as a continuous optimisation problem and so prove the optimal community structure or lack thereof for some graphons, something that is usually not possible for networks. Furthermore, we demonstrate that estimating a graphon from network data as an intermediate step can improve the detection of communities, in comparison with exclusively maximising the modularity of the network. While the choice of graphon-estimator may strongly influence the accord between the community structure of a network and its estimated graphon, we find that there is a substantial overlap if an appropriate estimator is used. Our study demonstrates that community detection for graphons is possible and may serve as a privacy-preserving way to cluster network data.</td>
</tr>
<tr id="bib_Klimm2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Klimm2022,
    author = {Florian Klimm and Nick S. Jones and Michael T. Schaub},
           title = {Modularity Maximization for Graphons},
           journal = {SIAM Journal on Applied Mathematics},
           publisher = {SIAM},
           year = {2022},
           volume = {82},
           number = {6},
           pages = {1930--1952},
           url = {https://arxiv.org/abs/2101.00503},
           doi = {10.1137/22M1492003}
}
    </pre></td>
</tr>
<tr id="Calmon2022" class="entry">
    <td> [36] Calmon, L.; Schaub, M.T. &amp; Bianconi, G. (2022), <i>"Higher-order signal processing with the Dirac operator"</i>, In Asilomar Conference on Signals, Systems, and Computers., November, 2022. , pp. 925-929.
        <p class="infolinks">[<a href="javascript:toggleInfo('Calmon2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Calmon2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/IEEECONF56349.2022.10052062" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2212.10196" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Calmon2022" class="abstract noshow">
    <td><b>Abstract</b>: The processing of signals on simplicial and cellular complexes defined by nodes, edges, and higher-order cells has recently emerged as a principled extension of graph signal processing for signals supported on more general topological spaces. However, most works so far have considered signal processing problems for signals associated to only a single type of cell such as the processing of node signals, or edge signals, by considering an appropriately defined shift operator, like the graph Laplacian or the Hodge Laplacian. Here we introduce the Dirac operator as a novel kind of shift operator for signal processing on complexes. We discuss how the Dirac operator has close relations but is distinct from the Hodge-Laplacian and examine its spectral properties. Importantly, the Dirac operator couples signals defined on cells of neighboring dimensions in a principled fashion. We demonstrate how this enables us, e.g., to leverage node signals for the processing of edge flows.</td>
</tr>
<tr id="bib_Calmon2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Calmon2022,
    author = {Lucille Calmon and Michael T. Schaub and Ginestra Bianconi},
           title = {Higher-order signal processing with the Dirac operator},
           booktitle = {Asilomar Conference on Signals, Systems, and Computers},
           year = {2022},
           pages = {925-929},
           url = {https://arxiv.org/abs/2212.10196},
           doi = {10.1109/IEEECONF56349.2022.10052062}
}
    </pre></td>
</tr>
<tr id="Yang2022" class="entry">
    <td> [37] Yang, M.; Isufi, E.; Schaub, M.T. &amp; Leus, G. (2022), <i>"Simplicial Convolutional Filters"</i>, IEEE Transactions on Signal Processing., September, 2022. , pp. 1-16.
        <p class="infolinks">[<a href="javascript:toggleInfo('Yang2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Yang2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/TSP.2022.3207045" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2201.11720" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Yang2022" class="abstract noshow">
    <td><b>Abstract</b>: We study linear filters for processing signals supported on abstract topological spaces modeled as simplicial complexes, which may be interpreted as generalizations of graphs that account for nodes, edges, triangular faces etc. To process such signals, we develop simplicial convolutional filters defined as matrix polynomials of the lower and upper Hodge Laplacians. First, we study the properties of these filters and show that they are linear and shift-invariant, as well as permutation and orientation equivariant. These filters can also be implemented in a distributed fashion with a low computational complexity, as they involve only (multiple rounds of) simplicial shifting between upper and lower adjacent simplices. Second, focusing on edge-flows, we study the frequency responses of these filters and examine how we can use the Hodge-decomposition to delineate gradient, curl and harmonic frequencies. We discuss how these frequencies correspond to the lower- and the upper-adjacent couplings and the kernel of the Hodge Laplacian, respectively, and can be tuned independently by our filter designs. Third, we study different procedures for designing simplicial convolutional filters and discuss their relative advantages. Finally, we corroborate our simplicial filters in several applications: to extract different frequency components of a simplicial signal, to denoise edge flows, and to analyze financial markets and traffic networks.</td>
</tr>
<tr id="bib_Yang2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Yang2022,
    author = {Maosheng Yang and Elvin Isufi and Michael T. Schaub and Geert Leus},
           title = {Simplicial Convolutional Filters},
           journal = {IEEE Transactions on Signal Processing},
           year = {2022},
           pages = {1-16},
           url = {https://arxiv.org/abs/2201.11720},
           doi = {10.1109/TSP.2022.3207045}
}
    </pre></td>
</tr>
<tr id="Zhu2022" class="entry">
    <td> [38] Zhu, J.; Jin, J.; Schaub, M.T.; Koutra, D.; Zhu, J.; Jin, J.; Loveland, D.; Schaub, M.T. &amp; Koutra, D. (2022), <i>"Improving Robustness of Graph Neural Networks with Heterophily-Inspired Designs"</i>, In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. New York, NY, USA, August, 2022. , pp. 2637–2647. Association for Computing Machinery.
        <p class="infolinks">[<a href="javascript:toggleInfo('Zhu2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Zhu2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1145/3534678.3539418" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2106.07767" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Zhu2022" class="abstract noshow">
    <td><b>Abstract</b>: We bridge two research directions on graph neural networks (GNNs), by formalizing the relation between heterophily of node labels (i.e., connected nodes tend to have dissimilar labels) and the robustness of GNNs to adversarial attacks. Our theoretical and empirical analyses show that for homophilous graph data, impactful structural attacks always lead to reduced homophily, while for heterophilous graph data the change in the homophily level depends on the node degrees. These insights have practical implications for defending against attacks on real-world graphs: we deduce that separate aggregators for ego- and neighbor-embeddings, a design principle which has been identified to significantly improve prediction for heterophilous graph data, can also offer increased robustness to GNNs. Our comprehensive experiments show that GNNs merely adopting this design achieve improved empirical and certifiable robustness compared to the best-performing unvaccinated model.<br>               Additionally, combining this design with explicit defense mechanisms against adversarial attacks leads to an improved robustness with up to 18.33 percent performance increase under attacks compared to the best-performing vaccinated model.</td>
</tr>
<tr id="bib_Zhu2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Zhu2022,
    author = {Jiong Zhu and Junchen Jin and Michael T. Schaub and Danai Koutra and Zhu, Jiong and Jin, Junchen and Loveland, Donald and Schaub, Michael T. and Koutra, Danai},
           title = {Improving Robustness of Graph Neural Networks with Heterophily-Inspired Designs},
           booktitle = {Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
           publisher = {Association for Computing Machinery},
           year = {2022},
           pages = {2637–2647},
           url = {https://arxiv.org/abs/2106.07767},
           doi = {10.1145/3534678.3539418}
}
    </pre></td>
</tr>
<tr id="Loveland2022" class="entry">
    <td> [39] Loveland, D.; Zhu, J.; Heimann, M.; Fish, B.; Schaub, M.T. &amp; Koutra, D. (2022), <i>"On Graph Neural Network Fairness in the Presence of Heterophilous Neighborhoods"</i>, In Deep Learning on Graphs Workshop, 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2022)., August, 2022. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Loveland2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Loveland2022','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2207.04376" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Loveland2022" class="abstract noshow">
    <td><b>Abstract</b>: We study the task of node classification for graph neural networks (GNNs) and establish a connection between group fairness, as measured by statistical parity and equal opportunity, and local assortativity, i.e., the tendency of linked nodes to have similar attributes. Such assortativity is often induced by homophily, the tendency for nodes of similar properties to connect. Homophily can be common in social networks where systemic factors have forced individuals into communities which share a sensitive attribute. Through synthetic graphs, we study the interplay between locally occurring homophily and fair predictions, finding that not all node neighborhoods are equal in this respect -- neighborhoods dominated by one category of a sensitive attribute often struggle to obtain fair treatment, especially in the case of diverging local class and sensitive attribute homophily. After determining that a relationship between local homophily and fairness exists, we investigate if the issue of unfairness can be associated to the design of the applied GNN model. We show that by adopting heterophilous GNN designs capable of handling disassortative group labels, group fairness in locally heterophilous neighborhoods can be improved by up to 25 percent over homophilous designs in real and synthetic datasets.</td>
</tr>
<tr id="bib_Loveland2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Loveland2022,
    author = {Loveland, Donald and Zhu, Jiong and Heimann, Mark and Fish, Ben and Schaub, Michael T. and Koutra, Danai},
           title = {On Graph Neural Network Fairness in the Presence of Heterophilous Neighborhoods},
           booktitle = {Deep Learning on Graphs Workshop, 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2022)},
           year = {2022},
           url = {https://arxiv.org/abs/2207.04376}
}
    </pre></td>
</tr>
<tr id="Scholkemper2022" class="entry">
    <td> [40] Scholkemper, M. &amp; Schaub, M.T. (2022), <i>"Blind Extraction of Equitable Partitions from Graph Signals"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)., May, 2022. , pp. 5832-5836.
        <p class="infolinks">[<a href="javascript:toggleInfo('Scholkemper2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Scholkemper2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP43922.2022.9746676" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2203.05407" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Scholkemper2022" class="abstract noshow">
    <td><b>Abstract</b>: Finding equitable partitions is closely related to the extraction of graph symmetries and of interest in a variety of applications context such as node role detection, cluster synchronization, consensus dynamics, and network control problems. In this work we study a blind identification problem in which we aim to recover an equitable partition of a network without the knowledge of the network’s edges but based solely on the observations of the outputs of an unknown graph filter. Specifically, we consider two settings. First, we consider a scenario in which we can control the input to the graph filter and present a method to extract the partition inspired by the well known Weisfeiler-Lehman (color refinement) algorithm. Second, we generalize this idea to a setting where only observe the outputs to random, low-rank excitations of the graph filter, and present a simple spectral algorithm to extract the relevant equitable partitions. Finally, we establish theoretical bounds on the error that this spectral detection scheme incurs and perform numerical experiments that illustrate our theoretical results and compare both algorithms.</td>
</tr>
<tr id="bib_Scholkemper2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Scholkemper2022,
    author = {Scholkemper, Michael and Schaub, Michael T.},
           title = {Blind Extraction of Equitable Partitions from Graph Signals},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
           year = {2022},
           pages = {5832-5836},
           url = {https://arxiv.org/abs/2203.05407},
           doi = {10.1109/ICASSP43922.2022.9746676}
}
    </pre></td>
</tr>
<tr id="Roddenberry2022" class="entry">
    <td> [41] Roddenberry, T.M.; Frantzen, F.; Schaub, M.T. &amp; Segarra, S. (2022), <i>"Hodgelets: Localized Spectral Representations of Flows On Simplicial Complexes"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)., May, 2022. , pp. 5922-5926.
        <p class="infolinks">[<a href="javascript:toggleInfo('Roddenberry2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Roddenberry2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP43922.2022.9747203" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2109.08728" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Roddenberry2022" class="abstract noshow">
    <td><b>Abstract</b>: We develop wavelet representations for edge-flows on simplicial complexes, using ideas rooted in combinatorial Hodge theory and spectral graph wavelets. We first show that the Hodge Laplacian can be used in lieu of the graph Laplacian to construct a family of wavelets for higher-order signals on simplicial complexes. Then, we refine this idea to construct wavelets that respect the Hodge-Helmholtz decomposition. For these Hodgelets, familiar notions of curl-free and divergence-free flows from vector calculus are preserved. We characterize the representational quality of our Hodgelets for edge flows in terms of frame bounds and demonstrate the use of these spectral wavelets for sparse representation of edge flows on real and synthetic data.</td>
</tr>
<tr id="bib_Roddenberry2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Roddenberry2022,
    author = {Roddenberry, T. Mitchell and Frantzen, Florian and Schaub, Michael T. and Segarra, Santiago},
           title = {Hodgelets: Localized Spectral Representations of Flows On Simplicial Complexes},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
           year = {2022},
           pages = {5922-5926},
           url = {https://arxiv.org/abs/2109.08728},
           doi = {10.1109/ICASSP43922.2022.9747203}
}
    </pre></td>
</tr>
<tr id="Peisker2022" class="entry">
    <td> [42] Peisker, F.; Halder, M.; Nagai, J.; Ziegler, S.; Kaesler, N.; Hoeft, K.; Li, R.; Bindels, E.M.J.; Kuppe, C.; Moellmann, J. &amp; others (2022), <i>"Mapping the cardiac vascular niche in heart failure"</i>, Nature Communications., May, 2022.  Vol. 13(1), pp. 1-20. Nature Publishing Group.
        <p class="infolinks">[<a href="javascript:toggleInfo('Peisker2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Peisker2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1038/s41467-022-30682-0" target="_blank">DOI</a>]</p>
    </td>
</tr>
<tr id="abs_Peisker2022" class="abstract noshow">
    <td><b>Abstract</b>: The cardiac vascular and perivascular niche are of major importance in homeostasis and during disease, but we lack a complete understanding of its cellular heterogeneity and alteration in response to injury as a major driver of heart failure. Using combined genetic fate tracing with confocal imaging and single-cell RNA sequencing of this niche in homeostasis and during heart failure, we unravel cell type specific transcriptomic changes in fibroblast, endothelial, pericyte and vascular smooth muscle cell subtypes. We characterize a specific fibroblast subpopulation that exists during homeostasis, acquires Thbs4 expression and expands after injury driving cardiac fibrosis, and identify the transcription factor TEAD1 as a regulator of fibroblast activation. Endothelial cells display a proliferative response after injury, which is not sustained in later remodeling, together with transcriptional changes related to hypoxia, angiogenesis, and migration. Collectively, our data provides an extensive resource of transcriptomic changes in the vascular niche in hypertrophic cardiac remodeling.</td>
</tr>
<tr id="bib_Peisker2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Peisker2022,
    author = {Peisker, Fabian and Halder, Maurice and Nagai, James and Ziegler, Susanne and Kaesler, Nadine and Hoeft, Konrad and Li, Ronghui and Bindels, Eric MJ and Kuppe, Christoph and Moellmann, Julia and others},
           title = {Mapping the cardiac vascular niche in heart failure},
           journal = {Nature Communications},
           publisher = {Nature Publishing Group},
           year = {2022},
           volume = {13},
           number = {1},
           pages = {1--20},
           doi = {10.1038/s41467-022-30682-0}
}
    </pre></td>
</tr>
<tr id="Roddenberry2022a" class="entry">
    <td> [43] Roddenberry, T.M.; Schaub, M.T. &amp; Hajij, M. (2022), <i>"Signal Processing On Cell Complexes"</i>, In IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)., May, 2022. , pp. 8852-8856.
        <p class="infolinks">[<a href="javascript:toggleInfo('Roddenberry2022a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Roddenberry2022a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP43922.2022.9747233" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2110.05614" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Roddenberry2022a" class="abstract noshow">
    <td><b>Abstract</b>: The processing of signals supported on non-Euclidean domains has attracted large interest recently. Thus far, such non-Euclidean domains have been abstracted primarily as graphs with signals supported on the nodes, though the processing of signals on more general structures such as simplicial complexes has also been considered. In this paper, we give an introduction to signal processing on (abstract) regular cell complexes, which provide a unifying framework encompassing graphs, simplicial complexes, cubical complexes and various meshes as special cases. We discuss how appropriate Hodge Laplacians for these cell complexes can be derived. These Hodge Laplacians enable the construction of convolutional filters, which can be employed in linear filtering and non-linear filtering via neural networks defined on cell complexes.</td>
</tr>
<tr id="bib_Roddenberry2022a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Roddenberry2022a,
    author = {Roddenberry, T. Mitchell and Schaub, Michael T. and Hajij, Mustafa},
           title = {Signal Processing On Cell Complexes},
           booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
           year = {2022},
           pages = {8852-8856},
           url = {https://arxiv.org/abs/2110.05614},
           doi = {10.1109/ICASSP43922.2022.9747233}
}
    </pre></td>
</tr>
<tr id="Neuhaeuser2022" class="entry">
    <td> [44] Neuhäuser, L.; Lambiotte, R. &amp; Schaub, M.T. (2022), <i>"Consensus Dynamics and Opinion Formation on Hypergraphs"</i>, In Higher-Order Systems. Cham, April, 2022. , pp. 347-376. Springer International Publishing.
        <p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/978-3-030-91374-8_14" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2105.01369" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Neuhaeuser2022" class="abstract noshow">
    <td><b>Abstract</b>: In this chapter, we derive and analyse models for consensus dynamics on hypergraphs. As we discuss, unless there are nonlinear node interaction functions, it is always possible to rewrite the system in terms of a new network of effective pairwise node interactions, regardless of the initially underlying multi-way interaction structure. We thus focus on dynamics based on a certain class of non-linear interaction functions, which can model different sociological phenomena such as peer pressure and stubbornness. Unlike for linear consensus dynamics on networks, we show how our nonlinear model dynamics can cause shifts away from the average system state. We examine how these shifts are influenced by the distribution of the initial states, the underlying hypergraph structure and different forms of non-linear scaling of the node interaction function.</td>
</tr>
<tr id="bib_Neuhaeuser2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@incollection{Neuhaeuser2022,
    author = {Neuhäuser, Leonie and Lambiotte, Renaud and Schaub, Michael T.},
           editor = {Battiston, Federico and Petri, Giovanni},
           title = {Consensus Dynamics and Opinion Formation on Hypergraphs},
           booktitle = {Higher-Order Systems},
           publisher = {Springer International Publishing},
           year = {2022},
           pages = {347--376},
           url = {https://arxiv.org/abs/2105.01369},
           doi = {10.1007/978-3-030-91374-8_14}
}
    </pre></td>
</tr>
<tr id="Schaub2022" class="entry">
    <td> [45] Schaub, M.T.; Seby, J.-B.; Roddenberry, T.M.; Zhu, Y. &amp; Segarra, S. (2022), <i>"Signal processing on simplicial complexes"</i>, In Higher-Order Systems. Cham, April, 2022. , pp. 301-328. Springer International Publishing.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2022','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2022','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/978-3-030-91374-8_12" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2106.07471" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2022" class="abstract noshow">
    <td><b>Abstract</b>: Higher-order networks have so far been considered primarily in the context of studying the structure of complex systems, i.e., the higher-order or multi-way relations connecting the constituent entities. More recently, a number of studies have considered dynamical processes that explicitly account for such higher-order dependencies, e.g., in the context of epidemic spreading processes or opinion formation. In this chapter, we focus on a closely related, but distinct third perspective: how can we use higher-order relationships to process signals and data supported on higher-order network structures. In particular, we survey how ideas from signal processing of data supported on regular domains, such as time series or images, can be extended to graphs and simplicial complexes. We discuss Fourier analysis, signal denoising, signal interpolation, and nonlinear processing through neural networks based on simplicial complexes. Key to our developments is the Hodge Laplacian matrix, a multi-relational operator that leverages the special structure of simplicial complexes and generalizes desirable properties of the Laplacian matrix in graph signal processing.</td>
</tr>
<tr id="bib_Schaub2022" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@incollection{Schaub2022,
    author = {Michael T. Schaub and Jean-Baptiste Seby and T. Mitchell Roddenberry and Yu Zhu and Santiago Segarra},
           editor = {Battiston, Federico and Petri, Giovanni},
           title = {Signal processing on simplicial complexes},
           booktitle = {Higher-Order Systems},
           publisher = {Springer International Publishing},
           year = {2022},
           pages = {301--328},
           url = {https://arxiv.org/abs/2106.07471},
           doi = {10.1007/978-3-030-91374-8_12}
}
    </pre></td>
</tr>
<tr id="Neuhaeuser2021b" class="entry">
    <td> [46] Neuh&auml;user, L.; Lambiotte, R. &amp; Schaub, M.T. (2021), <i>"Consensus dynamics on temporal hypergraphs"</i>, Phys. Rev. E., December, 2021.  Vol. 104(6), pp. 064305. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2021b','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2021b','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevE.104.064305" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2109.04985" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Neuhaeuser2021b" class="abstract noshow">
    <td><b>Abstract</b>: We investigate consensus dynamics on temporal hypergraphs that encode network systems with time-dependent, multi-way interactions. We compare this dynamics with that on appropriate projections of this higher-order network representation that flatten the temporal, the multi-way component, or both. For linear average consensus dynamics, we find that the convergence of a randomly switching time-varying system with multi-way interactions is slower than the convergence of the corresponding system with pairwise interactions, which in turn exhibits a slower convergence rate than a consensus dynamics on the corresponding static network. We then consider a nonlinear consensus dynamics model in the temporal setting. Here we find that in addition to an effect on the convergence speed, the final consensus value of the temporal system can differ strongly from the consensus on the aggregated, static hypergraph. In particular we observe a first-mover advantage in the consensus formation process: If there is a local majority opinion in the hyperedges that are active early on, the majority in these first-mover groups has a higher influence on the final consensus value - a behaviour that is not observable in this form in projections of the temporal hypergraph.</td>
</tr>
<tr id="bib_Neuhaeuser2021b" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Neuhaeuser2021b,
    author = {Neuh&auml;user, Leonie and Lambiotte, Renaud and Schaub, Michael T.},
           title = {Consensus dynamics on temporal hypergraphs},
           journal = {Phys. Rev. E},
           publisher = {American Physical Society},
           year = {2021},
           volume = {104},
           number = {6},
           pages = {064305},
           url = {https://arxiv.org/abs/2109.04985},
           doi = {10.1103/PhysRevE.104.064305}
}
    </pre></td>
</tr>
<tr id="Lambiotte2021" class="entry">
    <td> [47] Lambiotte, R. &amp; Schaub, M.T. (2021), <i>"Modularity and Dynamics on Complex Networks"</i>, December, 2021.  Cambridge University Press.
        <p class="infolinks">[<a href="javascript:toggleInfo('Lambiotte2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Lambiotte2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1017/9781108774116" target="_blank">DOI</a>] [<a href="https://michaelschaub.github.io/ModularityAndDynamicsOnComplexNetworks.pdf" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Lambiotte2021" class="abstract noshow">
    <td><b>Abstract</b>: Complex networks are typically not homogeneous, as they tend to display an array of structures at different scales. A feature that has attracted a lot of research is their modular organisation, i.e., networks may often be considered as being composed of certain building blocks, or modules. In this Element, the authors discuss a number of ways in which this idea of modularity can be conceptualised, focusing specifically on the interplay between modular network structure and dynamics taking place on a network. They discuss, in particular, how modular structure and symmetries may impact on network dynamics and, vice versa, how observations of such dynamics may be used to infer the modular structure. They also revisit several other notions of modularity that have been proposed for complex networks and show how these can be related to and interpreted from the point of view of dynamical processes on networks.</td>
</tr>
<tr id="bib_Lambiotte2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@book{Lambiotte2021,
    author = {Lambiotte, Renaud and Schaub, Michael T.},
           title = {Modularity and Dynamics on Complex Networks},
           publisher = {Cambridge University Press},
           year = {2021},
           url = {https://michaelschaub.github.io/ModularityAndDynamicsOnComplexNetworks.pdf},
           doi = {10.1017/9781108774116}
}
    </pre></td>
</tr>
<tr id="Stamm2021" class="entry">
    <td> [48] Neuhäuser, L.; Stamm, F.I.; Lemmerich, F.; Schaub, M.T. &amp; Strohmaier, M. (2021), <i>"Simulating systematic edge uncertainty in attributed social networks and its effects on rankings of minority nodes"</i>, Applied Network Science., November, 2021.  Vol. 6(86)
        <p class="infolinks">[<a href="javascript:toggleInfo('Stamm2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Stamm2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/s41109-021-00425-z" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2010.11546" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Stamm2021" class="abstract noshow">
    <td><b>Abstract</b>: Network analysis provides powerful tools to learn about a variety of social systems. However, most analyses implicitly assume that the considered data is error-free and reliable. Especially if the network consists of multiple groups, this assumption conflicts with the range of systematic reporting biases, measurement errors and other inaccuracies that are well documented in our community. In this paper, we model how such systematic uncertainty on edges of an attributed network can impact network analysis, in particular the ranking of nodes. We discuss how erroneous edge observations can be driven by external node attributes and the relative edge positions in the network, thereby opening a path towards a systematic study of the effects of edge-uncertainty for various network analysis tasks. To show how conclusions drawn from network analyses can get distorted due to such inaccuracies, we focus on the effects of edge-uncertainty on minority group representations in degree-based rankings. For that purpose, we analyze synthetic and real networks with varying homophily and group sizes. We find that introducing edge uncertainty can significantly alter the relative density of networks and result both in a strongly increased or decreased ranking of the minority, depending on the type of edge error and homophily. Our model enables researchers to include systematic edge-uncertainty in their analyses and thereby better account for the role of minorities in social networks.</td>
</tr>
<tr id="bib_Stamm2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Stamm2021,
    author = {Leonie Neuhäuser and Felix I. Stamm and Florian Lemmerich and Michael T. Schaub and Markus Strohmaier},
           title = {Simulating systematic edge uncertainty in attributed social networks and its effects on rankings of minority nodes},
           journal = {Applied Network Science},
           year = {2021},
           volume = {6},
           number = {86},
           url = {https://arxiv.org/abs/2010.11546},
           doi = {10.1007/s41109-021-00425-z}
}
    </pre></td>
</tr>
<tr id="Frantzen2021" class="entry">
    <td> [49] Frantzen, F.; Seby, J.-B. &amp; Schaub, M.T. (2021), <i>"Outlier Detection for Trajectories via Flow-embeddings"</i>, In 2021 55th Asilomar Conference on Signals, Systems, and Computers., October, 2021. , pp. 1568-1572.
        <p class="infolinks">[<a href="javascript:toggleInfo('Frantzen2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Frantzen2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/IEEECONF53345.2021.9723128" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2111.13235" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Frantzen2021" class="abstract noshow">
    <td><b>Abstract</b>: We propose a method to detect outliers in empirically observed trajectories on a discrete or discretized manifold modeled by a simplicial complex. Our approach is similar to spectral embeddings such as diffusion-maps and Laplacian eigenmaps, that construct vertex embeddings from the eigenvectors of the graph Laplacian associated with low eigenvalues. Here we consider trajectories as edge-flow vectors defined on a simplicial complex, a higher-order generalization of graphs, and use the Hodge 1-Laplacian of the simplicial complex to derive embeddings of these edge-flows. By projecting trajectory vectors onto the eigenspace of the Hodge 1-Laplacian associated to small eigenvalues, we can characterize the behavior of the trajectories relative to the homology of the complex, which corresponds to holes in the underlying space. This enables us to classify trajectories based on simply interpretable, low-dimensional statistics. We show how this technique can single out trajectories that behave (topologically) different compared to typical trajectories, and illustrate the performance of our approach with both synthetic and empirical data.</td>
</tr>
<tr id="bib_Frantzen2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Frantzen2021,
    author = {Frantzen, Florian and Seby, Jean-Baptiste and Schaub, Michael T.},
           title = {Outlier Detection for Trajectories via Flow-embeddings},
           booktitle = {2021 55th Asilomar Conference on Signals, Systems, and Computers},
           year = {2021},
           pages = {1568-1572},
           url = {https://arxiv.org/abs/2111.13235},
           doi = {10.1109/IEEECONF53345.2021.9723128}
}
    </pre></td>
</tr>
<tr id="Neuhaeuser2021a" class="entry">
    <td> [50] Neuhäuser, L.; Schaub, M.T.; Mellor, A. &amp; Lambiotte, R. (2021), <i>"Opinion Dynamics with Multi-body Interactions"</i>, In Network Games, Control and Optimization. Cham, September, 2021. , pp. 261-271. Springer International Publishing.
        <p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2021a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2021a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/978-3-030-87473-5_23" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2004.00901" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Neuhaeuser2021a" class="abstract noshow">
    <td><b>Abstract</b>: We introduce and analyse a three-body consensus model (3CM) for non-linear consensus dynamics on hypergraphs. Our model incorporates reinforcing group effects, which can cause shifts in the average state of the system even in if the underlying graph is complete (corresponding to a mean-field interaction), a phenomena that may be interpreted as a type of peer pressure. We further demonstrate that for systems with two clustered groups, already a small asymmetry in our dynamics can lead to the opinion of one group becoming clearly dominant. We show that the nonlinearity in the model is the essential ingredient to make such group dynamics appear, and demonstrate how our system can otherwise be written as a linear, pairwise interaction system on a rescaled network.</td>
</tr>
<tr id="bib_Neuhaeuser2021a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Neuhaeuser2021a,
    author = {Neuhäuser, Leonie and Schaub, Michael T. and Mellor, Andrew and Lambiotte, Renaud},
           editor = {Lasaulce, Samson and Mertikopoulos, Panayotis and Orda, Ariel},
           title = {Opinion Dynamics with Multi-body Interactions},
           booktitle = {Network Games, Control and Optimization},
           publisher = {Springer International Publishing},
           year = {2021},
           pages = {261--271},
           url = {https://arxiv.org/abs/2004.00901},
           doi = {10.1007/978-3-030-87473-5_23}
}
    </pre></td>
</tr>
<tr id="Yang2021" class="entry">
    <td> [51] Yang, M.; Isufi, E.; Schaub, M.T. &amp; Leus, G. (2021), <i>"Finite Impulse Response Filters for Simplicial Complexes"</i>, In 29th European Signal Processing Conference (EUSIPCO)., August, 2021. , pp. 2005-2009.
        <p class="infolinks">[<a href="javascript:toggleInfo('Yang2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Yang2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.23919/EUSIPCO54536.2021.9616185" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2103.12587" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Yang2021" class="abstract noshow">
    <td><b>Abstract</b>: In this paper, we study linear filters to process signals defined on simplicial complexes, i.e., signals defined on nodes, edges, triangles, etc. of a simplicial complex, thereby generalizing filtering operations for graph signals. We propose a finite impulse response filter based on the Hodge Laplacian, and demonstrate how this filter can be designed to amplify or attenuate certain spectral components of simplicial signals. Specifically, we discuss how, unlike in the case of node signals, the Fourier transform in the context of edge signals can be understood in terms of two orthogonal subspaces corresponding to the gradient-flow signals and curl-flow signals arising from the Hodge decomposition. By assigning different filter coefficients to the associated terms of the Hodge Laplacian, we develop a subspace-varying filter which enables more nuanced control over these signal types. Numerical experiments are conducted to show the potential of simplicial filters for sub-component extraction, denoising and model approximation.</td>
</tr>
<tr id="bib_Yang2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Yang2021,
    author = {Maosheng Yang and Elvin Isufi and Michael T. Schaub and Geert Leus},
           title = {Finite Impulse Response Filters for Simplicial Complexes},
           booktitle = {29th European Signal Processing Conference (EUSIPCO)},
           year = {2021},
           pages = {2005-2009},
           url = {https://arxiv.org/abs/2103.12587},
           doi = {10.23919/EUSIPCO54536.2021.9616185}
}
    </pre></td>
</tr>
<tr id="Scholkemper2021" class="entry">
    <td> [52] Scholkemper, M. &amp; Schaub, M.T. (2021), <i>"Local, Global And Scale-Dependent Node Roles"</i>, In 2021 IEEE International Conference on Autonomous Systems (ICAS)., August, 2021. , pp. 1-5.
        <p class="infolinks">[<a href="javascript:toggleInfo('Scholkemper2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Scholkemper2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICAS49788.2021.9551110" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2105.12598" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Scholkemper2021" class="abstract noshow">
    <td><b>Abstract</b>: This paper re-examines the concept of node equivalences like structural equivalence or automorphic equivalence, which have originally emerged in social network analysis to characterize the role an actor plays within a social system, but have since then been of independent interest for graph-based learning tasks. Traditionally, such exact node equivalences have been defined either in terms of the one hop neighborhood of a node, or in terms of the global graph structure. Here we formalize exact node roles with a scale-parameter, describing up to what distance the ego network of a node should be considered when assigning node roles - motivated by the idea that there can be local roles of a node that should not be determined by nodes arbitrarily far away in the network. We present numerical experiments that show how already "shallow" roles of depth 3 or 4 carry sufficient information to perform node classification tasks with<br>           high accuracy. These findings corroborate the success of recent graph-learning approaches that compute approximate node roles in terms of embeddings, by nonlinearly aggregating node features in an (un)supervised manner over relatively small neighborhood sizes. Indeed, based on our ideas we can construct a shallow classifier achieving on par results with recent graph neural network architectures.</td>
</tr>
<tr id="bib_Scholkemper2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Scholkemper2021,
    author = {Scholkemper, Michael and Schaub, Michael T.},
           title = {Local, Global And Scale-Dependent Node Roles},
           booktitle = {2021 IEEE International Conference on Autonomous Systems (ICAS)},
           year = {2021},
           pages = {1-5},
           url = {https://arxiv.org/abs/2105.12598},
           doi = {10.1109/ICAS49788.2021.9551110}
}
    </pre></td>
</tr>
<tr id="Faccin2021" class="entry">
    <td> [53] Faccin, M.; Schaub, M.T. &amp; Delvenne, J.-C. (2021), <i>"State aggregations in Markov chains and block models of networks"</i>, Physical Review Letters., August, 2021.  Vol. 127(7), pp. 078301. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Faccin2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Faccin2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevLett.127.078301" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2005.00337" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Faccin2021" class="abstract noshow">
    <td><b>Abstract</b>: We consider state aggregation schemes for Markov chains from an information-theoretic perspective. Specifically, we consider aggregating the states of a Markov chain such that the mutual information of the aggregated states separated by T time steps is maximized. We show that for T = 1 this approach recovers the maximum-likelihood estimator of the degree-corrected stochastic block model as a particular case, thereby enabling us to explain certain features of the likelihood landscape of this popular generative network model from a dynamical lens. We further highlight how we can uncover coherent, long-range dynamical modules for which considering a time-scale T >> 1 is essential, using synthetic flows and real-world ocean currents, where we are able to recover the fundamental features of the surface currents of the Oceans.</td>
</tr>
<tr id="bib_Faccin2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Faccin2021,
    author = {Faccin, M. and Schaub, M. T. and Delvenne, J.-C.},
           title = {State aggregations in Markov chains and block models of networks},
           journal = {Physical Review Letters},
           publisher = {American Physical Society},
           year = {2021},
           volume = {127},
           number = {7},
           pages = {078301},
           url = {https://arxiv.org/abs/2005.00337},
           doi = {10.1103/PhysRevLett.127.078301}
}
    </pre></td>
</tr>
<tr id="Nagai2021" class="entry">
    <td> [54] Nagai, J.S.; Leimkühler, N.B.; Schaub, M.T.; Schneider, R.K. &amp; Costa, I.G. (2021), <i>"CrossTalkeR: analysis and visualization of ligand–receptorne tworks"</i>, Bioinformatics., 05, 2021. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Nagai2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Nagai2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1093/bioinformatics/btab370" target="_blank">DOI</a>] [<a href="https://www.biorxiv.org/content/10.1101/2021.01.20.427390v2" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Nagai2021" class="abstract noshow">
    <td><b>Abstract</b>: Ligand–receptor (LR) network analysis allows the characterization of cellular crosstalk based on single cell RNA-seq data. However, current methods typically provide a list of inferred LR interactions and do not allow the researcher to focus on specific cell types, ligands or receptors. In addition, most of these methods cannot quantify changes in crosstalk between two biological phenotypes.CrossTalkeR is a framework for network analysis and visualization of LR interactions. CrossTalkeR identifies relevant ligands, receptors and cell types contributing to changes in cell communication when contrasting two biological phenotypes, i.e. disease versus homeostasis. A case study on scRNA-seq of human myeloproliferative neoplasms reinforces the strengths of CrossTalkeR for characterization of changes in cellular crosstalk in disease.CrosstalkeR is an R package available at: Github: https://github.com/CostaLab/CrossTalkeR.Supplementary data are available at Bioinformatics online.</td>
</tr>
<tr id="bib_Nagai2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Nagai2021,
    author = {Nagai, James S and Leimkühler, Nils B and Schaub, Michael T and Schneider, Rebekka K and Costa, Ivan G},
           title = {CrossTalkeR: analysis and visualization of ligand–receptorne tworks},
           journal = {Bioinformatics},
           year = {2021},
           note = {btab370},
           url = {https://www.biorxiv.org/content/10.1101/2021.01.20.427390v2},
           doi = {10.1093/bioinformatics/btab370}
}
    </pre></td>
</tr>
<tr id="Schaub2021" class="entry">
    <td> [55] Schaub, M.T.; Zhu, Y.; Seby, J.-B.; Roddenberry, T.M. &amp; Segarra, S. (2021), <i>"Signal Processing on Higher-Order Networks: Livin' on the Edge ... and Beyond"</i>, Signal Processing., January, 2021.  Vol. 187, pp. 108149.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2021','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1016/j.sigpro.2021.108149" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2101.05510" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2021" class="abstract noshow">
    <td><b>Abstract</b>: This tutorial paper presents a didactic treatment of the emerging topic of signal processing on higher-order networks. Drawing analogies from discrete and graph signal processing, we introduce the building blocks for processing data on simplicial complexes and hypergraphs, two common abstractions of higher-order networks that can incorporate polyadic relationships.We provide basic introductions to simplicial complexes and hypergraphs, making special emphasis on the concepts needed for processing signals on them. Leveraging these concepts, we discuss Fourier analysis, signal denoising, signal interpolation, node embeddings, and non-linear processing through neural networks in these two representations of polyadic relational structures. In the context of simplicial complexes, we specifically focus on signal processing using the Hodge Laplacian matrix, a multi-relational operator that leverages the special structure of simplicial complexes and generalizes desirable properties of the Laplacian matrix in graph signal processing. For hypergraphs, we present both matrix and tensor representations, and discuss the trade-offs in adopting one or the other. We also highlight limitations and potential research avenues, both to inform practitioners and to motivate the contribution of new researchers to the area.</td>
</tr>
<tr id="bib_Schaub2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2021,
    author = {Michael T. Schaub and Yu Zhu and Jean-Baptiste Seby and T. Mitchell Roddenberry and Santiago Segarra},
           title = {Signal Processing on Higher-Order Networks: Livin' on the Edge ... and Beyond},
           journal = {Signal Processing},
           year = {2021},
           volume = {187},
           pages = {108149},
           url = {https://arxiv.org/abs/2101.05510},
           doi = {10.1016/j.sigpro.2021.108149}
}
    </pre></td>
</tr>
<tr id="Roddenberry2020" class="entry">
    <td> [56] Roddenberry, T.M.; Schaub, M.T.; Wai, H.-T. &amp; Segarra, S. (2020), <i>"Exact Blind Community Detection from Signals on Multiple Graphs"</i>, IEEE Transactions on Signal Processing., August, 2020. 
        <p class="infolinks">[<a href="javascript:toggleInfo('Roddenberry2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Roddenberry2020','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/TSP.2020.3016494" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/2001.10944" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Roddenberry2020" class="abstract noshow">
    <td><b>Abstract</b>: Networks and data supported on graphs have become ubiquitous in the sciences and engineering. This paper studies the 'blind' community detection problem, where we seek to infer the community structure of a graph model given the observation of independent graph signals on a set of nodes whose connections are unknown. We model each observation as filtered white noise, where the underlying network structure varies with every observation. These varying network structures are modeled as independent realizations of a latent planted partition model (PPM), justifying our assumption of a constant underlying community structure over all observations. Under certain conditions on the graph filter and PPM parameters, we propose algorithms for determining (i) the number of latent communities and (ii) the associated partitions of the PPM. We then prove statistical guarantees in the asymptotic and non-asymptotic sampling cases. Numerical experiments on real and synthetic data demonstrate the efficacy of our algorithms.</td>
</tr>
<tr id="bib_Roddenberry2020" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Roddenberry2020,
    author = {Roddenberry, T. Mitchell and Schaub, Michael T. and Wai, Hoi-To and Segarra, Santiago},
           title = {Exact Blind Community Detection from Signals on Multiple Graphs},
           journal = {IEEE Transactions on Signal Processing},
           year = {2020},
           url = {https://arxiv.org/abs/2001.10944},
           doi = {10.1109/TSP.2020.3016494}
}
    </pre></td>
</tr>
<tr id="Schaub2020" class="entry">
    <td> [57] Schaub, M.T.; Segarra, S. &amp; Tsitsiklis, J.N. (2020), <i>"Blind identification of stochastic block models from dynamical observations"</i>, SIAM Journal on Mathematics of Data Science., May, 2020.  Vol. 2(2), pp. 335-367.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2020','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1137/19M1263340" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1905.09107" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2020" class="abstract noshow">
    <td><b>Abstract</b>: We consider a blind identification problem in which we aim to recover a statistical model of a network without knowledge of the network's edges, but based solely on nodal observations of a certain process. More concretely, we focus on observations that consist of snapshots of a diffusive process that evolves over the unknown network. We model the network as generated from an independent draw from a latent stochastic block model (SBM), and our goal is to infer both the partition of the nodes into blocks, as well as the parameters of this SBM. We present simple spectral algorithms that provably solve the partition recovery and parameter estimation problems with high accuracy. Our analysis relies on recent results in random matrix theory and covariance estimation, and associated concentration inequalities. We illustrate our results with several numerical experiments.</td>
</tr>
<tr id="bib_Schaub2020" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2020,
    author = {Schaub, Michael T. and Segarra, Santiago and Tsitsiklis, John N.},
           title = {Blind identification of stochastic block models from dynamical observations},
           journal = {SIAM Journal on Mathematics of Data Science},
           year = {2020},
           volume = {2},
           number = {2},
           pages = {335--367},
           url = {https://arxiv.org/abs/1905.09107},
           doi = {10.1137/19M1263340}
}
    </pre></td>
</tr>
<tr id="Schaub2020a" class="entry">
    <td> [58] Schaub, M.T.; Benson, A.R.; Horn, P.; Lippner, G. &amp; Jadbabaie, A. (2020), <i>"Random walks on simplicial complexes and the normalized Hodge 1-Laplacian"</i>, SIAM Review., May, 2020.  Vol. 62(2), pp. 353-391.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2020a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2020a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1137/18M1201019" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1807.05044" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2020a" class="abstract noshow">
    <td><b>Abstract</b>: Modeling complex systems and data with graphs has been a mainstay of the applied mathematics community. The nodes in the graph represent entities and the edges model the relations between them. Simplicial complexes, a mathematical object common in topological data analysis, have emerged as a model for multi-nodal interactions that occur in several complex systems; for example, biological interactions occur between a set of molecules rather than just two, and commu- nication systems can have group messages and not just person-to-person messages. While simplicial complexes can model multi-nodal interactions, many ideas from network analysis concerning dynam- ical processes lack a proper correspondence in the a simplicial complex model. In particular, diffusion processes and random walks, which underpin large parts of the network analysis toolbox including centrality measures and ranking, community detection, and contagion models, have so far been only scarcely studied for simplicial complexes. Here we develop a diffusion process on simplicial com- plexes that can serve as a foundation for making simplicial complex models more effective. Our key idea is to generalize the well-known relationship between the normalized graph Laplacian operator and random walks on graphs by devising an appropriate normalization for the Hodge Laplacian, the analog of the graph Laplacian for simplicial complexes. We demonstrate how our diffusion process can be used for system analysis by developing a generalization of PageRank for edges in simplicial complexes and analyzing a book co-purchasing dataset.</td>
</tr>
<tr id="bib_Schaub2020a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2020a,
    author = {Schaub, Michael T. and Benson, Austin R. and Horn, Paul and Lippner, Gabor and Jadbabaie, Ali},
           title = {Random walks on simplicial complexes and the normalized Hodge 1-Laplacian},
           journal = {SIAM Review},
           year = {2020},
           volume = {62},
           number = {2},
           pages = {353--391},
           url = {https://arxiv.org/abs/1807.05044},
           doi = {10.1137/18M1201019}
}
    </pre></td>
</tr>
<tr id="Zhu2020" class="entry">
    <td> [59] Zhu, Y.; Schaub, M.T.; Jadbabaie, A. &amp; Segarra, S. (2020), <i>"Network Inference from Consensus Dynamics with Unknown Parameters"</i>, IEEE Transactions on Signal and Information Processing over Networks., April, 2020.  Vol. 6, pp. 300-315.
        <p class="infolinks">[<a href="javascript:toggleInfo('Zhu2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Zhu2020','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/TSIPN.2020.2984499" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1908.01393" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Zhu2020" class="abstract noshow">
    <td><b>Abstract</b>: We explore the problem of inferring the graph Laplacian of a weighted, undirected network from snapshots of a single or multiple discrete-time consensus dynamics, subject to parameter uncertainty, taking place on the network. Specifically, we consider three problems in which we assume different levels of knowledge about the diffusion rates, observation times, and the input signal power of the dynamics. To solve these underdetermined problems, we propose a set of algorithms that leverage the spectral properties of the observed data and tools from convex optimization. Furthermore, we provide theoretical performance guarantees associated with these algorithms. We complement our theoretical work with numerical experiments, that demonstrate how our proposed methods outperform current state-of-the-art algorithms and showcase their effectiveness in recovering both synthetic and real-world networks.</td>
</tr>
<tr id="bib_Zhu2020" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Zhu2020,
    author = {Zhu, Yu and Schaub, Michael T. and Jadbabaie, Ali and Segarra, Santiago},
           title = {Network Inference from Consensus Dynamics with Unknown Parameters},
           journal = {IEEE Transactions on Signal and Information Processing over Networks},
           year = {2020},
           volume = {6},
           pages = {300--315},
           url = {https://arxiv.org/abs/1908.01393},
           doi = {10.1109/TSIPN.2020.2984499}
}
    </pre></td>
</tr>
<tr id="Avella-Medina2020" class="entry">
    <td> [60] Avella-Medina, M.; Parise, F.; Schaub, M. &amp; Segarra, S. (2020), <i>"Centrality measures for graphons: Accounting for uncertainty in networks"</i>, IEEE Transactions on Network Science and Engineering., January, 2020.  Vol. 7(1), pp. 520-537.
        <p class="infolinks">[<a href="javascript:toggleInfo('Avella-Medina2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Avella-Medina2020','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/TNSE.2018.2884235" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1707.09350" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Avella-Medina2020" class="abstract noshow">
    <td><b>Abstract</b>: As relational datasets modeled as graphs keep increasing in size and their data-acquisition is permeated by uncertainty, graph-based analysis techniques can become computationally and conceptually challenging. In particular, node centrality measures rely on the assumption that the graph is perfectly known --- a premise not necessarily fulfilled for large, uncertain networks. Accordingly, centrality measures may fail to faithfully extract the importance of nodes in the presence of uncertainty. To mitigate these problems, we suggest a statistical approach based on graphon theory: we introduce formal definitions of centrality measures for graphons and establish their connections to classical graph centrality measures. A key advantage of this approach is that centrality measures defined at the modeling level of graphons are inherently robust to stochastic variations of specific graph realizations. Using the theory of linear integral operators, we define degree, eigenvector, Katz and PageRank centrality functions for graphons and establish concentration inequalities demonstrating that graphon centrality functions arise naturally as limits of their counterparts defined on sequences of graphs of increasing size. The same concentration inequalities also provide high-probability bounds between the graphon centrality functions and the centrality measures on any sampled graph, thereby establishing a measure of uncertainty of the measured centrality score.</td>
</tr>
<tr id="bib_Avella-Medina2020" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Avella-Medina2020,
    author = {Avella-Medina, M. and Parise, F. and Schaub, M. and Segarra, S.},
           title = {Centrality measures for graphons: Accounting for uncertainty in networks},
           journal = {IEEE Transactions on Network Science and Engineering},
           year = {2020},
           volume = {7},
           number = {1},
           pages = {520--537},
           url = {https://arxiv.org/abs/1707.09350},
           doi = {10.1109/TNSE.2018.2884235}
}
    </pre></td>
</tr>
<tr id="Rosvall2019" class="entry">
    <td> [61] Rosvall, M.; Delvenne, J.-C.; Schaub, M.T. &amp; Lambiotte, R. (2019), <i>"Different Approaches to Community Detection"</i>, In Advances in Network Clustering and Blockmodeling., November, 2019. , pp. 105-119. John Wiley &amp; Sons, Ltd.
        <p class="infolinks">[<a href="javascript:toggleInfo('Rosvall2019','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Rosvall2019','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1002/9781119483298.ch4" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1712.06468" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Rosvall2019" class="abstract noshow">
    <td><b>Abstract</b>: A precise definition of what constitutes a community in networks has remained elusive. Consequently, network scientists have compared community detection algorithms on benchmark networks with a particular form of community structure and classified them based on the mathematical techniques they employ. However, this comparison can be misleading because apparent similarities in their mathematical machinery can disguise different reasons for why we would want to employ community detection in the first place. Here we provide a focused review of these different motivations that underpin community detection. This problem-driven classification is useful in applied network science, where it is important to select an appropriate algorithm for the given purpose. Moreover, highlighting the different approaches to community detection also delineates the many lines of research and points out open directions and avenues for future research.</td>
</tr>
<tr id="bib_Rosvall2019" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@incollection{Rosvall2019,
    author = {Rosvall, Martin and Delvenne, Jean-Charles and Schaub, Michael T. and Lambiotte, Renaud},
           editor = {Patrick Doreian and Vladimir Batagelj and Anuska Ferligoj},
           title = {Different Approaches to Community Detection},
           booktitle = {Advances in Network Clustering and Blockmodeling},
           publisher = {John Wiley &amp; Sons, Ltd},
           year = {2019},
           pages = {105--119},
           url = {https://arxiv.org/abs/1712.06468},
           doi = {10.1002/9781119483298.ch4}
}
    </pre></td>
</tr>
<tr id="Schaub2019c" class="entry">
    <td> [62] Schaub, M.T.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2019), <i>"Structured Networks and Coarse-Grained Descriptions"</i>, In Advances in Network Clustering and Blockmodeling., November, 2019. , pp. 333-361. John Wiley &amp; Sons, Ltd.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2019c','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2019c','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1002/9781119483298.ch12" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1804.06268" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2019c" class="abstract noshow">
    <td><b>Abstract</b>: This chapter discusses the interplay between structure and dynamics in complex networks. Given a particular network with an endowed dynamics, our goal is to find partitions aligned with the dynamical process acting on top of the network. We thus aim to gain a reduced description of the system that takes into account both its structure and dynamics.<br>In the first part, we introduce the general mathematical setup for the types of dynamics we consider throughout the chapter. We provide two guiding examples, namely consensus dynamics and diffusion processes (random walks), motivating their connection to social network analysis, and provide a brief discussion on the general dynamical framework and its possible extensions.<br>In the second part, we focus on the influence of graph structure on the dynamics taking place on the network, focussing on three concepts that allow us to gain insight into this notion. First, we describe how time scale separation can appear in the dynamics on a network as a consequence of graph structure. Second, we discuss how the presence of particular symmetries in the network give rise to invariant dynamical subspaces that can be precisely described by graph partitions. Third, we show how this dynamical viewpoint can be extended to study dynamics on networks with signed edges, which allow us to discuss connections to concepts in social network analysis, such as structural balance.<br>In the third part, we discuss how to use dynamical processes unfolding on the network to detect meaningful network substruc- tures. We then show how such dynamical measures can be related to seemingly different algorithm for community detection and coarse-graining proposed in the literature. We conclude with a brief summary and highlight interesting open future directions.</td>
</tr>
<tr id="bib_Schaub2019c" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@incollection{Schaub2019c,
    author = {Schaub, Michael T. and Delvenne, Jean-Charles and Lambiotte, Renaud and Barahona, Mauricio},
           editor = {Patrick Doreian and Vladimir Batagelj and Anuska Ferligoj},
           title = {Structured Networks and Coarse-Grained Descriptions},
           booktitle = {Advances in Network Clustering and Blockmodeling},
           publisher = {John Wiley &amp; Sons, Ltd},
           year = {2019},
           pages = {333--361},
           url = {https://arxiv.org/abs/1804.06268},
           doi = {10.1002/9781119483298.ch12}
}
    </pre></td>
</tr>
<tr id="Jia2019" class="entry">
    <td> [63] Jia, J.; Segarra, S.; Schaub, M.T. &amp; Benson, A.R. (2019), <i>"Graph-based Semi-Supervised &amp; Active Learning for Edge Flows"</i>, In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2019). New York, NY, USA, August, 2019. , pp. 761-771. ACM.
        <p class="infolinks">[<a href="javascript:toggleInfo('Jia2019','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Jia2019','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1145/3292500.3330872" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1905.07451" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Jia2019" class="abstract noshow">
    <td><b>Abstract</b>: We present a graph-based semi-supervised learning (SSL) method for learning edge flows defined on a graph. Specifically, given flow measurements on a subset of edges, we want to predict the flows on the remaining edges. To this end, we develop a computational framework that imposes certain constraints on the overall flows,such as (approximate) flow conservation. These constraints render our approach different from classical graph-based SSL for vertex labels, which posits that tightly connected nodes share similar labels and leverages the graph structure accordingly to extrapolate from a few vertex labels to the unlabeled vertices.We derive bounds for our method's reconstruction error and demonstrate its strong performance on synthetic and real-world flow networks from transportation, physical infrastructure, and the Web. Furthermore, we provide two active learning algorithms for selecting informative edges on which to measure flow, which has applications for optimal sensor deployment. The first strategy selects edges to minimize the reconstruction error bound and works well on flows that are approximately divergence-free. The second approach clusters the graph and selects bottleneck edges that cross cluster-boundaries, which works well on flows with global trends.</td>
</tr>
<tr id="bib_Jia2019" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Jia2019,
    author = {Jia, Junteng and Segarra, Santiago and Schaub, Michael T. and Benson, Austin R.},
           title = {Graph-based Semi-Supervised &amp; Active Learning for Edge Flows},
           booktitle = {Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2019)},
           publisher = {ACM},
           year = {2019},
           pages = {761--771},
           url = {https://arxiv.org/abs/1905.07451},
           doi = {10.1145/3292500.3330872}
}
    </pre></td>
</tr>
<tr id="Schaub2019a" class="entry">
    <td> [64] Schaub, M.T.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2019), <i>"Multiscale Dynamical Embeddings of Complex Networks"</i>, Phys. Rev. E., June, 2019.  Vol. 99(6), pp. 062308. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2019a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2019a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevE.99.062308" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1804.03733" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2019a" class="abstract noshow">
    <td><b>Abstract</b>: Complex systems and relational data are often abstracted as dynamical processes on networks. To understand, predict and control their behavior, a crucial step is to extract reduced descriptions of such networks. Inspired by notions from Control Theory, we propose a time-dependent dynamical similarity measure between nodes, which quantifies the effect a node-input has on the network. This dynamical similarity induces an embedding that can be employed for several analysis tasks. Here we focus on (i) dimensionality reduction, i.e., projecting nodes onto a low dimensional space that captures dynamic similarity at different time scales, and (ii) how to exploit our embeddings to uncover functional modules. We exemplify our ideas through case studies focusing on directed networks without strong connectivity, and signed networks. We further highlight how certain ideas from community detection can be generalized and linked to Control Theory, by using the here developed dynamical perspective.</td>
</tr>
<tr id="bib_Schaub2019a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2019a,
    author = {Schaub, Michael T. and Delvenne, Jean-Charles and Lambiotte, Renaud and Barahona, Mauricio},
           title = {Multiscale Dynamical Embeddings of Complex Networks},
           journal = {Phys. Rev. E},
           publisher = {American Physical Society},
           year = {2019},
           volume = {99},
           number = {6},
           pages = {062308},
           url = {https://arxiv.org/abs/1804.03733},
           doi = {10.1103/PhysRevE.99.062308}
}
    </pre></td>
</tr>
<tr id="Schaub2019" class="entry">
    <td> [65] Schaub, M.T.; Segarra, S. &amp; Wai, H. (2019), <i>"Spectral Partitioning of Time-varying Networks with Unobserved Edges"</i>, In 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2019)., May, 2019. , pp. 4938-4942.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2019','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2019','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/ICASSP.2019.8682815" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1904.11930" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2019" class="abstract noshow">
    <td><b>Abstract</b>: We discuss a variant of ‘blind’ community detection, in which we aim to partition an unobserved network from the observation of a (dynamical) graph signal defined on the network. We consider a scenario where our observed graph signals are obtained by filtering white noise input, and the underlying network is different for every observation. In this fashion, the filtered graph signals can be interpreted as defined on a time-varying network. We model each of the underlying network realizations as generated by an independent draw from a latent stochastic blockmodel (SBM). To infer the partition of the latent SBM, we propose a simple spectral algorithm for which we provide a theoretical analysis and establish consistency guarantees for the recovery. We illustrate our results using numerical experiments on synthetic and real data, highlighting the efficacy of our approach.</td>
</tr>
<tr id="bib_Schaub2019" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Schaub2019,
    author = {Schaub, M. T. and Segarra, S. and Wai, H.},
           title = {Spectral Partitioning of Time-varying Networks with Unobserved Edges},
           booktitle = {2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2019)},
           year = {2019},
           pages = {4938--4942},
           url = {https://arxiv.org/abs/1904.11930},
           doi = {10.1109/ICASSP.2019.8682815}
}
    </pre></td>
</tr>
<tr id="Schaub2018b" class="entry">
    <td> [66] Schaub, M.T. &amp; Segarra, S. (2018), <i>"Flow Smoothing And Denoising: Graph Signal Processing In The Edge-space"</i>, In 2018 IEEE Global Conference on Signal and Information Processing (GlobalSIP)., November, 2018. , pp. 735-739.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2018b','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2018b','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/GlobalSIP.2018.8646701" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1808.02111" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2018b" class="abstract noshow">
    <td><b>Abstract</b>: This paper focuses on devising graph signal processing tools for the treatment of data defined on the edges of a graph. We first show that conventional tools from graph signal processing may not be suitable for the analysis of such signals. More specifically, we discuss how the underlying notion of a `smooth signal' inherited from (the typically considered variants of) the graph Laplacian are not suitable when dealing with edge signals that encode a notion of flow. To overcome this limitation we introduce a class of filters based on the Edge-Laplacian, a special case of the Hodge-Laplacian for simplicial complexes of order one. We demonstrate how this Edge-Laplacian leads to low-pass filters that enforce (approximate) flow-conservation in the processed signals. Moreover, we show how these new filters can be combined with more classical Laplacian-based processing methods on the line-graph. Finally, we illustrate the developed tools by denoising synthetic traffic flows on the London street network.</td>
</tr>
<tr id="bib_Schaub2018b" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Schaub2018b,
    author = {Schaub, M. T. and Segarra, S.},
           title = {Flow Smoothing And Denoising: Graph Signal Processing In The Edge-space},
           booktitle = {2018 IEEE Global Conference on Signal and Information Processing (GlobalSIP)},
           year = {2018},
           pages = {735--739},
           url = {https://arxiv.org/abs/1808.02111},
           doi = {10.1109/GlobalSIP.2018.8646701}
}
    </pre></td>
</tr>
<tr id="Benson2018" class="entry">
    <td> [67] Benson, A.R.; Abebe, R.; Schaub, M.T.; Jadbabaie, A. &amp; Kleinberg, J. (2018), <i>"Simplicial closure and higher-order link prediction"</i>, Proceedings of the National Academy of Sciences., November, 2018.  Vol. 115(48), pp. E11221-E11230.
        <p class="infolinks">[<a href="javascript:toggleInfo('Benson2018','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Benson2018','comment')">Comment</a>]  [<a href="javascript:toggleInfo('Benson2018','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1073/pnas.1800683115" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1802.06916" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Benson2018" class="abstract noshow">
    <td><b>Abstract</b>: Networks provide a powerful formalism for modeling complex systems by using a model of pairwise interactions. But much of the structure within these systems involves interactions that take place among more than two nodes at once&mdash;for example, communication within a group rather than person to person, collaboration among a team rather than a pair of coauthors, or biological interaction between a set of molecules rather than just two. Such higher-order interactions are ubiquitous, but their empirical study has received limited attention, and little is known about possible organizational principles of such structures. Here we study the temporal evolution of 19 datasets with explicit accounting for higher-order interactions. We show that there is a rich variety of structure in our datasets but datasets from the same system types have consistent patterns of higher-order structure. Furthermore, we find that tie strength and edge density are competing positive indicators of higher-order organization, and these trends are consistent across interactions involving differing numbers of nodes. To systematically further the study of theories for such higher-order structures, we propose higher-order link prediction as a benchmark problem to assess models and algorithms that predict higher-order structure. We find a fundamental difference from traditional pairwise link prediction, with a greater role for local rather than long-range information in predicting the appearance of new interactions.</td>
</tr>
<tr id="rev_Benson2018" class="comment noshow">
    <td><b>Comment</b>: https://news.cornell.edu/stories/2019/01/predicting-future-combos-rap-songs-pharmaceuticals</td>
</tr>
<tr id="bib_Benson2018" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Benson2018,
    author = {Benson, Austin R. and Abebe, Rediet and Schaub, Michael T. and Jadbabaie, Ali and Kleinberg, Jon},
           title = {Simplicial closure and higher-order link prediction},
           journal = {Proceedings of the National Academy of Sciences},
           year = {2018},
           volume = {115},
           number = {48},
           pages = {E11221-E11230},
           url = {https://arxiv.org/abs/1802.06916},
           doi = {10.1073/pnas.1800683115}
}
    </pre></td>
</tr>
<tr id="Billeh2018" class="entry">
    <td> [68] Billeh, Y.N. &amp; Schaub, M.T. (2018), <i>"Feedforward architectures driven by inhibitory interaction patterns"</i>, Journal of Computational Neuroscience., February, 2018.  Vol. 44(1), pp. 63-74.
        <p class="infolinks">[<a href="javascript:toggleInfo('Billeh2018','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Billeh2018','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/s10827-017-0669-1" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1701.04905" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Billeh2018" class="abstract noshow">
    <td><b>Abstract</b>: Directed information transmission is a paramount requirement for many social, physical, and biological systems. For neural systems, scientists have studied this problem under the paradigm of feedforward networks for decades. In most models of feedforward networks, activity is exclusively driven by excitatory neurons and the wiring patterns between them while inhibitory neurons play only a stabilizing role for the network dynamics. Motivated by recent experimental discoveries of hippocampal circuitry and the diversity of inhibitory neurons throughout the brain, here we illustrate that one can construct such networks even if the connectivity between the excitatory units in the system remains random. This is achieved by endowing inhibitory nodes with a more active role in the network. Our findings demonstrate that feedforward activity can be caused by a much broader network-architectural basis than often assumed.</td>
</tr>
<tr id="bib_Billeh2018" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Billeh2018,
    author = {Billeh, Yazan N. and Schaub, Michael T.},
           title = {Feedforward architectures driven by inhibitory interaction patterns},
           journal = {Journal of Computational Neuroscience},
           year = {2018},
           volume = {44},
           number = {1},
           pages = {63--74},
           url = {https://arxiv.org/abs/1701.04905},
           doi = {10.1007/s10827-017-0669-1}
}
    </pre></td>
</tr>
<tr id="Segarra2017" class="entry">
    <td> [69] Segarra, S.; Schaub, M.T. &amp; Jadbabaie, A. (2017), <i>"Network Inference from Consensus Dynamics"</i>, In 56th IEEE Conference on Decision and Control (CDC 2017)., December, 2017. , pp. 3212-3217.
        <p class="infolinks">[<a href="javascript:toggleInfo('Segarra2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Segarra2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/CDC.2017.8264130" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1708.05329" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Segarra2017" class="abstract noshow">
    <td><b>Abstract</b>: We consider the problem of identifying the topology of a weighted, undirected network G from observing snapshots of multiple independent consensus dynamics. Specifically, we observe the opinion profiles of a group of agents for a set of M independent topics and our goal is to recover the precise relationships between the agents, as specified by the unknown network G. In order to overcome the under- determinacy of the problem at hand, we leverage concepts from spectral graph theory and convex optimization to unveil the underlying network structure. More precisely, we formulate the network inference problem as a convex optimization that seeks to endow the network with certain desired properties – such as sparsity – while being consistent with the spectral information extracted from the observed opinions. This is complemented with theoretical results proving consistency as the number M of topics grows large. We further illustrate our method by numerical experiments, which showcase the effectiveness of the technique in recovering synthetic and real-world networks.</td>
</tr>
<tr id="bib_Segarra2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@inproceedings{Segarra2017,
    author = {Segarra, Santiago and Schaub, Michael T. and Jadbabaie, Ali},
           title = {Network Inference from Consensus Dynamics},
           booktitle = {56th IEEE Conference on Decision and Control (CDC 2017)},
           year = {2017},
           pages = {3212--3217},
           url = {https://arxiv.org/abs/1708.05329},
           doi = {10.1109/CDC.2017.8264130}
}
    </pre></td>
</tr>
<tr id="Faccin2017" class="entry">
    <td> [70] Faccin, M.; Schaub, M.T. &amp; Delvenne, J.-C. (2017), <i>"Entrograms and coarse graining of dynamics on complex networks"</i>, Journal of Complex Networks., November, 2017. , pp. cnx055.
        <p class="infolinks">[<a href="javascript:toggleInfo('Faccin2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Faccin2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1093/comnet/cnx055" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1711.01987" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Faccin2017" class="abstract noshow">
    <td><b>Abstract</b>: Using an information theoretic point of view, we investigate how a dynamics acting on a network can be coarse grained through the use of graph partitions. Specifically, we are interested in how aggregating the state space of a Markov process according to a partition impacts on the thus obtained lower-dimensional dynamics. We highlight that for a dynamics on a particular graph there may be multiple coarse grained descriptions that capture different, incomparable features of the original process. For instance, a coarse graining induced by one partition may be commensurate with a time-scale separation in the dynamics, while another coarse graining may correspond to a different lower-dimensional dynamics that preserves the Markov property of the original process. Taking inspiration from the literature of Computational Mechanics, we find that a convenient tool to summarise and visualise such dynamical properties of a coarse grained model (partition) is the entrogram. The entrogram gathers certain information-theoretic measures, which quantify how information flows across time steps. These information theoretic quantities include the entropy rate, as well as a measure for the memory contained in the process, i.e., how well the dynamics can be approximated by a first order Markov process. We use the entrogram to investigate how specific macro-scale connection patterns in the state-space transition graph of the original dynamics result in desirable properties of coarse grained descriptions. We thereby provide a fresh perspective on the interplay between structure and dynamics in networks, and the process of partitioning from an information theoretic perspective. We focus on networks that may be approximated by both a core-periphery or a clustered organization, and highlight that each of these coarse grained descriptions can capture different aspects of a Markov process acting on the network.</td>
</tr>
<tr id="bib_Faccin2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Faccin2017,
    author = {Faccin, Mauro and Schaub, Michael T. and Delvenne, Jean-Charles},
           title = {Entrograms and coarse graining of dynamics on complex networks},
           journal = {Journal of Complex Networks},
           year = {2017},
           pages = {cnx055},
           url = {https://arxiv.org/abs/1711.01987},
           doi = {10.1093/comnet/cnx055}
}
    </pre></td>
</tr>
<tr id="Estrada2017" class="entry">
    <td> [71] Estrada, E.; Delvenne, J.-C.; Hatano, N.; Mateos, J.L.; Metzler, R.; Riascos, A.P. &amp; Schaub, M.T. (2017), <i>"Random Multi-Hopper Model. Super-Fast Random Walks on Graphs"</i>, Journal of Complex Networks., October, 2017. , pp. cnx043.
        <p class="infolinks">[<a href="javascript:toggleInfo('Estrada2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Estrada2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1093/comnet/cnx043" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1612.08631" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Estrada2017" class="abstract noshow">
    <td><b>Abstract</b>: We develop a model for a random walker with long-range hops on general graphs. This random multi-hopper jumps from a node to any other node in the graph with a probability that decays as a function of the shortest-path distance between the two nodes. We consider here two decaying functions in the form of the Laplace and Mellin transforms of the shortest-path distances. Remarkably, when the parameters of these transforms approach zero asymptotically, the multi-hopper's hitting times between any two nodes in the graph converge to their minimum possible value, given by the hitting times of a normal random walker on a complete graph. Stated differently, for small parameter values the multi-hopper explores a general graph as fast as possible when compared to a random walker on a full graph. Using computational experiments we show that compared to the normal random walker, the multi-hopper indeed explores graphs with clusters or skewed degree distributions more efficiently for a large parameter range. We provide further computational evidence of the speed-up attained by the random multi-hopper model with respect to the normal random walker by studying deterministic, random and real-world networks.</td>
</tr>
<tr id="bib_Estrada2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Estrada2017,
    author = {Estrada, E. and Delvenne, J.-C. and Hatano, N. and Mateos, J. L. and Metzler, R. and Riascos, A. P. and Schaub, M. T.},
           title = {Random Multi-Hopper Model. Super-Fast Random Walks on Graphs},
           journal = {Journal of Complex Networks},
           year = {2017},
           pages = {cnx043},
           url = {https://arxiv.org/abs/1612.08631},
           doi = {10.1093/comnet/cnx043}
}
    </pre></td>
</tr>
<tr id="Schaub*2017" class="entry">
    <td> [72] Schaub*, M.T.; Trefois*, M.; Dooren, P.V. &amp; Delvenne, J.-C. (2017), <i>"Sparse Matrix Factorizations For Fast Iterative Linear Solvers With Application To Laplacian Systems"</i>, SIAM Journal on Matrix Analysis and Applications., June, 2017.  Vol. 38(2), pp. 505-529.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub*2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub*2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1137/16M1077398" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1605.09148" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub*2017" class="abstract noshow">
    <td><b>Abstract</b>: In solving a linear system with iterative methods, one is usually confronted with the dilemma of having to choose between cheap, inefficient iterates over sparse search directions (e.g., coordinate descent), or expensive iterates in well-chosen search directions (e.g., conjugate gradients). In this paper, we propose to interpolate between these two extremes, and show how to perform cheap iterations along non-sparse search directions, provided that these directions admit a new kind of sparse factorization. For example, if the search directions are the columns of a hierarchical matrix, then the cost of each iteration is typically logarithmic in the number of variables. Using some graph-theoretical results on low-stretch spanning trees, we deduce as a special case a nearly-linear time algorithm to approximate the minimal norm solution of a linear system Bx=b where B is the incidence matrix of a graph. We thereby can connect our results to recently proposed nearly-linear time solvers for Laplacian systems, which emerge here as a particular application of our sparse matrix factorization.</td>
</tr>
<tr id="bib_Schaub*2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub*2017,
    author = {Schaub*, Michael T. and Trefois*, Maguy and Dooren, Paul Van and Delvenne, Jean-Charles},
           title = {Sparse Matrix Factorizations For Fast Iterative Linear Solvers With Application To Laplacian Systems},
           journal = {SIAM Journal on Matrix Analysis and Applications},
           year = {2017},
           volume = {38},
           number = {2},
           pages = {505--529},
           url = {https://arxiv.org/abs/1605.09148},
           doi = {10.1137/16M1077398}
}
    </pre></td>
</tr>
<tr id="Kiselev2017" class="entry">
    <td> [73] Kiselev, V.Y.; Kirschner, K.; Schaub, M.T.; Andrews, T.; Chandra, T.; Natarajan, K.N.; Reik, W.; Barahona, M.; Green, A.R. &amp; Hemberg, M. (2017), <i>"SC3 - consensus clustering of single-cell RNA-Seq data"</i>, Nature Methods., March, 2017.  Vol. 14(5), pp. 483-486.
        <p class="infolinks">[<a href="javascript:toggleInfo('Kiselev2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Kiselev2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1038/nmeth.4236" target="_blank">DOI</a>] [<a href="https://doi.org/10.1101/036558" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Kiselev2017" class="abstract noshow">
    <td><b>Abstract</b>: Using single-cell RNA-seq (scRNA-seq), the full transcriptome of individual cells can be acquired, enabling a quantitative characterisation of cell-type based on expression profiles. Due to the large variability in gene expression, assigning cells into groups based on the transcriptome remains challenging. We present Single-Cell Consensus Clustering (SC3), a tool for unsupervised clustering of scRNA-seq data. SC3 integrates many different clustering solutions through a consensus approach, thereby increasing its accuracy and robustness against noise. Tests on nine published datasets show that SC3 outperforms existing methods, yet SC3 remains scalable for large datasets, as shown by the analysis of a dataset containing &nbsp;45,000 cells. To enhance the accessibility to users with limited bioinformatics expertise, SC3 features an interactive graphical implementation, which aids the biological interpretation by identifying marker genes, differentially expressed genes and outlier cells. Finally, we apply SC3 to identify different subclones of neoplastic cells in data collected from patients.</td>
</tr>
<tr id="bib_Kiselev2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Kiselev2017,
    author = {Kiselev, Vladimir Yu. and Kirschner, Kristina and Schaub, Michael T. and Andrews, Tallulah and Chandra, Tamir and Natarajan, Kedar N. and Reik, Wolf and Barahona, Mauricio and Green, Anthony R. and Hemberg, Martin},
           title = {SC3 - consensus clustering of single-cell RNA-Seq data},
           journal = {Nature Methods},
           year = {2017},
           volume = {14},
           number = {5},
           pages = {483--486},
           url = {https://doi.org/10.1101/036558},
           doi = {10.1038/nmeth.4236}
}
    </pre></td>
</tr>
<tr id="Schaub2017" class="entry">
    <td> [74] Schaub, M.T.; Delvenne, J.-C.; Rosvall, M. &amp; Lambiotte, R. (2017), <i>"The many facets of community detection in complex networks"</i>, Applied Network Science., February, 2017.  Vol. 2(1), pp. 4.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/s41109-017-0023-6" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1611.07769" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2017" class="abstract noshow">
    <td><b>Abstract</b>: Community detection, the decomposition of a graph into essential building blocks, has been a core research topic in network science over the past years. Since a precise notion of what constitutes a community has remained evasive, community detection algorithms have often been compared on benchmark graphs with a particular form of assortative community structure and classified based on the mathematical techniques they employ. However, this comparison can be misleading because apparent similarities in their mathematical machinery can disguise different goals and reasons for why we want to employ community detection in the first place. Here we provide a focused review of these different motivations that underpin community detection. This problem-driven classification is useful in applied network science, where it is important to select an appropriate algorithm for the given purpose. Moreover, highlighting the different facets of community detection also delineates the many lines of research and points out open directions and avenues for future research.</td>
</tr>
<tr id="bib_Schaub2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2017,
    author = {Schaub, Michael T. and Delvenne, Jean-Charles and Rosvall, Martin and Lambiotte, Renaud},
           title = {The many facets of community detection in complex networks},
           journal = {Applied Network Science},
           year = {2017},
           volume = {2},
           number = {1},
           pages = {4},
           url = {https://arxiv.org/abs/1611.07769},
           doi = {10.1007/s41109-017-0023-6}
}
    </pre></td>
</tr>
<tr id="Bacik2016" class="entry">
    <td> [75] Bacik, K.A.; Schaub, M.T.; Beguerisse-Diaz, M.; Billeh, Y.N. &amp; Barahona, M. (2016), <i>"Flow-Based Network Analysis of the Caenorhabditis elegans Connectome"</i>, PLoS Computational Biology., August, 2016.  Vol. 12(8), pp. 1-27.
        <p class="infolinks">[<a href="javascript:toggleInfo('Bacik2016','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Bacik2016','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1371/journal.pcbi.1005055" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1511.00673" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Bacik2016" class="abstract noshow">
    <td><b>Abstract</b>: We exploit flow propagation on the directed neuronal network of the nematode C. elegans to reveal dynamically relevant features of its connectome. We find flow-based groupings of neurons at different levels of granularity, which we relate to functional and anatomical con- stituents of its nervous system. A systematic in silico evaluation of the full set of single and double neuron ablations is used to identify deletions that induce the most severe disruptions of the multi-resolution flow structure. Such ablations are linked to functionally relevant neu- rons, and suggest potential candidates for further in vivo investigation. In addition, we use the directional patterns of incoming and outgoing network flows at all scales to identify flow profiles for the neurons in the connectome, without pre-imposing a priori categories. The four flow roles identified are linked to signal propagation motivated by biological input- response scenarios.</td>
</tr>
<tr id="bib_Bacik2016" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Bacik2016,
    author = {Bacik, Karol A. and Schaub, Michael T. and Beguerisse-Diaz, Mariano and Billeh, Yazan N. and Barahona, Mauricio},
           title = {Flow-Based Network Analysis of the Caenorhabditis elegans Connectome},
           journal = {PLoS Computational Biology},
           year = {2016},
           volume = {12},
           number = {8},
           pages = {1--27},
           url = {https://arxiv.org/abs/1511.00673},
           doi = {10.1371/journal.pcbi.1005055}
}
    </pre></td>
</tr>
<tr id="Schaub2016" class="entry">
    <td> [76] Schaub, M.T.; O'Clery, N.; Billeh, Y.N.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2016), <i>"Graph partitions and cluster synchronization in networks of oscillators"</i>, Chaos., August, 2016.  Vol. 26(9), pp. 094821.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2016','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2016','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1063/1.4961065" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1608.04283" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2016" class="abstract noshow">
    <td><b>Abstract</b>: Synchronization dynamics depends strongly on the structure of the coupling between the oscillators. When the coupling network presents certain regularities, the dynamics can be coarse-grained into clusters by means of External Equitable Partitions and their associated quotient graphs. We exploit this graph-theoretical concept to study the phenomenon of cluster synchronization, in which different groups of nodes converge to distinct behaviors. We derive conditions and properties of networks in which such clustered behavior emerges, and show that the ensuing dynamics is the result of the localization of the eigenvectors of the associated graph Laplacians linked to the existence of invariant subspaces. The framework is applied to both linear and non- linear models, first for the standard case of networks with positive edges, before being generalized to the case of signed networks with both positive and negative interactions. We illustrate our results with examples of both signed and unsigned graphs for consensus dynamics and for partial synchronization of oscillator networks under the master stability function as well as Kuramoto oscillators.</td>
</tr>
<tr id="bib_Schaub2016" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2016,
    author = {Schaub, Michael T. and O'Clery, Neave and Billeh, Yazan N. and Delvenne, Jean-Charles and Lambiotte, Renaud and Barahona, Mauricio},
           title = {Graph partitions and cluster synchronization in networks of oscillators},
           journal = {Chaos},
           year = {2016},
           volume = {26},
           number = {9},
           pages = {094821},
           url = {https://arxiv.org/abs/1608.04283},
           doi = {10.1063/1.4961065}
}
    </pre></td>
</tr>
<tr id="Amor2016" class="entry">
    <td> [77] Amor, B.R.C.; Schaub, M.T.; Yaliraki, S.N. &amp; Barahona, M. (2016), <i>"Prediction of allosteric sites and mediating interactions through bond-to-bond propensities"</i>, Nature Communications., August, 2016.  Vol. 7(12477)
        <p class="infolinks">[<a href="javascript:toggleInfo('Amor2016','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Amor2016','comment')">Comment</a>]  [<a href="javascript:toggleInfo('Amor2016','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1038/ncomms12477" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1605.09710" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Amor2016" class="abstract noshow">
    <td><b>Abstract</b>: Allostery is a fundamental mechanism of biological regulation, in which binding of a molecule at a distant location affects the active site of a protein. Allosteric sites provide targets to fine-tune protein activity, yet we lack computational methodologies to predict them. Here we present an efficient graph-theoretical framework to reveal allosteric interactions (atoms and communication pathways strongly coupled to the active site) without a priori information of their location. Using an atomistic graph with energy-weighted covalent and weak bonds, we define a bond-to-bond propensity quantifying the non-local effect of instantaneous bond fluctuations propagating through the protein. Significant interactions are then identified using quantile regression. We exemplify our method with three biologically important proteins: caspase-1, CheY, and h-Ras, correctly predicting key allosteric interactions, whose significance is additionally confirmed against a reference set of 100 proteins. The almost-linear scaling of our method renders it suitable for high-throughput searches for candidate allosteric sites.</td>
</tr>
<tr id="rev_Amor2016" class="comment noshow">
    <td><b>Comment</b>: News articles: <br>http://www3.imperial.ac.uk/newsandeventspggrp/imperialcollege/newssummary/news_25-8-2016-15-3-8  <br>http://phys.org/news/2016-08-paths-proteins-reveal-drug.html  <br>http://naturalsciencenews.com/2016/08/27/mathematical-models-used-to-study-traffic-jams-can-help-researchers-understand-proteins/?platform=hootsuite</td>
</tr>
<tr id="bib_Amor2016" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Amor2016,
    author = {Amor, Benjamin R. C. and Schaub, Michael T. and Yaliraki, Sophia N. and Barahona, Mauricio},
           title = {Prediction of allosteric sites and mediating interactions through bond-to-bond propensities},
           journal = {Nature Communications},
           year = {2016},
           volume = {7},
           number = {12477},
           url = {https://arxiv.org/abs/1605.09710},
           doi = {10.1038/ncomms12477}
}
    </pre></td>
</tr>
<tr id="Salnikov2016" class="entry">
    <td> [78] Salnikov, V.; Schaub, M.T. &amp; Lambiotte, R. (2016), <i>"Using higher-order Markov models to reveal flow-based communities in networks"</i>, Scientific Reports., March, 2016.  Vol. 6, pp. 23194.
        <p class="infolinks">[<a href="javascript:toggleInfo('Salnikov2016','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Salnikov2016','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1038/srep23194" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1601.03516" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Salnikov2016" class="abstract noshow">
    <td><b>Abstract</b>: Complex systems made of interacting elements are commonly abstracted as networks, in which nodes are associated with dynamic state variables, whose evolution is driven by interactions mediated by the edges. Markov processes have been the prevailing paradigm to model such a network-based dynamics, for instance in the form of random walks or other types of diffusions. Despite the success of this modelling perspective for numerous applications, it represents an over-simplification of several real-world systems. Importantly, simple Markov models lack memory in their dynamics, an assumption often not realistic in practice. Here, we explore possibilities to enrich the system description by means of second-order Markov models, exploiting empirical pathway information. We focus on the problem of community detection and show that standard network algorithms can be generalized in order to extract novel temporal information about the system under investigation. We also apply our methodology to temporal networks, where we can uncover communities shaped by the temporal correlations in the system. Finally, we discuss relations of the framework of second order Markov processes and the recently proposed formalism of using non-backtracking matrices for community detection.</td>
</tr>
<tr id="bib_Salnikov2016" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Salnikov2016,
    author = {Salnikov, Vsevolod and Schaub, Michael T. and Lambiotte, Renaud},
           title = {Using higher-order Markov models to reveal flow-based communities in networks},
           journal = {Scientific Reports},
           year = {2016},
           volume = {6},
           pages = {23194},
           url = {https://arxiv.org/abs/1601.03516},
           doi = {10.1038/srep23194}
}
    </pre></td>
</tr>
<tr id="Schaub*2015" class="entry">
    <td> [79] Schaub*, M.T.; Billeh*, Y.; Anastassiou, C.A.; Koch, C. &amp; Barahona, M. (2015), <i>"Emergence of slow-switching assemblies in structured neuronal networks"</i>, PLoS Computational Biology., July, 2015.  Vol. 11(7), pp. e1004196.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub*2015','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub*2015','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1371/journal.pcbi.1004196" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1502.05656" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub*2015" class="abstract noshow">
    <td><b>Abstract</b>: Unraveling the interplay between connectivity and spatio-temporal dynamics in neuronal networks is a key step to advance our understanding of neuronal information processing. Here we investigate how particular features of network connectivity underpin the propensity of neural networks to generate slow-switching assembly (SSA) dynamics, i.e., sustained epochs of increased firing within assemblies of neurons which transition slowly between dif- ferent assemblies throughout the network. We show that the emergence of SSA activity is linked to spectral properties of the asymmetric synaptic weight matrix. In particular, the lead- ing eigenvalues that dictate the slow dynamics exhibit a gap with respect to the bulk of the spectrum, and the associated Schur vectors exhibit a measure of block-localization on groups of neurons, thus resulting in coherent dynamical activity on those groups. Through simple rate models, we gain analytical understanding of the origin and importance of the spectral gap, and use these insights to develop new network topologies with alternative connectivity paradigms which also display SSA activity. Specifically, SSA dynamics involv- ing excitatory and inhibitory neurons can be achieved by modifying the connectivity patterns between both types of neurons. We also show that SSA activity can occur at multiple time- scales reflecting a hierarchy in the connectivity, and demonstrate the emergence of SSA in small-world like networks. Our work provides a step towards understanding how network structure (uncovered through advancements in neuroanatomy and connectomics) can im- pact on spatio-temporal neural activity and constrain the resulting dynamics.</td>
</tr>
<tr id="bib_Schaub*2015" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub*2015,
    author = {Schaub*, Michael T. and Billeh*, Yazan and Anastassiou, Costas A. and Koch, Christof and Barahona, Mauricio},
           title = {Emergence of slow-switching assemblies in structured neuronal networks},
           journal = {PLoS Computational Biology},
           year = {2015},
           volume = {11},
           number = {7},
           pages = {e1004196},
           url = {https://arxiv.org/abs/1502.05656},
           doi = {10.1371/journal.pcbi.1004196}
}
    </pre></td>
</tr>
<tr id="Billeh*2014" class="entry">
    <td> [80] Billeh*, Y.N.; Schaub*, M.T.; Anastassiou, C.A.; Barahona, M. &amp; Koch, C. (2014), <i>"Revealing cell assemblies at multiple levels of granularity"</i>, Journal of Neuroscience Methods., October, 2014.  Vol. 236(0), pp. 92-106.
        <p class="infolinks">[<a href="javascript:toggleInfo('Billeh*2014','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Billeh*2014','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1016/j.jneumeth.2014.08.011" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1411.2103" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Billeh*2014" class="abstract noshow">
    <td><b>Abstract</b>: Background Current neuronal monitoring techniques, such as calcium imaging and multi-electrode arrays, enable recordings of spiking activity from hundreds of neurons simultaneously. Of primary importance in systems neuroscience is the identification of cell assemblies: groups of neurons that cooperate in some form within the recorded population. New method We introduce a simple, integrated framework for the detection of cell-assemblies from spiking data without a priori assumptions about the size or number of groups present. We define a biophysically-inspired measure to extract a directed functional connectivity matrix between both excitatory and inhibitory neurons based on their spiking history. The resulting network representation is analyzed using the Markov Stability framework, a graph theoretical method for community detection across scales, to reveal groups of neurons that are significantly related in the recorded time-series at different levels of granularity. Results and comparison with existing methods Using synthetic spike-trains, including simulated data from leaky-integrate-and-fire networks, our method is able to identify important patterns in the data such as hierarchical structure that are missed by other standard methods. We further apply the method to experimental data from retinal ganglion cells of mouse and salamander, in which we identify cell-groups that correspond to known functional types, and to hippocampal recordings from rats exploring a linear track, where we detect place cells with high fidelity. Conclusions We present a versatile method to detect neural assemblies in spiking data applicable across a spectrum of relevant scales that contributes to understanding spatio-temporal information gathered from systems neuroscience experiments.</td>
</tr>
<tr id="bib_Billeh*2014" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Billeh*2014,
    author = {Billeh*, Yazan N. and Schaub*, Michael T. and Anastassiou, Costas A. and Barahona, Mauricio and Koch, Christof},
           title = {Revealing cell assemblies at multiple levels of granularity},
           journal = {Journal of Neuroscience Methods},
           year = {2014},
           volume = {236},
           number = {0},
           pages = {92--106},
           url = {https://arxiv.org/abs/1411.2103},
           doi = {10.1016/j.jneumeth.2014.08.011}
}
    </pre></td>
</tr>
<tr id="Schaub2014" class="entry">
    <td> [81] Schaub, M.T.; Lehmann, J.; Yaliraki, S.N. &amp; Barahona, M. (2014), <i>"Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution"</i>, Network Science., April, 2014.  Vol. 2(1), pp. 66-89.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2014','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2014','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1017/nws.2014.4" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1303.6241" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2014" class="abstract noshow">
    <td><b>Abstract</b>: The analysis of complex networks has so far revolved mainly around the role of nodes and communities of nodes. However, the dynamics of interconnected systems is often focalized on edge processes, and a dual edge-centric perspective can often prove more natural. Here we present graph-theoretical measures to quantify edge-to-edge relations inspired by the notion of flow redistribution induced by edge failures. Our measures, which are related to the pseudo-inverse of the Laplacian of the network, are global and reveal the dynamical interplay between the edges of a network, including potentially non-local interactions. Our framework also allows us to define the embeddedness of an edge, a measure of how strongly an edge features in the weighted cuts of the network. We showcase the general applicability of our edge-centric framework through analyses of the Iberian power grid, traffic flow in road networks, and the C. elegans neuronal network.</td>
</tr>
<tr id="bib_Schaub2014" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2014,
    author = {Schaub, Michael T. and Lehmann, Jörg and Yaliraki, Sophia N. and Barahona, Mauricio},
           title = {Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution},
           journal = {Network Science},
           year = {2014},
           volume = {2},
           number = {1},
           pages = {66--89},
           url = {https://arxiv.org/abs/1303.6241},
           doi = {10.1017/nws.2014.4}
}
    </pre></td>
</tr>
<tr id="Delvenne2013" class="entry">
    <td> [82] Delvenne, J.-C.; Schaub, M.T.; Yaliraki, S.N. &amp; Barahona, M. (2013), <i>"The Stability of a Graph Partition: A Dynamics-Based Framework for Community Detection"</i>, In Dynamics On and Of Complex Networks, Volume 2., May, 2013. , pp. 221-242. Springer New York.
        <p class="infolinks"> [<a href="javascript:toggleInfo('Delvenne2013','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/978-1-4614-6729-8_11" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1308.1605" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="bib_Delvenne2013" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@incollection{Delvenne2013,
    author = {Delvenne, Jean-Charles and Schaub, Michael T. and Yaliraki, Sophia N. and Barahona, Mauricio},
           editor = {Mukherjee, Animesh and Choudhury, Monojit and Peruani, Fernando and Ganguly, Niloy and Mitra, Bivas},
           title = {The Stability of a Graph Partition: A Dynamics-Based Framework for Community Detection},
           booktitle = {Dynamics On and Of Complex Networks, Volume 2},
           publisher = {Springer New York},
           year = {2013},
           pages = {221--242},
           url = {https://arxiv.org/abs/1308.1605},
           doi = {10.1007/978-1-4614-6729-8_11}
}
    </pre></td>
</tr>
<tr id="Schaub2012b" class="entry">
    <td> [83] Schaub, M.T.; Lambiotte, R. &amp; Barahona, M. (2012), <i>"Encoding dynamics for multiscale community detection: Markov time sweeping for the map equation"</i>, Phys. Rev. E., August, 2012.  Vol. 86(2), pp. 026112. American Physical Society.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2012b','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2012b','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1103/PhysRevE.86.026112" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1109.6642" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2012b" class="abstract noshow">
    <td><b>Abstract</b>: The detection of community structure in networks is intimately related to finding a concise description of the network in terms of its modules. This notion has been recently exploited by the map equation formalism [ Rosvall and Bergstrom Proc. Natl. Acad. Sci. USA 105 1118 (2008)] through an information-theoretic description of the process of coding inter- and intracommunity transitions of a random walker in the network at stationarity. However, a thorough study of the relationship between the full Markov dynamics and the coding mechanism is still lacking. We show here that the original map coding scheme, which is both block-averaged and one-step, neglects the internal structure of the communities and introduces an upper scale, the "field-of-view" limit, in the communities it can detect. As a consequence, map is well tuned to detect clique-like communities but can lead to undesirable overpartitioning when communities are far from clique-like. We show that a signature of this behavior is a large compression gap: The map description length is far from its ideal limit. To address this issue, we propose a simple dynamic approach that introduces time explicitly into the map coding through the analysis of the weighted adjacency matrix of the time-dependent multistep transition matrix of the Markov process. The resulting Markov time sweeping induces a dynamical zooming across scales that can reveal (potentially multiscale) community structure above the field-of-view limit, with the relevant partitions indicated by a small compression gap.</td>
</tr>
<tr id="bib_Schaub2012b" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2012b,
    author = {Schaub, Michael T. and Lambiotte, Renaud and Barahona, Mauricio},
           title = {Encoding dynamics for multiscale community detection: Markov time sweeping for the map equation},
           journal = {Phys. Rev. E},
           publisher = {American Physical Society},
           year = {2012},
           volume = {86},
           number = {2},
           pages = {026112},
           url = {https://arxiv.org/abs/1109.6642},
           doi = {10.1103/PhysRevE.86.026112}
}
    </pre></td>
</tr>
<tr id="Schaub2012" class="entry">
    <td> [84] Schaub, M.T.; Delvenne, J.-C.; Yaliraki, S.N. &amp; Barahona, M. (2012), <i>"Markov Dynamics as a Zooming Lens for Multiscale Community Detection: Non Clique-Like Communities and the Field-of-View Limit"</i>, PLoS ONE., February, 2012.  Vol. 7(2), pp. e32210. Public Library of Science.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2012','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2012','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1371/journal.pone.0032210" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1109.5593" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2012" class="abstract noshow">
    <td><b>Abstract</b>: In recent years, there has been a surge of interest in community detection algorithms for complex networks. A variety of computational heuristics, some with a long history, have been proposed for the identification of communities or, alternatively, of good graph partitions. In most cases, the algorithms maximize a particular objective function, thereby finding the ‘right’ split into communities. Although a thorough comparison of algorithms is still lacking, there has been an effort to design benchmarks, i.e., random graph models with known community structure against which algorithms can be evaluated. However, popular community detection methods and benchmarks normally assume an implicit notion of community based on clique-like subgraphs, a form of community structure that is not always characteristic of real networks. Specifically, networks that emerge from geometric constraints can have natural non clique-like substructures with large effective diameters, which can be interpreted as long-range communities. In this work, we show that long-range communities escape detection by popular methods, which are blinded by a restricted "field-of-view" limit, an intrinsic upper scale on the communities they can detect. The field-of-view limit means that long-range communities tend to be overpartitioned. We show how by adopting a dynamical perspective towards community detection, in which the evolution of a Markov process on the graph is used as a zooming lens over the structure of the network at all scales, one can detect both clique- or non clique-like communities without imposing an upper scale to the detection. Consequently, the performance of algorithms on inherently low-diameter, clique-like benchmarks may not always be indicative of equally good results in real networks with local, sparser connectivity. We illustrate our ideas with constructive examples and through the analysis of real-world networks from imaging, protein structures and the power grid, where a multiscale structure of non clique-like communities is revealed.</td>
</tr>
<tr id="bib_Schaub2012" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2012,
    author = {Schaub, Michael T. and Delvenne, Jean-Charles and Yaliraki, Sophia N. and Barahona, Mauricio},
           title = {Markov Dynamics as a Zooming Lens for Multiscale Community Detection: Non Clique-Like Communities and the Field-of-View Limit},
           journal = {PLoS ONE},
           publisher = {Public Library of Science},
           year = {2012},
           volume = {7},
           number = {2},
           pages = {e32210},
           url = {https://arxiv.org/abs/1109.5593},
           doi = {10.1371/journal.pone.0032210}
}
    </pre></td>
</tr>
<tr id="Schaub2012a" class="entry">
    <td> [85] Schaub, M.T. &amp; Schultz, S. (2012), <i>"The Ising decoder: reading out the activity of large neural ensembles"</i>, Journal of Computational Neuroscience., February, 2012.  Vol. 32(1), pp. 101-118.
        <p class="infolinks">[<a href="javascript:toggleInfo('Schaub2012a','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2012a','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1007/s10827-011-0342-z" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1009.1828" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Schaub2012a" class="abstract noshow">
    <td><b>Abstract</b>: The Ising model has recently received much attention for the statistical description of neural spike train data. In this paper, we propose and demonstrate its use for building decoders capable of predicting, on a millisecond timescale, the stimulus represented by a pattern of neural activity. After fitting to a training dataset, the Ising decoder can be applied “online” for instantaneous decoding of test data. While such models can be fit exactly using Boltzmann learning, this approach rapidly becomes computationally intractable as neural ensemble size increases. We show that several approaches, including the Thouless–Anderson–Palmer (TAP) mean field approach from statistical physics, and the recently developed Minimum Probability Flow Learning (MPFL) algorithm, can be used for rapid inference of model parameters in large-scale neural ensembles. Use of the Ising model for decoding, unlike other problems such as functional connectivity estimation, requires estimation of the partition function. As this involves summation over all possible responses, this step can be limiting. Mean field approaches avoid this problem by providing an analytical expression for the partition function. We demonstrate these decoding techniques by applying them to simulated neural ensemble responses from a mouse visual cortex model, finding an improvement in decoder performance for a model with heterogeneous as opposed to homogeneous neural tuning and response properties. Our results demonstrate the practicality of using the Ising model to read out, or decode, spatial patterns of activity comprised of many hundreds of neurons.</td>
</tr>
<tr id="bib_Schaub2012a" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Schaub2012a,
    author = {Schaub, Michael T. and Schultz, Simon},
           title = {The Ising decoder: reading out the activity of large neural ensembles},
           journal = {Journal of Computational Neuroscience},
           year = {2012},
           volume = {32},
           number = {1},
           pages = {101--118},
           url = {https://arxiv.org/abs/1009.1828},
           doi = {10.1007/s10827-011-0342-z}
}
    </pre></td>
</tr>
</tbody>
</table>
<footer>
 <small>Created by <a href="http://jabref.sourceforge.net">JabRef</a> on 07/03/2025.</small>
</footer>
