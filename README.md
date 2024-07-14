****GCN-ARIMA HYBRID MODEL****

This code integrates Graph Convolutional Networks (GCN) and AutoRegressive Integrated Moving Average (ARIMA) to leverage the strengths of both spatial and temporal modeling techniques. 
The GCN component effectively captures spatial dependencies by processing the graph structure of the rail network, while the ARIMA component models the temporal aspects of passenger flow data. 
By sequentially combining these models, the hybrid approach aims to provide a comprehensive solution to the complex spatiotemporal dynamics inherent in urban rail systems.

**The primary objective of the paper :**

 Applying the hybrid GCN-ARIMA model to a dataset containing passenger flow data recorded at 10-minute, 15-minute, and 30-minute intervals for both in-flow and out-flow at each station. 

 The model's performance is evaluated using key metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Weighted Mean Absolute Percentage Error (MAPE), demonstrating significant improvements over traditional and standalone methods.

****PROPOSED WORK****
**Preprocessing:** Time series analysis will be applied to decompose the data into trend, seasonality, and residual components. Additionally, a graph representation of the rail network will be constructed to facilitate GCN modeling.
 **Model Development:**
 
 **GCN Implementation:** Graph Convolutional Networks will be implemented to capture spatial dependencies. Multiple GCN layers will process the graph data, extracting features that reflect the inter-station 
relationships.

 **ARIMA Integration:** The residuals from the GCN model will be fed into an ARIMA model to incorporate temporal dynamics. Parameter selection for ARIMA (e.g., autoregressive order, differencing, moving average order) will be optimized based on the decomposed time series components.

 **Hybridization:** We will explore both sequential and parallel integration strategies where GCN and ARIMA models inform each other iteratively or simultaneously to achieve the best prediction performance.

![image](https://github.com/user-attachments/assets/bfda854f-1c9e-42a2-b059-cf0665b994c9)


