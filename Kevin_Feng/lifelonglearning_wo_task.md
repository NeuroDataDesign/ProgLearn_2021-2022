# [Lifelong Learning Without a Task Oracle](https://arxiv.org/pdf/2011.04783.pdf)
Amanda Rios and Laurent Itti

## Abstract
- Supervised deep neural networks known to undergo sharp decline in accuracy of older tasks when new ones are learned = "catastrophic forgetting"
- current continual learning relies on biasing and/or parpartitioning a model to accommodate successive tasks incrementally. However, these methods largely depend on the availability of a task-oracle to confer task identities to each test sample, without which the models are entirely unable to perform.
- propose/compare task-assigning mappers which require little memory overhead
1. incremental unsupervised prototype using either nearest means, Gaussian mixture models, or fuzzy ART backbones
2. supervised incremental proto assignment with fast fuzzy ARTMAP
3. shallow perceptron trained via a dynamic coreset
- proposed model variants trained either from pre trained feature extractors or task-dependent feature embeddings of the main classifier network
- overall, methods perform close to a ground trouth oracle

## Learning without a task oracle
- major limiatation of task-dependent methods is inability to perform without task oracle
- determining task ID's is a learning procedure itself subject to catastrophic forgetting
- propose several task-mapper algo's to substitute the oracle input 
- models prio simplicity and low memory usage 
- to eval task mappers and baselines, use parameter superposition PSP with Beneficial Biases BD as standard state of the art task dependent backbone for fine grained classification 

