class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        st = []

        for token in tokens:

            if token == "+":
                a = st.pop()
                b = st.pop()
                st.append(b + a)

            elif token == "-":
                a = st.pop()
                b = st.pop()
                st.append(b - a)

            elif token == "*":
                a = st.pop()
                b = st.pop()
                st.append(b * a)

            elif token == "/":
                a = st.pop()
                b = st.pop()
                st.append(int(float(b) / a))

            else:
                st.append(int(token))

        return st[0]

                
        
        