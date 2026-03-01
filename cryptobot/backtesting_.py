"""Mixin para backtesting de estrategias."""


class BacktestMixin:
    """Métodos de backtesting: backtest() y backtest_plot()."""

    def backtest(self, cash: float = 10_000, commission: float = 0.001) -> "BacktestMixin":
        """
        Ejecuta backtest de la estrategia usando backtesting.py.

        Parameters
        ----------
        cash : float, default 10_000
            Capital inicial para la simulación.
        commission : float, default 0.001
            Comisión por trade (0.1% default, típico de exchanges crypto).

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        Métricas disponibles en self.backtest_results:
        - Total Return, Sharpe Ratio, Max Drawdown
        - Win Rate, # Trades, Avg Trade Duration
        - Equity curve

        Raises
        ------
        RuntimeError
            Si no se han generado señales con get_signals().
        """
        self._require_signals()
        # TODO: Implementar
        # 1. Crear Strategy class de backtesting.py que use self.signals
        # 2. Instanciar Backtest(self.data, strategy, cash, commission)
        # 3. bt.run()
        # 4. Guardar stats en self.backtest_results
        # 5. Guardar bt object en self._bt_object (para plot)
        # 6. Print métricas clave formateadas
        pass

    def backtest_plot(self) -> None:
        """
        Muestra el gráfico interactivo de backtesting.py.

        Incluye: equity curve, drawdown, señales de entrada/salida,
        y precio del activo.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado backtest() previamente.
        """
        if self._bt_object is None:
            raise RuntimeError(
                "❌ No hay backtest ejecutado. Ejecuta bot.backtest() primero."
            )
        # TODO: Implementar
        # self._bt_object.plot()
        pass
