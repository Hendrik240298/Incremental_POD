# Incremental Proper Orthogonal Decomposition (iPOD) and its application to reduced order modeling (ROM)
### Hendrik Fischer & Julian Roth (2023)

This repository contains a straightforward prototype implementation of the incremental POD to demonstrate its use in reduced order modeling.

## The incremental POD algorithm

The implementation of the iPOD is based on our [MORe DWR paper](https://doi.org/10.48550/arXiv.2304.01140), which is mainly influenced by the work of [Kühl et al.](https://arxiv.org/abs/2302.09149) An excerpt of the algorithm is depicted below. 

![iPOD_algorithm](https://github.com/Hendrik240298/Incremental_POD/assets/75631613/de8601e9-9644-4f65-89c8-1a692fc2541f)

## iPOD for reduced basis generation

The general idea of the incremental basis enrichment is to update the reduced basis whenever a new solution snapshot is available. Thus, we do not need to store all snapshots to build a basis, but can to it gradually with only the latest snapshot available. Leveraging this, we additionally introduce adaptive basis size determination and bunch updates. The latter bundles multiple snapshots for one update to improve performance. For further information, we refer to our work [Fischer et al.](https://doi.org/10.48550/arXiv.2304.01140) and to [Kühl et al.](https://arxiv.org/abs/2302.09149). Especially for an in-depth discussion of the algorithm and its parallelization, we refer to the latter.

We demonstrate the capability of the iPOD for on-the-fly reduced basis generation on the example of the Navier-Stokes equations. We borrow the full-order model from the FEniCS Project's [incompressible NSE tutorial](https://fenicsproject.org/pub/tutorial/html/._ftut1009.html). 

### Executing the code
The easiest way to run this Jupyter Notebook is to use Google Colab. To open the notebook in Google Colab you can click on "iPOD_RB_generation.ipynb" and replace the word 'github' in the url with 'githubtocolab' or you can click on [this link](https://colab.research.google.com/github/Hendrik240298/Incremental_POD/blob/main/iPOD_RB_generation.ipynb).

### Results

<img src="media/navier-stokes.gif" alt="navier-stokes"/>

## iPOD for reduced order modeling

For our incremental reduced order model we consider the heat equation problem from Section 5.2 from the [MORe DWR paper](https://doi.org/10.48550/arXiv.2304.01140). 
We have the domain $\Omega = (0,1) \times (0,1)$, homogeneous Dirichlet boundary conditions and initial conditions

$$
\begin{aligned}
u(0,x) &= 0 \qquad \forall x \in \Omega, \\
u(t,x) &= 0 \qquad \forall x \in \partial \Omega,
\end{aligned}
$$

and the right hand side function

$$
f(t, x) := \begin{cases}
        \sin(4 \pi t)  & \text{if } (x_1 - p_1)^2 + (x_2 - p_2)^2 < r^2,\\
        0 & \text{else},
    \end{cases}
$$

with $x = (x_1, x_2)$, midpoint $p = (p_1, p_2) = (\frac{1}{2}+\frac{1}{4} \cos(2 \pi t), \frac{1}{2}+\frac{1}{4} \sin(2 \pi t))$ and radius of the trajectory $r=0.125$.


### Executing the code
The easiest way to run this Jupyter Notebook is to use Google Colab. To open the notebook in Google Colab you can click on "iPOD_ROM.ipynb" and replace the word 'github' in the url with 'githubtocolab' or you can click on [this link](https://colab.research.google.com/github/Hendrik240298/Incremental_POD/blob/main/iPOD_ROM.ipynb).

### Results
We run this code from $t = 0 s$ until $t = 5 s$ and we note that the first revolution of the heat source is completed after 1 second. Therefore, we see in the temporal evolution of the POD basis size that the reduced basis only grows in the first second and then remains constant.

![heat_reduced_basis](https://github.com/Hendrik240298/Incremental_POD/blob/main/media/reduced_basis_heat.png)

We then see in the following video that our incremental reduced order solution is almost indistinguishable from the full order solution and the error is a few magnitudes smaller.

<img src="media/heat.gif" alt="heat"/>

## Citation

    @article{kuhl2024incremental,
        title = {An {I}ncremental {S}ingular {V}alue {D}ecomposition {A}pproach for {L}arge-{S}cale {S}patially {P}arallel \& {D}istributed but {T}emporally {S}erial {D}ata--{A}pplied to {T}echnical {F}lows},
        journal = {Comput. Phys. Commun.},
        volume = {296},
        pages = {109022},
        year = {2024},
        issn = {0010-4655},
        doi = {https://doi.org/10.1016/j.cpc.2023.109022},
        author = {Niklas K{\"u}hl and Hendrik Fischer and Michael Hinze and Thomas Rung},    
    }

    @article{FiRoWiChaFau2024,
        title = {{MORe} {DWR}: {Space}-time goal-oriented error control for incremental {POD}-based {ROM} for time-averaged goal functionals},
        journal = {J. Comput. Phys.},
        volume = {504},
        pages = {112863},
        year = {2024},
        issn = {0021-9991},
        doi = {https://doi.org/10.1016/j.jcp.2024.112863},
        author = {Hendrik Fischer and Julian Roth and Thomas Wick and Ludovic Chamoin and Amelie Fau},
    }

## Contact

Should you have any questions do not hesitate to send us an email at

    fischer@ifam.uni-hannover.de
    roth@ifam.uni-hannover.de
    
## Acknowledgements

This work arises from the [Scientific Computing Group](https://www.ifam.uni-hannover.de/en/research/scientific-computing) headed by [Professor Thomas Wick](https://thomaswick.org) at the Institute of Applied Mathematics at the [Leibniz University Hannover](https://www.uni-hannover.de/en/). In addition to internal support and resources, we acknowledge the funding of the German Research Foundation (DFG) within the framework of the [International Research Training Group on Computational Mechanics Techniques in High Dimensions GRK 2657](https://www.irtg2657.uni-hannover.de/en/) under Grant Number 433082294. 
In addition, Hendrik Fischer acknowledges the collaboration with the [Institute for Fluid Dynamics and Ship Theory](https://www.tuhh.de/fds/home/) at the [Hamburg University of Technology (TUHH)](https://www.tuhh.de/tuhh/en/tu-hamburg).
