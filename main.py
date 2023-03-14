# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main
import json

res = mean_var_std.calculate( [0,1,2,3,4,5,6,7,8] )
print(json.dumps(res['mean'], indent=4))
print(json.dumps(res['variance'], indent=4))

# Run unit tests automatically
main( module='test_module', exit=False )

