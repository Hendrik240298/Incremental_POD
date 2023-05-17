# Incremental Proper Orthogonal Decomposition (iPOD) and its application to reduced order modeling (ROM)
## Hendrik Fischer, Julian Roth (2023)

This repository contains a straightforward prototype implementation of the incremental POD (trimmed version of the incremental truncated SVD) to demonstrate its use in reduced order modeling.

## iPOD


## iPOD for snapshot compression



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

We run this code from $t = 0 s$ until $t = 5 s$ and we note that the first revolution of the heat source is completed after 1 second. Therefore, we see in the temporal evolution of the POD basis size that the reduced basis only grows in the first second and then remains constant.

![heat_reduced_basis](https://github.com/Hendrik240298/Incremental_POD/blob/main/media/reduced_basis_heat.png)

We then see in the following video that our incremental reduced order solution is almost indistinguishable from the full order solution and the error is a few magnitudes smaller.

https://github.com/Hendrik240298/Incremental_POD/assets/42407091/60f13c69-f270-4518-8e07-ffeb660e3ab9
