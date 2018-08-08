# NTCU_ML_HW3
https://hackmd.io/s/BkBUv1fbW
# 機器學習 HW03
##  104021615 黃翊軒
### Document
[ML_Homework3_2017](https://github.com/minori111/NTCU_ML_HW3/blob/master/ML-HW3-2017.pdf)
[NTCU_ML_HW3 github](https://github.com/minori111/NTCU_ML_HW3)

## Q1.
> Given $x$, $y$ in $F= \{x| g(x)\le 0, h(x)=0 \}$, we have
> $$g(tx+(1-t)y)\le tg(x)+(1-t)g(y)\le t\cdot 0+ (1-t)\cdot 0 = 0$$
> and $$h(tx+(1-t)y)= th(x)+(1-t)h(y)= t\cdot 0+ (1-t)\cdot 0 = 0$$
> for $t \in [0,1]$.
> Therefore $F$ is a convex set.

## Q2.
> Form Farkas' Lemma, either one of the following system has solutions but not both:
$(A)$
$$Ax \le 0, b^Tx>0$$
$(B)$
$$A^T\alpha = b, \alpha \ge 0,$$

> We want to prove one of the following system has solutions but not both:
$(I)$
$$Bx<0$$
$(II)$
$$B^T\alpha = 0, \alpha \ge 0$$

> Prove by the procedure
$$(I) \Rightarrow (A) \Rightarrow not (B) \Rightarrow not (II)$$
and
$$not (I) \Rightarrow not (A) \Rightarrow (B) \Rightarrow (II).$$

> First part, we assume $(I)$ has a solution $x$.
By Hint1, we have $$Bx+1z\le 0$ for some $z \le 0.$
Let $A = [B z]$ and 
\begin{align*}
x' = 
\begin{bmatrix}
x\\
1
\end{bmatrix}.
\end{align*}

> Suppose $(II)$ has a solution, then there exist a $\alpha \ge 0$ such that $B^T\alpha = 0$.
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

> By taking $\alpha' = \frac{\alpha}{z^T\alpha}$, 
we have $A^T\alpha' = b$ both has a solution and has no solution.
Therefore, we get a contradition.

> For second part, we assume $(I)$ has no solution.
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
agein, we have a $\alpha$ satisfying
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

> Therefore, we have $B^T\alpha = 0$ and $\alpha \ge 0$ for such $\alpha$.
That is the $(II)$ has a solution.


## Q3.
- [problem_3](https://github.com/minori111/NTCU_ML_HW3/blob/master/problem_3.pdf)
## Q4.
- [problem_4](https://github.com/minori111/NTCU_ML_HW3/blob/master/problem_4.pdf)
