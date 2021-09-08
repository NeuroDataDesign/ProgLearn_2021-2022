# Version Controlling Systems

The following notes are based on the wonderful git/VCS tutorial which can be found in [here](https://missing.csail.mit.edu/2020/version-control/)

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

## Useful GitHub Commands

### Basics 
 
* ```git help <command>``` : get help for a git command 
* ```git init``` : creates a new git repo, with data stored in the .git directory 
* ```git status``` : tells you what’s going on 
* ```git add <filename>``` : adds files to staging area 
* ```git commit``` : creates a new commit 
* ```git log``` : shows a flattened log of history 
* ```git log --all --graph --decorate``` : visualizes history as a DAG 
* ```git diff <filename>``` : show changes you made relative to the staging area 
* ```git diff <revision> <filename>``` : shows differences in a file between snapshots 
* ```git checkout <revision>``` : updates HEAD and current branch 
* ```git checkout <filename>``` : throws the changes in the working directory and resest to the HEAD 
 
### Branching and Merging 
 
* ```git branch``` : shows branches 
* ```git branch <name>``` : creates a branch 
* ```git checkout -b <name>``` : creates a branch and switches to it same as git branch <name>; git checkout <name> 
* ```git merge <revision>``` : merges into current branch 
* ```git mergetool``` : use a fancy tool to help resolve merge conflicts 
* ```git rebase``` : rebase set of patches onto a new base 
 
### Remotes 
 
* ```git remote``` : list remotes 
* ```git remote add <name> <url>``` : add a remote 
* ```git push <remote> <local branch>:<remote branch>``` : send objects to remote, and update remote reference 
* ```git branch --set-upstream-to=<remote>/<remote branch>``` : set up correspondence between local and remote branch 
* ```git fetch``` : retrieve objects/references from a remote 
* ```git pull``` : same as git fetch; git merge 
* ```git clone``` : download repository from remote 
 
### Undo 
 
* ```git commit --amend``` : edit a commit’s contents/message 
* ```git reset HEAD <file>``` : unstage a file 
* ```git checkout -- <file>``` : discard changes 
 
### Advanced Git 
 
* ```git config``` : Git is highly customizable 
* ```git clone --depth=1``` : shallow clone, without entire version history 
* ```git add -p``` : interactive staging 
* ```git rebase -i``` : interactive rebasing 
* ```git blame``` : show who last edited which line (and why?)
* ```git stash``` : temporarily remove modifications to working directory (git stash pop gets the stuff back) 
* ```git bisect``` : binary search history (e.g. for regressions) 
* ```.gitignore``` : specify intentionally untracked files to ignore 

## Best practices of writing good commit messages

The best practices below are extracted from [here](https://chris.beams.io/posts/git-commit/) and [here](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
 
* Separate subject from the body using a blank line 
* Limit the subject line to 50 characters 
* Capitalize the subject line 
* Do not end the subject line with a period 
* Subject line should be written as a command (e.g. Fix the bug) 
* Wrap the body at 72 characters (configure vim to do this!) 
* Use the body to explain what, why and how 

## Other Resources

* [How to recover from common git mistakes](https://ohshitgit.com/)
* When working on big projects/ workflows : [link1](https://nvie.com/posts/a-successful-git-branching-model/ ) [link2](https://www.endoflineblog.com/gitflow-considered-harmful ) [link3](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow )
* [ProGit Book](https://git-scm.com/book/en/v2)
* [Pull requests in Github](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests )


