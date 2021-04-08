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
<tr id="Yang2021" class="entry">
	<td> [1] Yang M, Isufi E, Schaub MT and Leus G (2021), <i>"Finite Impulse Response Filters for Simplicial Complexes"</i>, submitted. March, 2021.
	<p class="infolinks"> [<a href="javascript:toggleInfo('Yang2021','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2103.12587" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="bib_Yang2021" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Yang2021,
  author = {Maosheng Yang and Elvin Isufi and Michael T. Schaub and Geert Leus},
  title = {Finite Impulse Response Filters for Simplicial Complexes},
  booktitle = {Eusipco 2021},
  howpublished = {submitted},
  year = {2021},
  url = {https://arxiv.org/abs/2103.12587}
}
</pre></td>
</tr>
<tr id="Lambiotte2021" class="entry">
    <td> [2] Lambiotte, R. &amp; Schaub, M.T. (2021), <i>"Modularity and Dynamics on Complex Networks"</i>, March, 2021.  Cambridge University Press.
        <p class="infolinks"> [<a href="javascript:toggleInfo('Lambiotte2021','bibtex')">BibTeX</a>] [<a href="https://michaelschaub.github.io/ModularityAndDynamicsOnComplexNetworks.pdf" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="bib_Lambiotte2021" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@book{Lambiotte2021,
    author = {Renaud Lambiotte and Michael T. Schaub},
           title = {Modularity and Dynamics on Complex Networks},
           publisher = {Cambridge University Press},
           year = {2021},
           url = {https://michaelschaub.github.io/ModularityAndDynamicsOnComplexNetworks.pdf}
}
    </pre></td>
</tr>
<tr id="Klimm2021" class="entry">
	<td> [3] Klimm F, Jones NS and Schaub MT (2021), <i>"Modularity maximisation for graphons"</i>, submitted. January, 2021.
	<p class="infolinks">[<a href="javascript:toggleInfo('Klimm2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Klimm2021','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2101.00503" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Klimm2021" class="abstract noshow">
	<td><b>Abstract</b>: Networks are a widely-used tool to investigate the large-scale connectivity structure in complex systems and graphons have been proposed as an infinite size limit of dense networks. The detection of communities or other meso-scale structures is a prominent topic in network science as it allows the identification of functional building blocks in complex systems. When such building blocks may be present in graphons is an open question. In this paper, we define a graphon-modularity and demonstrate that it can be maximised to detect communities in graphons. We then investigate specific synthetic graphons and show that they may show a wide range of different community structures. We also reformulate the graphon-modularity maximisation as a continuous optimisation problem and so prove the optimal community structure or lack thereof for some graphons, something that is usually not possible for networks. Furthermore, we demonstrate that estimating a graphon from network data as an intermediate step can improve the detection of communities, in comparison with exclusively maximising the modularity of the network. While the choice of graphon-estimator may strongly influence the accord between the community structure of a network and its estimated graphon, we find that there is a substantial overlap if an appropriate estimator is used. Our study demonstrates that community detection for graphons is possible and may serve as a privacy-preserving way to cluster network data.</td>
</tr>
<tr id="bib_Klimm2021" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Klimm2021,
  author = {Florian Klimm and Nick S. Jones and Michael T. Schaub},
  title = {Modularity maximisation for graphons},
  howpublished = {submitted},
  year = {2021},
  url = {https://arxiv.org/abs/2101.00503}
}
</pre></td>
</tr>
<tr id="Schaub2021" class="entry">
	<td> [4] Schaub MT, Zhu Y, Seby J-B, Roddenberry TM and Segarra S (2021), <i>"Signal Processing on Higher-Order Networks: Livin' on the Edge ... and Beyond"</i>, submitted. January, 2021.
	<p class="infolinks">[<a href="javascript:toggleInfo('Schaub2021','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2021','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2101.05510" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Schaub2021" class="abstract noshow">
	<td><b>Abstract</b>: This tutorial paper presents a didactic treatment of the emerging topic of signal processing on higher-order networks. Drawing analogies from discrete and graph signal processing, we introduce the building blocks for processing data on simplicial complexes and hypergraphs, two common abstractions of higher-order networks that can incorporate polyadic relationships.We provide basic introductions to simplicial complexes and hypergraphs, making special emphasis on the concepts needed for processing signals on them. Leveraging these concepts, we discuss Fourier analysis, signal denoising, signal interpolation, node embeddings, and non-linear processing through neural networks in these two representations of polyadic relational structures. In the context of simplicial complexes, we specifically focus on signal processing using the Hodge Laplacian matrix, a multi-relational operator that leverages the special structure of simplicial complexes and generalizes desirable properties of the Laplacian matrix in graph signal processing. For hypergraphs, we present both matrix and tensor representations, and discuss the trade-offs in adopting one or the other. We also highlight limitations and potential research avenues, both to inform practitioners and to motivate the contribution of new researchers to the area.</td>
</tr>
<tr id="bib_Schaub2021" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Schaub2021,
  author = {Michael T. Schaub and Yu Zhu and Jean-Baptiste Seby and T. Mitchell Roddenberry and Santiago Segarra},
  title = {Signal Processing on Higher-Order Networks: Livin' on the Edge ... and Beyond},
  howpublished = {submitted},
  year = {2021},
  url = {https://arxiv.org/abs/2101.05510}
}
</pre></td>
</tr>
<tr id="Stamm2020" class="entry">
	<td> [5] Stamm FI, Neuhäuser L, Lemmerich F, Schaub MT and Strohmaier M (2020), <i>"Systematic edge uncertainty in attributed social networks and its effects on rankings of minority nodes"</i>, submitted. October, 2020.
	<p class="infolinks">[<a href="javascript:toggleInfo('Stamm2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Stamm2020','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2010.11546" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Stamm2020" class="abstract noshow">
	<td><b>Abstract</b>: Network analysis provides powerful tools to learn about a variety of social systems. However, most analyses implicitly assume that the considered data is error-free and reliable. Especially if the network consists of multiple groups, this assumption conflicts with the range of systematic reporting biases, measurement errors and other inaccuracies that are well documented in our community. In this paper, we model how such systematic uncertainty on edges of an attributed network can impact network analysis, in particular the ranking of nodes. We discuss how erroneous edge observations can be driven by external node attributes and the relative edge positions in the network, thereby opening a path towards a systematic study of the effects of edge-uncertainty for various network analysis tasks. To show how conclusions drawn from network analyses can get distorted due to such inaccuracies, we focus on the effects of edge-uncertainty on minority group representations in degree-based rankings. For that purpose, we analyze synthetic and real networks with varying homophily and group sizes. We find that introducing edge uncertainty can significantly alter the relative density of networks and result both in a strongly increased or decreased ranking of the minority, depending on the type of edge error and homophily. Our model enables researchers to include systematic edge-uncertainty in their analyses and thereby better account for the role of minorities in social networks.</td>
</tr>
<tr id="bib_Stamm2020" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Stamm2020,
  author = {Felix I. Stamm and Leonie Neuhäuser and Florian Lemmerich and Michael T. Schaub and Markus Strohmaier},
  title = {Systematic edge uncertainty in attributed social networks and its effects on rankings of minority nodes},
  howpublished = {submitted},
  year = {2020},
  url = {https://arxiv.org/abs/2010.11546}
}
</pre></td>
</tr>
<tr id="Peel2020" class="entry">
	<td> [6] Peel L and Schaub MT (2020), <i>"Detectability of hierarchical communities in networks"</i>, submitted. September, 2020.
	<p class="infolinks">[<a href="javascript:toggleInfo('Peel2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Peel2020','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2009.07525" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Peel2020" class="abstract noshow">
	<td><b>Abstract</b>: We study the problem of recovering a planted hierarchy of partitions in a network. The detectability of a single planted partition has previously been analysed in detail and a phase transition has been identified below which the partition cannot be detected. Here we show that, in the hierarchical setting, there exist additional phases in which the presence of multiple consistent partitions can either help or hinder detection. Accordingly, the detectability limit for non-hierarchical partitions typically provides insufficient information about the detectability of the complete hierarchical structure, as we highlight with several constructive examples.</td>
</tr>
<tr id="bib_Peel2020" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Peel2020,
  author = {Leto Peel and Michael T. Schaub},
  title = {Detectability of hierarchical communities in networks},
  howpublished = {submitted},
  year = {2020},
  url = {https://arxiv.org/abs/2009.07525}
}
</pre></td>
</tr>
<tr id="Schaub2020b" class="entry">
	<td> [7] Schaub MT and Peel L (2020), <i>"Hierarchical community structure in networks"</i>, submitted. September, 2020.
	<p class="infolinks">[<a href="javascript:toggleInfo('Schaub2020b','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Schaub2020b','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2009.07196" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Schaub2020b" class="abstract noshow">
	<td><b>Abstract</b>: Modular and hierarchical structures are pervasive in real-world complex systems. A great deal of effort has gone into trying to detect and study these structures. Important theoretical advances in the detection of modular, or "community", structures have included identifying fundamental limits of detectability by formally defining community structure using probabilistic generative models. Detecting hierarchical community structure introduces additional challenges alongside those inherited from community detection. Here we present a theoretical study on hierarchical community structure in networks, which has thus far not received the same rigorous attention. We address the following questions: 1)&nbsp;How should we define a valid hierarchy of communities? 2)&nbsp;How should we determine if a hierarchical structure exists in a network? and 3)&nbsp;how can we detect hierarchical structure efficiently? We approach these questions by introducing a definition of hierarchy based on the concept of stochastic externally equitable partitions and their relation to probabilistic models, such as the popular stochastic block model. We enumerate the challenges involved in detecting hierarchies and, by studying the spectral properties of hierarchical structure, present an efficient and principled method for detecting them.</td>
</tr>
<tr id="bib_Schaub2020b" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Schaub2020b,
  author = {Michael T. Schaub and Leto Peel},
  title = {Hierarchical community structure in networks},
  howpublished = {submitted},
  year = {2020},
  url = {https://arxiv.org/abs/2009.07196}
}
</pre></td>
</tr>
<tr id="Roddenberry2020" class="entry">
    <td> [8] Roddenberry, T.M.; Schaub, M.T.; Wai, H.-T. &amp; Segarra, S. (2020), <i>"Exact Blind Community Detection from Signals on Multiple Graphs"</i>, IEEE Transactions on Signal Processing., August, 2020. 
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
    <td> [9] Schaub, M.T.; Segarra, S. &amp; Tsitsiklis, J.N. (2020), <i>"Blind identification of stochastic block models from dynamical observations"</i>, SIAM Journal on Mathematics of Data Science., May, 2020.  Vol. 2(2), pp. 335-367.
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
    <td> [10] Schaub, M.T.; Benson, A.R.; Horn, P.; Lippner, G. &amp; Jadbabaie, A. (2020), <i>"Random walks on simplicial complexes and the normalized Hodge 1-Laplacian"</i>, SIAM Review., May, 2020.  Vol. 62(2), pp. 353-391.
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
<tr id="Faccin2020" class="entry">
	<td> [11] Faccin M, Schaub MT and Delvenne J-C (2020), <i>"State aggregations in Markov chains and block models of networks"</i>, submitted. May, 2020.
	<p class="infolinks">[<a href="javascript:toggleInfo('Faccin2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Faccin2020','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2005.00337" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Faccin2020" class="abstract noshow">
	<td><b>Abstract</b>: We consider state aggregation schemes for Markov chains from an information-theoretic perspective. Specifically, we consider aggregating the states of a Markov chain such that the mutual information of the aggregated states separated by T time steps is maximized. We show that for T = 1 this approach recovers the maximum-likelihood estimator of the degree-corrected stochastic block model as a particular case, thereby enabling us to explain certain features of the likelihood landscape of this popular generative network model from a dynamical lens. We further highlight how we can uncover coherent, long-range dynamical modules for which considering a time-scale T >> 1 is essential, using synthetic flows and real-world ocean currents, where we are able to recover the fundamental features of the surface currents of the Oceans.</td>
</tr>
<tr id="bib_Faccin2020" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Faccin2020,
  author = {Faccin, M. and Schaub, M. T. and Delvenne, J.-C.},
  title = {State aggregations in Markov chains and block models of networks},
  howpublished = {submitted},
  year = {2020},
  url = {https://arxiv.org/abs/2005.00337}
}
</pre></td>
</tr>
<tr id="Zhu2020" class="entry">
    <td> [12] Zhu, Y.; Schaub, M.T.; Jadbabaie, A. &amp; Segarra, S. (2020), <i>"Network Inference from Consensus Dynamics with Unknown Parameters"</i>, IEEE Transactions on Signal and Information Processing over Networks., April, 2020.  Vol. 6, pp. 300-315.
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
<tr id="Neuhaeuser2020" class="entry">
	<td> [13] Neuhäuser L, Schaub MT, Mellor A and Lambiotte R (2020), <i>"Opinion Dynamics with Multi-Body Interactions"</i>, submitted. April, 2020.
	<p class="infolinks">[<a href="javascript:toggleInfo('Neuhaeuser2020','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Neuhaeuser2020','bibtex')">BibTeX</a>] [<a href="https://arxiv.org/abs/2004.00901" target="_blank">URL</a>]</p>
	</td>
</tr>
<tr id="abs_Neuhaeuser2020" class="abstract noshow">
	<td><b>Abstract</b>: We introduce and analyse a three-body consensus model (3CM) for non-linear consensus dynamics on hypergraphs. Our model incorporates reinforcing group effects, which can cause shifts in the average state of the system even in if the underlying graph is complete (corresponding to a mean-field interaction), a phenomena that may be interpreted as a type of peer pressure. We further demonstrate that for systems with two clustered groups, already a small asymmetry in our dynamics can lead to the opinion of one group becoming clearly dominant. We show that the nonlinearity in the model is the essential ingredient to make such group dynamics appear, and demonstrate how our system can otherwise be written as a linear, pairwise interaction system on a rescaled network.</td>
</tr>
<tr id="bib_Neuhaeuser2020" class="bibtex noshow">
<td><b>BibTeX</b>:
<pre>
@misc{Neuhaeuser2020,
  author = {Neuhäuser, Leonie and Schaub, Michael T. and Mellor, Andrew and Lambiotte, Renaud},
  title = {Opinion Dynamics with Multi-Body Interactions},
  howpublished = {submitted},
  year = {2020},
  url = {https://arxiv.org/abs/2004.00901}
}
</pre></td>
</tr>
<tr id="Avella-Medina2020" class="entry">
    <td> [14] Avella-Medina, M.; Parise, F.; Schaub, M. &amp; Segarra, S. (2020), <i>"Centrality measures for graphons: Accounting for uncertainty in networks"</i>, IEEE Transactions on Network Science and Engineering., January, 2020.  Vol. 7(1), pp. 520-537.
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
    <td> [15] Rosvall, M.; Delvenne, J.-C.; Schaub, M.T. &amp; Lambiotte, R. (2019), <i>"Different Approaches to Community Detection"</i>, In Advances in Network Clustering and Blockmodeling., November, 2019. , pp. 105-119. John Wiley &amp; Sons, Ltd.
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
    <td> [16] Schaub, M.T.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2019), <i>"Structured Networks and Coarse-Grained Descriptions"</i>, In Advances in Network Clustering and Blockmodeling., November, 2019. , pp. 333-361. John Wiley &amp; Sons, Ltd.
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
    <td> [17] Jia, J.; Segarra, S.; Schaub, M.T. &amp; Benson, A.R. (2019), <i>"Graph-based Semi-Supervised &amp; Active Learning for Edge Flows"</i>, In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2019). New York, NY, USA, August, 2019. , pp. 761-771. ACM.
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
    <td> [18] Schaub, M.T.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2019), <i>"Multiscale Dynamical Embeddings of Complex Networks"</i>, Phys. Rev. E., June, 2019.  Vol. 99, pp. 062308. American Physical Society.
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
           pages = {062308},
           url = {https://arxiv.org/abs/1804.03733},
           doi = {10.1103/PhysRevE.99.062308}
}
    </pre></td>
</tr>
<tr id="Schaub2019" class="entry">
    <td> [19] Schaub, M.T.; Segarra, S. &amp; Wai, H. (2019), <i>"Spectral Partitioning of Time-varying Networks with Unobserved Edges"</i>, In 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2019)., May, 2019. , pp. 4938-4942.
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
    <td> [20] Schaub, M.T. &amp; Segarra, S. (2018), <i>"Flow Smoothing And Denoising: Graph Signal Processing In The Edge-space"</i>, In 2018 IEEE Global Conference on Signal and Information Processing (GlobalSIP)., November, 2018. , pp. 735-739.
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
    <td> [21] Benson, A.R.; Abebe, R.; Schaub, M.T.; Jadbabaie, A. &amp; Kleinberg, J. (2018), <i>"Simplicial closure and higher-order link prediction"</i>, Proceedings of the National Academy of Sciences., November, 2018.  Vol. 115(48), pp. E11221-E11230.
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
    <td> [22] Billeh, Y.N. &amp; Schaub, M.T. (2018), <i>"Feedforward architectures driven by inhibitory interaction patterns"</i>, Journal of Computational Neuroscience., February, 2018.  Vol. 44(1), pp. 63-74.
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
    <td> [23] Segarra, S.; Schaub, M.T. &amp; Jadbabaie, A. (2017), <i>"Network Inference from Consensus Dynamics"</i>, 56th IEEE Conference on Decision and Control (CDC 2017)., December, 2017. , pp. 3212-3217.
        <p class="infolinks">[<a href="javascript:toggleInfo('Segarra2017','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Segarra2017','bibtex')">BibTeX</a>] [<a href="https://doi.org/10.1109/CDC.2017.8264130" target="_blank">DOI</a>] [<a href="https://arxiv.org/abs/1708.05329" target="_blank">URL</a>]</p>
    </td>
</tr>
<tr id="abs_Segarra2017" class="abstract noshow">
    <td><b>Abstract</b>: We consider the problem of identifying the topology of a weighted, undirected network G from observing snapshots of multiple independent consensus dynamics. Specifically, we observe the opinion profiles of a group of agents for a set of M independent topics and our goal is to recover the precise relationships between the agents, as specified by the unknown network G. In order to overcome the under- determinacy of the problem at hand, we leverage concepts from spectral graph theory and convex optimization to unveil the underlying network structure. More precisely, we formulate the network inference problem as a convex optimization that seeks to endow the network with certain desired properties – such as sparsity – while being consistent with the spectral information extracted from the observed opinions. This is complemented with theoretical results proving consistency as the number M of topics grows large. We further illustrate our method by numerical experiments, which showcase the effectiveness of the technique in recovering synthetic and real-world networks.</td>
</tr>
<tr id="bib_Segarra2017" class="bibtex noshow">
    <td><b>BibTeX</b>:
        <pre>
@article{Segarra2017,
    author = {Segarra, Santiago and Schaub, Michael T. and Jadbabaie, Ali},
           title = {Network Inference from Consensus Dynamics},
           journal = {56th IEEE Conference on Decision and Control (CDC 2017)},
           year = {2017},
           pages = {3212--3217},
           url = {https://arxiv.org/abs/1708.05329},
           doi = {10.1109/CDC.2017.8264130}
}
    </pre></td>
</tr>
<tr id="Faccin2017" class="entry">
    <td> [24] Faccin, M.; Schaub, M.T. &amp; Delvenne, J.-C. (2017), <i>"Entrograms and coarse graining of dynamics on complex networks"</i>, Journal of Complex Networks., November, 2017. , pp. cnx055.
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
    <td> [25] Estrada, E.; Delvenne, J.-C.; Hatano, N.; Mateos, J.L.; Metzler, R.; Riascos, A.P. &amp; Schaub, M.T. (2017), <i>"Random Multi-Hopper Model. Super-Fast Random Walks on Graphs"</i>, Journal of Complex Networks., October, 2017. , pp. cnx043.
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
    <td> [26] Schaub*, M.T.; Trefois*, M.; Dooren, P.V. &amp; Delvenne, J.-C. (2017), <i>"Sparse Matrix Factorizations For Fast Iterative Linear Solvers With Application To Laplacian Systems"</i>, SIAM Journal on Matrix Analysis and Applications., June, 2017.  Vol. 38(2), pp. 505-529.
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
    <td> [27] Kiselev, V.Y.; Kirschner, K.; Schaub, M.T.; Andrews, T.; Chandra, T.; Natarajan, K.N.; Reik, W.; Barahona, M.; Green, A.R. &amp; Hemberg, M. (2017), <i>"SC3 - consensus clustering of single-cell RNA-Seq data"</i>, Nature Methods., March, 2017.  Vol. 14(5), pp. 483-486.
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
    <td> [28] Schaub, M.T.; Delvenne, J.-C.; Rosvall, M. &amp; Lambiotte, R. (2017), <i>"The many facets of community detection in complex networks"</i>, Applied Network Science., February, 2017.  Vol. 2(1), pp. 4.
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
    <td> [29] Bacik, K.A.; Schaub, M.T.; Beguerisse-Diaz, M.; Billeh, Y.N. &amp; Barahona, M. (2016), <i>"Flow-Based Network Analysis of the Caenorhabditis elegans Connectome"</i>, PLoS Computational Biology., August, 2016.  Vol. 12(8), pp. 1-27.
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
    <td> [30] Schaub, M.T.; O'Clery, N.; Billeh, Y.N.; Delvenne, J.-C.; Lambiotte, R. &amp; Barahona, M. (2016), <i>"Graph partitions and cluster synchronization in networks of oscillators"</i>, Chaos., August, 2016.  Vol. 26(9), pp. 094821.
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
    <td> [31] Amor, B.R.C.; Schaub, M.T.; Yaliraki, S.N. &amp; Barahona, M. (2016), <i>"Prediction of allosteric sites and mediating interactions through bond-to-bond propensities"</i>, Nature Communications., August, 2016.  Vol. 7(12477)
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
    <td> [32] Salnikov, V.; Schaub, M.T. &amp; Lambiotte, R. (2016), <i>"Using higher-order Markov models to reveal flow-based communities in networks"</i>, Scientific Reports., March, 2016.  Vol. 6, pp. 23194.
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
    <td> [33] Schaub*, M.T.; Billeh*, Y.; Anastassiou, C.A.; Koch, C. &amp; Barahona, M. (2015), <i>"Emergence of slow-switching assemblies in structured neuronal networks"</i>, PLoS Computational Biology., July, 2015.  Vol. 11(7), pp. e1004196.
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
    <td> [34] Billeh*, Y.N.; Schaub*, M.T.; Anastassiou, C.A.; Barahona, M. &amp; Koch, C. (2014), <i>"Revealing cell assemblies at multiple levels of granularity"</i>, Journal of Neuroscience Methods., October, 2014.  Vol. 236(0), pp. 92-106.
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
    <td> [35] Schaub, M.T.; Lehmann, J.; Yaliraki, S.N. &amp; Barahona, M. (2014), <i>"Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution"</i>, Network Science., April, 2014.  Vol. 2(1), pp. 66-89.
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
    <td> [36] Delvenne, J.-C.; Schaub, M.T.; Yaliraki, S.N. &amp; Barahona, M. (2013), <i>"The Stability of a Graph Partition: A Dynamics-Based Framework for Community Detection"</i>, In Dynamics On and Of Complex Networks, Volume 2., May, 2013. , pp. 221-242. Springer New York.
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
    <td> [37] Schaub, M.T.; Lambiotte, R. &amp; Barahona, M. (2012), <i>"Encoding dynamics for multiscale community detection: Markov time sweeping for the map equation"</i>, Phys. Rev. E., August, 2012.  Vol. 86(2), pp. 026112. American Physical Society.
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
    <td> [38] Schaub, M.T.; Delvenne, J.-C.; Yaliraki, S.N. &amp; Barahona, M. (2012), <i>"Markov Dynamics as a Zooming Lens for Multiscale Community Detection: Non Clique-Like Communities and the Field-of-View Limit"</i>, PLoS ONE., February, 2012.  Vol. 7(2), pp. e32210. Public Library of Science.
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
    <td> [39] Schaub, M. &amp; Schultz, S. (2012), <i>"The Ising decoder: reading out the activity of large neural ensembles"</i>, Journal of Computational Neuroscience., February, 2012.  Vol. 32(1), pp. 101-118.
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
    author = {Schaub, Michael and Schultz, Simon},
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
 <small>Created by <a href="http://jabref.sourceforge.net">JabRef</a> on 08/04/2021.</small>
</footer>
