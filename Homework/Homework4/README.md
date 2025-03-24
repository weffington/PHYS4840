# Problem 1
A quadradic curve is given by the following equation:
$$y=ax^2+bx+c.$$
So, in order to fit such a curve, we need three sample points. The central difference scheme works best when such points are placed symmetrically around some point $x$. Now, suppose we want to find the derivative at the point $x=0$. We can then place our three points at $x=-h$, $x=0$, and $x=h$. We want our quadratic equation to be equal to our three points at each x-value. Thus, we have $$ah^2-bh+c=f(-h),\ c=f(0),\ ah^2+bh+c=f(h),$$ for $x=-h$, $x=0$, and $x=h$ respectively. For an arbitrary quadratic curve, the derivative at $x=0$ is 
$$\frac{dy}{dx}=[2ax+b]_{x=0}=b.$$
Now, notice that 
$$2bh = f(h)-f(-h).$$
So, at $x=0$,
$$\frac{df}{dx} \approxeq \frac{dy}{dx} = \frac{f(h)-f(-h)}{2h}.$$
Therefore, the approximate derivative of $f(x)$ at any value of $x$ will be
$$\frac{df}{dx} \approxeq \frac{f(x+h)-f(x-h)}{2h}.$$
However, this is the exact same formula that we obtained for a central difference scheme using a linear function, giving us no improvement in our error order, despite using a higher-order approximation.
# Problem 2
## b)
Taking the derivative of $x^{a-1}e^{-x}$ gives $$(a-1)x^{a-2}e^{-x}-x^{a-1}e^{-x}.$$
Factoring out $e^{-x}$ and $x^{a-2}$ then gives $$x^{a-2}((a-1)-x)e^{-x}.$$ Setting this equation equation equal to $0$ and dividing through by $e^{-x}$ gives $$x^{a-2}((a-1)-x)=0.$$
We therefore have maximums and minimums at $x=0$ and $x=a-1$. At $x=0$, $$x^{a-1}e^{-x}=0.$$ At $x=a-1$, $$x^{a-1}e^{-x}=(a-1)^{a-1}e^{1-a}.$$
Therefore, the maximum of the integrand will be at $x=a-1$.

## c)
Setting $z=\frac{1}{2}$ gives that
$$\frac{1}{2}=\frac{x}{c+x}.$$
Solving this equation for $x$ gives that $x=c$. Now, since we want the maximum of the integrand to be at $z=\frac{1}{2}$, we should set $c=a-1$, since the maximum of the integrand is at $x=a-1$. We therefore obtain a change of variables in the form
$$x=\frac{(a-1)z}{1-z}.$$

## d)
If we write
$$x^{a-1}=e^{(a-1)\ln{x}},$$
then the integrand becomes
$$e^{(a-1)\ln{x}}*e^{-x}.$$
Using laws of exponents, we can then write the integrand as
$$e^{(a-1)\ln{x}-x}.$$

# Problem 3
## 1.
A property of real matrices is that, for some matrix $A$ and vectors $\textbf{v}$ and $\textbf{b}$, the equation $A\textbf{v}=\textbf{b}$ has a unique solution if and only if $\det{A} \neq 0$. For this problem's particular matrix, its determinant is 14.
Thus, our system of linear equations in this problem does in fact have a unique solution.

# Problem 4
Interpolation is used for fitting a curve to some data points, whereas numerical differentiation seeks to approximate the derivative at these data points. To go into more detail, numerical interpolation seeks to find some continuous function (linear, quadratic, etc.) that passes through each discrete data point, allowing us to approximate values in between each data point. Numerical differentiation however seeks to approximate the derivative at some data point given an arbitrary set of points. So, while both use similar mathematical methods, they ultimately accomplish different things.
