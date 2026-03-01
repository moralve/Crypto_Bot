"""Mixin para persistencia: guardar/cargar estado y trade history."""

import joblib
import pandas as pd


class PersistenceMixin:
    """Métodos de persistencia: save(), load(), trade_history()."""

    def save(self, name: str, path: str = ".") -> None:
        """
        Guarda el estado completo del bot a disco.

        Guarda: modelo entrenado, configuración, régimen, features,
        historial de trades, y métricas. NO guarda datos OHLCV crudos
        (se pueden re-descargar con fetch_data).

        Parameters
        ----------
        name : str
            Nombre del archivo (sin extensión).
            Se guarda como {name}.pkl
        path : str, default "."
            Directorio donde guardar. En Colab usa
            "/content/drive/MyDrive/" para persistencia.

        Examples
        --------
        >>> bot.save("mi_bot_v1")
        >>> bot.save("mi_bot_v1", path="/content/drive/MyDrive/bots/")
        """
        # TODO: Implementar
        # 1. Crear dict con estado completo:
        #    - config: symbol, timeframe, exchange, risk params
        #    - model: self.model, self.model_name, self.model_metrics
        #    - regime: self.regime, self.regime_model, self.regime_probabilities
        #    - strategy: self.selected_strategy
        #    - trades: self.trades
        #    - model_comparison: self.model_comparison
        # 2. joblib.dump(state, f"{path}/{name}.pkl")
        # 3. Print confirmación con tamaño del archivo
        pass

    def load(self, name: str, path: str = ".") -> "PersistenceMixin":
        """
        Carga estado previamente guardado.

        Parameters
        ----------
        name : str
            Nombre del archivo (sin extensión).
        path : str, default "."
            Directorio donde buscar.

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        Después de cargar, aún necesitas ejecutar fetch_data() para
        obtener datos actualizados. El modelo y configuración se
        restauran automáticamente.

        Examples
        --------
        >>> bot = CryptoBot()
        >>> bot.load("mi_bot_v1")
        >>> bot.fetch_data()  # datos frescos
        >>> bot.get_signals()  # usa modelo cargado
        """
        # TODO: Implementar
        # 1. joblib.load(f"{path}/{name}.pkl")
        # 2. Restaurar todos los atributos del state
        # 3. Print resumen de lo que se cargó
        pass

    def trade_history(self) -> pd.DataFrame:
        """
        Retorna historial de trades como DataFrame.

        Returns
        -------
        pd.DataFrame
            Columnas: timestamp, type (BUY/SELL), symbol, amount,
            price, stop_loss, take_profit, pnl, status.

        Notes
        -----
        Exportable con: bot.trade_history().to_csv("mis_trades.csv")
        """
        if not self.trades:
            print("📭 No hay trades registrados aún.")
            return pd.DataFrame()

        return pd.DataFrame(self.trades)
