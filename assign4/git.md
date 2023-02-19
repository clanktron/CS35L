# Differences between true "Git" repo and Eggert "Git" repo

The cloned repo of Git has only its master branch present, while the eggert copy has multiple branches; these being "maint", "next", "seen", and "todo".
These missing branches can still be found with `git branch -a` and "retrieved" with `git checkout <branchname corresponding to remote>` but are not present locally at the moment. The eggert copy is also behind by 79 commits whereas my repo is a fresh clone. 
