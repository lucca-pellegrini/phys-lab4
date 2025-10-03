#!/usr/bin/env python3
# SPDX-License-Identifier: ISC

"""
Análise do Experimento 4: Atrito Cinético
Analisa dados experimentais de atrito cinético em um plano inclinado.
Cria um gráfico de posição (x) vs tempo ao quadrado (t²) com regressão linear
para determinar aceleração e velocidade inicial.

Copyright © 2025 Lucca Pellegrini <lucca@verticordia.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""

import matplotlib.pyplot as plt
import numpy as np
from physplot import PhysPlot, linear


def main():
    # Dados experimentais do experimento de atrito cinético
    # Posição (Δx) em metros
    x_data = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35])

    # Tempo ao quadrado (t²) em segundos²
    t_squared_data = np.array(
        [
            0.0104500625,  # t = 0.10225 s
            0.0325441600,  # t = 0.18040 s
            0.0522944400,  # t = 0.22880 s
            0.0739840000,  # t = 0.27200 s
            0.1012608900,  # t = 0.31830 s
            0.1270100000,  # t = 0.35640 s
            0.1569816400,  # t = 0.39620 s
        ]
    )

    # Inicializa PhysPlot com configurações desse experimento
    plotter = PhysPlot()
    plt.rcParams["text.latex.preamble"] = r"\usepackage{siunitx}"

    print("Análise do Experimento de Atrito Cinético")
    print("=" * 50)
    print("Regressão linear: x = A·t² + B")
    print("onde A = a/2 (metade da aceleração) e B = v₀ (velocidade inicial)")
    print("-" * 50)

    # Realizar regressão linear: x vs t²
    results = plotter.plot_with_regression(
        data=(t_squared_data, x_data),
        func=linear,
        xlabel=r"Tempo ao quadrado $t^2$ [\si{\second\squared}]",
        ylabel=r"Posição $\Delta x$ [\si{\meter}]",
        title=r"Atrito Cinético: $\Delta x(t) = \frac{a}{2}t^2 + v_0t$",
        filename="kinetic_friction_plot.pdf",
        param_names=(r"\frac{a}{2}", r"v_0"),
        data_label="Valores medidos",
        fit_label="Ajuste Linear",
        legend_loc="upper left",
    )

    if results is None:
        print("ERRO: Regressão linear falhou")
        return

    # Extrair parâmetros ajustados
    half_a = results["params"][0]  # A = a/2
    v0 = results["params"][1]  # B = v₀
    acceleration = 2 * half_a  # a = 2A

    # Incertezas dos parâmetros
    half_a_std = results["params_std"][0]
    v0_std = results["params_std"][1]
    acceleration_std = 2 * half_a_std

    print("\nResultados da Regressão:")
    print(f"A (a/2) = {half_a:.4f} ± {half_a_std:.4f} m/s²")
    print(f"B (v₀)  = {v0:.4f} ± {v0_std:.4f} m/s")
    print(f"Aceleração a = {acceleration:.4f} ± {acceleration_std:.4f} m/s²")
    print(f"R² = {results['r_squared']:.4f}")

    # Interpretação física
    print("\nInterpretação Física:")
    print(f"Meia aceleração: a/2 = {half_a:.3f} m/s²")
    print(f"Velocidade inicial: v₀ = {v0:.3f} m/s")
    print(f"Aceleração completa: a = {acceleration:.3f} m/s²")
    print(f"Qualidade do ajuste: R² = {results['r_squared']:.4f}")

    print("\nGráfico salvo como 'kinetic_friction_plot.pdf'")


if __name__ == "__main__":
    main()
