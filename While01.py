def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans=0
    while i<len(s):
        if s[i].isdigit():
            ans+=1
        i+=1
    return ans  
print(main("salom5855"))
