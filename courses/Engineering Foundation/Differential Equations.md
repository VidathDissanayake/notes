# Differential Equations (DE)

> Vidath Dissanayake | Sri Lanka  
> Tags: #courses #courses/PreEng 
> Links: [Engineering Foundation](Engineering%20Foundation.md)
> Sources:  

---

# 1. Order, Degree and Variable Separation Method

 > Links:  
> Sources: [Order, Degree and Variable Separation](https://us02web.zoom.us/rec/play/-WTSWq4wu0MDXiMTREDZgPiLSoODnD5C8MAjudq1OV-G7WNKwINiayTuvrHP1OepRGsl4zui54DYYeOf.nReKNBv80Z_42dFm?hasValidToken=false&canPlayFromShare=true&from=share_recording_detail&startTime=1718449615000&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus02web.zoom.us%2Frec%2Fshare%2FcyVAJuHBIXRCiRDH6J8HZot03KjjNWRCwREirG2zXA3g_NTrqDphY6wS5eEAmBzt.OEaPQ5cDCObjmuft%3FstartTime%3D1718449615000) 

![DifferentialEquation HK Dass Chapter 3](assets/documents/DifferentialEquation%20HK%20Dass%20Chapter%203.pdf)

![classification of calculus](assets/images/classification%20of%20calculus.png) 

Differentiation and integration are inverse functions.

In A/L, we discuss Single Variable (Ordinary) calculus.

## Terminology

- Single variable functions - Functions consisting of a single variable. 
    - E.g: $y=f(x)$ 
- Multi variable functions - Functions consisting of multiple variables. 
    - E.g: $y=f(x_{1}, x_{2}, x_{3}, ...)$  
- Independent variable - The variable that does not depend on others. Usually $x$. The variable we change at will.
- Dependant variable - The variable that depends on the independent variable.
- Differential Coefficient/Derivatives - E.g: $\frac{dy}{dx}$ (Differentiation of $y$ with respect to $x$ / Derivative of $y$ w.r.t. $x$.)
- $\frac{d^{2}y}{dx^{2}}$  - Second order derivative of $y$ w.r.t. $x$ / Second derivative of $y$ w.r.t. $x$.

## Definition

An equation containing differential coefficients is known as a differential equation (DE).

## Formation of Differential Equations

Differential equations are obtained by differentiating ordinary equations and eliminating arbitrary constants.

E.g: 
1. $$\begin{gather}
y=e^{x}\sin{x} \longleftarrow \text{Equation} \\ 
\frac{dy}{dx}=e^{x}\cos{x}+e^{x}\sin{x} \\
\frac{dy}{dx}=e^{x}\cos{x}+y \longleftarrow \text{DE}\\
\frac{d^{2}y}{dx^{2}}=\left[-e^{x}\sin{x}+e^{x}\cos{x}\right]+\frac{dy}{dx} \\
\frac{d^{2}y}{dx^{2}}=\left[-y+\frac{dy}{dx}-y\right]+\frac{dy}{dx} \\
\frac{d^{2}y}{dx^{2}}-2\frac{dy}{dx}+2y=0 \longleftarrow \text{DE}
\end{gather}$$
2. $$\begin{gather}
y=A\sin{x}+B\cos{x} \longleftarrow \text{Equation} \\
\frac{dy}{dx}=A\cos{x}-B\sin{x} \\
\frac{d^{2}y}{dx^{2}}= -A\sin{x}-B\cos{x} \\
\frac{d^{2}y}{dx^{2}}+y=0 \longleftarrow \text{DE}
\end{gather}$$

## Properties of Differential Equations

### Order

The order of the highest differential coefficient is called the order of the DE.

### Degree

The degree of the highest differential coefficient after removing the radical signs and fractions of the dependent variable is called the degree of the DE.

E.g: 
- $\left(\frac{d^{2}y}{dx^{2}}\right)^3+x\left(\frac{dy}{dx}\right)^5+\sin{xy}=5x$ (order=2, degree=3)
- $\left(\frac{d^{2}y}{dx^{2}}\right)^3+\left(\frac{dy}{dx}\right)^\frac{5}{2}=+y=13$ (order=2, degree=6)
- $\left(\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}\right)^2+y^\frac{5}{3}=3$ (order=2, degree=6)
- $\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}=\sqrt{\sin{x}}$ (order=2, degree=1)

