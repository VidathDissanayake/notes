# Differential Equations (DE)

> Vidath Dissanayake | Sri Lanka  
> Tags: #courses #courses/PreEng 
> Links: [Engineering Foundation](Engineering%20Foundation.md)
> Sources: [Order, Degree and Variable Separation](https://us02web.zoom.us/rec/play/-WTSWq4wu0MDXiMTREDZgPiLSoODnD5C8MAjudq1OV-G7WNKwINiayTuvrHP1OepRGsl4zui54DYYeOf.nReKNBv80Z_42dFm?hasValidToken=false&canPlayFromShare=true&from=share_recording_detail&startTime=1718449615000&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus02web.zoom.us%2Frec%2Fshare%2FcyVAJuHBIXRCiRDH6J8HZot03KjjNWRCwREirG2zXA3g_NTrqDphY6wS5eEAmBzt.OEaPQ5cDCObjmuft%3FstartTime%3D1718449615000)  [DE2 - Homogeneous and Linear Dirrerential Equations](https://us02web.zoom.us/rec/play/CmaF8PzfwHMUThioSGcS6w7cf6giMuw4pI1slWa-kZkGd3iZuwovxkPyOzVSN7IacYyeGN80wb6C2Yg.pJjgEUjmlTUt3dbM?hasValidToken=false&canPlayFromShare=true&from=share_recording_detail&startTime=1719054065000&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus02web.zoom.us%2Frec%2Fshare%2FSNV4d9mKr_kxiBd1g2Rpz4py2GHuTcFQb139yXR82Xqd8H6_CHxhqPsoWmANeFwo.y-kPz38EyjDftV34%3FstartTime%3D1719054065000%26authuser%3D0)

---

Differentiation and integration are inverse functions.

In A/L, we discuss Single Variable (Ordinary) calculus.

## Tutes

![DifferentialEquation HK Dass Chapter 3](assets/documents/DifferentialEquation%20HK%20Dass%20Chapter%203.pdf)

![classification of calculus](assets/images/classification%20of%20calculus.png) 


## Terminology

- Single variable functions - Functions consisting of a single variable. 
    - E.g: $y=f(x)$ 
- Multi variable functions - Functions consisting of multiple variables. 
    - E.g: $y=f(x_{1}, x_{2}, x_{3}, ...)$  
- Independent variable - The variable that does not depend on others. Usually $x$. The variable we change at will.
- Dependant variable - The variable that depends on the independent variable.
- Differential Coefficient/Derivatives - E.g: $\frac{\text{d}y}{\text{d}x}$ (Differentiation of $y$ with respect to $x$ / Derivative of $y$ w.r.t. $x$.)
- $\frac{\text{d}^2y}{\text{d}x^{2}}$  - Second order derivative of $y$ w.r.t. $x$ / Second derivative of $y$ w.r.t. $x$.

## Definition

An equation containing differential coefficients is known as a differential equation (DE).

## Formation of Differential Equations

Differential equations are obtained by differentiating ordinary equations and eliminating arbitrary constants.

E.g: 
1. $$\begin{gather}
y=e^{x}\sin{x} \longleftarrow \text{Equation} \\ 
\frac{\text{d}y}{\text{d}x}=e^{x}\cos{x}+e^{x}\sin{x} \\
\frac{\text{d}y}{\text{d}x}=e^{x}\cos{x}+y \longleftarrow \text{DE}\\
\frac{\text{d}^{2}y}{\text{d}x^{2}}=\left[-e^{x}\sin{x}+e^{x}\cos{x}\right]+\frac{\text{d}y}{\text{d}x} \\
\frac{d^{2}y}{\text{d}x^{2}}=\left[-y+\frac{\text{d}y}{\text{d}x}-y\right]+\frac{\text{d}y}{\text{d}x} \\
\frac{\text{d}^{2}y}{\text{d}x^{2}}-2\frac{\text{d}y}{\text{d}x}+2y=0 \longleftarrow \text{DE}
\end{gather}$$
2. $$\begin{gather}
y=A\sin{x}+B\cos{x} \longleftarrow \text{Equation} \\
\frac{\text{d}y}{\text{d}x}=A\cos{x}-B\sin{x} \\
\frac{\text{d}^{2}y}{\text{d}x^{2}}= -A\sin{x}-B\cos{x} \\
\frac{\text{d}^{2}y}{\text{d}x^{2}}+y=0 \longleftarrow \text{DE}
\end{gather}$$

## Properties of Differential Equations

### Order

The order of the highest differential coefficient is called the order of the DE.

### Degree

The degree of the highest differential coefficient after removing the radical signs and fractions of the dependent variable is called the degree of the DE.

E.g: 
- $\left(\frac{\text{d}^{2}y}{\text{d}x^{2}}\right)^3+x\left(\frac{\text{d}y}{\text{d}x}\right)^5+\sin{xy}=5x$ (order=2, degree=3)
- $\left(\frac{\text{d}^{2}y}{\text{d}x^{2}}\right)^3+\left(\frac{\text{d}y}{\text{d}x}\right)^\frac{5}{2}=+y=13$ (order=2, degree=6)
- $\left(\frac{\text{d}^{2}y}{\text{d}x^{2}}+\frac{\text{d}y}{\text{d}x}\right)^2+y^\frac{5}{3}=3$ (order=2, degree=6)
- $\frac{\text{d}^{2}y}{\text{d}x^{2}}+\frac{\text{d}y}{\text{d}x}=\sqrt{\sin{x}}$ (order=2, degree=1)

## Solving Differential Equations

The process of obtaining an equation without containing derivatives from a DE is known as solving the DE. The obtained ordinary equation is known as the **solution** of the differential equation.

The solution satisfies the DE.

The number of arbitrary constants present in the solution is equal to the order of the DE.

The method of obtaining the solution is an integration involving process. Depending on the DE, various techniques (symbolic, numerical) are used.

A differential equation of the form  $\frac{d^{n}y}{\text{d}x^{n}}=f{x}$ can be solved by repeated integration.

E.g:
1. $$\begin{gather}\frac{\text{d}^{2}y}{\text{d}x^{2}}=x^2 \\
\frac{\text{d}y}{\text{d}x}=\frac{x^3}{3}+A \\
y=\frac{x^4}{12}+Ax+B
\end{gather}$$
2. $$\begin{gather}
y\frac{\text{d}y}{\text{d}x}=\cos{2x} \\
y^2=\sin{2x}+C
\end{gather}$$


## First Order Differential Equations

Depending on $F(x,y)$ various methods are used to solve the DE

1. Variable Separable
2. Homogeneous
3. Linear Differential Equations
4. Exact

### 1. Variable Separable

A DE of the form $\frac{\text{d}y}{\text{d}x}=\frac{f(x)}{g(y)}$ can be solved by separating variables and integration.

E.g:
1. $$\begin{gather}
\frac{1}{y}\frac{\text{d}y}{\text{d}x}=\cos{2x}\\
\frac{1}{y}\text{d}y=\cos{2x}\ \text{d}x\\
\int\frac{1}{y}\text{d}y=\int\cos{2x}\ \text{d}x\\
\ln{|y|}+C_1=\frac{\sin{2x}}{2}+C_2\\
\ln{|y|}=\frac{\sin{2x}}{2}+C\\
y=Ae^\frac{\sin{2x}}{2}\\
\text{where A is an arbitrary constant}
\end{gather}$$
2. $$\begin{gather}
\frac{\text{d}y}{\text{d}x}=\frac{x(y^2+1)}{x+1}\\
(y^2+1)\text{d}y=\frac{x}{x+1}\text{d}x\\
\int(y^2+1)\text{d}y=\int1-\frac{1}{x+1}\text{d}x\\
\tan^{-1}{y}=x-\ln{|x+1|}+C
\end{gather}$$
3. $$\begin{gather}
(xy^2+x)\text{d}x+(x^2y+y)\text{d}y=0\\
x(y^2+1)\text{d}x=-y(x^2+1)\text{d}y\\
\frac{x}{x^2+1}\text{d}x=-\frac{y}{y^2+1}\text{d}y\\
\int\frac{x}{x^2+1}\text{d}x=-\int\frac{y}{y^2+1}\text{d}y\\
\frac{1}{2}\ln{|x^2+1|}=-\frac{1}{2}\ln{|y^2+1|}+\frac{1}{2}\ln{|C|}\\
(x^2+1)(y^2+1)=C
\end{gather}$$
4. $$\begin{gather}
x\frac{\text{d}y}{\text{d}x}+\cot{y}=0\\
x\frac{\text{d}y}{\text{d}x}=-\cot{y}\\
\tan{y}\ \text{d}y=-\frac{1}{x}\text{d}x\\
\int\tan{y}\ \text{d}y=-\int\frac{1}{x}\text{d}x\\
-\ln{|\cos{y}|}=-\ln{|x|}-\ln{|C|}\\
\cos{y}=Cx\\\\
\text{when } x=\frac{1}{\sqrt{2}}, y=\frac{\pi}{4}\\\\
\cos{\frac{\pi}{4}}=C\frac{1}{\sqrt{2}}\implies C=1\\
\therefore{1}{\sqrt{2}}, y=\frac{\pi}{4}\\\\
\cos{\frac{\pi}{4}}=C\frac{1}{\sqrt{2}}\implies C=1\\
\therefore \text{Solution is } \cos{y}=x
\end{gather}$$

####  Reducible to Variable Separable

A differential equation of the form,
$$\frac{\text{d}y}{\text{d}x}=f(ax+by+c)$$
 can be reduced to variable separable by substituting $$z=ax+by+c$$
E.g: 
1. $$\begin{gather}
\frac{\text{d}y}{\text{d}x}=\sec(x+y)\\\\
\text{Sub: } z=x+y;\ \ \ \frac{dz}{\text{d}x}=1+\frac{\text{d}y}{\text{d}x}\\\\
\frac{dz}{\text{d}x}-1=\sec{z}\\
\frac{dz}{\text{d}x}=1+\sec{z}\\
\frac{dz}{\text{d}x}=\frac{1+\cos{z}}{\cos{z}}\\
\frac{\cos{z}}{1+\cos{z}}dz=\text{d}x\\
\left(1-\frac{1}{1+\cos{z}}\right)dz=\text{d}x\\
\left(1-\frac{1}{2\cos^2{\frac{z}{2}}}\right)dz=\text{d}x\\
\int\left(1-\frac{1}{2}\sec^2{\frac{z}{2}}\right)dz=\int \text{d}x\\
z-\frac{1}{2}\frac{\tan{\frac{z}{2}}}{\frac{1}{2}}=x+C\\
x+y-\tan{\frac{x+y}{2}}=x+C\\
y-\tan{\frac{x+y}{2}}=C
\end{gather}$$
2. $$\begin{gather}
\frac{\text{d}y}{\text{d}x}=\frac{x+2y-1}{x+2y+1}\\\\
\text{Sub: } z=x+2y;\ \ \ \frac{dz}{\text{d}x}=1+2\frac{\text{d}y}{\text{d}x}\\\\
\frac{1}{2}\left[\frac{dz}{\text{d}x}-1\right]=\frac{z-1}{z+1}\\
\frac{dz}{\text{d}x}=\frac{2(z-1)}{z+1}+1\\
\frac{dz}{\text{d}x}=\frac{3z-1}{z+1}\\
\frac{z+1}{3z-1}dz=\text{d}x\\
\frac{1}{3}\left(1+\frac{4}{3z-1}\right)dz=\text{d}x\\
\frac{1}{3}\int\left(1+\frac{4}{3z-1}\right)dz=\int \text{d}x\\
\frac{1}{3}z+\frac{4}{9}\ln{|3z-1|}=x+C_1\\
\frac{1}{3}(x+2y)+\frac{4}{9}\ln{|3(x+2y)-1|}=x+C_1\\
\frac{2}{3}(y-x)+\frac{4}{9}\ln{|3(x+2y)-1|}=C_1\\
6(y-x)+4\ln{|3(x+2y)-1|}=C\\
\end{gather}$$
3. $$\begin{gather}
\frac{\text{d}y}{\text{d}x}-x\tan{(y-x)}=1\\\\
\text{Sub: } z=y-x; \ \ \ \frac{dz}{\text{d}x}=\frac{\text{d}y}{\text{d}x}-1\\\\
\left(1+\frac{dz}{\text{d}x}\right)-x\tan{z}=1\\
\frac{dz}{\text{d}x}=x\tan{z}\\
\cot{z}\ dz=x\text{d}x\\
\int\cot{z}\ dz=\int x\text{d}x\\
\ln{|\sin{z}|}=\frac{x^2}{2}+C\\
\ln{|\sin{(y-x)}|}=\frac{x^2}{2}+C\\
\end{gather}$$

**Theorem:** If $y_1$ and $y_2$ are solutions of a **linear differential equation,** then $Ay_1+By_2$ is also a solution. 


### 2. Homogeneous Differential Equations

A homogeneous function is a function where the orders of all the terms are equal. 

E.g: 
- $f(x,y)=x^2+3xy+y^2 \longrightarrow$ This is a homogeneous equation of order 2.
- $f(x,y)=x^3+x^2+y \longrightarrow$ This is not a homogeneous equation.
- $(a+b)^3=a^3+3a^2b+3ab^2+b^3 \longrightarrow$ This is a homogeneous equation of order 3.

A differential equation of the form $$\frac{\text{d}y}{\text{d}x}=\frac{f(x,y)}{g(x,y)}$$ where both $f$ and $g$ are homogeneous functions of the same order is a homogeneous differential equation.

E.g:
- $$\frac{\text{d}y}{\text{d}x}=\frac{x^2+2xy+3y^2}{x^2+2y^2}$$
- $$\frac{\text{d}y}{\text{d}x}=\frac{x^3+2x^2y+y^3}{x^2y+2y^3}$$

Homogeneous differential equations can be reduced to variable separable by substituting $y=vx$, where $v$ is a function of $x$.

1. $$\begin{gather}\frac{\text{d}y}{\text{d}x}=\frac{xy+y^2}{x^2}\\\\\text{Sub: }y=vx\\\frac{\text{d}y}{\text{d}x}=v+x\frac{dv}{\text{d}x}\\\\v+x\frac{dv}{\text{d}x}=\frac{x(vx)+(vx)^2}{x^2}\\v+x\frac{dv}{\text{d}x}=\frac{x^2(v+v^2)}{x^2}; x\neq0\\v+x\frac{dv}{\text{d}x}=v+v^2\\\frac{1}{v^2}dv=\frac{1}{x}\text{d}x\\\int\frac{1}{v^2}dv=\int\frac{1}{x}\text{d}x\\-\frac{1}{v}=\ln{|x|}+C\\-\frac{x}{y}=\ln{|x|}+C\\y\ln{|x|}+Cy+x=0\end{gather}$$
2. $$\begin{gather}\frac{\text{d}y}{\text{d}x}=\frac{2xy+3y^2}{2xy+x^2}\\\\\text{Sub: }y=vx\\\frac{\text{d}y}{\text{d}x}=v+x\frac{dv}{\text{d}x}\\\\v+x\frac{dv}{\text{d}x}=\frac{2vx^2+3v^2x^2}{2vx^2+x^2}\\v+x\frac{dv}{\text{d}x}=\frac{2v+3v^2}{2v+1}\\x\frac{dv}{\text{d}x}=\frac{v^2+v}{2v+1}\\\frac{2v+1}{v^2+v}dv=\frac{1}{x}\text{d}x\\\int\frac{2v+1}{v^2+v}dv=\int\frac{1}{x}\text{d}x\\\ln|v^2+1|=ln|x|+lnC\\v^2+v=xC\\\left(\frac{y}{x}\right)^2+\left(\frac{y}{x}\right)=xC\\y^2+yx+x^3C\end{gather}$$
3. $$\begin{gather}x^2\text{d}y+y(x+y)\text{d}x=0\\\\\text{Sub: }y=vx\\\frac{\text{d}y}{\text{d}x}=v+x\frac{dv}{\text{d}x}\\\\x^2(v\text{d}x+xdv)+vx(x+vx)\text{d}x=0\\xdv+v(2+v)\text{d}x=0\\\frac{1}{v(2+v)}dv=-\frac{1}{x}\text{d}x\\\frac{1}{2}\int\frac{1}{v}-\frac{1}{(2+v)}dv=-\int\frac{1}{x}\text{d}x\\\frac{1}{2}\left[\ln{|v|}-\ln{|v+2|}\right]=-\ln{|x|}+C_1\\\ln{\left|\frac{vx^2}{v+2}\right|}=\ln{|C|}\\\frac{vx^2}{v+2}=C\\\frac{yx^2}{y+2x}=C\\yx^2=C(y+2x)\end{gather}$$
#### Reducible to Homogeneous

A differential equation of the form, $$\frac{\text{d}y}{\text{d}x}=\frac{ax+by+c}{px+qy+r}; \frac{a}{b}\neq\frac{p}{r}$$ can be reduced to a homogeneous differential equation by substituting $x=X+h$ and $y=Y+k$ where both $h$ and $k$ are constants such that $$\begin{align}ah+bk+c=0\\ph+qk+r=0\end{align}$$

E.g:
1. $$\begin{gather}\frac{\text{d}y}{\text{d}x}=\frac{x+2y-3}{2x+y-3}\\\\\text{Let $x=X+h$ and $y=Y+h$}\\\text{then d$x=$d$X$ and d$y$=d$Y$}\\\\\frac{\text{d}Y}{\text{d}X}=\frac{(X+h)+2(Y+k)-3}{2(X+h)+(Y+k)-3}\\\frac{\text{dY}}{\text{d}X}=\frac{X+2Y+(h+2k-3)}{2X+Y+(2h+k-3)}\\\\\text{Selecting $h$ and $k$:}\\h+2k-3=0\tag{1}\\2h+k-3=0\tag{2}\\\\(1)\times 2 -(2)\\\\3k-3=0\\k=1\\h=1\\\\\frac{\text{d}Y}{\text{d}X}=\frac{X+2Y}{2X+Y}\longleftarrow\text{Homogeneous Equation}\\\\\text{Let }Y=vX\implies \frac{\text{d}Y}{\text{d}X}=v+X\frac{\text{d}v}{\text{d}X}\\\\v+X\frac{\text{d}v}{\text{d}X}=\frac{1+2v}{2+v}\\X\frac{\text{d}v}{\text{d}X}=\frac{1-v^2}{2+v}\\\int  {\frac{2+v}{1-v^2}}\text{d}v=\int{\frac{1}{X}\text{d}X}\\\frac{1}{2}\int{\frac{3}{1-v}+\frac{1}{1+v}}\text{d}v=\int{\frac{1}{X}\text{d}X}\\ \frac{1}{2}[\ln{|1+v|}-3\ln{|1-v|}]=\ln{|X|}+C_{1}\\\ln{|1+v|}=2\ln{|X|}+3\ln{|1-v|}+C_{1}\\(1-v)^{3}X^{2}C=1+v\\(X-Y)^{3}C=X+Y\\(x-y)^{3}C=x+y-2\end{gather}$$
2. $$\begin{gather}
\frac{\text{d}y}{\text{d}x}=\frac{x-y-2}{x+y+6}\\
{x=X+h;\; y=Y+k,\;\;\;h=-2, \; k=-4}\\
\frac{\text{d}Y}{\text{d}X}=\frac{X-Y}{X+Y}\;;Y=VX\\
V+X{\frac{\text{d}V}{\text{d}X}}={\frac{1-V}{1+V}}\\
X\frac{\text{d}V}{\text{d}X}=\frac{1-2V-V^{2}}{1+V}\\
\frac{1+V}{1-2V-V^{2}}\text{d}V=\frac{1}{X}\text{d}X\\
-\frac{1}{2}\int{\frac{-2-2V}{1-2V-V^{2}}}\text{d}V=\int{\frac{1}{X}\text{d}X}\\
-\frac{1}{2}\ln{|1-2V-V^{2}|}=\ln{|X|}+C_{1}\\
X^{2}(1-2V-V^{2})=C\\
X^{2}\left( 1-2\frac{Y}{X}-\left( \frac{Y}{X} \right)^2\right)=C\\
X^{2}-2XY-Y^{2}=C\\
(x+2)^{2}-2(x+2)(y+4)-(y+4)^{2}=C\\
x^{2}+4x+4-2xy-8x-4y-16-y^{2}-8y-16=C\\
x^{2}-y^{2}-4x-12y-2xy-28=C
\end{gather}$$
### 3. Linear Differential Equations

A Differential equation is said to be linear if it satisfies the
following two conditions.
1) The dependent variable and its derivatives are first
degree
2) Each co-efficient depends on the independent variable
or constants.

