echo "#!/bin/sh
flake8 ." >> .git/hooks/pre-commit

chmod 777 .git/hooks/pre-commit