## Solving Differential Equations

The process of obtaining an equation without containing derivatives from a DE is known as solving the DE. The obtained ordinary equation is known as the **solution** of the differential equation.

The solution satisfies the DE.

The number of arbitrary constants present in the solution is equal to the order of the DE.

The method of obtaining the solution is an integration involving process. Depending on the DE, various techniques (symbolic, numerical) are used.

A differential equation of the form  $\frac{d^{n}y}{dx^{n}}=f{x}$ can be solved by repeated integration.

E.g:
1. $$\begin{gather}\frac{d^{2}y}{dx^{2}}=x^2 \\
\frac{dy}{dx}=\frac{x^3}{3}+A \\
y=\frac{x^4}{12}+Ax+B
\end{gather}$$
2. $$\begin{gather}
y\frac{dy}{dx}=\cos{2x} \\
y^2=\sin{2x}+C
\end{gather}$$


## First Order Differential Equations

Depending on $F(x,y)$ various methods are used to solve the DE

1. Variable Separable
2. Homogeneous
3. Linear Differential Equations
4. Exact

### 1. Variable Separable

A DE of the form $\frac{dy}{dx}=\frac{f(x)}{g(y)}$ can be solved by separating variables and integration.

E.g:
1. $$\begin{gather}
\frac{1}{y}\frac{dy}{dx}=\cos{2x}\\
\frac{1}{y}dy=\cos{2x}\ dx\\
\int\frac{1}{y}dy=\int\cos{2x}\ dx\\
\ln{|y|}+C_1=\frac{\sin{2x}}{2}+C_2\\
\ln{|y|}=\frac{\sin{2x}}{2}+C\\
y=Ae^\frac{\sin{2x}}{2}\\
\text{where A is an arbitrary constant}
\end{gather}$$
2. $$\begin{gather}
\frac{dy}{dx}=\frac{x(y^2+1)}{x+1}\\
(y^2+1)dy=\frac{x}{x+1}dx\\
\int(y^2+1)dy=\int1-\frac{1}{x+1}dx\\
\tan^{-1}{y}=x-\ln{|x+1|}+C
\end{gather}$$
3. $$\begin{gather}
(xy^2+x)dx+(x^2y+y)dy=0\\
x(y^2+1)dx=-y(x^2+1)dy\\
\frac{x}{x^2+1}dx=-\frac{y}{y^2+1}dy\\
\int\frac{x}{x^2+1}dx=-\int\frac{y}{y^2+1}dy\\
\frac{1}{2}\ln{|x^2+1|}=-\frac{1}{2}\ln{|y^2+1|}+\frac{1}{2}\ln{|C|}\\
(x^2+1)(y^2+1)=C
\end{gather}$$
4. $$\begin{gather}
x\frac{dy}{dx}+\cot{y}=0\\
x\frac{dy}{dx}=-\cot{y}\\
\tan{y}\ dy=-\frac{1}{x}dx\\
\int\tan{y}\ dy=-\int\frac{1}{x}dx\\
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
$$\frac{dy}{dx}=f(ax+by+c)$$
 can be reduced to variable separable by substituting $$z=ax+by+c$$
