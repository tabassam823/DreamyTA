1. persamaan diferensial untk permasalah tali : $$T \frac{d^2 y(x)}{dx^2} = f(x)$$ dengan syarat batas : $$y(0) = y(L) = 0 \rightarrow \text{periodik, homogen}$$ dan jika : $$f(x)=f_0 \left[ \left(x-\frac{L}{2}\right)^2 - \frac{L^2}{4} \right], \space 0 \lt x \lt L$$ Tentukan $y(x)$
2. persamaan dirferensial : $$\frac{d^2y(x)}{dx^2} + y(x) = f(x)$$ dengan syarat batas : $$y(0) = y(1) = 0$$ Tentukan $y(x)$ jika $f(x) = \sin(ax), \space 0\lt x \lt 1$, dengan menggunakan metode superposisi fungsi eigen
3. persamaan diferensial : $$\frac{d^2y(x)}{dx^2} - k_0^2 y(x) = f(x)$$ dengan syarat batas $y(0) = y(L) = 0$ dalam interval $0\lt x \lt 1$
	1. tunjukkan bahwa fungsi Green untuk $x \lt \epsilon$ yaitu :$$g(x|\epsilon)= -\frac{\sinh(k_0x) \sinh(K_0L-K_0\epsilon)}{k_0 \sinh(k_0L)}$$
	2. Tentukan fungsi green untuk $x \ge \epsilon$ 
	3. tentukan $y(x)$ dalam bentuk $f(x)$ dengan menggunakan integran fungsi Green
	4. tentukan $y(x)$ jika $f(x) = 5 \delta(x-5) + 10 \delta(x-10)$ 
4. Difusi panas sepanjang batas tak hingga dengan temperatur pada $x=0$ dikontrol oleh waktu: $$T(x=0,t)=\begin{cases}f(t), \space t\gt 0 \\ 0, \space t\lt0 \end{cases}$$ persamaan difusinya: $$D^2 \frac{\partial^2T(x,t)}{\partial x^2} - \frac{\partial T(x,t)}{\partial x^2} = 0$$ dengan $T(x,t) \rightarrow 0$ seiring $|x| \rightarrow \infty$ dan nilai $T(x,t)$ terdefinisi untuk seluruh $x$ dan $t\gt 0$. solusi $T(x,t)$: $$T(x,t)= \int_0^\infty d\tau f(\tau) g(x, t|\tau)$$
	1. tentukan persamaan diferensial dan syarat batas yang memenuhi $g(x, t|\tau)$
	2. tentukan $g(x, t|\tau)$
5. Persamaan Fedhol: $$\phi(x) = \lambda \int_{-x}^x dy [1 + \sin(x+y)] \phi(y)$$
	1. Tentukan nilai $\lambda$ dengan menggunakan separasi kernel
	2. tentukan seluruh solusi tak nol untuk $\phi(x)$
 