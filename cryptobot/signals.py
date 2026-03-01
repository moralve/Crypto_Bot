"""Mixin para generación de señales de trading."""


class SignalsMixin:
    """Métodos de señales: get_signals()."""

    def get_signals(self) -> "SignalsMixin":
        """
        Genera señales de trading usando el modelo entrenado.

        Las señales respetan el régimen de mercado:
        - Si el régimen actual es desfavorable para la estrategia → HOLD
        - Si el modelo predice oportunidad → BUY (1) o SELL (-1)
        - Si no hay oportunidad → HOLD (0)

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        Las señales se guardan en self.signals como pd.Series.
        Risk management (stop_loss, take_profit, position_sizing)
        se aplica en la etapa de ejecución, no en la generación de señales.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado train_models() previamente.
            Si no se ha ejecutado detect_regime() previamente.
        """
        self._require_model()
        self._require_regime()
        # TODO: Implementar
        # 1. Verificar si el régimen actual es favorable para la estrategia
        # 2. Si no es favorable: todas las señales = HOLD, con warning
        # 3. Si es favorable: predecir con self.model sobre datos recientes
        # 4. Convertir predicciones a señales: BUY (1), SELL (-1), HOLD (0)
        # 5. Guardar en self.signals
        # 6. Print resumen: última señal, confianza, fecha
        pass
