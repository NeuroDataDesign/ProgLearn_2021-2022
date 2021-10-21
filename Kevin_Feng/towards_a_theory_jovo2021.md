# Towards a theory of out-of-distribution learning
[Jovo etal. 2021](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DWPfdT4AAAAJ&sortby=pubdate&citation_for_view=DWPfdT4AAAAJ:Jxw8hHINxX0C)

### 1 Intro
- majority of current ml ai advances focus on in-distribution data: learning where the training and test data are assumed to be sampled from the same distribution
- IRL out of distribution more common 
- evaluating OOD algo's by accuracy isn't adequate
- make following changes to eval: we make a simple change to the classic in-distribution definition of a learning task: we no longer implicitly assume that the evaluation distribution that our learner will face at test/deployment time is the exact same distribution from which the training data are assumed to be sampled
- intro **learning efficiency**: quantifies how much a given learner is able to learn a task by leveraging data, quantifies relative number of samples required by one learner relative to the same learner that obtains other data
- define **out of distribution learnability** 
- Goal: ood is key capability that biological learning agents leverage, so this work aims to bridge gap between ml ai and biological agents

### 2
![image](https://user-images.githubusercontent.com/89429238/137249012-18733e0d-910e-4a8b-a99a-dc8cc9c01624.png)
- our goal is to minimize risk
- solving decision problems depends on knowing true dist. but in learning problems is this partially or completely unknown, so a learner must leverage data to estimate a hypothesis
- learner uses n data points to provide a good guess for h in 2.1
- Data space S: data need not be query action pairs, data space is the union of all posssbile sequences, so S* is set of all n-length lists of S-valued data for any n belonging to N
- Statistical model: is a collection of admissble distributions 
- Learners: f(S_n) = h_hat_n
- Error: E:FxSxPxR |->|R

![image](https://user-images.githubusercontent.com/89429238/137249739-6cb697c3-65e1-4f44-bc1e-d2804061f9dd.png)

Learning task

![image](https://user-images.githubusercontent.com/89429238/137250296-b6ebd2a4-8390-4747-8181-0d8a7a4412dd.png)

### 3 
In generalized learning problems, may be multiple datasets, tasks, learners, etc, so augment above components of a learning task to be able to account for this

General learning task is to choose a learner f that learns a hypothesis h_hat_n minimzers error E

Learning Efficiency

![image](https://user-images.githubusercontent.com/89429238/137251053-f9ece497-c073-48f3-988b-fdd6afb0f4df.png)

![image](https://user-images.githubusercontent.com/89429238/137251479-5915c304-5b7a-4bbf-9d69-cc4f054d4096.png)

Weak OOD learnablility

![image](https://user-images.githubusercontent.com/89429238/137251623-340fb484-66d4-4fe5-bbdb-045e6d119620.png)

Strong OOD learnability 

![image](https://user-images.githubusercontent.com/89429238/137827290-590228bf-4fe3-4f29-b2be-9d50494cbb73.png)

- definition of learning: f (the learner) learns from S_n (the dataset) on task *t* when R_XY(hhat_n) (risk) improves which is definition of weak OOD learnability above

### 4 Theoretical Results
for task *t*, if we have strong ood learned at target sample size n, then we have weakly ood learned at target sample size n (strong impolies weak)
- strongly ood learned means that we can get arbitrarily to optimal performance with arbitrarily high probability 
- weak ood learn means to perform better than base performance R_XY(hhat_n) with arbitrarily high probability
- peroforming arbitrarily well implies performing better than base

Strong implies non-uniform. for task t, if we have strongly ood learned at sample size n, then we non-uniformly ood learned at sample size n
- non-uniformly ood learn: we can get arb close to optimal performance with arb high probability for all distributions in the task model given a certain number of data points that depends on the distribution

Positive transfer is weaker than ood learning. for arb task t, if f weakly ood learnd from S^B, then f also positvely transfers from S^B. however converse is not always true. -> class of pos transfer learning problems bigger than class of weakly ood learning problems

Weak ood meta learner: exists tasks t suc hthat with zero data sampled from the eval distribution of that task, f can weakly ood learn, but f does not strongly ood learn
- implies that class of weakly ood learning problems is smaller than class of strongly ood learning problems

Weak meta-learning does not imply non-uniform meta-learning. There are tasks t for which weak ood meta-learning does not imply non-uniform ood meta-learing

### 5 
learning efficiency for in-distribution learning 
- we say f learns in this task if log LE > 0

![image](https://user-images.githubusercontent.com/89429238/137832428-4a8a19d8-6ad8-4fad-b6dd-11e69d26722f.png)

Transfer learning is arguably the simplest OOD learning scenario with one udnerlying task t along with an explicit set of J datasets {S^1,...,S^j}
- S^1 data associated with task t often called target data
- S^2-S6J sometimes called side info or source data, avail to assist in learning and producing a better hypothesis

Learning Efficiency for transfer learning
- We say that f transfer learns in this supertask if log LE > 0 

![image](https://user-images.githubusercontent.com/89429238/137833732-5cd12291-9de8-469d-b4d2-5973dd629251.png)

- identical to previous, transfer learning is a generalization of in-distribution learning 

Learning efficiency for multitask learning:

![image](https://user-images.githubusercontent.com/89429238/138001485-82fa1e1a-7405-4282-8478-db6494ba6f22.png)

- to quant learning across tasks: intro non-neg weights per task, *w* = (w_1, w_2, ...) where sum(w_t) = 1

Multitask learning 

![image](https://user-images.githubusercontent.com/89429238/138002338-e6232bf5-a868-47ee-b05e-409fd3c2905d.png)

- weights important cuz we may have multiple tasks but only be interested in the transfer to one task

Meta-learning: learning to learn
- goal is to see if having multiple datasets improves eff on task t and compared to just having one new dataset

![image](https://user-images.githubusercontent.com/89429238/138002800-5fe5caf1-08db-4bc4-9ef8-476dfdc76f76.png)

- if environment T=T_k then meta-learning = multitask learning, meaning meta-learning is a generalization of multitask learning
- key diff is meta-learning has unobserved tasks, whereas in multitask learner as a prior access to all tasks
- weak meta-learing like weak multitask learning, corresponds to setting where log of avg learning efficiencies is pos
- strong meta-learning like strong multitask learning, corresponds to setting where log of each learning efficiency is pos, f pos transfers for each task in the environment

Continual learning 
- anything about a task can change in any moment
- must have computational upper bound of o(n) space and/or O(n^2) time, in practice be far more efficient

Given task of interest t, S^<t = set of data points up to and including the last data point from task t
LE for FT 

![image](https://user-images.githubusercontent.com/89429238/138005658-18533e92-9115-44d6-9129-0bbddb3082a2.png)

LE for BT

![image](https://user-images.githubusercontent.com/89429238/138005680-c6186b51-dec3-41c1-9d17-e9598dbb2ea9.png)

Multiplying both above gives LE for that task 

![image](https://user-images.githubusercontent.com/89429238/138005721-0c32d5df-74a2-4b4a-bae7-338025b0abb1.png)

So,

![image](https://user-images.githubusercontent.com/89429238/138005778-c03fdbb0-e11b-4925-9bf1-541ba4a6a3f3.png)

Lifelong Learning
- lifelong learning differs from continual learning because in lifelong learning the weights of each task may change over time (more like biological learning, ie frog doesnt need to know how to swim as tadpole so that task weight becomes 0)
- lifelong learning comp contraints can change over lifetime 
- should also be able to re-allocate resources to ensure it doesn't forget crucial skills (ie how to breath)

![image](https://user-images.githubusercontent.com/89429238/138006297-a0455e27-8309-4b3a-b9a8-53adabe4eab3.png)

### 6 Discussion
- introduced learning efficiency: ask whether something has learned = whether something has log pos LE
- LE also provides measure to quantify how much a given learner has learned
- we can use learning curves to compare performances of different learners: LE as a function of sample size n
- 
