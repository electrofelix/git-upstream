# What is git-upstream?

git-upstream is an open source Python application that can be used to keep in sync with upstream open source projects, mainly OpenStack.

git-upstream provides new git subcommands to support rebasing of local-carried patches on top of upstream repositories. It provides commands to ease the use of git for who needs to integrate big upstream projects in their environment (i.e., feature branch creation/finishing, release starting/finishing). The operations are performed using Git commands.

**Note**: currently git-upstream can be used only for projects that are maintained with Gerrit as it relies on the presence of Change-Id's.
Nevertheless, the code is quite modular and can be extended to use any part of commit message (e.g., other headers).

Specifically, current git-upstream version supports the following features

* **Single upstream branch import**

  Your repository is tracking an upstream project and has local changes applied and no other branch is merged in. This can also be applied to tracking upstream packaging branches: *e.g.*, ubuntu/master => ubuntu/saucy-proposed/nova + local packaging changes.

* **Multi branch import (upstream branch + additional branches)**

  In this case, your project tracks an upstream repository, merges in an arbitrary number of branches and applies local carried changes.

* **Re-reviewing**

  Reviewing (w/ Gerrit) of all locally applied changes if desired.
git-upstream creates an import branch in a manner that allows it to be fully re-reviewed or merged into master and pushed.

* **Detailed logging**

  git-upstream can output to both console and log file simultaneously. Multiple levels and these are managed separately for log file and console output.
This means jobs run by Jenkins can save a detailed log file separately as an artefact while printing status information to the console if those running the jobs don’t wish to have the console spammed with the details.

* **Dropping of changes that appear upstream**

  Compares Change-Id's of changes applied since previous import with those that have appeared on the upstream branch since the last import point.

* **Interactive mode**

  Once the list of changes to be re-applied has been determined (and those to be dropped have been pruned), the tool can open an editor (controlled by your git editor settings) for users to review those changes to be made and allow them to perform further operations such as re-ordering, dropping of obsolete changes, squashing.

* **Dropping local changes**

  It’s always possible for local changes to be superseded by upstream changes, so when these are identified and marked as such, we should drop them.

  This can also occur where a change was applied locally, modified when being upstreamed based on review feedback and the resulting differences were ported to the internal as well. While the original change will be automatically dropped, also useful to drop the additional ported changes automatically if possible, rather than have it cause conflicts.

# Using git-upstream

Please see `USAGE.md`

# Available commands

## import

### Description

Import code from specified upstream branch. Creates an import branch from the specified upstream branch, and optionally merges additional branches given as arguments. Current branch, unless overridden by the `--into` option, is used as the target branch from which a list of changes to apply onto the new import is constructed based on the the specified strategy. Once complete it will merge and replace the contents of the target branch with those from the import branch, unless `--no-merge` is specified.

### Usage

```
git upstream import [-h] [-d] [-i] [-f] [--merge] [--no-merge]
                           [-s <strategy>] [--into <branch>]
                           [--import-branch <import-branch>]
                           [<upstream-branch>] [<branches> [<branches> ...]]
```

### Arguments

```
positional arguments:
   <upstream-branch>     Upstream branch to import. Must be specified if you
                        wish to provide additional branches.
  <branches>            Branches to additionally merge into the import branch
                        using default git merging behaviour

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry-run         Only print out the list of commits that would be
                        applied.
  -i, --interactive     Let the user edit the list of commits before applying.
  -f, --force           Force overwrite of existing import branch if it
                        exists.
  --merge               Merge the resulting import branch into the target
                        branch once complete
  --no-merge            Disable merge of the resulting import branch
  -s <strategy>, --strategy <strategy>
                        Use the given strategy to re-apply locally carried
                        changes to the import branch. (default: drop)
  --into <branch>       Branch to take changes from, and replace with imported
                        branch.
  --import-branch <import-branch>
                        Name of import branch to use
```

## drop

### Description

Mark a commit as dropped. Marked commits will be skipped during the upstream rebasing process. See also the "git upstream import" command.

### Usage

```
git upstream drop [-h] [-a <author>] <commit>
```

### Arguments

```
positional arguments:
  <commit>              Commit to be marked as dropped

optional arguments:
  -h, --help            show this help message and exit
  -a <author>, --author <author>
                        Git author for the mark
```

## supersede

### Description

Mark a commit as superseded by a set of change-ids. Marked commits will be
skipped during the upstream rebasing process. See also the "git upstream
import" command.

### Usage

```
git upstream supersede [-h] [-f] [-u <upstream-branch>]
                       <commit> <change id> [<change id> ...]
```

### Arguments

```
positional arguments:
  <commit>              Commit to be marked as superseded
  <change id>           Change id which makes <commit> obsolete. The change id
                        must be present in <upstream-branch> to drop <commit>.
                        If more than one change id is specified, all must be
                        present in <upstream-branch> to drop <commit>

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           Apply the commit mark even if one or more change ids
                        could not be found. Use this flag carefully as commits
                        will not be dropped during import command execution as
                        long as all associated change ids are present in the
                        local copy of the upstream branch
  -u <upstream-branch>, --upstream-branch <upstream-branch>
                        Search change ids values in <upstream-branch> branch
                        (default: upstream/master)
```

# Authors
git-upstream was written by Darragh Bailey <dbailey@hp.com>.

# Acknowledgements

Thanks to *Aleksander Korzynski* and *Stanisław Pitucha* for taking the original design spec and some basic manual steps and experimenting with initial implementations.

To *Davide Guerri*, for picking up a rough python tool and turning it into something that was actually usable.

Also to *Jon Paul Sullivan* and *Monty Taylor* to listening and providing a sounding board for different approaches.

And finally to *Coleman Corrigan* among numerous others who acted as willing guinea pigs for the original manual approach.

Hope this eventually helped save you time and some hair.