In other words, an $n ^{th}$  order differential equation is linear if it is
in the form of $$\begin{array}{c}{{\displaystyle b_{n}(x)\frac{\text{d}^{n}y}{\text{d} x^{n}}\!+\!b_{n\!-\!1}(x)\frac{\text{d}^{n\!-\!1}y}{\text{d} x_{n\!-\!1}}\!+\!\dots\dots\dots\dots\!+\!b_{0}(x)y=g(x)}}\\ {{\mathrm{~where~}}b_{i}(x)\;{\mathsf{and}}\;g(x)\;{\mathrm{are~functions~of~x.}}}\end{array}$$

If the differential equation is not linear, then it is said to be a **non-linear** DE.

$$\begin{array}{l}{{\displaystyle{\mathrm{A~differenti~Equation~of~the~form,}}}}\\ {{\displaystyle{\frac{\text{d} y}{\text{d} x}}+p(x)y=q(x)}}\\ {{\mathrm{is~called~a~linear~differential~equation.}}}\\  \\
{{\displaystyle{\mathrm{Multiply~both~sides~by}}\,e^{\int p(x)\text{d} x}}}\\ {{\displaystyle e^{\int p(x)\text{d} x}\times\left[{\displaystyle{\frac{\text{d} y}{\text{d} x}}}+p(x)y\right]=e^{\int p(x)\text{d} x}\times q(x)}}\\ {{\displaystyle{\frac{\text{d} y}{\text{d} x}}e^{\int p(x)\text{d} x}+e^{\int p(x)\text{d} x}p(x)y=e^{\int p(x)\text{d} x}\times q(x)}}\\ {{\displaystyle{\frac{\text{d}}{\text{d}x}\left[y\times e^{\int p(x)\text{d} x}\right]}=e^{\int p(x)\text{d} x}\times q(x)}} \\ \\

