"""Mixin para escaneo multi-símbolo."""

import pandas as pd


class ScannerMixin:
    """Métodos de scanner: scan()."""

    def scan(self, symbols: list[str] = None) -> pd.DataFrame:
        """
        Escanea múltiples criptomonedas y muestra régimen + señal de cada una.

        Parameters
        ----------
        symbols : list of str, optional
            Lista de símbolos a escanear.
            Default: ["BTC", "ETH", "SOL", "BNB", "XRP"]

        Returns
        -------
        pd.DataFrame
            Tabla con columnas: Symbol, Regime, Confidence,
            Signal, Price, Change_24h.

        Examples
        --------
        >>> bot.scan()
        >>> bot.scan(symbols=["BTC", "ETH", "SOL", "AVAX", "DOGE"])

        Notes
        -----
        Este método crea instancias temporales de CryptoBot para cada
        símbolo. Usa la misma configuración (timeframe, exchange) del
        bot actual pero NO modifica su estado.
        """
        if symbols is None:
            symbols = ["BTC", "ETH", "SOL", "BNB", "XRP"]

        # TODO: Implementar
        # 1. Para cada symbol:
        #    a. Crear CryptoBot temporal con misma config
        #    b. fetch_data (últimos 30 días para rapidez)
        #    c. create_features()
        #    d. detect_regime()
        #    e. Recopilar: symbol, regime, confidence, price, change_24h
        # 2. Construir DataFrame resumen
        # 3. Print tabla formateada
        # 4. Retornar DataFrame
        pass
