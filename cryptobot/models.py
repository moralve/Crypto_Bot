"""Mixin para model training: entrenamiento, optimización y feature importance."""

from typing import Optional

import pandas as pd


class ModelsMixin:
    """Métodos de model training: train_models(), optimize_model(), feature_importance(), plot_feature_importance()."""

    def train_models(
        self,
        window: str = "expanding",
        window_size: int = 60,
    ) -> "ModelsMixin":
        """
        Entrena y compara múltiples modelos ML para la estrategia seleccionada.

        Modelos evaluados:
        - Logistic Regression
        - SVM (RBF kernel)
        - Random Forest
        - XGBoost

        Usa TimeSeriesSplit para validación temporal (sin data leakage).

        Parameters
        ----------
        window : str, default "expanding"
            Tipo de ventana de entrenamiento:
            - "expanding": usa todos los datos disponibles hasta t.
              Más estable, más datos de training.
            - "sliding": usa solo los últimos window_size períodos.
              Se adapta mejor a cambios de régimen.
        window_size : int, default 60
            Tamaño de la ventana para modo "sliding" (en períodos).

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        El mejor modelo se auto-selecciona basado en F1-score.
        Resultados de comparación disponibles en self.model_comparison.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado select_strategy() previamente.
        """
        self._require_features()
        self._require_strategy()
        # TODO: Implementar
        # 1. Crear target (y) basado en la estrategia seleccionada
        #    - trend_following: ¿precio sube más de X% en N períodos?
        #    - mean_reversion: ¿precio regresa a SMA en N períodos?
        #    - momentum: ¿el momentum continúa en N períodos?
        # 2. Preparar X (features) e y (target)
        # 3. Split temporal según window type:
        #    - expanding: TimeSeriesSplit
        #    - sliding: rolling window manual
        # 4. Para cada modelo:
        #    a. Fit con pipeline (StandardScaler + modelo)
        #    b. Calcular métricas: accuracy, precision, recall, f1, auc
        # 5. Crear DataFrame comparativo (self.model_comparison)
        # 6. Auto-seleccionar mejor modelo por F1
        # 7. Guardar en self.model, self.model_name, self.model_metrics
        # 8. Print tabla comparativa
        pass

    def optimize_model(self, model_name: Optional[str] = None) -> "ModelsMixin":
        """
        Optimiza hiperparámetros del modelo usando GridSearchCV.

        Parameters
        ----------
        model_name : str, optional
            Modelo a optimizar. Si None, optimiza el mejor modelo
            de train_models(). Opciones: "logistic_regression",
            "svm", "random_forest", "xgboost".

        Returns
        -------
        CryptoBot
            Retorna self para permitir method chaining.

        Notes
        -----
        Usa TimeSeriesSplit como cv para respetar temporalidad.
        Los grids de hiperparámetros están predefinidos por modelo.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado train_models() previamente.
        """
        self._require_model()
        # TODO: Implementar
        # 1. Definir param_grid según modelo:
        #    - random_forest: n_estimators, max_depth, min_samples_split
        #    - xgboost: n_estimators, max_depth, learning_rate
        #    - svm: C, gamma, kernel
        #    - logistic_regression: C, penalty
        # 2. GridSearchCV con TimeSeriesSplit
        # 3. Refit con mejores parámetros
        # 4. Actualizar self.model y self.model_metrics
        # 5. Print mejores parámetros y mejora en métricas
        pass

    def feature_importance(self, top_n: int = 15) -> pd.DataFrame:
        """
        Muestra las features más importantes del modelo entrenado.

        Parameters
        ----------
        top_n : int, default 15
            Número de features a mostrar.

        Returns
        -------
        pd.DataFrame
            DataFrame con columnas: feature, importance, ordenado descendente.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado train_models() previamente.
        """
        self._require_model()
        # TODO: Implementar
        # 1. Extraer importances del modelo:
        #    - Tree-based: .feature_importances_
        #    - Linear: .coef_
        #    - SVM: usar permutation_importance
        # 2. Crear DataFrame ordenado
        # 3. Retornar top_n
        pass

    def plot_feature_importance(self, top_n: int = 15) -> None:
        """
        Gráfico de barras horizontal con las features más importantes.

        Parameters
        ----------
        top_n : int, default 15
            Número de features a mostrar.

        Raises
        ------
        RuntimeError
            Si no se ha ejecutado train_models() previamente.
        """
        self._require_model()
        # TODO: Implementar
        # 1. Llamar self.feature_importance(top_n)
        # 2. Plotly horizontal bar chart
        # 3. Colores de la paleta definida
        pass