{{\mathrm{By~integrating,}}}\\ 
{{\displaystyle y\times e^{\int p(x)\text{d} x}=\int\left[e^{\int p(x)\text{d} x}\times q(x)\right]\text{d} x}} \\ \\

\mathrm{Let}\,e^{\int p(x)d x}=\mathrm{Integrating\,Factor}=IF\\ \\{\mathrm{Then~solution~is}}\\
\displaystyle y\times IF=\int{IF\times q(x)\text{d}x}+C
\end{array}$$

1. $$\begin{gather}
\frac{\text{d}y}{\text{d}x} -y=e^x\cos x \\\\
p(x)=-1 \\
q(x)=e^x\cos x \\
IF=e^{\int{-1 \mathrm{dx}}}=e^{-x} \\\\
ye^{-x}=\int{e^{-x}\times e^x \cos{x}\ \mathrm{dx}} +C \\
ye^{-x}=\int{\cos{x}\ \mathrm{dx}} +C \\
ye^{-x}=\sin x +C
\end{gather}$$
2. $$\begin{gather}
(x+1)\frac{\text{d}y}{\text{d}x} -y=e^{x}(x+1)^{2} \\
\frac{\text{d}y}{\text{d}x} + \left( \frac{-1}{x+1} \right)y=e^{x}(x+1) \\\\
p(x)=\left( \frac{-1}{x+1} \right) \\
q(x)=e^{x}(x+1) \\
IF=e^{\int{\left( \frac{-1}{x+1} \right)\mathrm{dx}}}=e^{-\ln{|x+1|}}=e^{\ln{|\left( \frac{1}{x+1} \right)|}}=\left( \frac{1}{x+1} \right) \\\\
y\times\left( \frac{1}{x+1} \right)=\int{\left( \frac{1}{x+1} \right)\times e^{x}(x+1)\ \mathrm{dx}} +C \\
\left( \frac{y}{x+1} \right)=e^{x}+C \\
y=e^{x}(x+1)+C(x+1)
\end{gather}$$