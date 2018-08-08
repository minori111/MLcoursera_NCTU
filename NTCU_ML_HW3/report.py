# -*- coding: utf-8 -*-
"""
Created on Wed May 24 01:25:41 2017

@author: whisp
"""

Form Farkas' Lemma, either one of the following system has solutions but not both:
$(A)$
$$Ax \le 0, b^Tx>0$$
$(B)$
$$A^T\alpha = b, \alpha \ge 0,$$

We want to prove one of the following system has solutions but not both:
$(I)$
$$Bx<0$$
$(II)$
$$B^T\alpha = 0, \alpha \ge 0$$

Prove by the procedure
$$(I) \Rightarrow (A) \Rightarrow not (B) \Rightarrow not (II)$$
and
$$not (I) \Rightarrow not (A) \Rightarrow (B) \Rightarrow (II).$$

First part, we assume $(I)$ has a solution $x$.
By Hint1, we have $$Bx+1z\le 0$ for some $z \le 0.$
Let $A = [B z]$ and 
\begin{align*}
x' = 
\begin{bmatrix}
x\\
1
\end{bmatrix}.
\end{align*}

Then we get $$Ax' = Bx + 1z \le 0$$
and choose 
\begin{align*}
b = 
\begin{bmatrix}
O\\
1
\end{bmatrix}
\end{align*}
such that $b^Tx'>0$

By Farkas' Lemma, $$A^T\alpha'=b , \alpha' \ge 0$$ has no solution.

Suppose $(II)$ has a solution, then there exist a $\alpha \ge 0$ such that $B^T\alpha = 0$.
Then we have 
\begin{align*}
A^T\alpha = 
\begin{bmatrix}
B^T\\
z^T
\end{bmatrix}
\alpha = 
\begin{bmatrix}
B^T\alpha\\
z^T\alpha
\end{bmatrix}
=
\begin{bmatrix}
O\\
z^T\alpha
\end{bmatrix}
\ge O.
\end{align*}

By taking $\alpha' = \frac{\alpha}{z^T\alpha}$, 
we have $A^T\alpha' = b$ both has a solution and has no solution.
Therefore, we get a contradition.


For second part, we assume $(I)$ has no solution.
So the $$Ax' = Bx + 1z \le 0$$ has no solution for all $b$.
From Farkas' Lemma, $$A^T\alpha'=b , \alpha' \ge 0$$ has a solution.
In fact, taking 
\begin{align*}
b = 
\begin{bmatrix}
O\\
1
\end{bmatrix}
\end{align*}
agein, we have $\alpha$ satisfying
\begin{align*}
A^T\alpha = 
\begin{bmatrix}
B^T\\
z^T
\end{bmatrix}
\alpha = 
\begin{bmatrix}
B^T\alpha\\
z^T\alpha
\end{bmatrix}
=
\begin{bmatrix}
O\\
z^T\alpha
\end{bmatrix}
\ge O.
\end{align*}

Therefore, we have $B^T\alpha = 0$ and $\alpha \ge 0$ for such $\alpha$.
That is the $(II)$ has a solution.



