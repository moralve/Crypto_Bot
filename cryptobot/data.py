"""Mixin para data pipeline: descarga y resumen de datos OHLCV."""

from datetime import datetime, timedelta
from typing import Optional


class DataMixin:
    """Métodos de data pipeline: fetch_data() y summary()."""

    def fetch_data(
        self,
        last_days: int = 90,
        start: Optional[str] = None,
        end: Optional[str] = None,
    ) -> "DataMixin":
        """
        Obtiene datos OHLCV del exchange via CCXT.

        Soporta dos modos:
        - Por cantidad de días: bot.fetch_data(last_days=90)
        - Por rango de fechas: bot.fetch_data(start="2024-01-01", end="2024-12-31")

        Las columnas del DataFrame siguen el formato requerido
        por backtesting.py: Open, High, Low, Close, Volume.

        Parameters
        ----------
        last_days : int, default 90
            Número de días hacia atrás desde hoy. Se ignora si start/end están definidos.
        start : str, optional
            Fecha de inicio en formato "YYYY-MM-DD".
        end : str, optional
            Fecha de fin en formato "YYYY-MM-DD". Default: hoy.

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Examples
        --------
        >>> bot.fetch_data()
        >>> bot.fetch_data(last_days=180)
        >>> bot.fetch_data(start="2024-01-01", end="2024-06-30")
        """
        # TODO: Implementar
        # 1. Calcular since_timestamp basado en last_days o start/end
        # 2. Llamar self._exchange.fetch_ohlcv(self._pair, self.timeframe, since, limit)
        # 3. Paginar si es necesario (CCXT tiene límite por request)
        # 4. Construir DataFrame con columnas: Open, High, Low, Close, Volume
        # 5. Index: DatetimeIndex con nombre "Date"
        # 6. Guardar en self.data
        # 7. Print resumen: rango de fechas, registros, precio actual
        pass

    def summary(self) -> None:
        """
        Muestra resumen del dataset cargado.

        Incluye: rango de fechas, número de registros, precio actual,
        cambio porcentual, high/low del período, y estadísticas básicas.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado fetch_data() previamente.
        """
        self._require_data()
        # TODO: Implementar
        # 1. Rango de fechas (primer y último registro)
        # 2. Número de registros
        # 3. Precio actual (último close)
        # 4. Cambio % en el período
        # 5. High/Low del período
        # 6. self.data.describe() formateado
        pass
