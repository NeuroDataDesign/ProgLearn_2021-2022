# Version Controlling Systems

## Introduction 
 
* VCS keeps track of the changes made to the source code. This is done through a series of snapshots.

* VCS facilitates collaborations. (sending code to others, resolving issues, etc.) 
 
* Why is version control useful? Even when you’re working by yourself, it can let you look at old snapshots of a project, keep a log of why certain changes were made, work on parallel branches of development, and much more.  
 
* Modern VCSs also let you easily (and often automatically) answer questions like: 
    * Who wrote this module? 
    * When was this particular line of this particular file edited? By whom? Why was it edited? 
    * Over the last 1000 revisions, when/why did a particular unit test stop working? 

## Git's Data Model

* The following figure represents a simple Git's data model.

![](https://github.com/Laknath1996/ProgLearn_2021-2022/blob/main/Ashwin_De_Silva/assets/images/git_data_model.png)

* In Git jargon,  
    * A file : blob 
    * A directory : tree 
    * The top-level tree that's being tracked : snapshot/commit 
    * A directed acyclic graph (DAG) of snapshots : history
    * Branching : work on things in parallel  
    * Merging : combine the changes from difference branches of development 
 
* Each snapshot in git refers to a set of parents. A snapshot might descend from multiple parents due to merging and branching. 

* Commit history as a DAG: 

![](https://github.com/Laknath1996/ProgLearn_2021-2022/blob/main/Ashwin_De_Silva/assets/images/branching.png)

* The circles represent the individual commits. The arrows represent the 'comes before' relation. (They point to the parent of each commit/ previous commit).

![](https://github.com/Laknath1996/ProgLearn_2021-2022/blob/main/Ashwin_De_Silva/assets/images/merging.png)

* After 3rd commit, history branches in to two (two independently features being developed parallelly) and merges to create a snapshot that incorporates both the features. 

* Commits are immutable. The edits to the commit history create new commits and are pointed to new ones. Also, there could be merge conflicts. Conflicts have to be resolved by the developer using tools like mergetools, vimdiff, and other adavanced IDEs. 
 
* The commits contains meta data like author, message, etc. Each commit would have a hexadecimal ID string and a human readable reference (e.g. "fix bug") that maps to it.  
 
* An object is a blob, tree, or a commit. All objects are content-addresses by SHA-1 hash (hexadecimal ID – machine readable).  
 
* References (human readable) are pointers to commits. E.g. master reference points to the latest commit in the main branch of development. The references points to a particular snapshot in history instead of the hexadecimal ID. "Where we currently are" --> "HEAD" reference. 
 
* Git repository is the collection of data objects and references. (stores the git data model).  
 
* The git commands helps us manipulate the commit DAG by adding objects and adding/updating references. When typing a command, think about the manipulation made to the commit DAG by the said command. E.g. “discard uncommitted changes and make the ‘master’ ref point to commit 5d83f9e” is done by git checkout master; git reset --hard 5d83f9e 
 
* The staging area helps specify which modifications should be included in the next snapshot.  
 
* Github is a repository host for git. You don't need to have a Github account to use git command-line interface.


