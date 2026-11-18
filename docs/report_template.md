# PathSnap: Technical Report Template

**Course:** UE24CS352A - Machine Learning  
**Project:** PathSnap: Distributed Map-Matching & Route Reconstruction  
**Team Members:** Member 1, Member 2, Member 3, Member 4  

---

## 1. Challenge Overview & Problem Context
*Briefly describe the noisy GPS map-matching challenge, GPS dropout/multipath errors, and the system objective.*

---

## 2.2 Dataset Understanding and Exploratory Data Analysis (Member 1)
1. **Preprocessing:** How raw `.track`, `.nodes`, and `.arcs` files were preprocessed and transformed.
2. **Patterns Observed:** GPS sampling rate, noise patterns, coordinate systems, missing values.
3. **Feature Extraction:** Features extracted for candidate points and rationale.
4. **Visualisations:**
   - Missing-value analysis table.
   - GPS trajectory plots.
   - Road-network connectivity plots.
   - Interactive Folium map of selected trip.

---

## 3. Model Experimentation and Comparison (Member 2)

### 3.1 Overall Model Comparison Table
| Model | Algorithm Family | Key Configuration | CV Macro F1 | Top-1 Accuracy | Route Continuity | Student-Test Macro F1 | Log Loss | Inference Time |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model 1 | Logistic Regression | Regularized L2 | | | | | | |
| Model 2 | KNN | k=5, distance-weighted | | | | | | |
| Model 3 | Random Forest | n_estimators=100 | | | | | | |
| Model 4 | Extra Trees | n_estimators=100 | | | | | | |
| Model 5 | Multi-Layer Perceptron | (64, 32), Adam | | | | | | |

### 3.2 Individual Model Analyses
*(Answer questions A: Model Understanding, B: Training & Config, C: Experimental Results for each of the 5 models)*

### 3.3 Model Visualisations
- CV Macro F1 comparison bar chart.
- Student-testing Top-1 Accuracy & F1 comparison.
- Log Loss comparison where applicable.
- Confusion matrices.

---

## 4. Bayesian Hyperparameter Optimisation (Member 2)
1. Hyperparameters included in the search space.
2. Distributions and ranges.
3. Objective function and number of trials.
4. Best hyperparameters identified.
5. Comparison between untuned vs tuned model.

---

## 5. HMM and Viterbi Route Reconstruction (Member 3)
1. **Hidden States:** Definition of road segments as states.
2. **Emission Probabilities:** Modeling candidate likelihood.
3. **Transition Probabilities:** Shortest network path vs Euclidean/Haversine distance.
4. **GPS Gaps & Disconnected Segments:** Penalty handling and recovery.
5. **Comparison:** Classifier-only vs Classifier + HMM decoding table and analysis.

---

## 6. Geographical Visualisation Using Folium (Member 3)
- Screenshots and interactive maps illustrating:
  - Original noisy GPS observations (Blue markers).
  - Road-network geometry.
  - Reconstructed predicted route (Green polyline).
  - Start / End markers and layer control.

---

## 7. API, UI and Deployment (Member 4)
1. **Distributed Two-Laptop Architecture:**
   - Laptop 1 (Server): FastAPI REST server hosting model inference, road network lookup, and server-side evaluation.
   - Laptop 2 (Client): Streamlit interactive dashboard with embedded Folium maps.
2. **Data Leakage Prevention:**
   - Ground truth (`.route`) strictly isolated on Laptop 1; only evaluated post-inference.
3. **Screenshots:**
   - Working UI on Laptop 2 showing evaluated trip, map, and metrics.
   - Terminal / CMD on Laptop 1 showing incoming inference requests with timestamped HTTP 200 logs.
4. **Latency Analysis:**
   - Average inference time per trip in milliseconds.