E.g: 
1. $$\begin{gather}
\frac{dy}{dx}=\sec(x+y)\\\\
\text{Sub: } z=x+y;\ \ \ \frac{dz}{dx}=1+\frac{dy}{dx}\\\\
\frac{dz}{dx}-1=\sec{z}\\
\frac{dz}{dx}=1+\sec{z}\\
\frac{dz}{dx}=\frac{1+\cos{z}}{\cos{z}}\\
\frac{\cos{z}}{1+\cos{z}}dz=dx\\
\left(1-\frac{1}{1+\cos{z}}\right)dz=dx\\
\left(1-\frac{1}{2\cos^2{\frac{z}{2}}}\right)dz=dx\\
\int\left(1-\frac{1}{2}\sec^2{\frac{z}{2}}\right)dz=\int dx\\
z-\frac{1}{2}\frac{\tan{\frac{z}{2}}}{\frac{1}{2}}=x+C\\
x+y-\tan{\frac{x+y}{2}}=x+C\\
y-\tan{\frac{x+y}{2}}=C
\end{gather}$$
2. $$\begin{gather}
\frac{dy}{dx}=\frac{x+2y-1}{x+2y+1}\\\\
\text{Sub: } z=x+2y;\ \ \ \frac{dz}{dx}=1+2\frac{dy}{dx}\\\\
\frac{1}{2}\left[\frac{dz}{dx}-1\right]=\frac{z-1}{z+1}\\
\frac{dz}{dx}=\frac{2(z-1)}{z+1}+1\\
\frac{dz}{dx}=\frac{3z-1}{z+1}\\
\frac{z+1}{3z-1}dz=dx\\
\frac{1}{3}\left(1+\frac{4}{3z-1}\right)dz=dx\\
\frac{1}{3}\int\left(1+\frac{4}{3z-1}\right)dz=\int dx\\
\frac{1}{3}z+\frac{4}{9}\ln{|3z-1|}=x+C_1\\
\frac{1}{3}(x+2y)+\frac{4}{9}\ln{|3(x+2y)-1|}=x+C_1\\
\frac{2}{3}(y-x)+\frac{4}{9}\ln{|3(x+2y)-1|}=C_1\\
6(y-x)+4\ln{|3(x+2y)-1|}=C\\
\end{gather}$$
3. $$\begin{gather}
\frac{dy}{dx}-x\tan{(y-x)}=1\\\\
\text{Sub: } z=y-x; \ \ \ \frac{dz}{dx}=\frac{dy}{dx}-1\\\\
\left(1+\frac{dz}{dx}\right)-x\tan{z}=1\\
\frac{dz}{dx}=x\tan{z}\\
\cot{z}\ dz=xdx\\
\int\cot{z}\ dz=\int xdx\\
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

A differential equation of the form $$\frac{dy}{dx}=\frac{f(x,y)}{g(x,y}$$ where both $f$ and $g$ are homogeneous functions of the same order is a homogeneous differential equation.

E.g:
- $$\frac{dy}{dx}=\frac{x^2+2xy+3y^2}{x^2+2y^2}$$
- $$\frac{dy}{dx}=\frac{x^3+2x^2y+y^3}{x^2y+2y^3}$$
Homogeneous differential equations can be reduced to variable separable by substituting $y=vx$, where $v$ is a function of $x$.

1. $$\begin{gather}\frac{dy}{dx}=\frac{xy+y^2}{x^2}\\\\\text{Sub: }y=vx\\\frac{dy}{dx}=v+x\frac{dv}{dx}\\\\v+x\frac{dv}{dx}=\frac{x(vx)+(vx)^2}{x^2}\\v+x\frac{dv}{dx}=\frac{x^2(v+v^2)}{x^2}; x\neq0\\v+x\frac{dv}{dx}=v+v^2\\\frac{1}{v^2}dv=\frac{1}{x}dx\\\int\frac{1}{v^2}dv=\int\frac{1}{x}dx\\-\frac{1}{v}=\ln{|x|}+C\\-\frac{x}{y}=\ln{|x|}+C\\y\ln{|x|}+Cy+x=0\end{gather}$$
2. $$\begin{gather}\frac{dy}{dx}=\frac{2xy+3y^2}{2xy+x^2}\\\\\text{Sub: }y=vx\\\frac{dy}{dx}=v+x\frac{dv}{dx}\\\\v+x\frac{dv}{dx}=\frac{2vx^2+3v^2x^2}{2vx^2+x^2}\\v+x\frac{dv}{dx}=\frac{2v+3v^2}{2v+1}\\x\frac{dv}{dx}=\frac{v^2+v}{2v+1}\\\frac{2v+1}{v^2+v}dv=\frac{1}{x}dx\\\int\frac{2v+1}{v^2+v}dv=\int\frac{1}{x}dx\\\ln|v^2+1|=ln|x|+lnC\\v^2+v=xC\\\left(\frac{y}{x}\right)^2+\left(\frac{y}{x}\right)=xC\\y^2+yx+x^3C\end{gather}$$
3. $$\begin{gather}x^2dy+y(x+y)\\\\\text{Sub: }y=vxdx=0\\\frac{dy}{dx}=v+x\frac{dy}{dx}\end{gather}$$