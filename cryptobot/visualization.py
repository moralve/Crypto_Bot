"""Mixin para visualización: gráficos de precio, señales y performance."""

import plotly.graph_objects as go

from .constants import COLOR_PALETTE


class VisualizationMixin:
    """Métodos de visualización: plot_price(), plot_signals(), plot_performance()."""

    def plot_price(self) -> None:
        """
        Gráfico de velas japonesas (candlestick) con Plotly.

        Muestra OHLC data con volumen en panel inferior.
        Colores: paleta definida en COLOR_PALETTE.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado fetch_data() previamente.
        """
        self._require_data()
        # TODO: Implementar
        # 1. go.Candlestick con OHLC
        # 2. Panel de volumen abajo
        # 3. Colores de la paleta definida (COLOR_PALETTE)
        # 4. Layout responsive
        pass

    def plot_signals(self) -> None:
        """
        Gráfico de precio con señales de trading marcadas.

        BUY señales: triángulos verdes (▲)
        SELL señales: triángulos rojos (▼)
        Overlay sobre candlestick chart.

        Raises
        ------
        RuntimeError
            Si no se han generado señales con get_signals().
        """
        self._require_signals()
        # TODO: Implementar
        # 1. Base: candlestick chart
        # 2. Overlay: markers para BUY (green up triangle)
        # 3. Overlay: markers para SELL (red down triangle)
        pass

    def plot_performance(self) -> None:
        """
        Gráfico de equity curve y drawdown.

        Panel superior: equity curve vs buy-and-hold.
        Panel inferior: drawdown.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado backtest() previamente.
        """
        if self.backtest_results is None:
            raise RuntimeError(
                "❌ No hay backtest ejecutado. Ejecuta bot.backtest() primero."
            )
        # TODO: Implementar
        # 1. Equity curve del bot vs buy-and-hold
        # 2. Panel de drawdown
        # 3. Anotaciones: max drawdown, final return
        pass
