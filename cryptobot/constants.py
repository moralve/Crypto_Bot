"""Constantes globales del CryptoBot."""

VALID_TIMEFRAMES = ["1h", "4h", "1d"]

REGIME_LABELS = {0: "Bear 🔴", 1: "Sideways 🟡", 2: "Bull 🟢"}

STRATEGY_REGISTRY = {
    "trend_following": {
        "name": "Trend Following (SMA Crossover)",
        "description": "Sigue la dirección de la tendencia usando cruces de medias móviles",
        "best_regimes": ["Bull", "Bear"],
        "worst_regimes": ["Sideways"],
    },
    "mean_reversion": {
        "name": "Mean Reversion (Bollinger Bands)",
        "description": "Apuesta a que el precio regresa a su media cuando se aleja demasiado",
        "best_regimes": ["Sideways"],
        "worst_regimes": ["Bull", "Bear"],
    },
    "momentum": {
        "name": "Momentum (RSI + Volume)",
        "description": "Identifica movimientos fuertes y se sube a ellos",
        "best_regimes": ["Bull"],
        "worst_regimes": ["Sideways"],
    },
}

COLOR_PALETTE = {
    "yellow": "#F0B90B",
    "dark": "#1E2329",
    "green": "#0ECB81",
    "red": "#F6465D",
    "gray": "#474D57",
}
