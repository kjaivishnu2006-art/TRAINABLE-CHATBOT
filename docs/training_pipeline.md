# Machine Learning Training Pipelines

VYOMA AI deploys optimized, decoupled training algorithms specifically formulated for real-time App Inventor interfaces. The entire strategy focuses on executing massive tensor logic efficiently on generic CPUs.

## 1. Vision Training Pipeline
**Technique:** Deep Feature Extraction + Support Vector Machines (SVM).

1. **Ingestion**: Raw images are loaded and resized uniformly to `224x224` pixels.
2. **Convolution Pass**: Pre-processed pixels are fed through a pre-trained (ImageNet mappings) headless `MobileNetV2` Neural Network to extract abstract visual elements natively (e.g., shapes, fur textures).
3. **Data Morphing**: The complex output array is squeezed into a 1D Feature Vector.
4. **Shallow Training**: The 1D Vectors corresponding to their uploaded `class_names` are fed into a linear Support Vector Machine (`SVC`) to carve mathematical boundaries separating the classes.
5. **Serialization**: Resultant weights and bounds are saved iteratively as `.joblib` binary formats, holding a minimal hard disk footprint.

## 2. Audio Training Pipeline
**Technique:** Time-Series Spectrography & K-Nearest Neighbors (KNN).

1. **Frequency Normalization**: `.wav` files ingested from App Inventor's `SoundRecorder` are forcibly down-sampled natively to `16 kHz` to strip arbitrary silence variants and standardize time horizons.
2. **MFCC Extraction**: The wave stream passes through the `librosa` algorithm, collapsing raw amplitudes into 40 distinct Mel-Frequency Cepstral Coefficients (MFCCs). This creates a perceptual scale mathematically mirroring human hearing.
3. **Mean Axis Pooling**: The extracted time-series limits are averaged to produce a strict geometric coordinate in vector space.
4. **Cluster Formation**: The coordinates are mapped via the `KNeighborsClassifier` algorithm, where spatial boundary density declares the likelihood (`predict_proba`) of new uploads matching adjacent clusters.

## 3. Text Training Pipeline
**Technique:** Term Frequency Scaling.

1. **Tokenization**: UTF-8 Strings are lowercased, and punctuation/noise is regex-stripped globally.
2. **Frequency Matrix**: `TfidfVectorizer` maps terms to proportional occurrences, heavily penalizing universally common words (like "the", "and") while spotlighting core dataset identifiers.
3. **Cosine Vector Search**: A non-neural matrix algorithm locates the mathematical slope intersection most similar to the trained intents.
