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
\tan^{-1}{y}=x-ln|x+1|+C
\end{gather}$$
3. $$\begin{gather}
(xy^2+x)dx+(x^2y+y)dy=0\\
x(y^2+1)dx=-y(x^2+1)dy\\
\frac{x}{x^2+1}dx=-\frac{y}{y^2+1}dy\\
\int\frac{x}{x^2+1}dx=-\int\frac{y}{y^2+1}dy\\
\frac{1}{2}ln|x^2+1|=-\frac{1}{2}ln|y^2+1|+\frac{1}{2}ln|C|\\
(x^2+1)(y^2+1)=C
\end{gather}$$
4. $$\begin{gather}
x\frac{dy}{dx}+\cot{y}=0\\
x\frac{dy}{dx}=-\cot{y}\\
\tan{y}\ dy=-\frac{1}{x}dx\\
\int\tan{y}\ dy=-\int\frac{1}{x}dx\\
-ln|\cos{y}|=-ln|x|-ln|C|\\
\cos{y}=Cx\\\\
\text{when } x=\frac{1}{\sqrt{2}}, y=\frac{\pi}{4}\\\\
\cos{\frac{\pi}{4}}=C\frac{1}{\sqrt{2}}\implies C=1\\
\therefore{1}{\sqrt{2}}, y=\frac{\pi}{4}\\\\
\cos{\frac{\pi}{4}}=C\frac{1}{\sqrt{2}}\implies C=1\\
\therefore \text{Solution is } \cos{y}=x
\end{gather}$$

### 2. Reducible to Variable Separable

A differential equation of the form,
$$\frac{dy}{dx}=f(ax+by+c)$$
 can be reduced to variable separable by substituting $$z=ax+by+c$$
E.g: 
1. $$\begin{gather}
\frac{dy}{dx}=\sec(x+y)\\
\text{Sub: } z=x+y;\ \ \ \frac{dz}{dx}=1+\frac{dy}{dx}\\
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