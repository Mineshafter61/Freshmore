$$
\begin{align*}
v_T(r)=C_1&=\sqrt{\frac{gm_r}{C^*r^2}} \\
&=\sqrt{\frac{gm_r}{C^*}}\times\sqrt{\frac{1}{r^2}} \\
&=\sqrt{\frac{g(Ar^2+B)}{C^*}}\times\sqrt{\frac{1}{r^2}} \\
&=\sqrt{\frac{g}{C^*}}\times\sqrt{\frac{Ar^2+B}{r^2}}\\
&=\sqrt{\frac{g}{C^*}}\times\sqrt{A+\frac{B}{r^2}} \\
v_T'(r)=C_1'&=\frac{d}{dr}\left(\sqrt{\frac{g}{C^*}}\times\sqrt{A+\frac{B}{r^2}}\right) \\
\text{let }K=\sqrt{\frac{g}{C^*}}&,\text{ since it is a constant} \\
v_T'(r)=C_1'&=K\times\frac{d}{dr}\left(\sqrt{A+\frac{B}{r^2}}\right) \\
&=K\times\frac{d}{dr}\left(A+\frac{B}{r^2}\right)^{\frac{1}{2}} \\
&=K\times\frac{1}{2}\left(A+\frac{B}{r^2}\right)^{-\frac{1}{2}}\left( -\frac{2B}{r^3} \right) \\
&=K \frac{-2B}{2r^3\left( \sqrt{A+\frac{B}{r^2}} \right)} \\
&=-K \frac{B}{r^3\left( \sqrt{A+\frac{B}{r^2}} \right)} \\
&=-\sqrt{\frac{g}{C^*}}\left[\frac{B}{r^3\left( \sqrt{A+\frac{B}{r^2}} \right)}\right]
\end{align*}
$$
Shit
$$
\begin{align*}
\text{From design task 2(a)}: \\
t_{f}=\frac{C_1}{g}\ln x&=\frac{C_1}{g}\ln\left( \frac{C_3}{2C_2}\left( 1+\sqrt{\frac{C_3^2-4C_2}{C_3^2}} \right) \right) \\
x'&=\left(\frac{C_3}{2C_2}\right)'\left( 1+\sqrt{ 1-\frac{4C_2}{C_3^2}} \right)+\left( \frac{C_3}{2C_2} \right)\left( 1+\sqrt{\left( 1-\frac{4C_2}{C_3^2} \right)} \right)' \\
&=\left(\frac{C_3'(2C_2)-C_3(2C_2)'}{(2C_2)^2}\right)\left(1+\sqrt{1-\frac{4C_2}{C_3^2}} \right)+\left( \frac{C_3}{2C_2} \right)\left( \frac{1}{2\sqrt{1-\frac{4C_2}{C_3^2}}} \right)\left(1-\frac{4C_2}{C_3^2}\right)' \\
&=\left(\frac{2C_2C_3'-2C_2'C_3}{4C_2^2}\right)\left(1+\sqrt{ 1-\frac{4C_2}{C_3^2}} \right)+\left(\frac{C_3}{2C_2}\right)\left(\frac{1}{2\sqrt{ 1-\frac{4C_2}{C_3^2}}} \right)\left(-\frac{(4C_2)'C_3^2-4C_2(C_3^2)'}{(C_3^2)^2}\right)' \\
&=\left(\frac{C_2C_3'-C_2'C_3}{2C_2^2}\right)\left(1+\sqrt{ 1-\frac{4C_2}{C_3^2}} \right)+\left(\frac{C_3}{2C_2}\right)\left(\frac{1}{2\sqrt{ 1-\frac{4C_2}{C_3^2}}}\right)\left(-\frac{4C_2'C_3^2-4C_2(2C_3C_3')}{(C_3^2)^2}\right)' \\
&=\left(\frac{C_2C_3'-C_2'C_3}{2C_2^2}\right)\left(1+\sqrt{ 1-\frac{4C_2}{C_3^2}} \right)-\left( \frac{1}{C_2} \right)\left(\frac{1}{\sqrt{ 1-\frac{4C_2}{C_3^2}}}\right)\left(\frac{C_2'C_3-2C_2C_3'}{C_3^2}\right) \\
\therefore t_f'&=\frac{C_1'}{g}\ln x+\frac{C_1}{g}x' \\
&=\frac{C_1'}{g}\ln \left(\frac{C_3}{2C_2}\left(1+\sqrt{\frac{C_3^2-4C_2}{C_3^2}}\right)\right)+\frac{C_1}{g}\cdot
\left[ \left( \frac{C_2C_3'-C_2'C_3}{2C_2^2} \right) \left( 1+\sqrt{1-\frac{4C_2}{C_3^2}} \right) - \left( \frac{1}{C_2} \right) \left( \frac{1}{\sqrt{1-\frac{4C_2}{C_3^2}}} \right) \left( \frac{C_2'-C_3-2C_2C_3'}{C_3^2} \right) \right] \\
\text{From design task 1(a)}: \\
C_2&=\frac{C_1+v_0}{C_1-v_0} \\
\therefore C_2'&=\frac{C_1'(C_1-v_0)+C_1'(C_1+v_0)}{(C_1+v_0)^2} \\
\text{From design task 2(a)}: \\
C_3&=(C_2+1)e^{\frac{(H-s_0)g}{C_1^2}} \\
\therefore C_3'&=C_2'e^{\frac{(H-s_0)g}{C_1^2}}+(C_2+1)e^{\frac{(H-s_0)g}{C_1^2}}\cdot\frac{-2C_1'(H-s_0)g}{C_1^3}
\end{align*}
$$
