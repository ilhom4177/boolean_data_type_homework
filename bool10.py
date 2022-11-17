import math
def main(a):
    """check that the number "a" is a perfect square.
    Args:
	@@ -6,4 +7,5 @@ def main(a):
        bool
    """
    # Write your code here
    return (math.sqrt(a))%1==0  
print(main(10))    