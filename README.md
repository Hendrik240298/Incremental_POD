# Incremental Proper Orthogonal Decomposition (iPOD) and its application to reduced order modeling (ROM)
### Hendrik Fischer, Julian Roth (2023)

This repository contains a straightforward prototype implementation of the incremental POD to demonstrate its use in reduced order modeling.

## The incremental POD algorithm

The implementation of the iPOD is based on our work [[1](https://doi.org/10.48550/arXiv.2304.01140)] and an excerpt of the algorithm is depicted below. 

![iPOD_algorithm](https://github.com/Hendrik240298/Incremental_POD/assets/75631613/e76d1f8f-5093-40b6-a737-948af63a5067)


## iPOD for reduced basis generation

The general idea of the incremental basis enrichment is to update the reduced basis whenever a new solution snapshot is available. Thus, we do not need to store all snapshots to build a basis, but can to it gradually with only the latest snapshot available. Leveraging this, we additionally introduce adaptive basis size determination and bunch updates. The latter bundles mutliple snapshots for one update to improve performance. For further information we refer to our works [[1](https://doi.org/10.48550/arXiv.2304.01140), [2](https://arxiv.org/abs/2302.09149)].

We demonstrate the capability of the iPOD for on-the-fly reduced basis generation on the example of the Navier-Stokes equations. We borrow the full-order model from the FEniCS Project's [incompressible NSE tutorial](https://fenicsproject.org/pub/tutorial/html/._ftut1009.html). 


## iPOD for reduced order modeling

For our incremental reduced order model we consider the heat equation: <br>
Find $u: [0,T] \times \bar\Omega \rightarrow \mathbb{R}$ such that

$$
\begin{aligned}
\partial_t u  - \Delta_x u &= f \quad \text{in} \quad (0,T) \times \Omega, \\
\qquad\qquad\quad  u &= 0 \quad \text{on} \quad (0,T) \times \partial\Omega, \\
\qquad\qquad  u &= u_0 \quad \text{on} \quad \lbrace 0 \rbrace \times \Omega,
\end{aligned}
$$

where $\Omega \subset \mathbb{R}^d$ with $d \in \lbrace 1, 2, 3 \rbrace$ is an open domain and the Laplacian of $u$, denoted by $\Delta_x u$, is defined as

$$
\Delta_x u = \sum_{i = 1}^d \partial_{x_i} u.
$$

More conretely, we use the model problem from Section 5.2 from the [MORe DWR paper](https://doi.org/10.48550/arXiv.2304.01140). 
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
#### iPOD basis generation for Navier-Stokes equations
https://github.com/Hendrik240298/Incremental_POD/assets/75631613/5c4e0a07-7e1e-4f90-9cb9-2c6116560efe

#### Incremental reduced order modeling for heat eqaution
We run this code from $t = 0 s$ until $t = 5 s$ and we note that the first revolution of the heat source is completed after 1 second. Therefore, we see in the temporal evolution of the POD basis size that the reduced basis only grows in the first second and then remains constant.

![heat_reduced_basis](https://github.com/Hendrik240298/Incremental_POD/blob/main/media/reduced_basis_heat.png)

We then see in the following video that our incremental reduced order solution is almost indistinguishable from the full order solution and the error is a few magnitudes smaller.

https://github.com/Hendrik240298/Incremental_POD/assets/42407091/60f13c69-f270-4518-8e07-ffeb660e3ab9



