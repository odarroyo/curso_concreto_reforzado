# 🏛️ Curso de Diseño de Concreto Armado - Herramientas Interactivas

Plataforma web didáctica para la visualización y aprendizaje de la mecánica seccional no lineal, diagramas de interacción y momento-curvatura en concreto armado.

🌐 **Portal Web Oficial:** [https://odarroyo.github.io/curso_concreto_reforzado/](https://odarroyo.github.io/curso_concreto_reforzado/)

---

## 📚 Módulos Educativos

### 📘 Fundamentos del Concreto Armado

#### 1. 📏 [Capacidad y Diseño de Vigas con Bloque de Whitney](https://odarroyo.github.io/curso_concreto_reforzado/capacidad_y_diseno_vigas.html)
- Doble modalidad basada en el script oficial de clase: Análisis de Capacidad ($M_n, \phi M_n$) y Diseño por momento actuante ($M_u \to \rho, A_{s,\text{req}}$).
- Visualizador cuádruple sincronizado: Sección, Euler-Bernoulli, bloque equivalente de Whitney y equilibrio de fuerzas con compresión al lado derecho.
- Criterio de ductilidad ($\varepsilon_t \ge 0.005 \implies \phi = 0.90$), asistente de armaduras comerciales colombianas (NSR-10 / ACI 318), pizarrón MathJax paso a paso y consola Python en vivo.

#### 2. 📜 [El Bloque de Whitney (1937) vs. Modelo de Fibras](https://odarroyo.github.io/curso_concreto_reforzado/bloque_whitney_vs_fibras.html)
- El hito histórico de Whitney (1937) y el salto de esfuerzos admisibles (ASD) a resistencia última (USD).
- Comparativa interactiva continua para cualquier profundidad del eje neutro $c$: $C_c$, centroide $\bar{y}_c$, $P_n$ y $M_n$.
- 3 paneles dinámicos: Cinemática, Duelo de Esfuerzos y Diagrama $P-M$.
- Fundamento físico de segundo orden y exportador a Python.

#### 3. 📘 [Cálculo de un Punto (P, M) con Fibras](https://odarroyo.github.io/curso_concreto_reforzado/calculo_punto_fibras.html)
- Cinemática de deformaciones planas de Euler-Bernoulli.
- Modelo constitutivo de Hognestad no confinado y acero elastoplástico.
- **Lupa didáctica:** Sustitución y cálculo numérico paso a paso ($y_i \to \varepsilon_i \to \sigma_i \to F_i \to d_i \to M_i$).
- Balanza de equilibrio estático de fuerzas axiales y momentos flectores.
- Convergencia de discretización numérica (5 a 100 fibras).

#### 4. 📗 [Diagrama de Interacción Completo (P - M)](https://odarroyo.github.io/curso_concreto_reforzado/material_educativo_fibras.html)
- Envolvente completa de flexocompresión nominal $(P_n, M_n)$ y de diseño $(P_u, M_u)$.
- Factores de reducción de resistencia $\phi$ según NSR-10 / ACI 318.
- Clasificación de modos de falla (Falla dúctil controlada por tracción, balanceada y controlada por compresión).
- 5 paneles dinámicos sincronizados a 60 FPS.

---

### 🔬 Comportamiento Avanzado y No Lineal

#### 5. 🌀 [Diagrama Momento - Curvatura (M - φ)](https://odarroyo.github.io/curso_concreto_reforzado/momento_curvatura_educativo.html)
- **El "Momento Eureka":** Construcción de la curva $M-\phi$ a partir de la familia de curvas de interacción $P-M$ a diferentes niveles de deformación $\varepsilon_c$ cortadas a carga axial constante $P_{\text{target}}$.
- Simulador animado paso a paso con seguimiento de la mecánica interna.
- Cálculo de ductilidad seccional $\mu_\phi = \phi_u / \phi_y$ y rigidez secante elástica.
- Presets para vigas (flexión pura), columnas sismorresistentes y muros estructurales.

#### 6. 🎯 [Utilidad del Diagrama Momento - Curvatura (M - φ)](https://odarroyo.github.io/curso_concreto_reforzado/utilidad_momento_curvatura.html)
- **Aviso Metodológico y Alcance:** Enfatiza que los resultados son **estimaciones seccionales preliminares** para orientar el criterio práctico y **NO reemplazan un análisis estructural no lineal riguroso** (Pushover global o NL-THA).
- **Pilar 1: Rigidez Efectiva Refinada ($EI_{eff} = M_y / \phi_y$):** Reemplazo del factor simplificado de código ($0.70 I_g$ en columnas), demostrando cómo el agrietamiento real a la fluencia alarga el período estructural $T$ y amplifica las derivas laterales $\Delta$.
- **Pilar 2: Ductilidad Seccional ($\mu_\phi = \phi_u / \phi_y$):** Verificación directa de la idoneidad del detallado de estribos y la capacidad inelástica antes del pandeo de barras longitudinales (DMO vs DES).
- **Pilar 3: Sobrerresistencia y Cortante por Capacidad ($V_e = 2M_{pr}/L_c$):** Evaluación del momento probable $M_{pr}$ (con endurecimiento $1.25 f_y$ y confinamiento Mander) para prevenir falla frágil por cortante en columnas sísmicas.
- **Pilar 4: Rotación Plástica ($\theta_p = \phi_p \cdot L_p$):** Estimación de la longitud de rótula plástica de Paulay & Priestley (1992) y cotejo con niveles de desempeño ASCE 41-17 (IO, LS, CP).
- Visualizador doble de Canvas (Diagrama $M-\phi$ bilineal y Elevación de Columna con perfil $\phi(z)$), 5 retos socráticos y exportador de código Python.

#### 7. 🔬 [Modelo de Concreto Confinado según Mander et al. (1988)](https://odarroyo.github.io/curso_concreto_reforzado/tutorial_mander_confinamiento.html)
- Mecánica física de la **acción de arco** en secciones rectangulares y cálculo analítico del coeficiente de efectividad $k_e$.
- Visualizador interactivo 2D a escala de la sección transversal, barras amarradas vs libres y áreas inefectivas parabólicas ($\sum w_i^{\prime 2}/6$).
- Vista en elevación con abombamiento vertical inefectivo entre capas de estribos a separación $s$.
- **Superficie multiaxial de falla de William-Warnke:** Digitalización precisa de la Figura 4 de Mander (1988) para secciones rectangulares con presiones asimétricas ($f'_{lx} \neq f'_{ly}$), isolíneas de $K$ e indicación del punto de operación en tiempo real.
- **Ley constitutiva $\sigma_c - \varepsilon_c$ de Popovics:** Núcleo confinado vs recubrimiento no confinado con *spalling* y modo comparador (*Ghost Curve*).
- **Balance de energía de Mander:** Cálculo analítico de la deformación última $\varepsilon_{cu}$ al fracturar el primer estribo transversal.
- Presets normativos (Pobre, DMO, DES, Viga asimétrica y Validación del Ejemplo Numérico del Paper 1988), lupa didáctica paso a paso y retos socráticos.

#### 8. 🧱 [Cálculo de un Punto con Concreto Confinado](https://odarroyo.github.io/curso_concreto_reforzado/calculo_punto_fibras_confinado.html)
- Diferenciación explícita entre el **recubrimiento no confinado** (Hognestad: $f'_c, \varepsilon_u = 0.0038$) y el **núcleo confinado** por estribos (Mander: $f'_{cc} = K \cdot f'_c, \varepsilon_{u,cc} = 5\varepsilon_{0,cc}$).
- Desglose de fuerzas axiales y momentos flectores por zonas (Recubrimiento, Núcleo, Acero).
- Lupa didáctica para inspeccionar la ley constitutiva aplicada a cada elemento.
- Comparativa en tiempo real con y sin confinamiento activo ($K = 1.3$ vs $K = 1.0$).

#### 9. 📈 [Diagrama de Interacción P - M Confinado](https://odarroyo.github.io/curso_concreto_reforzado/diagrama_interaccion_confinado.html)
- Superposición interactiva de las dos envolventes: **Confinada (Púrpura Mander)** vs **No Confinada (Naranja Hognestad)**.
- Cuantificación en tiempo real de la ganancia en compresión axial ($\Delta P_n$) y flexión ($\Delta M_n$).
- Análisis del incremento en compresión pura $P_0$ (+15.8%) y la invariancia física en tracción pura $P_t$.
- Puntos notables interactivos: Momento Máximo, Falla Balanceada, Límite por Tracción y Compresión pura.

#### 10. 🏛️ [Modelo de Fibras de Sección General (int_diag2)](https://odarroyo.github.io/curso_concreto_reforzado/modelo_fibras_seccion_general.html)
- Implementación general del algoritmo de fibras `int_diag2` de `funcion_general.py` para geometrías arbitrarias.
- **Visualizador interactivo de fibras:** Malla 2D de fibras de concreto coloreadas por gradiente de esfuerzo y barras de acero proporcionales.
- Cálculo automático del centroide seccional $\bar{y}$ y momentos flectores respecto a $\bar{y}$.
- Presets del script de clase: Sección rectangular, Muro con aletas en T ($B=2.5\text{ m}, h=2.05\text{ m}$), Muro asimétrico y Columna I.
- Generador y exportador de código Python para ejecutar en Spyder o Jupyter.

---

## 💻 Características Técnicas
- **100% Autocontenido:** Desarrollado con HTML5, CSS moderno y JavaScript Vanilla.
- **Sin Dependencias:** No requiere instalación de Python, Jupyter ni servidores.
- **Multiplataforma:** Compatible con navegadores en PC, Mac, tablets y celulares.
- **Modo Claro / Modo Oscuro:** Alto contraste para proyección en clase o estudio nocturno.
- **Exportación:** Generación de archivos CSV y código LaTeX para informes de laboratorio.

---

Prof. Orlando Arroyo — *Diseño de Concreto Armado*
