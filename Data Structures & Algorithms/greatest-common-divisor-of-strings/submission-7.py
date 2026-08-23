class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcdOfStringsrec(str1, str2):
            len1, len2 = len(str1), len(str2)

            def isDivisor(s):
                l = len(s)

                if len1 % l != 0 or len2 % l != 0:
                    return False

                f1, f2 = len1 // l, len2 // l

                return s * f1 == str1 and s * f2 == str2

            # Try prefixes from longest to shortest
            for l in range(min(len1, len2), 0, -1):
                candidate = str1[:l]

                if isDivisor(candidate):
                    return candidate

            return ''

        return gcdOfStringsrec(str1, str2)
            

        