![image](https://user-images.githubusercontent.com/89429238/152909184-c55ab8f8-0e89-418e-a726-42947b29811d.png)

### Incremental Unsupervised Task Mappers
- leverage prototype-based networks only for incremental task-mappying, form of coarse0level indentification
- couple them with efficient task-dependent deep network fine-grained classifier, seek a complementarity that enables more efficient lifelong learning
1. *Nearest Means Classifier (NMC)*: to learn a new task, start with a fixed embedding of this task and perform K-means clustering. K resulting prototypes all receive an attached super-label equal to the current task's ID. Keep a running dictionary D_map of the cluster to task mapping:

![image](https://user-images.githubusercontent.com/89429238/153300346-8919a645-3c1c-40e8-93cd-e53d45d74a74.png)

- For any given sample, find closest store prototype and use its task label as the predicted task:

![image](https://user-images.githubusercontent.com/89429238/153300445-b79ea106-fddc-4cc2-b59c-394af88570b0.png)

2. *Gaussian Mixture Model Classifier (GMMC)*: Guassian Mixtures (GM) to perform task-wise incremental prototype generation. Encode variance information and perform soft-assignment, more robust to outliers during clustering vs NMC. For each new task, K GM prototypes are computed from extracted fixed embedding of that task with overall distribution: 

![image](https://user-images.githubusercontent.com/89429238/153300995-9cb98db7-4705-4a29-86a8-1472d74d7381.png)

- \mu_i, \sigma_i are mean and covariance of each of the K Gaussian distributions
-  Also save K Gaussian weights, w_i, per task
-  At each task switch we re-norm them to:

![image](https://user-images.githubusercontent.com/89429238/153301297-a390af53-e04f-41b5-911b-ef59147b3fdc.png)

- task mapper then becomes a distionary containing assignments from GM params to task super-labels: 

![image](https://user-images.githubusercontent.com/89429238/153301423-1cd694f9-0407-4245-8635-b65bad3bc540.png)

3. *Fuzzy ART Classifier:* In this variant we generate the incremental prototypes with an unsupervised fuzzy ART network
- ART networks were initially proposed to overcome the stability-plasticity dilemma by accepting and adapting a stored prototype only when an input is sufficiently similar to it
- when new input pattern not close to any existing proto, new node is created with that input as a proto template
- similarity depends on vigilance param p, with 0 < p < 1, when p small similarity cond is easier to achieve = coarse categorization with few protos
- p close to 1 results in many finely divided categories at cost of large memory consumption
- One further specification of ART is that an input x of dimension D undergoes a pre-processing step called complement coding, which doubles its dimension to 2D while keeping a constant norm, x∗ = [x,~1 − x]. This procedure prevents category proliferation [19] but makes each prototype also occupy double amount of space.

![image](https://user-images.githubusercontent.com/89429238/153302140-49b5e2e5-8c26-4dc8-b534-45d1e9897a17.png)

- during learning of each task, if for x a proto w_i is sufficiently similar by satisfying: 

![image](https://user-images.githubusercontent.com/89429238/153346153-62794df9-edad-4d0b-9726-c04fa8fff617.png)

then w_i can be updated according to:

![image](https://user-images.githubusercontent.com/89429238/153346276-36673ada-5062-42ca-aa15-efeddf0e0d4b.png)

- adapt an unsupervised ART for incremental task classification, as a new task is learned, set p = 1 for all protos of already learned tasks
- also keep running dictionary D_map with task mappings between protos and their corresponding task super-labels
- task is predicted as: 

![image](https://user-images.githubusercontent.com/89429238/153346980-8159f0b2-7845-41f2-b5a3-ba0bd624f4ec.png)

### Supervised Prototype Mapping (ARTMAP)
- employs a supervised fuzzy ART (ARTMAP) architecture
- naturally allows for incremental learning without interference to previous protos
- advantage of using an ARTMAP for mapping is they allow for incremental learning without interference to prev protos
- in case of a category mismatch, vigilance is adjusted temporarily, called match tracking:

![image](https://user-images.githubusercontent.com/89429238/153348439-89fdecc6-d9a2-4440-b32d-863f3bfe0cd6.png)

### perceptron with coreset replay (PCR)
- incrementally map feature arrays to task assignments using a shallow perceptron aided by replay from a fixed-size memory coreset
- features used as inputs obtained via transfer-learning from a fronzen feature extractor 

1. *Corset Building:* 
- at time of insertion into memory buffer, select a number of feature vectors from new task equal to N/T(t), N is size of corset and T(t) is total number of tasks learned until then
- at each task-switch we re-comp the per-task allowance and remove and equiv number of old feature vectors per task, maintaining a homogeneos task representation in the corset at all times

2. *Perceptron Training:* 
final is optimized by stochastic gradient descent: 
![image](https://user-images.githubusercontent.com/89429238/153351545-30d988bc-026a-4e62-980f-fc3fb80ba79e.png)

- where \lambda_mem weighs the importance of old tasks relative to new
- dynamically setting \lambda_mem = T_mem/T_all during training worked best
- T_mem referes to the number of tasks in memory and T_all = T_mem + T_new
- During training, the perceptron is not reinitialized, to enable forward transfer of knowledge

### Perceptron + replay of task-specific embeddings (PCR-E)
- we use a PSP-BD fine-grained classifier and sift through PSP-BD keys and biases to collect all task-specific output responses which are then concatenated and used as input to a shallow perceptron
- each task, perceptron learns to map this concatenated array to the correct task label
- keep a coreset with previous tasks' feature arrays as prev described

### Task-Mapper Baselines and Baseline-Modifications
- include upper and lower bound baselines which consist of training the task-dependent fine-grained classifier with ground truth task labels and random task assignments, respectively
- additional baseline = mod'd version of Multi-head KM which includes other relevant task-specific elements such as PSP partitioning and BD biases

1. *Baseline-Entropy:* 
- given input pattern, sift through PSP task partitions and task-specific BD biases for all tasks seen far, obtaining multiple task-condidtioned embeddings
- predict task assignment by the index of task embedding, f(x,\theta_t), which yields lowest predictive uncertainty, lowest out entropy:

![image](https://user-images.githubusercontent.com/89429238/153354986-ecd0c2e4-01d1-483b-9d8a-b579c5aae9cf.png)

2. *Baseline - Expert Autoencoder Gates (AE-gates):*
- one single-layer undercomplete autoencoder (AE) in trained separately for each task, capturing shared task statistics in it's latent space encodings
- test time, pass a test sample through all AE's meanwhile computing for each AE the mean squared reconstruction error (MSE)
- final task prediction is given by AE with lowest MSE: 

![image](https://user-images.githubusercontent.com/89429238/153355831-e88c93fc-a5ad-48d9-add9-a8a64ace2e06.png)

3. *Baseline - Clustering in Multi-Head Outputs (KM-heads):* 
- one seperate output head is created for each task, for a total of T heads
- after supervised trainig of current task t, a forward pass with the current tasks' data gives an embedding of head H(t) which is then clustered via k-means
- proto's stored, procedure repeated after each task is learned, resulting, at time t, in a number T(t) of different embeddings as well as T(t) * N protos
- testtime, task predicted by running sample through network, at each head computing min dist from that sample to the closest head-specific proto
- overall task pred is given by abs min dist from all heads
- winner head is then used to perform fine-grained classfication:

![image](https://user-images.githubusercontent.com/89429238/153357555-062ef501-a6b8-475b-9765-30acfd26a133.png)

4. *Baseline Modification - clustering in multi-head or shared-head with PSP-BD Task-partitioning (KM-heads):*
- enable two versions of readout, one with multiple heads and the other with a shared head for all tasks

### *Experiment Descriptions - Datasets*
A. 8 Datasets experiment
B. Permuted MNIST
C. Sequence of 10 Cifar100 superclasses

### **RESULTS**
A. *Task Estimation - Parameter Dependency*

![image](https://user-images.githubusercontent.com/89429238/153362122-c2ae17f9-4b10-4201-9360-55b231346ace.png)

