# [Lifelong Learning With a Task Oracle](https://arxiv.org/pdf/2011.04783.pdf)
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


