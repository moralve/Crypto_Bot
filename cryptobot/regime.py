"""Mixin para market intelligence: régimen de mercado y estrategias."""

import numpy as np

from .constants import REGIME_LABELS, STRATEGY_REGISTRY


class RegimeMixin:
    """Métodos de market intelligence: detect_regime(), regime_report(), recommend_strategies(), select_strategy()."""

    def detect_regime(self, n_regimes: int = 3) -> "RegimeMixin":
        """
        Detecta el régimen de mercado actual usando Gaussian Mixture Model.

        Clasifica el mercado en regímenes basados en:
        - Returns (retornos porcentuales)
        - Volatilidad (rolling std de returns)
        - Trend strength (pendiente de SMA)
        - Volume change (cambio porcentual de volumen)

        El GMM provee probabilidades suaves para cada régimen,
        no una clasificación binaria. Ejemplo: "72% Bull, 20% Sideways, 8% Bear".

        Parameters
        ----------
        n_regimes : int, default 3
            Número de regímenes a detectar.
            Default 3: Bull 🟢, Bear 🔴, Sideways 🟡.

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado create_features() previamente.
        """
        self._require_features()
        # TODO: Implementar
        # 1. Seleccionar features para clustering: returns, volatility, trend, volume_change
        # 2. Escalar con StandardScaler
        # 3. Fit GaussianMixture(n_components=n_regimes)
        # 4. Predecir régimen del último período
        # 5. Obtener probabilidades con .predict_proba()
        # 6. Mapear clusters a labels (Bull/Bear/Sideways) basado en mean returns
        # 7. Guardar en self.regime, self.regime_probabilities, self.regime_model
        # 8. Print régimen actual con confianza
        pass

    def regime_report(self) -> None:
        """
        Visualización detallada del régimen actual.

        Muestra:
        - Régimen actual con probabilidad
        - Distribución histórica de regímenes
        - Gráfico de precio coloreado por régimen
        - Métricas por régimen (return promedio, volatilidad, duración)

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado detect_regime() previamente.
        """
        self._require_regime()
        # TODO: Implementar
        # 1. Tabla de probabilidades de cada régimen
        # 2. Plotly chart: precio con background coloreado por régimen
        # 3. Estadísticas por régimen: avg return, avg volatility, avg duration
        pass

    def recommend_strategies(self) -> None:
        """
        Recomienda estrategias de trading basadas en el régimen actual.

        Para cada estrategia del registry:
        1. Ejecuta un backtest rápido en datos del régimen actual
        2. Calcula Sharpe ratio, win rate, total return
        3. Rankea estrategias de mejor a peor
        4. Indica cuáles son recomendadas (🟢) y cuáles no (🔴)

        Mapping régimen → estrategia:
        - Bull: Trend Following, Momentum > Mean Reversion
        - Bear: Mean Reversion, Short Momentum > Trend Following
        - Sideways: Mean Reversion, Range Trading > Trend Following

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado detect_regime() previamente.
        """
        self._require_regime()
        # TODO: Implementar
        # 1. Para cada estrategia en STRATEGY_REGISTRY:
        #    a. Crear señales basadas en la lógica de la estrategia
        #    b. Backtest rápido sobre períodos con el régimen actual
        #    c. Calcular métricas
        # 2. Rankear por Sharpe ratio
        # 3. Marcar como recomendada (🟢) o no recomendada (🔴)
        # 4. Print tabla formateada con resultados
        pass

    def select_strategy(self, strategy: str) -> "RegimeMixin":
        """
        Selecciona una estrategia de trading.

        Parameters
        ----------
        strategy : str
            Nombre de la estrategia. Opciones:
            "trend_following", "mean_reversion", "momentum".

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Raises
        ------
        ValueError
            Si la estrategia no está en el registry.
        """
        if strategy not in STRATEGY_REGISTRY:
            available = list(STRATEGY_REGISTRY.keys())
            raise ValueError(
                f"Estrategia '{strategy}' no válida. Opciones: {available}"
            )

        self.selected_strategy = strategy
        info = STRATEGY_REGISTRY[strategy]
        print(f"✅ Estrategia seleccionada: {info['name']}")
        print(f"   {info['description']}")
        return self
