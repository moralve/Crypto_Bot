"""Mixin para feature engineering: indicadores técnicos."""


class FeaturesMixin:
    """Métodos de feature engineering: create_features()."""

    def create_features(self, mode: str = "core") -> "FeaturesMixin":
        """
        Agrega indicadores técnicos al DataFrame.

        Dos modos disponibles:
        - "core": ~10 indicadores clave que se cubrieron en el curso.
          Ideal para exploración y comprensión.
        - "full": 86+ indicadores via ta.add_all_ta_features().
          Ideal para training de modelos donde feature importance
          determina qué indicadores son relevantes.

        Parameters
        ----------
        mode : str, default "core"
            "core" para indicadores esenciales, "full" para todos.

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Core Features
        -------------
        - SMA_20, SMA_50 : Medias móviles simples
        - RSI_14 : Relative Strength Index
        - MACD, MACD_signal : Moving Average Convergence Divergence
        - BB_upper, BB_lower : Bollinger Bands
        - ATR_14 : Average True Range (volatilidad)
        - volume_change : Cambio porcentual del volumen
        - returns : Retorno porcentual diario
        - volatility_20 : Volatilidad rolling 20 períodos

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado fetch_data() previamente.
        ValueError
            Si mode no es "core" o "full".
        """
        self._require_data()
        # TODO: Implementar
        # mode="core":
        #   1. Calcular cada indicador con la librería `ta`
        #   2. Agregar returns y volatility manualmente
        #   3. Dropear NaN rows iniciales
        #
        # mode="full":
        #   1. ta.add_all_ta_features(...)
        #   2. Dropear NaN rows iniciales
        #   3. Print cantidad de features agregados
        #
        # Guardar en self.features
        pass
