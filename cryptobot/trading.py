"""Mixin para paper trading en testnet."""


class TradingMixin:
    """Métodos de paper trading: connect_testnet(), execute(), status()."""

    def connect_testnet(self, api_key: str, api_secret: str) -> "TradingMixin":
        """
        Conecta al testnet del exchange para paper trading.

        Parameters
        ----------
        api_key : str
            API key del testnet (NO usar keys de producción).
        api_secret : str
            API secret del testnet.

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        Cada exchange tiene su propio testnet:
        - Bybit: testnet.bybit.com
        - Binance: testnet.binance.vision
        - OKX: demo mode dentro de la plataforma

        ⚠️  NUNCA uses API keys de tu cuenta real aquí.
        """
        # TODO: Implementar
        # 1. Crear nueva instancia de exchange con sandbox=True
        # 2. Configurar api_key y api_secret
        # 3. Verificar conexión con fetch_balance()
        # 4. self._testnet_connected = True
        # 5. Print balance del testnet
        pass

    def execute(self, mode: str = "paper") -> dict:
        """
        Ejecuta la señal más reciente.

        Parameters
        ----------
        mode : str, default "paper"
            Modo de ejecución:
            - "paper": ejecuta en testnet (requiere connect_testnet())
            - "live": ⛔ DESHABILITADO — solo para referencia educativa

        Returns
        -------
        dict
            Información del trade ejecutado:
            {type, symbol, amount, price, stop_loss, take_profit, timestamp}

        Notes
        -----
        Risk management se aplica automáticamente:
        - Position size basado en max_position_pct
        - Stop loss basado en stop_loss_pct
        - Take profit basado en take_profit_pct

        Raises
        ------
        RuntimeError
            Si no hay señales o no está conectado al testnet.
        ValueError
            Si mode="live" (no permitido en este curso).
        """
        if mode == "live":
            raise ValueError(
                "⛔ Modo 'live' deshabilitado. Este bot es educativo. "
                "Usa mode='paper' con el testnet."
            )
        self._require_signals()
        self._require_testnet()
        # TODO: Implementar
        # 1. Obtener última señal
        # 2. Si HOLD: print "Sin acción" y retornar
        # 3. Si BUY o SELL:
        #    a. Calcular position size (balance * max_position_pct)
        #    b. Calcular stop_loss y take_profit prices
        #    c. Ejecutar orden via CCXT: create_market_order(...)
        #    d. Registrar trade en self.trades
        #    e. Print confirmación del trade
        # 4. Retornar dict con detalles del trade
        pass

    def status(self) -> None:
        """
        Muestra estado actual del bot en testnet.

        Incluye:
        - Balance actual (USDT + cripto)
        - Posiciones abiertas
        - Último trade ejecutado
        - P&L no realizado
        - P&L total

        Raises
        ------
        RuntimeError
            Si no está conectado al testnet.
        """
        self._require_testnet()
        # TODO: Implementar
        # 1. fetch_balance()
        # 2. Posiciones abiertas (si las hay)
        # 3. Último trade de self.trades
        # 4. Calcular P&L
        # 5. Print formateado
        pass
