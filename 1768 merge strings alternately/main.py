from solution import Solution
import sys

if __name__ == "__main__":
    #soln = Solution()
    #print(soln.mergeAlternately(sys.argv[1],sys.argv[2]))
    soln = Solution()
    assert soln.mergeAlternately("abc", "pqr")=="apbqcr"
    soln = Solution()
    assert soln.mergeAlternately("pqr", "abc")=="paqbrc"
    soln = Solution()
    assert soln.mergeAlternately("pqrs", "abc")=="paqbrcs"
    soln = Solution()
    assert soln.mergeAlternately("abcd", "pqr")=="apbqcrd"
    soln = Solution()
    assert soln.mergeAlternately("ab", "pqrs")=="apbqrs"
    soln = Solution()
    assert soln.mergeAlternately("abcd", "pq")=="apbqcd"
    print("SUCCESS")
