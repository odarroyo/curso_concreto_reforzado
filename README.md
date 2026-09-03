# 🏛️ Curso de Diseño de Concreto Armado I - Herramientas Interactivas

Plataforma web didáctica para la visualización y aprendizaje de la mecánica seccional no lineal, diagramas de interacción y momento-curvatura en concreto armado.

🌐 **Portal Web Oficial:** [https://odarroyo.github.io/curso_concreto_reforzado/](https://odarroyo.github.io/curso_concreto_reforzado/)

---

## 📚 Módulos Educativos

### 1. 📘 [Cálculo de un Punto (P, M) con Fibras](https://odarroyo.github.io/curso_concreto_reforzado/calculo_punto_fibras.html)
- Cinemática de deformaciones planas de Euler-Bernoulli.
- Modelo constitutivo de Hognestad no confinado y acero elastoplástico.
- **Lupa didáctica:** Sustitución y cálculo numérico paso a paso ($y_i \to \varepsilon_i \to \sigma_i \to F_i \to d_i \to M_i$).
- Balanza de equilibrio estático de fuerzas axiales y momentos flectores.
- Convergencia de discretización numérica (5 a 100 fibras).

### 2. 📗 [Diagrama de Interacción Completo (P - M)](https://odarroyo.github.io/curso_concreto_reforzado/material_educativo_fibras.html)
- Envolvente completa de flexocompresión nominal $(P_n, M_n)$ y de diseño $(P_u, M_u)$.
- Factores de reducción de resistencia $\phi$ según NSR-10 / ACI 318.
- Clasificación de modos de falla (Falla dúctil controlada por tracción, balanceada y controlada por compresión).
- 5 paneles dinámicos sincronizados a 60 FPS.

### 3. 🌀 [Diagrama Momento - Curvatura (M - φ)](https://odarroyo.github.io/curso_concreto_reforzado/momento_curvatura_educativo.html)
- **El "Momento Eureka":** Construcción de la curva $M-\phi$ a partir de la familia de curvas de interacción $P-M$ a diferentes niveles de deformación $\varepsilon_c$ cortadas a carga axial constante $P_{\text{target}}$.
- Simulador animado paso a paso con seguimiento de la mecánica interna.
- Cálculo de ductilidad seccional $\mu_\phi = \phi_u / \phi_y$ y rigidez secante elástica.
- Presets para vigas (flexión pura), columnas sismorresistentes y muros estructurales.

### 4. 🧱 [Cálculo de un Punto con Concreto Confinado](https://odarroyo.github.io/curso_concreto_reforzado/calculo_punto_fibras_confinado.html)
- Diferenciación explícita entre el **recubrimiento no confinado** (Hognestad: $f'_c, \varepsilon_u = 0.0038$) y el **núcleo confinado** por estribos (Mander: $f'_{cc} = K \cdot f'_c, \varepsilon_{u,cc} = 5\varepsilon_{0,cc}$).
- Desglose de fuerzas axiales y momentos flectores por zonas (Recubrimiento, Núcleo, Acero).
- Lupa didáctica para inspeccionar la ley constitutiva aplicada a cada elemento.
- Comparativa en tiempo real con y sin confinamiento activo ($K = 1.3$ vs $K = 1.0$).

### 5. 📈 [Diagrama de Interacción P - M Confinado](https://odarroyo.github.io/curso_concreto_reforzado/diagrama_interaccion_confinado.html)
- Superposición interactiva de las dos envolventes: **Confinada (Púrpura Mander)** vs **No Confinada (Naranja Hognestad)**.
- Cuantificación en tiempo real de la ganancia en compresión axial ($\Delta P_n$) y flexión ($\Delta M_n$).
- Análisis del incremento en compresión pura $P_0$ (+15.8%) y la invariancia física en tracción pura $P_t$.
- Puntos notables interactivos: Momento Máximo, Falla Balanceada, Límite por Tracción y Compresión pura.

### 6. 🏛️ [Modelo de Fibras de Sección General (int_diag2)](https://odarroyo.github.io/curso_concreto_reforzado/modelo_fibras_seccion_general.html)
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
Prof. Orlando Arroyo — *Diseño de Concreto Armado I*
